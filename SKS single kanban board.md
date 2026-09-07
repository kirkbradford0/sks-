# SKS single kanban board

Updated: 2026-08-30

Purpose: one board for Sparky/Codex, Hermes, GrokBot, AlphaBot, KinloaBot, FlowBot, Bravo, Charlie, MedicBot, and future agents. Do not create competing boards unless this file points to them.

Fleet identity + runtime proof (who is actually alive, which Telegram bot): `SKS fleet roster 2026-09-07.md`. Chat is not state. SKS is the only Source of Truth.

September pointing document (same direction for every agent): `SKS STRIKE TEAM SEPT handoff 2026-09-07.md`. Not a second board.

Repository governance and source precedence: `SKS repository governance 2026-08-30.md`

Canonical project map: `SKS canonical build index 2026-08-18.md`

Snowball worker contract: `SKS Snowball execution contract.md`

Hermes execution cockpit: Kanban board `snowball-command`. `ACTIVE` means status `running`; `ready` and `todo` are queued. Global WIP governor: `kanban.max_in_progress = 3`.

## Command & Life Map Schema (Strike Force Playbook)

Status: ACTIVE — inserted 2026-08-23 per Kirk (H.I.L. Governor) directive. This is the command hierarchy, project portfolio, cost model, and reasoning pipeline for the SKS strike team. Treat it as canonical doctrine until Kirk revises it.

```text
                               ┌───────────────────────────┐
                               │   KIRK BRADFORD (H.I.L.)  │
                               │   Human-in-the-Loop Governor│
                               └─────────────┬─────────────┘
                                             │
                       ┌─────────────────────┴─────────────────────┐
                       ▼                                           ▼
         ┌───────────────────────────┐               ┌───────────────────────────┐
         │   SPARKY / OPENAI ($110)  │               │   HERMES / OPENCLAW ($20) │
         │   Mind / Orchestrator     │               │   Body / Execution Engine │
         └─────────────┬─────────────┘               └─────────────┬─────────────┘
                       │                                           │
         ┌─────────────┴─────────────┐               ┌─────────────┴─────────────┐
         ▼                           ▼               ▼                           ▼
  ┌──────────────┐            ┌──────────────┐┌──────────────┐            ┌──────────────┐
  │  WET TEAMS   │            │  DRY TEAMS   ││ CLAW ENGINE  │            │  REPOS & DB  │
  │ ChatGPT,     │            │ Terminal,    ││ 7 Claw System│            │ SKS, SKS     │
  │ Codex, Grok  │            │ Claude Code, ││ (Patriarch) │            │ Skills, D:\  │
  │ + Hermes     │            │ Gemini, etc. │└──────────────┘            └──────────────┘
  └──────────────┘            └──────────────┘
```

### 1. AI Agent Strike Team & Operating Costs

| Agent | Role / Alias | Engine Function | Cost / Allocation |
|---|---|---|---|
| Orchestrator | Sparky (OpenAI / ChatGPT) | Mind / Consciousness: Translates Kirk's intent into explicit execution plans, orchestrates agent loops, performs meta-evaluation. | $110 / month |
| Execution Engine | Hermes / OpenClaw | Body / Hands: Code generation, task automation, file operations, web scraping, and terminal actions. | $20 / month (Ollama + API) |
| Wet Teams | Hybrid Orchestration | ChatGPT OpenAI, Codex, DeepSeek V4, Grok paired directly with Hermes for heavy logic and math. | Variable API Usage |
| Dry Teams | Terminal Autonomous | Grok in Terminal, Claude Code Terminal, Gemini, Lovable agents. | Subscription / API |

### 2. Core Project Portfolio & Repositories

```text
                       ┌───────────────────────────────────────────┐
                       │          KIRK'S PROJECT ECOSYSTEM         │
                       └─────┬───────────────────┬───────────┬─────┘
                             │                   │           │
            ┌────────────────┴┐          ┌───────┴──────┐   └────────────────┐
            ▼                 ▼          ▼              ▼                    ▼
     ┌──────────────┐  ┌────────────┐┌──────────────┐┌──────────────┐  ┌───────────┐
     │ FELONS MELON │  │ AUTOMOTIVE ││ DATA & MEDIA ││ JOB & TRADING│  │ SKS ARCH  │
     │  REENTRY PLAT│  │  SOLUTIONS ││ KINLOASLATE  ││ ENGINES      │  │ REPOSITOR │
     └──────────────┘  └────────────┘└──────────────┘└──────────────┘  └───────────┘
```

