# Agent Status Packet

Use this packet when AlphaBot, KinloaBot, GrokBot, Hermes, Codex, or another SKS agent reports current ownership, interfaces, needs, blockers, next actions, or repo connection state.

The seven core keys preserve the SKS status/contract protocol. Optional connection metadata may be added but must not replace them.

```json
{
  "agent": "AlphaBot | KinloaBot | GrokBot | Hermes | Codex | string",
  "status": "working | waiting | blocked | offline | unknown",
  "owns": ["string"],
  "interfaces": [
    {
      "name": "string",
      "type": "string",
      "contract": "string"
    }
  ],
  "needs": ["string"],
  "blockers": ["string"],
  "next": ["string"],
  "date": "YYYY-MM-DD",
  "source": "evidence for this snapshot",
  "repo": "kirkbradford0/sks-",
  "connection": "connected | blocked | pending | unknown",
  "branch": "string",
  "planned_paths": ["string"]
}
```

## Rules

- Core keys are `agent`, `status`, `owns`, `interfaces`, `needs`, `blockers`, and `next`.
- Use arrays even for one item. Use an empty array when there is no verified item.
- Treat `date` and `source` as freshness evidence; a board assignment alone is not proof an agent is running.
- Use `unknown` or `waiting` instead of repeating an unverified `working` claim.
- Do not include secrets, tokens, private machine identifiers, unnecessary private paths, or personal data.
- Prefer explicit contracts over long prose.
- Use explicit branches and repository-relative paths when connection metadata is needed.
- Flag anything that requires user approval.
- If two agents plan to edit the same path, report the collision before pushing.
- Validate the JSON before committing it.

## Historical assignments (2026-08-17 snapshot; not runtime proof)

```json
{
  "KinloaBot": "building trade station",
  "AlphaBot": "building shop kiosk frontend guts",
  "GrokBot": "reply relay to Codex",
  "Hermes": "realtime information and coordination path",
  "Codex": "coordination, repo hygiene, contracts, and verification"
}
```

For current work, read `SKS single kanban board.md` and verify a live runtime/session before marking an agent `working`.
