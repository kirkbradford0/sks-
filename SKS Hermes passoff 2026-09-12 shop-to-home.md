# SKS Hermes passoff 2026-09-12 — SHOP → HOME (Slim Jim in transit)

Alpha passing to the home machine (Lenovo, C:\Users\kirkb). Kirk tested the
GEV globe and approved. SSD "KIRKSLIMJIM" (4TB, D: on shop) travels with him.

## State at passoff
- SparkPost repo kirkbradford0/sparkpost HEAD **5abbc1ee** (verified on origin):
  founder console w/ GEV panel, dual-write boss sorter, kill chain + 3 briefs
  force-added, GEV launcher + integration plan.
- God's Eye View installed keyless at C:/Users/bradf/gods-eye-view (shop).
  Runs at localhost:4173 via `npm run dev`. Launcher:
  `python sparkpost/gev_button.py`. Kirk test-drove it — FUN, approved.
- Brain: 5/5 Maslow files mirrored at D:/sparkpost-brain/brain/ (verified
  file-for-file). Engine mirror at D:/sparkpost-brain/engine/ (verified).
- Cron "SparkPost heartbeat" runs on the SHOP machine only (id bd269e3a6791,
  daily 08:00, deliver=local). Nothing schedules itself at home.
- sks- handoff base doc: "SKS Hermes handoff 2026-09-12.md" (commit 44c6a7e).

## Slim Jim at home — first 5 minutes
1. Plug in SSD. Note its drive letter (may not be D: at home).
2. SparkPost brain/engine mirror lives at <SSD>:\sparkpost-brain\.
   If letter ≠ D:, set once: `setx SPARKPOST_MIRROR "<letter>:/sparkpost-brain"`
   (boss_sorter + console read it; without it they just run local-only — safe).
3. Engine: `git clone https://github.com/kirkbradford0/sparkpost` (Credential
   Manager as kirkbradford0 works at home too) — the repo is the recovery key;
   SSD is the brain backup. Both exist; use either.
4. GEV at home (optional tonight): needs Node 24.x +
   `git clone https://github.com/bilawalsidhu/gods-eye-view` + `npm ci` +
   `cp .env.example .env` + `npm run dev`. Or skip — the SSD carries the plan,
   and GEV rebuilds in ~5 min on any machine (zero keys).

## TONIGHT'S KILL CHAIN (staged, waiting on Kirk)
1. **Motley Fool submit** — ledger line 1 confirmed ⬜ Ready. Packet at
   C:\Users\bradf\Job Applications\Motley_Fool_Contract_AI_Writer_2026-09-04\
   (shop machine — packet also needed at home OR submit from shop tomorrow).
   Greenhouse 5202271007. KIRK PRESSES SUBMIT. Hermes never does.
2. **Google OAuth re-auth** — dead since 09-11 (invalid_grant). At home run:
   `python <hermes>/skills/productivity/google-workspace/scripts/setup.py --auth-url`
   then Kirk clicks the link (sign in kirkbradford0@gmail.com), then run
   setup.py to catch the code. Link expires ~30 min — generate fresh.
3. **Target package gap** — SPARKPOST_TARGET_PACKAGE_20260912.md was never on
   the shop machine. Mythos holds it; home session should collect/re-stage.

## Doctrine reminders (unchanged)
- Engine → GitHub. Brain/PII → SSD + local only. Never cloud, never repos.
- Every session ends with full SSD sync + GitHub push. Kirk always has an exit.
- Nothing sends, submits, or pays without Kirk's click.

## Next lanes (priority order)
1. MF submit + OAuth (money lane, tonight)
2. Utah camera pack for GEV (cctv_sources.utah.json from UDOT public feeds) —
   first GEV artifact that graduates toward FM service-finder
3. Venmo business profile (Kirk's 30-min app task) + QR codes on site
4. FM narrative: server-side paywall enforcement before Stripe goes live
   (see briefs/FM-NARRATIVE-PRODUCT-DOSSIER-2026-09-12.md §5)
