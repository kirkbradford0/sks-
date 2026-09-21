# SKS running tasks list

Updated: 2026-09-21 (pass 0007 MT) by Hermes cron "SKS running tasks"
Owner: whoever is on duty. Cron job "SKS running tasks" refreshes this file and commits.
Rule: anything in the works or incomplete lives here. Done items get struck and then removed on next pass. Chat is not state — this file + SKS repo is.
Routing doctrine (PATRIARCH-ROUTING.md v1.0, 2026-09-17): every task carries `route: <target> · tier: local|worker|frontier|kirk · basis: <reason>`. Frontier = exception handler, earned after 2 stuck worker attempts, never for money/reputation lanes. Lessons go to `lessons/` in sks- (dir created on first real lesson).

## OPEN — Kirk (H.I.L.) owes

- [ ] Name a Telegram bot for MedicBot (never @theegrokbot)
  route: kirk · tier: kirk · basis: identity/naming is Kirk's call
- [ ] Click Submit on **Intro — Content Marketing Writer (Contract)** (Ashby `jobs.ashbyhq.com/intro/30d6b523-512a-444f-bfca-32c8004bdbeb`, $50–100/hr remote US) — packet ready at Job Applications\Intro_Content_Marketing_Writer_2026-09-12\; ledger row 1 ⬜ Ready (re-verified 2026-09-17, untouched since 09-12). NOTE: Motley Fool 5202271007 is DEAD (ATS closed, packet quarantined to _dead/, ledger 💀) — do not submit Fool.
  route: kirk · tier: kirk · basis: Light Board submit rule — only Kirk clicks Submit
- [ ] Go/no-go on Bravo recon trio (brain/name 2026-09-12, verified live): OWID Senior Data Writer (remote £80–120K, paid residency); VOA Utah Grant Writer (SLC hybrid $60–65K, only W-2 option, fair-chance-friendly); OpenTrain AI Technical Writer RLHF (fully remote $90–140/hr part-time, stacks with Intro). Recon only — nothing applied. (Charlie re-hit 2026-09-15: Intro live unsubmitted, OpenTrain recon URL dead, OWID+VOA still live.)
  route: kirk · tier: kirk · basis: applications leave the machine — Kirk gates
- [ ] Venmo lane gate (briefs/VENMO-LANE-REPORT-2026-09-12.md): Kirk approves Venmo Business Profile setup + pre-filled QR codes + placement on felonsmelons.com before anything goes live. Discounts run in Stripe coupons, not Venmo.
  route: kirk · tier: kirk · basis: money lane
- [ ] Pick first Bravo build target (Lane 1 Felons Melon K3 on a branch — shop kiosk is parked until FM works). Charlie 2026-09-15: if the sortie was a Bravo build review, NAME the card — no named card, no review.
  route: kirk · tier: kirk · basis: card assignment stays with Kirk
- [ ] **Open + sign Charlie's Mini Build Map v2** (handoff 2026-09-15, built, not certified): one card, five workflow columns, local sidecar `mini-build-map/index.html` (NOT in sks- repo), schema `types/build-map.ts`, `?autotest=1` → VERIFIED. Kirk opens it; if the map is the sortie, Charlie reviews Alpha/Bravo cards on it once signed. Pointing note: `SKS Charlie Mini Build Map v2 2026-09-15.md`.
  route: kirk (open/sign) · tier: kirk · basis: certification gate
- [ ] Paste/photo the next burn snapshot (bank cash, brokerage total, debt) to Charlie — Charlie's private burn-desk (handoff 2026-09-17) computes runway; do NOT treat invested as liquid. No cron on the burn-desk unless Kirk asks. Charlie built it, does not certify the books — money decisions stay Kirk.
  route: kirk (snapshot) → charlie (compute) · tier: worker · basis: local math; money clicks stay Kirk
- [ ] Click a fresh Google auth link (google-workspace setup.py --auth-url) — OAuth token revoked since 2026-09-11 (invalid_grant); Gmail auto-sort + gws CLI dead until re-authed. Verified dead 2026-09-17: google_token.json mtime still 2026-09-01; the staged 2026-09-13 11:28 pending flow was never exchanged and is expired — generate fresh, don't reuse.
  route: worker (generate link) → kirk (click) · tier: kirk · basis: OAuth click is Kirk's

