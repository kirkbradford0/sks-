# SKS FM K3 blocker map — 2026-08-30

Kirk left OfficeLeft. Tree fast-forwarded. **Do not merge to `main` from this machine while Kirk is gone** — `.github/workflows/vercel-deploy.yml` deploys production on every `main` push.

## SHAs

| Place | SHA | Date | Notes |
|---|---|---|---|
| Local + origin/main | `c8daaac06eebb71c7d2f53cc06f24ddd28ecc1cc` | 2026-07-22 | ff-only pull from `efa4f67` (was 126 behind) |
| Live `felonsmelon.com` | UNKNOWN — **not this SHA** | CDN Age ~24d on homepage | Live hero is "Your story. Told right." Local hero is "You left with nothing / This is the access spot." |

K2 locked the GitHub repo. It did **not** prove Vercel is serving that repo. Home-Kirk must confirm the Vercel project source before any production deploy.

## Blocker map (current source)

### B1 — Free letter CTA lies
- Homepage `FMLandingBillboard` "Start free" and "Start Interview — It's Free" point to `/onboarding`.
- `/onboarding` is public in middleware, then client `fetch("/api/onboarding/v2/status")` 401 → `window.location.replace("/signup?next=%2Fonboarding")`.
- Real guest interview already exists: `/interview` + `PreAuthInterviewFlow` (localStorage draft, narrative preview, then signup).
- Live site (different bundle) also claims "Free · No account needed" and sends Step 1 to `/onboarding`.

Fix on branch, not main: point free CTAs at `/interview`; on 401 send guests to `/interview` not signup.

### B2 — Job board is demo data
- `src/app/job-board/page.tsx` comment: "Demo jobs for initial load (will be replaced with Supabase data in production)".
- Hardcoded Chicago/LA/NY roles. Not live scrapes.
- Live `/job-board` showed "Loading live jobs..." — different UI than this SHA. Either way, do not claim live listings.

Fix on branch: label SAMPLE so a stranger is not sold fake jobs. Do not invent a scraper in K3.

### B3 — Stripe webhook
- Code is real (`src/app/api/stripe/webhook/route.ts`): signature verify + billing sync.
- `DEPLOYMENT.md` line still says "placeholder-level" — doc lag, not missing handler.
- Live `POST /api/stripe/checkout` 401 requires sign-in (intended).
- Cannot prove Vercel has `STRIPE_WEBHOOK_SECRET` without Kirk / a test charge. No charges while he is gone.

### B4 — Auth walls that are honest in this SHA, dishonest on live
This SHA already says "Sign in first" on HyperJobs, Proof, Sparky. Live tools page still advertised some as Available/Skeleton. Copy QA is K4 after the live SHA is the locked SHA.

## Rules while shop is empty

1. SKS notes first, then code.
2. FM work on branch `k3-launch-honesty` only. Never `git push origin main` from OfficeLeft tonight.
3. No Stripe live session. No new accounts in Kirk's name. No kiosk. No K8 packet.
4. Interrupt ≠ done. Next burst re-reads this file + going-home handoff.

## Recall for home-Kirk

- SKS: `https://github.com/kirkbradford0/sks-` SHA of going-home commit `f8a7db77c1d91df5a3c7f9bb7f17cdb33e88e597` plus this file's later commit.
- FM tree: `C:\Users\bradf\Documents\Codex\felonsmelon-dev`
- Money path: FM+ $19.99/mo
- First question at home: is Vercel production hooked to `felonsmelonkirkbradford0gmail` `main`? If no, K2 is a git lock only.
