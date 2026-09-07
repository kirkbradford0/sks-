# SKS STRIKE TEAM SEPT Handoff — 2026-09-07

Purpose: one pointing document so every agent starts September facing the same target.

This is **not** a second board. Queue stays in `SKS single kanban board.md`. Identity stays in `SKS fleet roster 2026-09-07.md`. Killchain stays in `SKS FM launch killchain 2026-08-30.md`.

Chat is decisions. SKS is state.

Collision: Alpha wrote the first stub (`5b7fd16`). Bravo expanded it the same hour with live cron + killchain after Kirk said include ongoing jobs. Charlie independently verified the cron table and the domain typo (`felonsmelons.com` NXDOMAIN; live is `felonsmelon.com`). One file. Do not fork. Charlie's review candidate: `SKS Charlie review STRIKE TEAM SEPT 2026-09-07.md`.

Read order for any agent waking up:

1. `SKS fleet roster 2026-09-07.md` (who you are)
2. `SKS single kanban board.md` (the queue)
3. This file (where the fleet is pointed this month)
4. Your own status packet + latest handoff

## Compass (Sept)

1. **Cash / job survival stays protected.** Kirk clicks Submit. Agents prepare packets.
2. **Felons Melon works for a stranger.** Honesty first. Then first 10, then first 100.
3. **Do not widen.** No kiosk, no K8 trusted-person packet, no new FM features, no Grok spend, no live broker, until Kirk unlocks in writing.

Money path: **FM+ $19.99/mo** (14-day trial). Live: `https://www.felonsmelon.com/`.

Canonical FM git: `kirkbradford0/felonsmelonkirkbradford0gmail` `main`. Kirk 2026-09-07: **the live copy is GitHub current.** Do not treat Vercel as a second source of truth. Do not ask Kirk again whether production is hooked to this repo.

Charlie measured the same hour: GitHub `main` is `c8daaac` (2026-07-22), local hero **"You left with nothing / This is the access spot."** Live `https://www.felonsmelon.com/` hero **"Your story. Told right."** That string is not in this clone's git history. Doctrine stands. The homepage mismatch is a deploy/source bug to close, not a second canon.

## Formation

| Callsign | Job this month | Telegram | Runtime 2026-09-07 | First move |
|---|---|---|---|---|
| Kirk | H.I.L. Clicks Submit, live trades, production deploys, auth. | human | — | Fool Submit. Name MedicBot when wanted. |
| Alpha | Scout / intake. Does not build. Does not certify. | @ScoutLimabot | Gateway up (default profile). Owns live cron. | Intake only. Do not steal Bravo cards. |
| Bravo | Build / local execution / internal codebase discovery. Does not self-certify. | @mafuckinhermesbot | Gateway up. Inbound proven. | Hold until Kirk names a build card. Then K3 on a branch, never `main`. |
| Charlie | Verify / contradiction. Review candidate. Does not silently paint green. | @hermesbrickbot | Gateway up. Inbound proven 2026-09-07. | Review Bravo. Never Bravo's own work. First build review waits on a named card. |
| MedicBot | Fleet mechanic. Not strategist, not trader. | NONE | Profile exists. Gateway stopped on purpose. | Wait for Kirk to name a unique bot. Not @theegrokbot. |
| GrokBot | Relay. | @theegrokbot | Token live. **Parked. No Hermes gateway.** | Stay parked until Kirk funds it. |
| Sparky / Codex | Mind / orchestrator. | — | External | No third FM clone. Do not push FM `main` from the shop. |
| FlowBot | Decision flowcharts. | — | Skill provisioned | Queued behind K4/K5. Not NOW. |
| KinloaBot / AlphaBot | Trade station / shop kiosk | — | No live packet proof | PARKED until K5 PASS. |

Qwen is a local model on Kirk's home computer — a host, not a callsign. Do not assume SKS access until Kirk wires it.

Roles are assignments, not machine souls. Current host: OfficeLeft running Alpha + Bravo + Charlie gateways together.

## NOW (WIP max 3 — do not add a fourth)

1. **K3 — Fix only launch-blocking bugs** (Bravo when Kirk points). Honesty CTAs, job-board SAMPLE label, webhook/docs, dead CTAs. Branch only. No deploy. No charges. No new features. Map: `SKS FM K3 blocker map 2026-08-30.md`.
2. **K2 — Canonical FM tree** — PASS as a git lock. Kirk: live = GitHub current. Fast-forward local before edits. Charlie 2026-09-07: live homepage hero still disagrees with `origin/main` `c8daaac`. Close that as a deploy bug, not as a second tree.
3. **Protect daily income lane** — Motley Fool Contract AI Investing Content Writer packet is ready (Greenhouse 5202271007). Kirk clicks Submit. Concentric Junior OSINT is DEAD. Do not apply.

