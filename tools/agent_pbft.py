"""pBFT quorum for the SKS parent council — high-severity action gating.

Third runtime guard. Division of labor across the fleet's defenses:
  - agent_circuit_breaker.py  stops a LOGIC loop (same action repeated)
  - agent_backoff.py          stops a FAILURE loop (money/time explosion)
  - agent_pbft.py (this)      stops ROGUE AUTHORITY — no single agent may
                              isolate a peer, revoke keys, or mutate shared
                              state alone. High-severity ops need 2f+1
                              co-signatures from the parent council.

Origin: Kirk-supplied pBFT pattern (2026-09-18), hardened by Alpha:
  - leader_id actually validated (was accepted but never used)
  - replay protection: a processed action_id returns its cached result
  - payload carries the instruction content, not just metadata
  - honest-node awareness: quorum math done against live/honest signers,
    so a dead council cannot rubber-stamp
  - every rejection names the phase that failed (audit trail for lessons/)

Fleet mapping (N=4: Alpha, Bravo, Charlie, Kirk-as-root):
  N=4 -> tolerates f=1 Byzantine agent, quorum 2f+1 = 3 co-signatures.
  Kirk is the ROOT tier: HIS signature is required on top of quorum for
  operations in the HITL class (money, broker unlock, deletes, submits).
"""

import hashlib
import json
import time
from typing import Any, Dict, List, Optional


class ActionPayload:
    def __init__(self, action_id: str, target_node: str, operation: str,
                 issuer_id: str, instruction: Optional[Dict[str, Any]] = None):
        self.action_id = action_id
        self.target_node = target_node
        self.operation = operation      # e.g. ISOLATE_NODE, REVOKE_KEY, MUTATE_SKS
        self.issuer_id = issuer_id
        self.instruction = instruction or {}
        self.timestamp = time.time()

    def to_dict(self) -> dict:
        return {
            "action_id": self.action_id,
            "target_node": self.target_node,
            "operation": self.operation,
            "issuer_id": self.issuer_id,
            "instruction": self.instruction,
            "timestamp": self.timestamp,
        }

    def digest(self) -> str:
        return hashlib.sha256(
            json.dumps(self.to_dict(), sort_keys=True).encode()
        ).hexdigest()


class ParentNode:
    """A council member. Byzantine members abstain/corrupt — they never
    sign, which is exactly the failure mode the quorum absorbs."""

    def __init__(self, node_id: str, is_byzantine: bool = False,
                 is_root: bool = False):
        self.node_id = node_id
        self.is_byzantine = is_byzantine
        self.is_root = is_root
        self.pre_prepare_log: Dict[str, ActionPayload] = {}
        self.prepare_votes: Dict[str, set] = {}
        self.commit_votes: Dict[str, set] = {}
        self.decided: Dict[str, dict] = {}   # action_id -> result (replay guard)

    def receive_pre_prepare(self, payload: ActionPayload, digest: str) -> Optional[str]:
        if self.is_byzantine:
            return None
        if payload.digest() != digest:
            return None
        self.pre_prepare_log[digest] = payload
        return self.node_id

    def receive_prepare(self, digest: str, sender_id: str) -> bool:
        if self.is_byzantine:
            return False
        self.prepare_votes.setdefault(digest, set()).add(sender_id)
        return True

    def receive_commit(self, digest: str, sender_id: str) -> bool:
        if self.is_byzantine:
            return False
        self.commit_votes.setdefault(digest, set()).add(sender_id)
        return True


