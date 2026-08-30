# SKS FM launch killchain — 2026-08-30

Status: ACTIVE
Owner: Hermes (traffic control) under Kirk H.I.L.
Compass: get Felons Melon working, then first 100 users, then marketing and trusted-person monthly packets.
Not this push: Auto kiosk, new FM features, trusted-person DCFS/PO line, trading expansion.

Money path confirmed by Kirk: **FM+ $19.99/mo** (14-day trial). Sponsor $19 and Org $49/mo stay on the pricing page but are not the first-100-users wedge.

## Live facts (verified this session, shop PC OfficeLeft)

| Check | Result | Evidence |
|---|---|---|
| Domain | LIVE HTTPS 200 | `https://www.felonsmelon.com/` Server: Vercel |
| Pricing | Free / FM+ $19.99/mo / Sponsor $19 / Org $49/mo | `/pricing` |
| Stripe checkout | EXISTS, auth-gated | `POST /api/stripe/checkout` `{"kind":"fm_plus"}` → HTTP 401 `requiresSignIn: true`, `signInPath: /login?next=%2Fpricing` |
| Old checkout path | Dead | `GET /api/checkout` → 410 Gone |
| Guest letter claim | CONFLICT | Homepage: "Free · No account needed" + `/onboarding`. `/onboarding` is account signup. |
| Auth walls | Several tools are not free-open | `/proof`, `/dashboard`, `/start`, `/hyperjobs` → 307 `/signup` |
| Resume | Open, empty until interview | `/resume` 200 |
| Employment engine | Open; Pro locks follow-up + interview prep | `/employment` 200 |
| Job board | Page 200; listings not proven | `/job-board` HTML says "Loading live jobs..." |
| Webhooks | Not production-ready in local docs | `DEPLOYMENT.md`: "Stripe webhook handling is still placeholder-level" |
| Canonical tree from bootstrap | MISSING on this machine | `C:\Users\kirkb\felons-melon\felonsmelonkirkbradford0gmail` does not exist |
| Closest local tree | Stale vs unknown live SHA | `C:\Users\bradf\Documents\Codex\felonsmelon-dev` remote `kirkbradford0/felonsmelonkirkbradford0gmail`, last local commit `efa4f67` 2026-06-09 |

No FM application code was changed this session.

## Iron rules

1. Verify → save to SKS → verify the remote SHA. An interrupt is not a completion.
2. No FM code mutation, deploy, Stripe live charge, or schema change until the locked tree is fast-forwarded to origin/main. Kirk locked K2 2026-08-30 ("Do it") while leaving the shop.
3. WIP = 3. One card in progress. One successor per PASS.
4. Kirk clicks Post, pays, deploys, and final-submits. Hermes does everything up to that click.
5. Trusted-person monthly packet (PO / case worker / DCFS) is SHELVED until the app actually works.
6. Auto kiosk is NEXT APP after FM works — not this killchain.

## Killchain

Cards are sequential. Do not start a later card while an earlier one is BLOCKED.

### K1 — Verify the live customer path
Lane: FM BUILD / QA
Owner: Hermes
Status: EVIDENCE SAVED 2026-08-30 — result FAIL (honesty + unproven jobs). Closed as recon.
Do:
- Walk homepage → letter → resume → jobs → signup → pricing → checkout gate.
- Record every broken CTA, auth surprise, empty job board, and false claim.
- Do not create accounts, do not use Kirk's card, do not mutate code.
Success: one evidence table of PASS/FAIL/BLOCKED per step, saved in SKS.
Successor: K2 if path is coherent; K3 if launch blockers are named.

### K2 — Lock one canonical production tree
Lane: FM BUILD
Owner: Kirk + Hermes
Status: PASS 2026-08-30 — Kirk "Do it" while leaving shop
Locked:
- Repo: `kirkbradford0/felonsmelonkirkbradford0gmail`
- Branch: `main`
- Local: `C:\Users\bradf\Documents\Codex\felonsmelon-dev`
- Live: `https://www.felonsmelon.com/`
Working-tree sync at lock: local `efa4f67` was 126 commits behind origin `c8daaac`. Fast-forward required before K3 edits.
Duplicates stay frozen: `felons-melon-app`, `felonsmelon-appwrite-migration`, zip archives, missing `C:\Users\kirkb\...` path.

### K3 — Fix only launch-blocking bugs
Lane: FM BUILD
Owner: Hermes (shop empty; Codex optional later)
Status: ACTIVE after ff-only pull of locked tree
In scope: Stripe trial checkout after sign-in, webhook completion, guest vs signup honesty, job-board empty state, dead CTAs.
Out of scope: new modules, trusted-person routing, kiosk, marketing site rebuilds.
Success: named bugs have before/after evidence on the live URL.

### K4 — Independent public QA
Lane: FM BUILD / QA
Owner: GrokBot (or Kirk if no Grok runtime)
Status: QUEUED behind K3
Do: copy, spelling, metadata, every major CTA, mobile + desktop, no secrets in client bundle.
Success: independent reviewer signs PASS or BLOCKED. Hermes may not certify its own work.

### K5 — Release receipt
Lane: FM BUILD
Owner: FlowBot + Sparky
Status: QUEUED behind K4
Success: one go/no-go record: commit, URL, checks, rollback point.

### K6 — First 10 real users
Lane: FM GROWTH
Owner: Kirk (human), Hermes prepares materials
Status: QUEUED behind K5
Do: 10 people who can complete letter → resume → job match without Kirk standing over them.
Success: 10 named/countable completions, not page views.

### K7 — First 100 users
Lane: FM GROWTH
Owner: Kirk + Hermes marketing lane
Status: QUEUED behind K6
Do: evidence-backed posts pointing at the live working path. Kirk clicks Post.

### K8 — Trusted-person monthly packet (SHELVED)
Lane: FM PRODUCT
Owner: unassigned
Status: SHELVED
Intent: a user can send recovery/proof output each month to a PO, case worker, DCFS, or other trusted person.
Do not design or build until K5 is PASS.

### K9 — Auto kiosk (NEXT APP, not this chain)
Lane: AUTO
Owner: AlphaBot / later
Status: PARKED until FM works.

## Current WIP (max 3)

1. K1 Verify live customer path — Hermes — IN PROGRESS
2. K2 Lock canonical production tree — Kirk — BLOCKED, needs one answer
3. Protect daily income lane — Kirk — stays protected, not cancelled

Everything else stays queued.

## Kirk interrupt required for K2

Name the production working tree. Recommended default on this machine unless Kirk overrides:

- Repo: `kirkbradford0/felonsmelonkirkbradford0gmail`
- Local: `C:\Users\bradf\Documents\Codex\felonsmelon-dev`
- Live: `https://www.felonsmelon.com/`

If that is wrong, say the real path. Do not let Codex invent a third clone.