**A. Felon's Melon (felonsmelon.com)** — Reentry platform combining automated legal narrative generation, daily budgeting, job/networking tools, and therapy booking.

Core Modules:
- FM Budget Module: 5-step financial system (M1 Take-Home, M2 Monthly Nut, M3 Trap Wall, M4 Daily Number, M5 Exit Ramp).
- Recovery & Therapy Network: Direct booking engine for online therapy, life skills courses, and legal/narrative generation.
- Automated Publishing Loop: Daily generation of 2–3 articles connecting justice-impacted stories, auto tools, spirituality, and reentry support across Medium, Substack, and social channels.

**B. Automotive Repair Software Suite**
- Bradford Automotive / Sparky Auto: Kiosk and shop management system running on local hardware and server backends.
- Pocket Bays CRM: Work order processing, repair closer, and scheduling suite (The "Kobayashi Maru" repair scheduler).
- Automotive Kiosk: Customer self-intake hardware and digital shop front, targeted for deployment within 30 days.

**C. Content Engine & KinloaSlate Memory**
- KinloaSlate: Long-term external memory architecture and media engine storing historical context, state deltas, and brand assets.
- Content Production Goal: 70 articles produced via Sparky/Hermes loop for YouTube, VTubing/Forecasting, and Substack, driving traffic directly into Felon's Melon and auto shop tools.

**D. Job Generation & Trading Systems**
- Lead Gen & Scraping: Alpha Kinloa, KirkHermes BOT, and Killchain scrapers targeting job listings and client outreach.
- Trading Engine: Swing trading + covered call strategies designed to grow monthly capital reserves and build the emergency firewall.

### 3. Repository Architecture & Storage (SKS)

```text
┌────────────────────────────────────────────────────────────────────────┐
┌────────────────────────────────────────────────────────────────────────┐
│                          SKS (STRIKE TEAM SYSTEM)                      │
├────────────────────────────────────────────────────────────────────────┤
│ • SKS Main Repo: Onboarding, strategy, logic flows, execution plans   │
│ • SKS SKILLS (Private Repo): Hermes execution prompts & agent skills  │
│ • SKS Phase I (D:\ Ext Drive): Archives, Marketing, KinloaSlate Memory │
│ • SKS Phase III: Server backends for Kiosks, Pocket Bays, & Shop CRM   │
└────────────────────────────────────────────────────────────────────────┘
```

### 4. Architectural Agentic Loops & Reasoning Pipeline

Every task passes through an extended 8-Stage Agentic Loop before output is finalized:

```text
[Stage 1: UNDERSTAND] ──► [Stage 2: PLAN] ──► [Stage 3: EXECUTE]
         ▲                                            │
         │                                            ▼
[Stage 5: ITERATE]   ◄── [More Tools?] ◄── [Stage 4: VERIFY]
         │                     │ (No)
         ▼                     ▼
[Stage 7: OPTIMIZE] ──► [Stage 6: SUMMARIZE]
         │                     │
         ▼                     ▼
[Stage 8: PATRIARCH] ──► Final Delivery / New Plan Assigned
```

- **Understand**: Parse request, classify user intent.
- **Plan**: Determine tool sequence and execution order.
- **Execute**: Run local commands, call tools, and generate code/SQL.
- **Verify**: Test results and validate outputs against requirements.
- **Iterate**: Loop back with updated context if additional tools are needed.
- **Summarize**: Deliver finalized response under safety counter limits (max_loop_iterations = 5).
- **Optimize & Educate**: Refine underlying prompts and document learned patterns.
- **Patriarch Assignment**: Patriarch evaluates system state, re-allocates sub-agents, and initiates new goals.

### 5. The 7 Claw OpenClaw System (Command Hierarchy)

