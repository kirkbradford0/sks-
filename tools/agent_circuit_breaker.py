"""Agent circuit breaker — runtime fallback for the SKS fleet.

Detects an agent stuck in an execution loop (repeating the same
action+params) BEFORE it burns tokens or produces a third copy of the
same bad output. Pair with DABS-QUARANTINE.md: the breaker stops the
loop at runtime; DABS stops the message at the repo layer.

Origin: Kirk-supplied pattern (2026-09-18), hardened by Alpha:
  - sliding-window repeat detection (catches alternating A,B,A,B loops,
    not just consecutive identical states)
  - canonical JSON hashing (stable across dict ordering / nested params)
  - bounded history (deque, no memory leak)
  - trip state + reset so an override is logged, not silent

Usage:
    breaker = AgentCircuitBreaker(max_repeats=3, window=8)
    if breaker.check("search_web", {"q": "same query"}):
        # supervisor override: prune context, inject backtracking goal
"""

import hashlib
import json
from collections import deque
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


class AgentCircuitBreaker:
    def __init__(self, max_repeats: int = 3, window: int = 8, history_cap: int = 64):
        if window < max_repeats:
            raise ValueError("window must be >= max_repeats")
        self.max_repeats = max_repeats
        self.window = window
        self._history: deque = deque(maxlen=history_cap)
        self.tripped_at: Optional[str] = None
        self.trips: List[Dict[str, Any]] = []

    def _hash_state(self, action: str, params: Dict[str, Any]) -> str:
        """Canonical hash of the agent's intent — order-independent."""
        payload = json.dumps(
            {"action": action, "params": params},
            sort_keys=True, default=str, separators=(",", ":"),
        )
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def check(self, action: str, params: Dict[str, Any]) -> bool:
        """True if this state has appeared >= max_repeats times inside the
        recent window (loop detected). Consecutive AND alternating loops trip."""
        h = self._hash_state(action, params)
        self._history.append(h)
        recent = list(self._history)[-self.window:]
        repeats = recent.count(h)
        return repeats >= self.max_repeats

    def trip(self, agent_name: str = "unknown", context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Record an override event. Call after check() returns True,
        when the supervisor injects the backtracking objective."""
        event = {
            "time_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "agent": agent_name,
            "last_states": len(self._history),
            "note": "circuit breaker tripped — supervisor override issued",
        }
        self.trips.append(event)
        self.tripped_at = event["time_utc"]
        return event

    def reset(self) -> None:
        """Call after a successful supervisor override / fresh approach,
        so the agent gets a clean window to try the new path."""
        self._history.clear()
        # trips/tripped_at are intentionally kept — audit trail


# --- wiring example for AgentOrchestrator (Patriarch controller) ---
class AgentOrchestrator:
    def __init__(self, breaker: Optional[AgentCircuitBreaker] = None):
        self.breaker = breaker or AgentCircuitBreaker()

    def execute_step(self, agent, context: Dict[str, Any]):
        action, params = agent.plan_next_step(context)

        # Agent swimming against the black rim?
        if self.breaker.check(action, params):
            self.breaker.trip(agent_name=getattr(agent, "name", "unknown"))
            return self.trigger_supervisor_override(agent, context)

        return agent.perform_action(action, params)

    def trigger_supervisor_override(self, agent, context: Dict[str, Any]):
        """Supervisor intervention (masking the rim / changing the local
        landscape): prune repetitive context, force a backtrack objective."""
        clean_context = {
            "goal": context["goal"],
            "system_override": (
                "CRITICAL: You are stuck in an execution loop hitting a "
                "boundary condition. Ignore your previous approach. "
                "Backtrack one step and explore an alternative path."
            ),
        }
        agent.reset_short_term_memory()
        return agent.plan_next_step(clean_context)
