# SKS repository governance — 2026-08-30

Purpose: define which SKS documents control which kind of state, preserve the status/contract protocol, and stop snapshots from becoming competing sources of truth.

## Repository identity

- Canonical remote: `https://github.com/kirkbradford0/sks-.git` (the trailing dash is part of the name).
- Default and working branch: `main`, tracking `origin/main`.
- Authentication: Git for Windows Credential Manager (`credential.helper=manager`). Never put tokens in remotes, files, status packets, or handoffs.
- Update loop: `pull -> read canonical board -> update owned state -> validate -> commit -> push -> verify remote`.

## Source precedence

1. `SKS single kanban board.md` — only active cross-agent work queue and current command doctrine.
2. `SKS canonical build index 2026-08-18.md` (or a newer replacement explicitly linked by the board) — project and artifact inventory.
3. `SKS [agent] status packet.json` — dated agent-owned snapshot; its date and evidence determine freshness.
4. `SKS [contract name] contract.md` — interface contract; beats prose and chat assumptions.
5. `SKS integration board.md` — compatibility glance snapshot only; it must not become a second work queue.
6. `SKS hierarchy 2026-08-17.md`, project maps, briefs, and mission packages — dated reference snapshots.
7. `SKS Hermes handoff YYYY-MM-DD.md` and run receipts — append-only evidence of sessions, not live state.

When sources disagree, use the highest applicable source above, verify live state where possible, and record the discrepancy rather than silently choosing the most convenient claim.

## JSON status/contract protocol

Every agent status packet keeps these core keys:

```json
{
  "agent": "string",
  "status": "working | waiting | blocked | offline | unknown",
  "owns": [],
  "interfaces": [],
  "needs": [],
  "blockers": [],
  "next": []
}
```

Optional metadata such as `date`, `version`, `source`, `repo`, `connection`, `branch`, and `planned_paths` may be added without replacing the core keys. A board assignment is not runtime proof. Use `unknown` or `waiting` when current execution cannot be verified.

## Duplicate and stale-source audit

No file was removed during the 2026-08-30 audit. The following are retained but must be read with these limits:

- `SKS integration board.md` duplicates agent and work status from the canonical board and has not been refreshed since 2026-08-17. It is a compatibility snapshot, not the active queue.
- `SKS hierarchy 2026-08-17.md` contains a dated `Current Gaps` list that already names the now-existing integration board and GrokBot packet as missing.
- `AGENT_STATUS_PACKET.md` used a connection-oriented shape that omitted the seven core status keys. It is now a compatibility-aware template using the core protocol plus optional connection metadata.
- `SKS Hermes status packet.json` is valid JSON but dated 2026-08-17; its GitHub/CLI blocker and delivery claims require live verification before reuse.
- `SKS GrokBot status packet.json` is valid JSON but dated 2026-08-17; its local-ahead/push-hang claim is historical until GrokBot supplies evidence.
- `SKS FlowBot status packet.json` is valid JSON but dated 2026-08-19; runtime availability should be rechecked before assignment.
- The old `README.md` did not identify canonical documents; it now points readers here first.

## Hygiene and session close

- Never commit `.env` files, tokens, credentials, private keys, machine identifiers, or unnecessary private local paths.
- Validate every JSON packet before committing.
- Stage named files rather than sweeping unrelated worktree files into a commit.
- Preserve another agent's untracked or modified files unless ownership is confirmed.
- End every Hermes work session with `SKS Hermes handoff YYYY-MM-DD.md`, then commit, push, and verify the remote commit.
- Handoffs must distinguish observed facts from unresolved or historical claims.