```text
                          ┌───────────────────────────┐
                          │   KIRK (Human Governor)   │
                          └─────────────┬─────────────┘
                                        │
                          ┌─────────────▼─────────────┐
                          │   SPARKY (Orchestrator)   │
                          └─────────────┬─────────────┘
                                        │
                     ┌──────────────────┴──────────────────┐
                     ▼                                     ▼
        ┌─────────────────────────┐           ┌─────────────────────────┐
        │  HERMES / OPENCLAW RUN  │           │   KINLOASLATE MEMORY    │
        └────────────┬────────────┘           └─────────────────────────┘
                     │
 ┌───────────┬───────┴───┬───────────┬───────────┬───────────┬───────────┐
 ▼           ▼           ▼           ▼           ▼           ▼           ▼
Claw 1      Claw 2      Claw 3      Claw 4      Claw 5      Claw 6      Claw 7
SCOUT       INTAKE      SCORE       RESEARCH    ROUTER      PRODUCTION  VERIFICATION
```

- **Claw 1 (SCOUT)**: Observes environment without interpretation (Alpha = external web/job signals, Bravo = internal codebase discovery, Charlie = contradiction detection).
- **Claw 2 (INTAKE)**: Evaluates incoming signals, classifies data, and verifies provenance.
- **Claw 3 (SCORE)**: Deduplicates, evaluates value, and prioritizes action items.
- **Claw 4 (RESEARCH)**: Contextualizes queries, identifies solutions, and validates references.
- **Claw 5 (ROUTER)**: Verifies constraints, assigns risk ratings, and routes tasks to appropriate execution targets.
- **Claw 6 (PRODUCTION)**: Builds code, outputs drafts, records media, and hands off build artifacts.
- **Claw 7 (VERIFICATION)**: Evaluates build quality against criteria, inspects lineage, and ensures safety before deployment.

### 6. Real Monthly Budget & Cash Flow Allocation

```text
   ┌───────────────────────────────────────────────────────────────────┐
   │                  MONTHLY REAL CASH FLOW SYSTEM                   │
   └─────────────────────────────────┬─────────────────────────────────┘
                                     │
                     ┌───────────────┴───────────────┐
                     ▼                               ▼
       ┌───────────────────────────┐   ┌───────────────────────────┐
       │     FIXED OVERHEAD        │   │  STRIKE TEAM TECH STACK   │
       │   Monthly Nut (M2)        │   │  Sparky ($110) + Hermes   │
       │   Rent, Utilities, Auto   │   │  ($20) = $130/mo          │
       └─────────────┬─────────────┘   └─────────────┬─────────────┘
                     │                               │
                     └───────────────┬───────────────┘
                                     │
                                     ▼
                       ┌───────────────────────────┐
                       │     NET DISCRETIONARY     │
                       └─────────────┬─────────────┘
                                     │
                       ┌─────────────┴─────────────┐
                       ▼                           ▼
        ┌───────────────────────────┐ ┌───────────────────────────┐
        │     70% CHECKING          │ │     30% FIREWALL & SEED   │
        │ Daily Operating Number    │ │ $500 Buffer -> Swing Trade│
        │ (Food, Gas, Incidentals)  │ │ & Covered Calls (M5)      │
        └───────────────────────────┘ └───────────────────────────┘
```

**A. Operational Tech Expenses**
- Sparky / OpenAI Suite: $110 / month
- Hermes / Ollama / OpenClaw Membership: $20 / month
- Base Infrastructure Cost: $130 / month

**B. Personal & Business Capital Routing (70/30 Rule)**
- Take-Home Income: Gross earnings adjusted for 21% estimated tax bite.
- Monthly Nut: Rent, utilities, vehicle maintenance, groceries, and debt payments.
- Discretionary Allocations:
  - 70% Operating Pool: Serves as the Daily Number allowance for everyday expenses.
  - 30% Growth Pool: Directs capital straight to the $500 Emergency Buffer, followed by capital seeding for swing trading and covered call strategies.

## Rules

