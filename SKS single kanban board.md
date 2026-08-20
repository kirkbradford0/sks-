# SKS single kanban board

Updated: 2026-08-20

Purpose: one board for Sparky/Codex, Hermes, GrokBot, AlphaBot, KinloaBot, FlowBot, and future agents. Do not create competing boards unless this file points to them.

Canonical project map: `SKS canonical build index 2026-08-18.md`

## Rules

- One card = one outcome.
- Every card has an owner, lane, evidence link, and next action.
- Chat is for decisions. This board is for state.
- Felons Melon is the compass, not fog. Mention it when values or users matter; do not let it blur cash/app execution.
- Do not publish secrets, tokens, private machine identifiers, or unnecessary local paths.
- User does final submit on job applications, financial moves, public posts, production deploy approval, and account/auth changes.
- For the 2026-08-21 push: Kirk protects the job-hunt lane. The agent swarm handles Felons Melon final deployment cleanup in parallel.
- FINAL DEPLOYMENT means cleanup, verification, hardening, and release. No new feature expansion unless Kirk explicitly reopens scope.
- A board assignment is not proof an agent is running. Confirm a real runtime/session/poller before treating work as in progress.

## Lanes

### NOW

| Card | Owner | Lane | Evidence | Next Action |
|---|---|---|---|---|
| Protect daily income lane | Kirk + Sparky | Cash / job survival | `SKS project map 2026-08-19.md`; `job-hunt/` | Kirk runs applications/interviews first; Sparky handles tailoring, research, tracker updates, and follow-up support |
| Verify active agent runtimes | Sparky + Hermes | Coordination | agent status packets; current SKS board | Confirm which agents actually have a live runtime/session that can read SKS; mark inactive agents as waiting instead of pretending they are working |
| Lock one canonical FM production repo + branch | Sparky/Codex | Felons Melon deployment | Drive `FelonsMelon_Code_Inventory_FINAL_Aug19_2026_DRAFT_EMAIL.md`; `SKS canonical build index 2026-08-18.md` | Choose the production repo/branch, record it here, freeze duplicate build paths, and create a rollback tag/commit before changes |
| Finish FM landing + domain release path | AlphaBot + Codex | Felons Melon deployment | `kirkbradford0/Idea-Repo-123-` branch `claude/rebuild-fm-landing-5jxdV` | Reuse the strongest Hero/CTA/FMScore/HowItWorks components, remove dead links/placeholders, verify responsive layout, then produce a deployable preview |
| Verify Supabase/auth/data boundaries | Codex + Sparky | Felons Melon hardening | FM NOW master; existing Supabase integration | Verify required env vars, auth/guest behavior, RLS, proof/check-in writes, and failure handling using redacted evidence only; do not expose service keys in SKS |
| Run production smoke test | Browser Harness + Sparky | Felons Melon QA | live/preview URL after deploy candidate exists | Test desktop + mobile landing, navigation, CTA, signup/guest entry, form validation, 404s, refresh/deep links, and obvious console/network failures |
| Run independent public-copy/link QA | GrokBot | Felons Melon QA | deploy candidate + Aug 19 inventory | Check public claims, spelling, metadata, title/description, broken links, contact paths, and whether every major CTA leads somewhere real; return only evidence-backed fixes |
| Enforce security/privacy release gate | Sparky + Codex reviewer split | Felons Melon hardening | FM NOW master G14-G15 rules; `03_HARDENING_PROMPT — Secure, Stabilize, and Release` | Confirm no secrets/private records in client bundle, logs, GitHub, analytics, or public error output; builder and reviewer must be distinct on high-risk changes |
| Create release receipt + rollback play | FlowBot + Sparky | Felons Melon release | results from build, QA, auth, privacy, and deploy checks | Produce one go/no-go record containing commit, deployed target, checks passed/failed, blockers, owner, and exact rollback point |
| Freeze non-job/non-FM build expansion for this push | Sparky | Coordination | user directive 2026-08-20 | Keep trading, AutoFlow expansion, archive mining, and new FM features out of NOW until job hunt block and FM release gate are complete |

### FINAL FM RELEASE GATE

Felons Melon is GO only when all of these are evidenced:

- Canonical production repo and branch are recorded.
- A rollback commit/tag exists before release changes.
- Production build completes without unresolved release-blocking errors.
- Domain/HTTPS and primary route load correctly.
- Mobile and desktop smoke tests pass.
- Major navigation and CTAs lead to real destinations.
- Supabase/auth/guest flows behave as intended.
- RLS/data-write checks pass where applicable.
- No secrets or sensitive user data appear in public client code, logs, GitHub, analytics, or error messages.
- Public copy contains no known false or unsupported claims.
- One independent reviewer verifies the release-critical work.
- Release receipt records PASS, BLOCKED, or ROLLBACK with evidence.

### NEXT

