# SKS running tasks list

Updated: 2026-09-12 (06:00 pass) by Alpha (@ScoutLimabot)
Owner: whoever is on duty. Cron job "SKS running tasks" refreshes this file and commits.
Rule: anything in the works or incomplete lives here. Done items get struck and then removed on next pass. Chat is not state — this file + SKS repo is.

## OPEN — Kirk (H.I.L.) owes

- [ ] Name a Telegram bot for MedicBot (never @theegrokbot)
- [ ] Click Submit on Motley Fool packet (Greenhouse 5202271007) — packet ready in Job Applications; ledger still shows "Ready" (re-verified 2026-09-12)
- [ ] Go/no-go on Bravo recon trio (brain/name 2026-09-12, verified live): OWID Senior Data Writer (remote £80–120K, paid residency); VOA Utah Grant Writer (SLC hybrid $60–65K, only W-2 option, fair-chance-friendly); OpenTrain AI Technical Writer RLHF (fully remote $90–140/hr part-time, stacks with MF contract). Recon only — nothing applied.
- [ ] Venmo lane gate (briefs/VENMO-LANE-REPORT-2026-09-12.md): Kirk approves Venmo Business Profile setup + pre-filled QR codes + placement on felonsmelons.com before anything goes live. Discounts run in Stripe coupons, not Venmo.
- [ ] Pick first Bravo build target (Lane 1 Felons Melon K3 on a branch — shop kiosk is parked until FM works)
- [ ] Say go / no-go on the two new Fool-shaped scouted jobs (Intro contract writer $50–100/hr via Ashby; LearnLux financial content writer Greenhouse 5381389008) — scout-only until Kirk says go (job-hunt/tonight-2026-09-07.md)
- [ ] Click a fresh Google auth link (google-workspace setup.py --auth-url) — OAuth token revoked since 2026-09-11 (invalid_grant); Gmail auto-sort + gws CLI dead until re-authed. NOTE: staged link expires ~30 min — regenerate fresh at the 04:30 home-machine sortie instead of using the stale one.

## OPEN — Fleet tasks

- [ ] **Execute kill chain on home-machine sortie (2026-09-13 04:30)** — briefs/KILL-CHAIN-STAGED-2026-09-12.md in this repo. MF confirmed Ready. Steps: regenerate fresh Google OAuth link (setup.py --auth-url) at 04:30, Kirk clicks, then verify Gmail auto-sort + gws recover. GAP: SPARKPOST_TARGET_PACKAGE_20260912.md was NOT on shop machine — Mythos must re-stage or home machine pulls it from sparkpost repo.
- [ ] **Wire Hermes into Discord server `--SKS---`** — server ID 1546468280343072808, invite from kirkbradford0 expires 2026-10-07. Still NOT done (no Discord token wired in any profile). Steps: Kirk creates Discord app at discord.com/developers/applications, resets token, enables Developer Mode, copies server ID; Alpha wires token into a profile gateway. Do NOT post the token in SKS repo or chat.
- [ ] Build apply-light harness from spec v1 (SKS apply-light harness build spec v1 2026-09-07.md) — builder: Claude, operator: Hermes, hard rule: no auto-submit, no PII off-machine. Scaffold exists at C:\Users\bradf\apply-light-harness\ (BUILD-SPEC.md only).
- [ ] **Review Kirk's FIRST WARBOARD TEST.pdf** (repo root, uploaded 2026-09-07, commit 6b62f34) — still unreviewed as of 2026-09-12 06:00. On-duty agent: open it, respond to Kirk, file a dated note.
- [ ] GEV integration next lane: Utah camera pack (UDOT feeds) → FM service-finder mode, per briefs/GEV-INTEGRATION-PLAN-2026-09-12.md in sparkpost repo. Launcher (gev_button.py) done; keyless instance runs localhost:4173 via `npm run dev`.
- [ ] Bravo: first build task — unassigned until Kirk picks
- [ ] Charlie: first **build** review waits on Kirk naming Bravo's card. Live-vs-git review already filed.
- [ ] MedicBot: start gateway once Telegram bot exists
- [ ] Qwen (home computer): standby until Kirk wires it into SKS
- [ ] GrokBot: stays parked, zero spend, until Kirk funds it

## IN PROGRESS — standing desks

- [ ] Markets: live USDE book 100 sh @ $8.29 — 3% stop $8.04, +3% sell 50 @ $8.54, ladder $8.37 → $8.20 out. No live API orders (broker LOCKED). Paper desk cron **paused** 2026-09-07; TwoAM research 2 AM cron also currently **disabled** (verified 2026-09-09).
- [ ] Felons Melon: 100-user goal; front page = Stripe TEST checkout; Gazette desks standing. Narrative doctrine (2026-09-12): client-side only, core = fm-narrative-engine.ts (806 ln) + fm-prompt-library/narratives.ts in felonsmelon-dev (richest clone); pro paywall needs server-side enforcement before real money. Venmo lane next (design + integration, Kirk gates).
- [ ] SparkPost (C:/Users/bradf/sparkpost, repo kirkbradford0/sparkpost): heartbeat cron daily 08:00 (digest → inbox → boss sorter → brain; never touches brain/PII). STORAGE DOCTRINE: session ends with full SSD sync (D:/sparkpost-brain) + GitHub push; brain (PII) never in repos/cloud. Console: python sparkpost_console.py. GEV launcher button done (5abbc1e).
- [ ] Shop kiosk: Lovable check-in still discards data — backend wiring lives at C:/Users/bradf/kiosk-node/
- [ ] Job search: Fool packet ready; two new Fool-shaped jobs scouted 2026-09-07 (Intro, LearnLux — see job-hunt/tonight-2026-09-07.md); Bravo recon trio 2026-09-12 awaiting go/no-go. DEAD, do not chase: Concentric Junior OSINT, Augur Researcher (board empty, deadline past), INFUSE B2B Content Writer 4707669005 (closed).

## DONE (recent, keep for one pass)

- [x] 2026-09-12: SSD storage doctrine live on shop machine — D:/sparkpost-brain mirror (brain/ + engine/), boss_sorter.py dual-writes with soft-degrade; brain verified 5/5 mirrored (handoff addendum)
- [x] 2026-09-12: SparkPost founder side live — private repo kirkbradford0/sparkpost pushed, console v0, boss sorter archive fix (selftest 6/6), heartbeat cron created
- [x] 2026-09-12: FM narrative recon filed (briefs/FM-NARRATIVE-RECON-2026-09-12.md) — confirmed NO narrative API route; narrative is client-side
- [x] 2026-09-12: Venmo lane decision made (briefs/VENMO-LANE-REPORT-2026-09-12.md) — skip Venmo/Braintree API; free Business Profile + QR codes + Stripe coupons
- [x] 2026-09-12: FM narrative product dossier filed (briefs/FM-NARRATIVE-PRODUCT-DOSSIER-2026-09-12.md) + GEV launcher + integration plan (sparkpost repo HEAD 5abbc1e)
- [x] 2026-09-12: ApHidMonitorService root-caused as red herring (Dell touchpad helper, not Hermes); service disabled via elevated sc.exe
