# SKS running tasks list

Updated: 2026-09-29 (pass 0015, ~06:05 MT) by Hermes cron "SKS running tasks"
Owner: whoever is on duty. Cron job "SKS running tasks" refreshes this file and commits.
Rule: anything in the works or incomplete lives here. Done items get struck and then removed on next pass. Chat is not state — this file + SKS repo is.
Routing doctrine (PATRIARCH-ROUTING.md v1.0, 2026-09-17): every task carries `route: <target> · tier: local|worker|frontier|kirk · basis: <reason>`. Frontier = exception handler, earned after 2 stuck worker attempts, never for money/reputation lanes. Lessons go to `lessons/` in sks- (dir created on first real lesson).

## CATCH-UP PROTOCOL (2026-09-21, Kirk order: no copy-paste, no token burn)

Any agent (Bravo, Charlie, MedicBot, new seats) catching up does it from the repo, NOT from pasted chat context:
1. `git pull` sks- (and sparkpost/operation_snow_strike/dabs as relevant)
2. Read: SKS running tasks list.md → latest dated handoff for your seat → PATRIARCH-ROUTING.md
3. Work your OPEN items, commit handoffs back. Kirk pastes nothing.
Chat (Telegram/Discord) is for orders and questions — never for transferring state.

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
- [ ] Click a fresh Google auth link — TWO dead tokens (both invalid_grant), verified 2026-09-26: (a) gws google_token.json mtime still 2026-09-01 (re-verified 09-28); Gmail auto-sort + gws CLI dead; (b) felonsmelon@gmail.com for campaign test volley — PKCE verifier armed (google_oauth_pending.json mtime 09-25 18:01) and the port-80 catcher is RE-ARMED 2026-09-29 06:0x (it died on reboot — machine up since 09-23; restarted oauth_catcher_server.py as PID 19268, verified: approval page HTTP 200 on shop LAN http://192.168.1.253/Felon%20Melon_Kirk/hermes-approval.html, embedded auth URL state matches pending verifier, capture path writes google_oauth_captured.txt end-to-end). Kirk approves as felonsmelon@gmail.com and pastes back the full localhost?code= URL (or clicks the approval-page auth link — the catcher catches it). Blocks: test volley, Gmail drafts, auto-sort, gws.
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
- [ ] **SnowStrike** (C:/Users/bradf/snowstrike, repo kirkbradford0/operation_snow_strike, built+pushed 2590444 on 2026-09-19): FM marketing campaign machine — 100 FM users by Dec 25, 2026, harden date Oct 1. Locked 10-step daily loop, five-seat team, volley schema with [UNVERIFIED-HOT] quarantine, open-case content banned repo-wide. **Re-verified 2026-09-27: ZERO volleys have run** — volleys/ empty, repo HEAD unchanged 2590444 since 09-19; daily cron still NOT wired (live crons: "SKS running tasks" 6-hourly + "SparkPost heartbeat" 08:00, both pinned to ollama-cloud/glm-5.3-flash, deliver=telegram war-drum). Runbook is docs/DAILY-SKILL-PROMPT.md (Kirk trigger: "run the SnowStrike volley", or wire the daily cron). Outreach gate baked in: agents stage packets, Kirk clicks Send — never automate the send.
  route: hermes/sparky → kirk (sends) · tier: worker · basis: publish/send clicks stay Kirk
- [ ] **Operation Meráki (NEW 2026-09-26/27 — SnowStrike marketing lane split out per Kirk)** — repo kirkbradford0/Operation-Mer-ki (initial commit 44b96b8, README only so far; local clone C:/Users/bradf/Operation-Mer-ki). Go-between node: Kirk'/viking-go-between/Operation Meráki/ (SYNC-STATUS.md confirms shop→Lenovo sync working, 09-26). Kirk's planning doc (SnowStrike separation txt) restates the 10-step daily loop + tagline "Don't chase attention. Create enough legitimate signal that attention has somewhere to land." Relationship: GitHub repo = durable cross-agent copy; go-between folder = roving copy both machines see. OPEN: build out repo (campaign code, passoffs, run logs) and decide Meráki-vs-SnowStrike lane split — Kirk hasn't named the split owner yet.
  route: kirk (lane split) → alpha/bravo (build) · tier: worker · basis: naming/owner is Kirk's

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
  - Dwell clock (re-checked 2026-09-27 pass 0010, dabs repo 137bd6c — unchanged): pending = charlie-001..004 + bravo-001 (dwell **elapsed 2026-09-21**) + alpha-001 (intake rule, entered 2026-09-19 → eligible 2026-09-22). verified/ still EMPTY. Five-plus days overdue — verification is the blocker on M1.
- [ ] BEFORE wiring Discord bots into the swarm: stand up dabs intake flow (card naming DABS-YYYYMMDD-<agent>-<seq>.md, dwell tracking). Discord is not connected until the airlock exists.

## ADDED 2026-09-18 (Charlie passoff — source committed 1cbe40f 2026-09-19)

- [ ] **INTAKE RULE (Kirk 2026-09-19, dabs DABS-20260919-alpha-001)**: inference-agent intake asks case status FIRST (open/closed/none); open-case answers are LOCAL-ONLY — never cloud (Supabase etc.), repo, or chat, because third-party-hosted data is discoverable by defense AND prosecution. Pending: Charlie doctrine check + Kirk root sign-off.
  route: charlie (verify) + kirk (root) · tier: kirk · basis: product-logic + legal handling gate
- [ ] **WB-03 legal-content verification harness (war board)** — Charlie's card, due **2026-10-02**, not started. Bravo owns WB-02. Resume via private skill `charlie-fm-api-passoff` in `kirkbradford0/sks-skills` (instructions stay in private vault, not sks-). Source state now COMMITTED 2026-09-19 (1cbe40f): `SKS Charlie status packet.json` (status "working"), `skills/README.md` overflow note, `SKS Charlie passoff 2026-09-18.md`. SparkPost-as-skill not yet written.
  route: charlie · tier: worker · basis: verification harness is Charlie's role

## ADDED 2026-09-18 (Alpha): Muse seat accepted

- [ ] When Discord connects: hold Muse to the 2-day deliverable (culture layer pins/rituals + "what we learned" thread in the board, due ~2026-09-20); source of truth stays sks-/dabs. (Muse accepted the fifth seat 2026-09-18 ~10:35 MT — struck from list per done-removal rule.)

## ADDED 2026-09-29 (Hermes passoff 2dd8c21 — 09-28/29 night: campaign model + OAuth war). DONE 09-28: port-80 listener consolidation (then re-verified/re-ARMED 09-29 06:0x pass 0015 — catcher died on reboot, restarted).

- [ ] NEW 2026-09-29 00:58: **Emailsmissingfiles.zip landed in go-between root** (13 files: README + 6 FM segment email templates — fm_fresh_arrest, fm_probation, fm_parole, fm_college_open_case, + followup 1/2, each html+txt). Merge-field syntax {first_name}/{state}/{link}/{address}/{unsub}/{original_subject}; sequence day-0 → day-4 → day-10; CAN-SPAM rules; HOLD: no send until one real user completes intake to a delivered narrative in production. OPEN: unzip into Operation-Mer-ki repo (campaign code goes THERE per Kirk split order) + wire to campaign lane.
  route: hermes/bravo · tier: worker · basis: unpack + stage; sends stay Kirk

- [ ] **PATRIARCH / MITCH two-role loop (Kirk doctrine 09-26)**: PATRIARCH supervises/verifies/sequences; MITCH executes bounded tasks and returns evidence. Kirk's ownership correction: Patriarch = shop-PC agent (Codex lane — went dark when shop box was down); Hermes (this Telegram DM) = Sparky = runs on OfficeLeft.
  route: hermes/sparky · tier: local · basis: doctrine already Kirk-approved
- [ ] **Local Ollama Sparky approved (Kirk 09-28)** for FM website /api/sparky route: Qwen 2.5 7B or Llama 3.1 8B at localhost:11434, $0/mo, data never leaves machine; adapter pattern (SPARKY_PROVIDER env) for later swap. DeepSeek cloud lane parked (key-drop folder on Kirk's OTHER profile C:/Users/kirkb — does NOT sync to shop PC; login kirkbradford1@icloud.com). NOT built yet — Bravo/alpha build target.
  route: bravo · tier: worker · basis: build task, Kirk approved approach
- [ ] **Kirk action: gift zip FELONS MELON Front End Paths.zip could NOT be received** — shop PC has no D: drive. Kirk must copy the zip from D:/KinloaSlate/Dewey/KinloaSlate/Memory_Bank KH-1b/ into OneDrive/Desktop/Felon Melon_Kirk/ or the viking-go-between folder.
  route: kirk · tier: kirk · basis: file copy only Kirk can do cross-machine

## ADDED 2026-09-25 (handoffs 1cbd482 sniperbot + 0e97f55 Hermes — campaign 100x100 + HIL-DECK)

- [ ] **Campaign 100x100 wave-1 (GREEN LIGHT Kirk 09-25)** — West Coast only (CA/OR/WA), 100 orgs + 100 people, then PAUSE/review/respond. Transparent cold email (anti-spam review concluded): honest subject, identify in line 1, one follow-up max after 7d, real reply-to, opt-out honored, no open-case advice (FM INTAKE RULE), HITL — Kirk presses go per batch. Wave-1 staked: 6 verified emails + 10 contact-form-only (go-between campaign-100x100/orgs/wave-1-org-list.md; re-counted 2026-09-27 = 16 staked). NEXT: Kirk reviews outreach-email-ORGS-draft.md → batch-1 send with approval → continue org harvest toward 100. People lane = ONLY public askers (reddit r/Felons etc), never scraped/bought lists. UPDATE 2026-09-27: MISSION.md in go-between now carries KIRK-COPY RULE (every outbound BCCs kirkbradford1@icloud.com + kinloaslate@gmail.com — NOT kirkbradford0) + anti-spam rules; still no batch sent (Kirk hasn't reviewed the draft).
  - PLANNING STAKED in go-between (2026-09-27/28): `12-WEEK-ROADMAP-2026-09-27.md` (batch structure = test 10 → Batch A 30 → B 30 → C 30, weekly scoreboard map to 100 users by Dec 14-20, Sunday-review ritual) + `TOMORROW-PLAN-2026-09-28.md` (send-day checklist). THREE PRE-SEND BLOCKERS from tomorrow-plan: (1) OAuth — google_oauth_captured.txt caught junk (`/favicon.ico`, mtime 09-26 20:50), PKCE verifier still armed, Kirk must paste the localhost?code= URL **or re-issue fresh — 09-28 night passoff (2dd8c21) ranks phone-side rendering as the top blocker: auth URL verified 302-live from shop PC; if nothing loads on any device, re-issue fresh state/verifier (costs nothing)**; (2) outreach-email-ORGS-draft.md **domain FIXED 09-28 (pass 0012): both felonsmelons.com hits → felonsmelon.com SINGULAR, re-verified in draft** — re-presents for Kirk approval; (3) NEW 2026-09-28 ~13:57: **BATCH-0-CHECKLIST-2026-09-28.md staked in go-between** — 5-step Batch-0 send checklist (OAuth step 1, token verify, 10 drafts with 3 landing-page variants A/B/C across the 10, Kirk presses send per draft, tracker + 7d follow-up; health gates: bounce <3%, zero spam complaints before Batch A, hard cap 50/day). Approval page hermes-approval.html refreshed 13:56 on Desktop/Felon Melon_Kirk, local server confirmed live HTTP 200 same hour. Gmail caps verified: 500 recipients/day, BCCs count → steady-state self-cap 50 cold emails/day.
  - **CAMPAIGN MODEL LOCKED 09-28 night (passoff 2dd8c21, Kirk-approved)**: ONE constant first email to everyone (no city/persona variation in the message) — variation lives at the HYPERLINK (three landing pages: start-a-case intake / "AI that knows recovery" / parole-organization help, all funneling to felonsmelon.com); tracker counts replies at day 7; adjust and repeat. Hard scoreboard: 100 real FM users; 10-sales-per-100 conversion hypothesis behind the $19 kit.
  - **EMAIL STACK PIVOTED 09-28 (Kirk's calls)**: Gmail remains the SEND account but Proton Mail (free 150/day, receive) + Brevo (free 300/day, SMTP send, real bounce/spam reports) approved as $0/mo two-lane pattern; **App-Password/2FA lane KILLED by Kirk** — never re-raise it. BCC rule FINAL: kirkbradford1@icloud.com + kinloaslate@gmail.com; sender felonsmelon@gmail.com; reply-to kirkbradford0@gmail.com. **Himalaya v2.1.0 installed+verified ~/bin/himalaya.exe (09-28) as keyless terminal client.** OPEN: Brevo account/SMTP key not yet created — needs Kirk signup, pairs with Test-volley blocked-on-OAuth. **OAuth consent specifics from 09-28 war: project felonsmelonsparkpost Testing mode — felonsmelon@gmail.com ADDED to Test users (confirmed on-screen); consent screen itself NEVER rendered for Kirk; hermes/oauth_catcher_server.py (port 80, CAPTURED page + code→google_oauth_captured.txt) end-to-end tested, still armed; approval page verified 200 via shop-PC LAN http://192.168.1.253/Felon Melon_Kirk/hermes-approval.html.**
  - **Campaign repo split (Kirk order 09-27, confirmed 09-28)**: ALL campaign code/logs → kirkbradford0/Operation-Mer-ki, never mixed into sks-/dabs/sparkpost.
  route: hermes → kirk (review + send) · tier: kirk · basis: outreach sends are Kirk's click
- [ ] **Test volley (10 emails)** — Kirk seeds (kirkbradford0@gmail + kirkbradford1@icloud) + 5 West Coast orgs; plain text + hyperlinks; from felonsmelon@gmail.com; Gmail DRAFT queue; Kirk presses send; then trace paths/links/rendering. Domain rule locked: felonsmelon.com (singular) live HTTP 200 — felonsmelons.com (plural) DNS-dead, never link it. BLOCKED on Gmail OAuth paste-back (see Kirk owes).
  route: hermes (drafts) → kirk (send) · tier: kirk · basis: HITL send gate
- [ ] **HIL-DECK open items** (sparkpost/hil-deck, commit e9b6336): (1) verify first deck execution through SparkPost heartbeat — as of 2026-09-26 hil-deck/done/ is empty, nothing processed yet; (2) Charlie cold-verify the deck server finish-capture path (Hermes smoke-tested it itself — no-self-certify rule). Deck server on OfficeLeft port 8799 dies on reboot; START-DECK.bat is the launcher. First deck = 6 cards: D1 test volley, D2 Pinterest batch, D3 $19 kit price, D4 FB engine-vs-Marketplace, D5 Discord briefs, D6 Amazon gating (Kirk-only).
  route: hermes (heartbeat exec) · charlie (cold verify) · tier: worker · basis: playbooked lanes; sends/purchases stay HITL

## ADDED 2026-09-26 (sniperbot passoff in go-between, 09-26 session)

- [ ] Sniperbot next Monday rhythm (daily rhythm start): (1) run hindsight skill (kirks-hindsight-context) — Monday muscle; (2) first Pinterest pin from inventory pairing matrix (cheetah/rock or SpaceX trap angle); (3) org batch 2 harvest toward 100 (16 staked so far). Source: go-between PASSOFF-sniperbot-2026-09-26.md. Also awaiting Kirk: FM Gmail + Telegram send approval ("he said shortly" 09-26 — NOT yet received), inventory review for re-laning.
  route: hermes/sniperbot · tier: local · basis: research/build lanes; sends stay Kirk