| Card | Owner | Lane | Evidence | Next Action |
|---|---|---|---|---|
| FM core module port after release | Sparky/AlphaBot | Felons Melon product | GitHub `Felon-s-Melon-2.0` | After landing/release is stable and Kirk reopens scope, extract only the highest-value check-in/craving/mentor flows into the canonical app |
| Run FM article traffic lane | Hermes + GrokBot + Sparky | Felons Melon marketing | `kirkbradford0/sks-skills`; `SKS Hermes article pipeline built 2026-08-18.md` | After release gate passes, produce evidence-backed posts that point to the live FM experience; Kirk handles final public post action |
| Update job tracker | Kirk + Sparky | Cash / job survival | Employment Engine Run Drive docs | Log applications, statuses, follow-ups, and next-contact dates |
| AutoFlow paid pilot cut | Sparky + Kirk | Shippable app / cash | Lovable `AutoFlow Solutions`, `Pocket Work Order Pro` | Resume only after the current job-hunt + FM deployment push |
| Consolidate AutoFlow + KAS Lite | AlphaBot/Sparky | Auto shop tools | Lovable project inventory | Resume only after the current job-hunt + FM deployment push |
| Define Hermes -> Kinloa candidate-feed contract | Hermes + KinloaBot + Sparky | Trading / money path | `SKS Hermes status packet.json` | Resume after the current job-hunt + FM deployment push |
| Build SKS browser harness notes | Sparky | Tools | browser-use/browser-harness | Document safe setup and usage once local/runtime connection details are confirmed |

### BACKLOG

| Card | Owner | Lane | Evidence | Next Action |
|---|---|---|---|---|
| Human-impact tracker | Sparky | Felons Melon mission | `SKS Felons Melon AI human impact 2026-08-17.md` | Turn design rules into product checklist |
| Context Bridge / Markup review | GrokBot/Sparky | Coordination tools | Lovable `Context Bridge` | Decide if it becomes visual SKS board UI |
| Proof Engine review | Sparky | FM product | Lovable `yourproof` | Compare against canonical production app after release before importing anything |
| Judge's Advocate monetization | Sparky/Kirk | Small utility | Lovable `felonsbestfriend` | Decide whether to sell/free as FM gadget after release |
| Market Terrain Map cannibalization | Hermes/Sparky | Trading research | Lovable `Market Terrain Map` | Pull evidence-led UI concepts into TwoAM only if useful later |
| Memory House review | Sparky | Memory/tools | Lovable `seemyfiles` | Cannibalize visual memory metaphor later |

### WAITING / BLOCKED

| Card | Owner | Lane | Blocker | Unblock |
|---|---|---|---|---|
| AlphaBot deployment assignment | AlphaBot + Sparky | FM frontend | No current AlphaBot status packet/runtime proof in SKS | Publish/refresh `SKS AlphaBot status packet.json` and confirm target repo/branch |
| Browser Harness release test | Browser Harness + Sparky | FM QA | Requires a reachable deploy candidate and connected browser runtime | Provide/resolve deploy candidate, then run smoke test |
| GrokBot local board push | GrokBot | Coordination | Local GitHub auth hang may still apply | Grok confirms current status; top-level SKS board remains canonical |
| KinloaBot work | KinloaBot + Sparky | Trade station | Deliberately deprioritized for current push | Resume after job-hunt + FM deployment release gate |
| Auto-apply employment engine | Kirk/Sparky | Job survival | CAPTCHAs, logins, ToS, final submit risk | Keep materials/research engine; Kirk final-submits applications |

### DONE

| Card | Owner | Lane | Evidence |
|---|---|---|---|
| Create SKS repo source-of-truth board | Sparky | Coordination | `SKS integration board.md` |
| Add hierarchy | Sparky | Coordination | `SKS hierarchy 2026-08-17.md` |
| Add Sparky AI awareness brief | Sparky | Awareness | `SKS Sparky AI awareness 2026-08-17.md` |
| Add Felons Melon human-impact AI brief | Sparky | Mission | `SKS Felons Melon AI human impact 2026-08-17.md` |
| Add Hermes status packet | Sparky/Hermes | Realtime | `SKS Hermes status packet.json` |
| Add GrokBot status packet | Sparky/GrokBot | Coordination | `SKS GrokBot status packet.json` |
| Connect Lovable connector | Kirk + Sparky | Inventory | Workspace inventory completed |
| Create canonical build index | Sparky | Inventory | `SKS canonical build index 2026-08-18.md` |
| Onboard FlowBot | Kirk + Sparky | Coordination / tools | `SKS FlowBot status packet.json` |
| Consolidate FM code/assets final inventory | Grok / SKS | Felons Melon inventory | Drive `FelonsMelon_Code_Inventory_FINAL_Aug19_2026_DRAFT_EMAIL.md` |

## Card Template

```json
{
  "title": "string",
  "owner": "Kirk | Sparky | Codex | Hermes | GrokBot | AlphaBot | KinloaBot | FlowBot | Browser Harness",
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