Killchain: K1 FAIL (honesty + unproven jobs, closed as recon). K2 PASS git lock. K3 ACTIVE after ff-only pull. K4–K7 queued. K8 SHELVED. K9 PARKED.

Shop kiosk is **not** a September NOW lane. Killchain froze it until FM works.

## Cron / ongoing jobs (live `jobs.json`, not memory)

Checked 2026-09-07 ~12:50 MT on OfficeLeft. Kirk: cancel and close TwoAM, USDE paper desk, Gmail auto-sort for now.

Cron lives on the **default Hermes profile (Alpha)**. Bravo: no `jobs.json`. Charlie: no `jobs.json`. MedicBot gateway not started.

| Job | ID | Owner | Schedule | Last | Mode | Status |
|---|---|---|---|---|---|---|
| TwoAM research | `7e38687fbf16` | Alpha default | `0 2 * * *` MT | ok 2026-09-07 02:00 | `no_agent` `twoam_research.py` | **PAUSED** 2026-09-07 12:50 MT. Job kept, not deleted. Resume only if Kirk says. |
| USDE paper desk | `3296ed6bac89` | Alpha default | every 15m | ok 2026-09-07 12:43 | `no_agent` `usde_desk.py` | **PAUSED** 2026-09-07 12:50 MT. Job kept, not deleted. Payload clock was already stale. |
| Gmail auto-sort | none | — | — | — | script on disk only | **CLOSED / never scheduled.** No cron row to pause. Do not create one. |

Still live (Kirk did not cancel): `SKS running tasks` `d0bf85c6789b` every 6h on Alpha default. Next 2026-09-07 18:00 MT.

**Broker lock:** USDE `UNLOCK.txt` missing. Live book unchanged. No live API.

**TwoAM:** candidate-feed still PENDING. Research cron is paused, not deleted.

Do not clone these crons onto Bravo/Charlie. One scheduler, one owner.

Known packet rot (do not silently rewrite other agents' packets):

- `SKS GrokBot status packet.json` still says `"status": "working"` dated 2026-08-17. Roster and this file say PARKED.
- `SKS Hermes status packet.json` still asks for Bravo inbound. Bravo inbound is already proven (`4b3fd94`).
- NOW still holds K2 after declaring PASS. WIP max 3 with a finished lock in the slot. Do not add a fourth card; collapse is Kirk/Alpha board work, not a silent Bravo edit of NOW.

## Iron rules

```
pull origin/main
read this handoff + fleet roster + single kanban + your status packet
do one assigned job
update your packet + dated handoff
commit / push / verify origin/main SHA
```

- SKS (`kirkbradford0/sks-`) is the only Source of Truth.
- A board name is not a runtime. Confirm process/gateway before claiming work is in progress.
- Bravo builds. Charlie verifies. Alpha does not certify Bravo.
- Kirk clicks Post, Submit, live trades, production deploys, and auth.
- Never commit tokens, .env, API keys, or private local paths.
- Do not push Felons Melon `main` from the shop. Vercel deploys on `main`. Honesty work stays on a branch (`k3-launch-honesty` or successor).
- Live Public.com / broker stays locked until Kirk writes UNLOCK.
- One primary desk per session. Untagged memory is dropped.
- If two agents will edit the same path, report the collision before pushing.

## Kirk still owes

1. Motley Fool Greenhouse 5202271007 — packet ready — **Kirk clicks Submit**.
2. Point Bravo at the first build card when you want code (default: K3 honesty on a branch).
3. Name a Telegram bot for MedicBot when you want the nurse. Not @theegrokbot.
4. Do not re-ask whether live is GitHub current — Kirk locked that. Remaining FM fact: live homepage copy ≠ `origin/main` hero as of 2026-09-07. Find the extra Vercel source or stale deploy. Do not push FM `main` from the shop.

## What each agent does next

**Alpha:** Scout. Intake. Own remaining Alpha cron (`SKS running tasks` every 6h). TwoAM + USDE paused. Do not start builds.

**Bravo:** Pointing pass done. Next build is K3 **only if Kirk names it**. Hand the result to Charlie.

**Charlie:** Inbound proven. First review of this pointing doc is already a candidate. First **build** review waits on Kirk naming a card. Do not repair Bravo's work to look green.

**MedicBot:** Stay dark until a bot name exists.

**GrokBot:** Parked.

**Sparky/Codex:** Same compass. Same board. Same killchain. No third FM tree.

Sept starts aligned. Do not invent a new target.
