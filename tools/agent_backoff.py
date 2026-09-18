"""Exponential backoff + cost kill switch — the recursive-work guard.

Companion to agent_circuit_breaker.py. The breaker stops a LOGIC loop
(same action repeated); this stops a FAILURE loop (exceptions retried
forever) and puts a hard wall-clock ceiling on any recursive/explosive
work so a runaway can never produce a surprise bill.

Origin: Kirk-supplied pattern (2026-09-18), hardened by Alpha:
  - max_retries enforced BEFORE sleeping (never sleep on a doomed retry)
  - wall-clock budget guard (secs) — catches slow-cost-explosion, not
    just fast failure loops (original only counted attempts)
  - optional per-call cost hook: max_spend_usd checked after each call
  - jitter to avoid synchronized fleet retries hammering a rate limit
  - reset on success so the next task starts fresh
  - named exception (EscalationLimit) instead of bare SystemError

Usage:
    backoff = ExponentialBackoffBreaker(max_retries=5, max_elapsed_s=120)
    result = execute_agent_task_with_rate_control(
        agent_func, args,
        backoff=backoff,
        cost_hook=lambda: running_cost_usd,   # optional
        max_spend_usd=0.50,                   # optional
    )
"""

import random
import time
from typing import Any, Callable, List, Optional


class EscalationLimit(RuntimeError):
    """Raised when retries, wall-clock, or spend budget is exhausted."""


class ExponentialBackoffBreaker:
    def __init__(
        self,
        base_delay: float = 1.0,
        max_delay: float = 60.0,
        backoff_factor: float = 2.0,
        max_retries: int = 5,
        max_elapsed_s: Optional[float] = None,
        jitter: float = 0.25,          # +-25% on each sleep
    ):
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.factor = backoff_factor
        self.max_retries = max_retries
        self.max_elapsed_s = max_elapsed_s
        self.jitter = jitter
        self.attempt = 0
        self.started_at: Optional[float] = None
        self.sleep_log: List[float] = []

    def _elapsed(self) -> float:
        if self.started_at is None:
            self.started_at = time.monotonic()
        return time.monotonic() - self.started_at

    def get_backoff_time(self) -> float:
        """Exponential delay with jitter, capped at max_delay."""
        delay = min(self.base_delay * (self.factor ** self.attempt), self.max_delay)
        delay *= 1.0 + random.uniform(-self.jitter, self.jitter)
        self.attempt += 1
        return max(delay, 0.0)

    def reset(self) -> None:
        self.attempt = 0
        self.started_at = None
        self.sleep_log.clear()


def execute_agent_task_with_rate_control(
    agent_func: Callable,
    args: tuple = (),
    kwargs: Optional[dict] = None,
    backoff: Optional[ExponentialBackoffBreaker] = None,
    cost_hook: Optional[Callable[[], float]] = None,
    max_spend_usd: Optional[float] = None,
    on_retry: Optional[Callable[[int, float, BaseException], None]] = None,
) -> Any:
    """Run agent_func with exponential backoff on failure.

    Kill switches (first one hit wins):
      1. max_retries attempts exhausted            -> EscalationLimit
      2. max_elapsed_s of wall clock burned        -> EscalationLimit (slow cost explosion)
      3. cost_hook() exceeds max_spend_usd         -> EscalationLimit (real money)
    """
    backoff = backoff or ExponentialBackoffBreaker()
    kwargs = kwargs or {}

    while True:
        # --- kill switches checked BEFORE each attempt, so a budget of N
        # means exactly N calls, never N+1 ---
        if backoff.attempt >= backoff.max_retries:
            raise EscalationLimit(
                f"Escalation limit: attempt budget {backoff.max_retries} "
                f"exhausted for {getattr(agent_func, '__name__', agent_func)}."
            )
        if backoff.max_elapsed_s is not None and backoff.attempt > 0 and backoff._elapsed() >= backoff.max_elapsed_s:
            raise EscalationLimit(
                f"Escalation limit: wall-clock budget {backoff.max_elapsed_s}s "
                f"exhausted after {backoff.attempt} retries."
            )
        if cost_hook is not None and max_spend_usd is not None and backoff.attempt > 0:
            try:
                spend = float(cost_hook())
            except Exception:
                spend = float("inf")   # broken cost meter = assume worst
            if spend >= max_spend_usd:
                raise EscalationLimit(
                    f"Escalation limit: spend ${spend:.2f} hit budget ${max_spend_usd:.2f}."
                )

        try:
            result = agent_func(*args, **kwargs)
            backoff.reset()          # success — next task starts fresh
            return result
        except (EscalationLimit, KeyboardInterrupt, SystemExit):
            raise                    # never backoff a kill signal
        except BaseException as e:
            sleep_time = backoff.get_backoff_time()
            backoff.sleep_log.append(sleep_time)
            if on_retry:
                on_retry(backoff.attempt, sleep_time, e)
            time.sleep(sleep_time)
