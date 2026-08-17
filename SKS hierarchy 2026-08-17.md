# SKS hierarchy - 2026-08-17

Purpose: current operating hierarchy for Felons Melon / SKS / Sparky and the agent swarm as of 2026-08-17.

## North Star

Felons Melon is the human-impact mission layer.

Its job is to keep the whole build pointed at people affected by AI, especially people facing second-chance employment barriers, automated screening, criminal-record drag, reentry friction, worker displacement, surveillance, and community costs from AI infrastructure.

## Operating Stack

```text
Felons Melon
  Human-impact mission, second-chance lens, worker dignity, appeal rights

SKS repo
  Public coordination board, source of truth, status packets, contracts, dated briefs

Sparky / Codex
  Coordinator, repo hygiene, contract drafting, verification, grounded summaries

Hermes
  Realtime research bridge, TwoAM congressional research engine, candidate-feed owner

GrokBot
  Relay / reply channel, external status and message board builder

KinloaBot
  Trade station builder, consumer of Hermes candidate-feed once contract is wired

AlphaBot
  Shop kiosk frontend guts, UI implementation and front-end connection work

Browser Harness
  Live browser bridge / precious gift: real browser state, uploads/downloads, logged-in workflows when safely connected
```

## Agent Roles

| Layer | Owner | Current Role | Current Artifact |
|---|---|---|---|
| Mission | Felons Melon | People-first AI impact compass | `SKS Felons Melon AI human impact 2026-08-17.md` |
| Coordination | SKS repo | Shared source of truth | https://github.com/kirkbradford0/sks- |
| Coordinator | Sparky / Codex | Contracts, repo hygiene, verification, summaries | `SKS Sparky AI awareness 2026-08-17.md` |
| Realtime | Hermes | Current information and TwoAM research pipeline | `SKS Hermes status packet.json` |
| Relay | GrokBot | Message/status board and cross-agent replies | pending status packet |
| Trade | KinloaBot | Trade station | pending status packet |
| Kiosk | AlphaBot | Shop kiosk frontend guts | pending status packet |
| Browser | browser-harness | Live browser operations and self-healing helper flow | https://github.com/browser-use/browser-harness |

## Authority Rules

1. User intent wins.
2. Human-impact constraints from Felons Melon guide product decisions.
3. SKS repo is the shared memory board for cross-agent state.
4. Status packets beat chat recollection.
5. Contracts beat assumptions.
6. Source links beat unsourced claims.
7. No public secrets, tokens, private machine identifiers, or unnecessary local paths.
8. High-stakes AI decisions need human review, appeal paths, and source trails.

## File Naming Convention

Visible coordination files should use spaced SKS names:

```text
SKS [subject] [date].md
SKS [agent] status packet.json
SKS [contract name] contract.md
```

Legacy/current exception:

```text
AGENT_STATUS_PACKET.md
```

Keep it for compatibility, but prefer spaced names for new board files.

## Current Gaps

- Need `SKS integration board.md` with active agent rows.
- Need `SKS candidate feed contract.md` to connect Hermes to KinloaBot.
- Need `SKS GrokBot status packet.json`.
- Need `SKS KinloaBot status packet.json`.
- Need `SKS AlphaBot status packet.json`.
- Need `SKS browser harness notes.md` after local connection/install details are known.

## Memory Pin

If Sparky gets asked what is going on, check this order:

1. `SKS hierarchy YYYY-MM-DD.md`
2. agent status packets
3. dated awareness briefs
4. contract files
5. live tools / web / browser harness when current state matters