- One card = one outcome.
- Every card has an owner, lane, evidence link, and next action.
- Every dispatched Hermes worker starts with `kanban_show()` and returns the exact Snowball Closeout in `SKS Snowball execution contract.md`.
- A completed card may propose exactly one bounded successor. No successor becomes ACTIVE when three cards are already `running`.
- VERIFY → CERTIFY → NAME → SIGN → NEXT CARD. An actor may not independently certify its own work.
- Chat is for decisions. This board is for state.
- Felons Melon is the compass, not fog. Mention it when values or users matter; do not let it blur cash/app execution.
- Do not publish secrets, tokens, private machine identifiers, or unnecessary local paths.
- User does final submit on job applications, financial moves, public posts, production deploy approval, and account/auth changes.
- For the 2026-08-21 push: Kirk protects the job-hunt lane. The agent swarm handles Felons Melon final deployment cleanup in parallel.
- FINAL DEPLOYMENT means cleanup, verification, hardening, and release. No new feature expansion unless Kirk explicitly reopens scope.
- A board assignment is not proof an agent is running. Confirm a real runtime/session/poller before treating work as in progress.

## Lanes

### NOW

WIP governor: max 3. Killchain source: `SKS FM launch killchain 2026-08-30.md`. Money path: FM+ $19.99/mo. K2 locked. Kirk left the shop — continue on OfficeLeft.

| Card | Owner | Lane | Evidence | Next Action |
|---|---|---|---|---|
| K3 Fix only launch-blocking bugs | Hermes | Felons Melon hardening | Killchain K3; going-home handoff; tree 126 behind origin `c8daaac` | ff-only pull locked tree, then fix honesty/onboarding, job-board empty state, webhook/checkout. No deploy, no charges, no new features |
| K2 Lock one canonical FM production repo + branch | Kirk + Hermes | Felons Melon deployment | Kirk "Do it" 2026-08-30; `kirkbradford0/felonsmelonkirkbradford0gmail` `main`; local `C:\Users\bradf\Documents\Codex\felonsmelon-dev`; live `https://www.felonsmelon.com/` | PASS. Fast-forward local (126 behind) before edits. Duplicates frozen |
| Protect daily income lane | Kirk + Sparky | Cash / job survival | `SKS project map 2026-08-19.md`; `job-hunt/` | Kirk runs applications/interviews first; Sparky handles tailoring, research, tracker updates, and follow-up support |

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
| K3 Fix only launch-blocking bugs | Codex + Hermes verify | Felons Melon hardening | Killchain K3; live checkout 401-auth-gate; DEPLOYMENT.md webhook placeholder | After K1 evidence + K2 tree lock: Stripe trial after sign-in, webhook completion, guest vs signup honesty, job-board empty state, dead CTAs. No new features |
| K4 Independent public QA | GrokBot or Kirk | Felons Melon QA | Killchain K4 | After K3: copy, metadata, every major CTA, mobile + desktop. Hermes may not certify its own work |
| K5 Release receipt + rollback | FlowBot + Sparky | Felons Melon release | Killchain K5 | After K4: one go/no-go record with commit, URL, checks, rollback point |
| K6 First 10 real users | Kirk + Hermes | Felons Melon growth | Killchain K6 | After K5: 10 people who complete letter → resume → job match without Kirk standing over them |
| K7 First 100 users | Kirk + Hermes | Felons Melon growth | Killchain K7; kanban `fm-growth` | After K6: evidence-backed posts to the live working path. Kirk clicks Post |
| Finish FM landing + domain release path | AlphaBot + Codex | Felons Melon deployment | `kirkbradford0/Idea-Repo-123-` branch `claude/rebuild-fm-landing-5jxdV` | Fold into K3 only if K1 proves landing is still a launch blocker |
| Verify Supabase/auth/data boundaries | Codex + Sparky | Felons Melon hardening | FM NOW master; existing Supabase integration | Fold into K3 after K2. Redacted evidence only; do not expose service keys in SKS |
| Run production smoke test | Browser Harness + Sparky | Felons Melon QA | live URL `https://www.felonsmelon.com/` | Fold into K1/K4. Desktop + mobile, CTA, signup/guest, 404s, refresh/deep links |
| Enforce security/privacy release gate | Sparky + Codex reviewer split | Felons Melon hardening | FM NOW master G14-G15 | Fold into K4/K5. Builder and reviewer must be distinct |
| Verify active agent runtimes | Sparky + Hermes | Coordination | agent status packets; current SKS board | Confirm live runtime before treating an agent as working |
| Freeze non-job/non-FM build expansion for this push | Sparky | Coordination | user directive 2026-08-20; killchain 2026-08-30 | Keep trading, AutoFlow, kiosk, trusted-person packet, and new FM features out of NOW until K5 PASSES |
| FM core module port after release | Sparky/AlphaBot | Felons Melon product | GitHub `Felon-s-Melon-2.0` | After landing/release is stable and Kirk reopens scope, extract only the highest-value check-in/craving/mentor flows into the canonical app |
| Run FM article traffic lane | Hermes + GrokBot + Sparky | Felons Melon marketing | `kirkbradford0/sks-skills`; `SKS Hermes article pipeline built 2026-08-18.md` | After K5, produce evidence-backed posts that point to the live FM experience; Kirk handles final public post action |
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
| K8 Trusted-person monthly packet | unassigned | Felons Melon product | Killchain K8 | SHELVED until K5 PASS. User sends recovery/proof monthly to PO / case worker / DCFS. Do not design yet |
| K9 Auto kiosk next app | AlphaBot / later | Auto shop tools | Killchain K9; `bradfordautosolutionscheckin.lovable.app` | PARKED until FM works. Do not start this chain |

