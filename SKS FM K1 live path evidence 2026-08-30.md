# SKS FM K1 live path evidence — 2026-08-30

Card: K1 Verify live FM customer path
Signed by: Hermes (observation only — not independent certification)
Result: FAIL (launch blockers named). Not a code-fix card.
Live target: https://www.felonsmelon.com/
Method: HTTP headers + page extract. No account created. No Stripe charge. No code mutation.

## Path table

| Step | URL | HTTP | Result | Blocker |
|---|---|---|---|---|
| Homepage | `/` | 200 Vercel | PASS | Live. Hero: letter / resume / jobs. Claims "Free · No account needed" |
| Pricing | `/pricing` | 200 | PASS | Free $0, FM+ $19.99/mo 14-day trial, Sponsor $19, Org $49/mo |
| Stripe checkout | `POST /api/stripe/checkout` `{"kind":"fm_plus"}` | 401 | PASS as a gate, FAIL as a guest money path | Body: account required, `signInPath=/login?next=%2Fpricing`. No charge attempted |
| Dead checkout | `GET /api/checkout` | 410 | INFO | Old path gone. Current path is `/api/stripe/checkout` |
| Stripe checkout OPTIONS/GET | `GET /api/stripe/checkout` | 405 | INFO | POST-only. Expected |
| Onboarding / free letter | `/onboarding` | 200 | FAIL vs homepage claim | Page is "Create your account" (email/password + footprint A/B/C). Not a guest questionnaire |
| Signup | `/signup` | 200 | PASS | Account create, no payment required copy |
| Login | `/login` | 200 | PASS | Exists |
| Start / intake | `/start` | 307 | FAIL as free intake | Redirects `/signup?next=%2Fstart&portal=member` |
| HyperJobs | `/hyperjobs` | 307 via extract | FAIL as advertised tool | Tools page says "Skeleton live"; unauth hits signup |
| Proof | `/proof` | 307 | AUTH WALL | `/signup?next=%2Fproof&portal=member` |
| Dashboard | `/dashboard` | 307 | AUTH WALL | `/signup?next=%2Fdashboard&portal=member` |
| Resume | `/resume` | 200 | PASS empty | "No employment data found yet. Complete the narrative interview first" |
| Employment engine | `/employment` | 200 | PASS with Pro locks | Follow-up + interview prep locked until Pro |
| Job board | `/job-board` | 200 | BLOCKED / unproven | HTML: "Loading live jobs...". Listings not verified without JS session |
| Tools index | `/tools` | 200 | MIXED | Mix of Available / Skeleton live / Gate A–C live |
| Narrative workspace | `/narrative` | 200 | OPEN PAGE | Pricing marks it Pro / sign-in required. Header GET was 200; membership gate not fully proven from headers |
| Tour | `/tour` | 200 | PASS | Page loads |
| Health API | `/api/health` | 404 | INFO | No public health endpoint |
| Jobs API | `/api/jobs` | 404 | INFO | No public jobs API at that path |

## Launch blockers for K3 (do not fix until K2)

1. Homepage says free letter with no account. `/onboarding` is signup. Honesty bug.
2. Several tools advertised as available (`/start`, `/hyperjobs`, `/proof`) bounce unauth users to signup.
3. Job board does not prove live listings from a no-JS fetch.
4. Stripe trial cannot start until sign-in. That is intended per server, but webhook completion is still documented as placeholder in local `DEPLOYMENT.md` (2026-06-09 tree). Live webhook behavior is UNKNOWN until K2 + authenticated test.
5. Canonical working tree is not on this machine. Closest local clone last commit 2026-06-09. Live Vercel SHA unknown.

## Explicitly not done

- No FM source edit
- No deploy
- No Stripe live session
- No new user account
- No Google Drive write (OAuth `invalid_grant`)

## Successor

K2 — Kirk names the production repo/branch/local folder. Recommended default: `kirkbradford0/felonsmelonkirkbradford0gmail` at `C:\Users\bradf\Documents\Codex\felonsmelon-dev`, live URL `https://www.felonsmelon.com/`.
