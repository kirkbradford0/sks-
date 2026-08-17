# Agent Status Packet

Use this packet when AlphaBot, KinloaBot, GrokBot, Hermes, Codex, or any other SKS agent needs to report repo connection state, ownership, blockers, or handoff needs.

```json
{
  "agent": "AlphaBot | KinloaBot | GrokBot | Hermes | Codex",
  "repo": "kirkbradford0/sks-",
  "connection": "connected | blocked | pending",
  "branch": "string",
  "planned_paths": ["string"],
  "first_push_eta": "string",
  "needs_from_codex": ["string"]
}
```

## Rules

- Do not include secrets, tokens, private machine identifiers, or personal data.
- Prefer stable contracts over long prose.
- Use explicit branch names and file paths.
- Flag anything that requires user approval.
- If two agents plan to edit the same path, report it before pushing.

## Current Assignments

```json
{
  "KinloaBot": "building trade station",
  "AlphaBot": "building shop kiosk frontend guts",
  "GrokBot": "reply relay to Codex",
  "Hermes": "realtime information and coordination path",
  "Codex": "coordination, repo hygiene, contracts, and verification"
}
```