## OPEN — Fleet tasks

- [ ] **Patriarch routing layer live as doctrine (PATRIARCH-ROUTING.md v1.0, commit 5225492, 2026-09-17)** — protocol, not a daemon: observer/router/record-keeper/optimizer around the loop; escalation ladder (local GLM → worker by role → frontier as exception handler); Lessons in `lessons/LESSON-<slug>-YYYY-MM-DD.md` (one per file, created when a frontier solve is recorded); Kirk stays HITL on consequential routing. Shared spec so Sparky's implementation and Hermes read the same doctrine — Sparky side not yet confirmed aligned.
  route: alpha/hermes (apply routing lines each pass) · tier: local · basis: protocol already playbooked
- [ ] **Execute kill chain on home-machine sortie** — brief at sparkpost repo `briefs/KILL-CHAIN-STAGED-2026-09-12.md` (NOT in this sks- repo). The 2026-09-13 04:30 window passed with no evidence of execution; the 09-13 11:28 OAuth flow was staged but never exchanged (link expired). Needs re-run: (1) Intro submit (Kirk clicks), (2) fresh Google OAuth link → Kirk clicks → verify Gmail auto-sort + gws recover, (3) collect/re-stage SPARKPOST_TARGET_PACKAGE_20260912.md (not on shop machine; Mythos holds it or home pulls from sparkpost repo).
  route: hermes/alpha → kirk · tier: kirk · basis: contains money-lane submit + OAuth click
- [ ] **Wire Hermes into Discord server `--SKS---`** — server ID 1546468280343072808, invite from kirkbradford0 expires 2026-10-07. Still NOT done (no Discord token wired in any profile). Steps: Kirk creates Discord app at discord.com/developers/applications, resets token, enables Developer Mode, copies server ID; Alpha wires token into a profile gateway. Do NOT post the token in SKS repo or chat.
  route: kirk (token) → alpha (wire) · tier: worker · basis: token handling is Kirk's; wiring is playbooked
- [ ] Build apply-light harness from spec v1 (SKS apply-light harness build spec v1 2026-09-07.md) — builder: Claude, operator: Hermes, hard rule: no auto-submit, no PII off-machine. Scaffold exists at C:\Users\bradf\apply-light-harness\ (BUILD-SPEC.md only, no build progress as of 2026-09-17).
  route: bravo · tier: worker · basis: specialized build task, no escalation signal
- [ ] **WARBOARD PRIORITY ONE (Kirk 9/7/26, reviewed 2026-09-14): simplify Felons Melon into a simple buy** — one story, one one-time fee, one letter to sign and hand in. À-la-carte add-ons; Kirk's favorite = **Clear My Warrant Letter** (pull records, write what the courts ask for, reasonable dollar to close / PTA route). Full read: `SKS Hermes warboard review 2026-09-14.md`. Fits 2026-09-12 client-side narrative doctrine; scope/pricing gated by Kirk.
  route: bravo (build) · tier: worker · basis: build task; scope/pricing gated by Kirk
- [ ] Recovery companion AI ($5–10 talk/type lane for people in recovery) — warboard idea 9/7/26, "would be a life saver." Idea only; needs Kirk go/no-go before any build.
  route: kirk · tier: kirk · basis: go/no-go gate
- [ ] GEV integration next lane: Utah camera pack (UDOT feeds) → FM service-finder mode, per briefs/GEV-INTEGRATION-PLAN-2026-09-12.md in sparkpost repo. Launcher (gev_button.py) done; keyless instance runs localhost:4173 via `npm run dev`.
  route: bravo · tier: worker · basis: integration build, plan already written
- [ ] Bravo: first build task — unassigned until Kirk picks (see Kirk owes)
- [ ] Charlie: first **build** review waits on Kirk naming Bravo's card. Live-vs-git review already filed. 2026-09-15: ran immune pass (`SKS Charlie review immune pass 2026-09-15.md`), built Mini Build Map v2 — see Kirk owes. 2026-09-17: built private burn-desk on shop box (see standing desks); packet re-proven same day. 2026-09-18: attack pass on tools@56005ad filed as dabs charlie-001..004 (see handoff); operational skills moved to private `kirkbradford0/sks-skills` vault — public `sks-/skills/` is a boundary stub only.
  route: charlie · tier: worker · basis: verification is Charlie's role
