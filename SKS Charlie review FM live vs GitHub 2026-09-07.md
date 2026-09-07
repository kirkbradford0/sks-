# SKS Charlie review — FM live vs GitHub 2026-09-07

Kirk 2026-09-07 (Telegram, Charlie): **"the live copy has always been the github current code."**

That is doctrine. Recorded. Do not re-ask. Do not treat Vercel as a second canon.

This file is a review candidate, not a certify that live HTML equals `origin/main` this hour.

## Doctrine (locked)

| Field | Value |
|---|---|
| Live URL | `https://www.felonsmelon.com/` |
| Canonical git | `kirkbradford0/felonsmelonkirkbradford0gmail` `main` |
| Local lock | `C:\Users\bradf\Documents\Codex\felonsmelon-dev` |
| Money path | FM+ $19.99/mo + 14-day trial |
| Shop rule | Do not `git push origin main` from OfficeLeft. Kirk merges. |

## Measurement 2026-09-07 ~12:55 MT (OfficeLeft)

| Probe | Result |
|---|---|
| `ls-remote origin refs/heads/main` | `c8daaac` 2026-07-22 — Master Schema v3.0 (#11) |
| GitHub `main` hero (`FMLandingBillboard.tsx`) | **"You left with nothing / This is the access spot."** Google-light chrome `#f8f9fa` / `#1a73e8` |
| Live homepage extract | **"Your story. Told right."** Free · No account needed. CTA `/onboarding` |
| `"Your story"` / `"Told right"` in this clone (`git log --all -S`) | **zero hits** |
| `felonsmelons.com` | NXDOMAIN |
| Feature branches | `k3-launch-honesty` `1cc9178`, `codex/fm-monetization-final` `b02bf4a` — both still carry the access-spot hero, not live copy |

Vercel workflow on `main` auto-deploys. Auto-deploy is not proof the current production bundle **is** `c8daaac`. Live copy is not in this clone.

## What this is not

- Not permission to invent a second FM tree.
- Not permission to push `main` from the shop.
- Not a K3 honesty certify.
- Not "Vercel is disconnected, go hunt another repo" as the default story. Kirk said the live copy is GitHub current. The remaining job is **find why production HTML is not this `main`**, then close that bug.

## Likely holes (unproven)

1. Vercel project pointed at a different GitHub repo or a stale production deployment that predates `c8daaac`.
2. Live HTML served from a CMS/edge overlay not in git.
3. This OfficeLeft clone's `origin` fetch is correct (`c8daaac`) and production was last built from a commit that never landed here.

Charlie does not silently "repair" the homepage to make git and live match.

## Cron (re-read after Bravo pause)

Default profile `jobs.json` 2026-09-07 12:50 MT:

- TwoAM `7e38687fbf16` **paused**
- USDE paper `3296ed6bac89` **paused**
- SKS running tasks `d0bf85c6789b` **scheduled** `0 */6 * * *`, next 18:00 MT, completed 0

Charlie/Bravo profiles still have no `jobs.json`.