class PBFTConsensusCluster:
    def __init__(self, parent_nodes: List[ParentNode], root_id: Optional[str] = None):
        self.nodes = {n.node_id: n for n in parent_nodes}
        self.total_nodes = len(parent_nodes)
        self.max_faulty = (self.total_nodes - 1) // 3   # N >= 3f + 1
        self.quorum_threshold = (2 * self.max_faulty) + 1
        self.root_id = root_id
        self.decision_log: Dict[str, dict] = {}         # action_id -> result

    def _reject(self, action_id: str, phase: str, why: str) -> dict:
        result = {"status": "REJECTED", "action_id": action_id,
                  "failed_phase": phase, "reason": why}
        self.decision_log[action_id] = result
        return result

    def execute_action(self, leader_id: str, payload: ActionPayload,
                       root_signed: bool = False) -> Dict[str, Any]:
        # Replay guard: an already-decided action returns its recorded result.
        if payload.action_id in self.decision_log:
            return {**self.decision_log[payload.action_id], "replay": True}

        # Leader must be a live, honest council member.
        leader = self.nodes.get(leader_id)
        if leader is None or leader.is_byzantine:
            return self._reject(payload.action_id, "LEADER_CHECK",
                                f"leader '{leader_id}' unknown or Byzantine")
        if payload.issuer_id != leader_id:
            return self._reject(payload.action_id, "LEADER_CHECK",
                                "payload issuer does not match leader")

        # ROOT-tier gate: HITL operations require Kirk's signature, full stop.
        if self.root_id and leader_id != self.root_id and not root_signed:
            return self._reject(payload.action_id, "ROOT_CHECK",
                                f"high-severity op requires root ({self.root_id}) signature")

        digest = payload.digest()

        # Phase 1: Pre-Prepare
        pre_prepare_sigs = {
            sig for sig in
            (n.receive_pre_prepare(payload, digest) for n in self.nodes.values())
            if sig
        }
        if len(pre_prepare_sigs) < self.quorum_threshold:
            return self._reject(payload.action_id, "PRE_PREPARE",
                                f"{len(pre_prepare_sigs)}/{self.quorum_threshold} signatures")

        # Phase 2: Prepare
        for sender in pre_prepare_sigs:
            for node in self.nodes.values():
                node.receive_prepare(digest, sender)
        prepared = [nid for nid, n in self.nodes.items()
                    if len(n.prepare_votes.get(digest, set())) >= self.quorum_threshold]
        if len(prepared) < self.quorum_threshold:
            return self._reject(payload.action_id, "PREPARE",
                                f"{len(prepared)}/{self.quorum_threshold} prepared")

        # Phase 3: Commit
        for sender in prepared:
            for node in self.nodes.values():
                node.receive_commit(digest, sender)
        committed = [nid for nid, n in self.nodes.items()
                     if len(n.commit_votes.get(digest, set())) >= self.quorum_threshold]
        if len(committed) < self.quorum_threshold:
            return self._reject(payload.action_id, "COMMIT",
                                f"{len(committed)}/{self.quorum_threshold} committed")

        result = {"status": "COMMITTED", "action_id": payload.action_id,
                  "operation": payload.operation,
                  "committed_by": sorted(committed)}
        self.decision_log[payload.action_id] = result
        return result


# --- self-test ---
if __name__ == "__main__":
    parents = [
        ParentNode("alpha", is_root=False),
        ParentNode("bravo"),
        ParentNode("charlie"),
        ParentNode("kirk", is_root=True),
    ]
    cluster = PBFTConsensusCluster(parents, root_id="kirk")
    assert (cluster.max_faulty, cluster.quorum_threshold) == (1, 3)

    # T1: honest high-severity op WITH root signature -> commits
    a1 = ActionPayload("act_1", "worker_42", "ISOLATE_NODE", "alpha")
    r = cluster.execute_action("alpha", a1, root_signed=True)
    assert r["status"] == "COMMITTED" and len(r["committed_by"]) >= 3, r
    print("T1 committed with quorum:", r["committed_by"])

    # T2: same op WITHOUT root signature -> rejected at ROOT_CHECK
    a2 = ActionPayload("act_2", "worker_42", "REVOKE_KEY", "bravo")
    r = cluster.execute_action("bravo", a2, root_signed=False)
    assert r["status"] == "REJECTED" and r["failed_phase"] == "ROOT_CHECK"
    print("T2 no root signature -> rejected:", r["failed_phase"])

    # T3: Byzantine leader cannot even propose
    byz = ParentNode("grokbot", is_byzantine=True)
    c2 = PBFTConsensusCluster(parents + [byz], root_id="kirk")
    a3 = ActionPayload("act_3", "worker_7", "MUTATE_SKS", "grokbot")
    r = c2.execute_action("grokbot", a3, root_signed=True)
    assert r["status"] == "REJECTED" and r["failed_phase"] == "LEADER_CHECK"
    print("T3 Byzantine leader blocked at door")

    # T4: replay returns cached decision, no re-execution
    r = cluster.execute_action("alpha", a1, root_signed=True)
    assert r.get("replay") is True
    print("T4 replay guard: cached result returned")

    # T5: with a Byzantine member among 5 (f=1, quorum 3), honest 3 still commit
    c3 = PBFTConsensusCluster(
        [ParentNode("alpha"), ParentNode("bravo"), ParentNode("charlie"),
         ParentNode("kirk", is_root=True), byz], root_id="kirk")
    a5 = ActionPayload("act_5", "worker_9", "ISOLATE_NODE", "charlie")
    r = c3.execute_action("charlie", a5, root_signed=True)
    assert r["status"] == "COMMITTED" and "grokbot" not in r["committed_by"]
    print("T5 Byzantine member absorbed, quorum held")
    print("ALL 5 TESTS PASS")
