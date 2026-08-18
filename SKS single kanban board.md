# SKS single kanban board

Updated: 2026-08-18

Purpose: one board for Sparky/Codex, Hermes, GrokBot, AlphaBot, KinloaBot, and future agents. Do not create competing boards unless this file points to them.

Canonical project map: `SKS canonical build index 2026-08-18.md`

## Rules

- One card = one outcome.
- Every card has an owner, lane, evidence link, and next action.
- Chat is for decisions. This board is for state.
- Felons Melon is the compass, not fog. Mention it when values or users matter; do not let it blur cash/app execution.
- Do not publish secrets, tokens, private machine identifiers, or unnecessary local paths.
- User does final submit on job applications, financial moves, public posts, and account/auth changes.

## Lanes

### NOW

| Card | Owner | Lane | Evidence | Next Action |
|---|---|---|---|---|
| Protect daily income lane | Kirk + Sparky | Cash / job survival | Google Drive `fm_7day_battle_plan_20260814.md` | Run today's job-search block before deep app work |
| Define Hermes -> Kinloa candidate-feed contract | Hermes + KinloaBot + Sparky | Trading / money path | `SKS Hermes status packet.json` | Publish `SKS candidate feed contract.md` |
| Get AlphaBot status into origin | AlphaBot + Sparky | Kiosk / frontend | pending | Publish `SKS AlphaBot status packet.json` |
| Get KinloaBot status into origin | KinloaBot + Sparky | Trade station | pending | Publish `SKS KinloaBot status packet.json` |
| Keep Grok board aligned with origin | GrokBot + Sparky | Coordination | `SKS GrokBot status packet.json` | Confirm whether to keep top-level SKS board, `board/`, or both |
| Convert handwritten notes into cards | Kirk + Sparky | Intake | incoming handwritten notes | Convert each note into kanban cards and GitHub board updates |

### NEXT

| Card | Owner | Lane | Evidence | Next Action |
|---|---|---|---|---|
| AutoFlow paid pilot cut | Sparky + Kirk | Shippable app / cash | Lovable `AutoFlow Solutions`, `Pocket Work Order Pro` | Decide smallest paid pilot offer for one shop |
| Consolidate AutoFlow + KAS Lite | AlphaBot/Sparky | Auto shop tools | Lovable project inventory | Identify overlapping flows: intake, estimate, budget cap, RO export |
| Build SKS browser harness notes | Sparky | Tools | browser-use/browser-harness | Document safe setup and usage once connected locally |
| Pull FM landing components | Sparky/AlphaBot | Felons Melon product | Drive inventory: `Idea-Repo-123-` branch | Reuse Hero/CTA/FMScore only after cash lane is protected |
| Port FM core modules | Sparky/AlphaBot | Felons Melon product | GitHub `Felon-s-Melon-2.0` | Extract check-in, craving journal, mentor flow, AA steps later |
| Update job tracker | Kirk + Sparky | Cash / job survival | Employment Engine Run Drive doc | Log applications, statuses, follow-ups |

### BACKLOG

| Card | Owner | Lane | Evidence | Next Action |
|---|---|---|---|---|
| Human-impact tracker | Sparky | Felons Melon mission | `SKS Felons Melon AI human impact 2026-08-17.md` | Turn design rules into product checklist |
| Context Bridge / Markup review | GrokBot/Sparky | Coordination tools | Lovable `Context Bridge` | Decide if it becomes visual SKS board UI |
| Proof Engine review | Sparky | FM product | Lovable `yourproof` | Compare against `Felon-s-Melon-2.0` before choosing main app |
| Judge's Advocate monetization | Sparky/Kirk | Small utility | Lovable `felonsbestfriend` | Decide whether to sell/free as FM gadget |
| Market Terrain Map cannibalization | Hermes/Sparky | Trading research | Lovable `Market Terrain Map` | Pull evidence-led UI concepts into TwoAM only if useful |
| Memory House review | Sparky | Memory/tools | Lovable `seemyfiles` | Cannibalize visual memory metaphor later |

### WAITING / BLOCKED

| Card | Owner | Lane | Blocker | Unblock |
|---|---|---|---|---|
| GrokBot local board push | GrokBot | Coordination | Local GitHub auth hang | User/Grok completes auth or Sparky keeps mirrored top-level board |
| Lovable desktop account switch | Kirk | Lovable | Desktop app may not be on desired account | Connector now sees `Kirk's Lovable`; user handles desktop login if needed |
| Full Lovable project completeness | Sparky | Inventory | Workspace reports 36 projects; connector page returned visible project summaries | Re-query later if additional pagination/results become available |
| Auto-apply employment engine | Kirk/Sparky | Job survival | CAPTCHAs, logins, ToS, final submit risk | Keep materials engine; user final-submits applications |

### DONE

| Card | Owner | Lane | Evidence |
|---|---|---|---|
| Create SKS repo source-of-truth board | Sparky | Coordination | `SKS integration board.md` |
| Add today's hierarchy | Sparky | Coordination | `SKS hierarchy 2026-08-17.md` |
| Add Sparky AI awareness brief | Sparky | Awareness | `SKS Sparky AI awareness 2026-08-17.md` |
| Add Felons Melon human-impact AI brief | Sparky | Mission | `SKS Felons Melon AI human impact 2026-08-17.md` |
| Add Hermes status packet | Sparky/Hermes | Realtime | `SKS Hermes status packet.json` |
| Add GrokBot status packet | Sparky/GrokBot | Coordination | `SKS GrokBot status packet.json` |
| Connect Lovable connector | Kirk + Sparky | Inventory | Workspace `Kirk's Lovable`, 36 projects reported |
| Create canonical build index | Sparky | Inventory | `SKS canonical build index 2026-08-18.md` |

## Card Template

```json
{
  "title": "string",
  "owner": "Kirk | Sparky | Hermes | GrokBot | AlphaBot | KinloaBot",
  "lane": "cash | app | mission | coordination | archive",
  "status": "now | next | backlog | waiting | done",
  "evidence": ["repo/file/url"],
  "next_action": "one concrete move",
  "blocked_by": []
}
```

## Intake Rule For Handwritten Notes

When Kirk sends handwritten material:

1. Transcribe the note.
2. Extract decisions, project names, tasks, blockers, and deadlines.
3. Add or update cards in this file.
4. If a note defines a new project, add it to `SKS canonical build index 2026-08-18.md` or its newest replacement.
5. Keep the original note context available by linking the source if it is stored in Drive/GitHub.