- [ ] MedicBot: start gateway once Telegram bot exists (Kirk names it — see Kirk owes)
- [ ] Qwen (home computer): standby until Kirk wires it into SKS
- [ ] GrokBot: stays parked, zero spend, until Kirk funds it
  route: kirk · tier: kirk · basis: funding is Kirk's; never autonomous spend

## IN PROGRESS — standing desks

- [ ] Markets: live USDE book 100 sh @ $8.29 — 3% stop $8.04, +3% sell 50 @ $8.54, ladder $8.37 → $8.20 out. No live API orders (broker LOCKED). Paper desk cron **paused** 2026-09-07; TwoAM research 2 AM cron also currently **disabled** (verified 2026-09-09).
- [ ] Felons Melon: 100-user goal; front page = Stripe TEST checkout; Gazette desks standing. Narrative doctrine (2026-09-12): client-side only, core = fm-narrative-engine.ts (806 ln) + fm-prompt-library/narratives.ts in felonsmelon-dev (richest clone); pro paywall needs server-side enforcement before real money. Venmo lane next (design + integration, Kirk gates). FM hero mismatch re-verified by Charlie 2026-09-15: live hero "Your story. Told right." vs origin/main `c8daaac` "You left with nothing." — unchanged since 2026-09-07. Charlie did NOT push FM main on 09-17.
- [ ] SparkPost (C:/Users/bradf/sparkpost, repo kirkbradford0/sparkpost): heartbeat cron daily 08:00 (digest → inbox → boss sorter → brain; never touches brain/PII). STORAGE DOCTRINE: session ends with full SSD sync (D:/sparkpost-brain) + GitHub push; brain (PII) never in repos/cloud. Console: python sparkpost_console.py. GEV launcher button done (5abbc1e).
- [ ] Shop kiosk: Lovable check-in still discards data — backend wiring lives at C:/Users/bradf/kiosk-node/
- [ ] Job search: Intro packet ready (Kirk clicks Submit — see Kirk owes); DEAD, do not chase: Motley Fool 5202271007 (ATS closed 2026-09-12, Charlie commit 8cec618), LearnLux 5381389008 (closed 2026-09-12), Concentric Junior OSINT, Augur Researcher, INFUSE B2B Content Writer 4707669005. Aggregators still echo the corpses — re-hit the employer board before any Submit.
- [ ] Charlie burn-desk (private, shop box only, handoff 2026-09-17): splits cash / invested / debt, three runways, flags incomplete nut + zero income, refuses to annualize a 2-day cash drop. 8 unit tests pass. Personal amounts stay OFF SKS — SKS records only that the desk exists. Not certified; not on cron.
- [ ] **SnowStrike** (C:/Users/bradf/snowstrike, repo kirkbradford0/operation_snow_strike, built+pushed 2590444 on 2026-09-19): FM marketing campaign machine — 100 FM users by Dec 25, 2026, harden date Oct 1. Locked 10-step daily loop, five-seat team, volley schema with [UNVERIFIED-HOT] quarantine, open-case content banned repo-wide. Loop start date = **2026-09-21 (today)** — as of pass 0007 00:00 MT no volley has run and the daily cron is still NOT wired (cron list re-checked 2026-09-21: only "SKS running tasks" + "SparkPost heartbeat" active). Runbook is docs/DAILY-SKILL-PROMPT.md (Kirk trigger: "run the SnowStrike volley", or wire the daily cron). Outreach gate baked in: agents stage packets, Kirk clicks Send — never automate the send.
  route: hermes/sparky → kirk (sends) · tier: worker · basis: publish/send clicks stay Kirk

## ADDED 2026-09-19 (Alpha weekend warboard, commit 5aeb5cc) — read `SKS weekend warboard + week goals 2026-09-19.md` for full cards

- [ ] W1 Alpha: WB-01 statute map — 10 Utah re-entry questions → le.utah.gov cites + honesty lines. Success = `SKS WB-01 Utah statute map v1 2026-09-19.md` in sks- + DABS card filed.
  route: alpha · tier: local · basis: research build; Charlie verifies
