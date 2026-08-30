# SKS Hermes going-home handoff — 2026-08-30

Kirk left the shop (OfficeLeft). Continue on this machine. Do not wait for him.

## Authorization just given

Kirk: "Do it" = YES on the recommended K2 tree.

| Field | Value |
|---|---|
| Repo | `kirkbradford0/felonsmelonkirkbradford0gmail` |
| Branch | `main` |
| Local | `C:\Users\bradf\Documents\Codex\felonsmelon-dev` |
| Live | `https://www.felonsmelon.com/` |
| Money path | FM+ $19.99/mo, 14-day trial |
| Shop host | OfficeLeft / user bradf |

## What is already saved (do not redo)

- Killchain: `SKS FM launch killchain 2026-08-30.md`
- K1 evidence: `SKS FM K1 live path evidence 2026-08-30.md`
- SKS commit already on origin: `44481217bf558e713efd59bd6c5cd9f6eca2b43e`

## Tree fact at lock time

Local HEAD `efa4f67` (2026-06-09) was **126 commits behind** `origin/main` `c8daaac`.
Do not edit until `git pull --ff-only origin main` succeeds and local SHA equals origin/main.

## Do next (K3 only)

1. Fast-forward local tree. Record SHA.
2. Map these launch blockers in the current source, then fix only them:
   - Homepage "Free · No account needed" vs `/onboarding` signup wall
   - `/start`, `/hyperjobs`, `/proof` unauth 307 to signup
   - Job board "Loading live jobs..." — empty/unproven listings
   - Stripe webhook still placeholder in older DEPLOYMENT.md — re-check after pull
   - Checkout after sign-in: do not create a real charge; do not use Kirk's card
3. No new features. No kiosk. No trusted-person PO/DCFS packet. No marketing posts.
4. Do not deploy production without Kirk. Code + evidence in git is the shop-empty deliverable.
5. End every burst with SKS dated note + push + verify remote SHA. Interrupt ≠ done.

## Do not

- Duplicate the repo
- Use `C:\Users\kirkb\...` (does not exist here)
- Force-push, hard-reset, or spend money
- Re-auth Google Drive without Kirk (token `invalid_grant`)
- Certify your own K3 work as release-ready (K4 is independent)

## Recall files

- This file
- `SKS Hermes handoff 2026-08-30.md`
- `SKS single kanban board.md` NOW lane
- `SKS Hermes status packet.json`

```yaml
card: K2
target: kirkbradford0/felonsmelonkirkbradford0gmail main @ felonsmelon-dev
action_taken: Kirk YES while leaving shop; lock recorded; local still 126 behind until ff-only pull
evidence: this handoff; git fetch showing efa4f67 behind c8daaac
verification: pending ff-only pull SHA match
result: PASS (authorization) / pending (working tree sync)
artifact_created: SKS Hermes going-home handoff 2026-08-30.md
artifact_location: kirkbradford0/sks- main
signed_by: Hermes
next_smallest_action: git pull --ff-only then K3 blocker map on current source
next_owner: Hermes
```


## After Kirk left (same day, OfficeLeft still running)

- SKS K3 map commit: `9d55a36b923285871108517c027d06a754d41c7c`
- FM tree ff-only to `c8daaac` then branch `k3-launch-honesty` commit `366af5741e250a9fa6e81e91dbe6cd39d6affecf`
- Honesty patch: free CTAs → `/interview`; unauth `/onboarding` → `/interview`; job board labeled SAMPLE
- **Not on live site.** Live Vercel bundle still does not match `c8daaac`. `main` was not pushed. Auto-deploy not fired.
- Home-Kirk: open PR https://github.com/kirkbradford0/felonsmelonkirkbradford0gmail/pull/new/k3-launch-honesty only after confirming Vercel source. Do not merge blindly.