### WAITING / BLOCKED

| Card | Owner | Lane | Blocker | Unblock |
|---|---|---|---|---|
| AlphaBot deployment assignment | AlphaBot + Sparky | FM frontend | No current AlphaBot status packet/runtime proof in SKS | Publish/refresh `SKS AlphaBot status packet.json` and confirm target repo/branch |
| Browser Harness release test | Browser Harness + Sparky | FM QA | Requires a reachable deploy candidate and connected browser runtime | Provide/resolve deploy candidate, then run smoke test |
| GrokBot local board push | GrokBot | Coordination | Local GitHub auth hang may still apply | Grok confirms current status; top-level SKS board remains canonical |
| MedicBot Telegram assignment | MedicBot + Kirk | Coordination | Profile medicbot exists, gateway stopped | Kirk names a unique Telegram bot. Do not use @theegrokbot |
| KinloaBot work | KinloaBot + Sparky | Trade station | Deliberately deprioritized for current push | Resume after job-hunt + FM deployment release gate |
| Auto-apply employment engine | Kirk/Sparky | Job survival | CAPTCHAs, logins, ToS, final submit risk | Keep materials/research engine; Kirk final-submits applications |

### DONE

| Card | Owner | Lane | Evidence |
|---|---|---|---|
| Stand up Bravo + Charlie Telegram runtimes | Hermes Alpha | Coordination | `SKS fleet roster 2026-09-07.md`; Bravo @mafuckinhermesbot ping 269; Charlie @hermesbrickbot ping 1410 |
| Bravo inbound proven | Kirk + Bravo | Coordination | Kirk welcome in @mafuckinhermesbot 2026-09-07; `SKS Bravo status packet.json` |
| Charlie inbound proven | Kirk + Charlie | Coordination | Kirk session on @hermesbrickbot 2026-09-07; `SKS Charlie status packet.json` |
| STRIKE TEAM SEPT Handoff | Alpha stub + Bravo expand | Coordination | `SKS STRIKE TEAM SEPT handoff 2026-09-07.md` — pointing doc, live cron, Charlie review candidate |
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
| Bootstrap FM WarBoard orchestration | Kirk + Sparky | Coordination | Drive folder `WarBoards - Sparky, Kirks caduceus for Hermes`; `FM-WARBOARD-RUN-001 — Hermes Orchestration Bootstrap — 2026-08-30` |
| Write FM launch killchain + K1 live evidence | Hermes | Felons Melon QA | `SKS FM launch killchain 2026-08-30.md`; `SKS FM K1 live path evidence 2026-08-30.md`; board NOW collapsed to 3 |
| K1 Verify live FM customer path | Hermes | Felons Melon QA | `SKS FM K1 live path evidence 2026-08-30.md` — FAIL honesty + unproven jobs |
| K2 Lock canonical FM tree | Kirk + Hermes | Felons Melon deployment | Kirk "Do it" 2026-08-30; `felonsmelonkirkbradford0gmail` main; going-home handoff |

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