- [ ] W2 Alpha: WB-05 outreach target list draft — 10 Utah/defense-adjacent attorneys + 10 re-entry non-profits. Success = `SKS WB-05 outreach targets v1 2026-09-19.md`, 20 rows, no invented emails.
  route: alpha · tier: local · basis: research build; Kirk gates sending
- [ ] W3 Kirk: GLM swap for Bravo + Charlie — both profiles answer a test prompt on local GLM, then one line in AGENT_STATUS_PACKET.md ("Bravo + Charlie on local GLM as of <date>"). NOT done as of 09-19 (no GLM line in packet).
  route: kirk · tier: kirk · basis: infra/config is Kirk's
- [ ] W5 Muse nudge: WB-04 Constitution + Voice — 2-day deliverable due ~2026-09-20; constitution v0 skeleton filed to sks- even if rough.
  route: muse · tier: worker · basis: accepted seat deliverable
- [ ] M1 (Monday 09-21+) Charlie: verification debt — verify agent_pbft.py + circuit breakers, resolve DABS charlie-001..004 + bravo-001 at 72h, WB-03 skeleton + first failing test. Author never certifies own work.
  route: charlie · tier: worker · basis: verification is Charlie's role
- [ ] M2 Bravo (on GLM): WB-02 drafting pipeline skeleton — motion-support draft template, citation slots reference WB-01 v1 only.
  route: bravo · tier: worker · basis: build task
- [ ] M3 Alpha (Judge hat): accept/flag/escalate logic live; first ruling = WB-01 goes to Charlie, routing table updated.
  route: alpha · tier: local · basis: rotation doctrine

## ADDED 2026-09-18 (Alpha, Kirk-directed): DABS quarantine gate before Discord wiring
- [ ] NEW RULE: all agent messages/claims enter kirkbradford0/dabs first, 72h dwell, then Charlie/promoting-agent verifies before entering SKS. Doctrine: DABS-QUARANTINE.md. Hot lane (prices/alerts) flows direct but tagged [UNVERIFIED-HOT] with same-session cross-check.
  - Dwell clock (checked 2026-09-21 pass 0007, dabs repo 137bd6c — unchanged): pending = charlie-001..004 + bravo-001 (entered 2026-09-18 → 72h dwell **elapsed 2026-09-21**; eligible for Charlie verification NOW, nothing moves until a different agent verifies — M1 below) + alpha-001 (intake rule, entered 2026-09-19 → eligible 2026-09-22). verified/ still empty.
- [ ] BEFORE wiring Discord bots into the swarm: stand up dabs intake flow (card naming DABS-YYYYMMDD-<agent>-<seq>.md, dwell tracking). Discord is not connected until the airlock exists.

## ADDED 2026-09-18 (Charlie passoff — source committed 1cbe40f 2026-09-19)

- [ ] **INTAKE RULE (Kirk 2026-09-19, dabs DABS-20260919-alpha-001)**: inference-agent intake asks case status FIRST (open/closed/none); open-case answers are LOCAL-ONLY — never cloud (Supabase etc.), repo, or chat, because third-party-hosted data is discoverable by defense AND prosecution. Pending: Charlie doctrine check + Kirk root sign-off.
  route: charlie (verify) + kirk (root) · tier: kirk · basis: product-logic + legal handling gate
- [ ] **WB-03 legal-content verification harness (war board)** — Charlie's card, due **2026-10-02**, not started. Bravo owns WB-02. Resume via private skill `charlie-fm-api-passoff` in `kirkbradford0/sks-skills` (instructions stay in private vault, not sks-). Source state now COMMITTED 2026-09-19 (1cbe40f): `SKS Charlie status packet.json` (status "working"), `skills/README.md` overflow note, `SKS Charlie passoff 2026-09-18.md`. SparkPost-as-skill not yet written.
  route: charlie · tier: worker · basis: verification harness is Charlie's role

## ADDED 2026-09-18 (Alpha): Muse seat accepted

- [ ] When Discord connects: hold Muse to the 2-day deliverable (culture layer pins/rituals + "what we learned" thread in the board, due ~2026-09-20); source of truth stays sks-/dabs. (Muse accepted the fifth seat 2026-09-18 ~10:35 MT — struck from list per done-removal rule.)
