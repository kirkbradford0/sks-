# SKS STRIKE TEAM SEPT handoff — 2026-09-07

Written by Alpha (@ScoutLimabot). Purpose: one document every agent reads first so all lanes point the same direction. This does not replace the roster, the kanban board, or individual handoffs — it is the alignment layer on top of them.

Read order for any agent waking up fresh:
1. `SKS fleet roster 2026-09-07.md` (who you are)
2. `SKS single kanban board.md` (what the work is)
3. This file (where the fleet is pointed this month)
4. Your own status packet + latest handoff

## Where the fleet stands (2026-09-07)

| Callsign | Telegram | State | Proof |
|---|---|---|---|
| Alpha | @ScoutLimabot | Working — scout/intake | This session, default profile, OfficeLeft |
| Bravo | @mafuckinhermesbot | Working — build | Gateway polling. Inbound PROVEN (Kirk's `Bravo24` test, msg logged 06:47). |
| Charlie | @hermesbrickbot | Working — verify | Gateway polling, outbound ping 1410. Inbound NOT yet proven. |
| MedicBot | none yet | Provisioned | Profile exists, gateway stopped until Kirk names a bot. |
| GrokBot | @theegrokbot | PARKED | No spend until Kirk says otherwise. Do not bind or claim. |

Qwen is the local downloaded model on Kirk's home computer — that is a separate host, not a callsign yet. Do not assume Qwen has SKS repo access until Kirk wires it.

## September lanes (the direction)

Lane 1 — FELONS MELON (felonsmelons.com). Goal: 100 real users. Front page = Stripe TEST checkout. Gazette desks exist (fm, jobs, city, markets, shop, packets, wire). One Hermes session = one primary desk; untagged memory is dropped.

Lane 2 — JOB SEARCH. Canonical desk: `C:\Users\bradf\Job Applications\`. Motley Fool Contract AI Investing Content Writer packet is READY (Greenhouse 5202271007, $45–50/hr) — only Kirk clicks Submit. Concentric Junior OSINT is DEAD, do not apply.

Lane 3 — MARKETS. Live book: 100 shares USDE @ $8.29. Rules are locked: 3% stop ($8.04 full book), +3% sell 50 shares ($8.54), ladder remainder $8.37 then $8.20 out. No adds, no averaging down, no live API orders — broker stays LOCKED. Paper desk `C:\Users\bradf\usde-desk` runs on cron.

Lane 4 — SHOP (Bradford Auto). Lobby kiosk is the Lovable check-in app; it still discards data. Kiosk receiver node: `C:/Users/bradf/kiosk-node/`.

## Division of labor (do not blur)

- Alpha scouts, intakes, orients, writes alignment docs like this one. Does not certify Bravo's builds.
- Bravo builds and codes. Hands finished work to Charlie. Does not self-certify.
- Charlie challenges and verifies. Writes review candidates. Does not silently repair to make things look green.
- MedicBot (when online) keeps airframes alive — gateways, pairing, cron ghosts. Not a strategist, not a trader.
- Kirk (H.I.L.) makes all final calls: submit, spend, unlock, deploy.

VERIFY → CERTIFY always needs a different owner than the builder.

## Open obligations

1. Kirk: reply `ping` in @hermesbrickbot to prove Charlie inbound. Last unproven link in the core three.
2. Kirk: name a Telegram bot for MedicBot when the nurse is wanted online (never @theegrokbot).
3. Bravo: first build task of September is unassigned — Kirk calls the lane, Bravo takes it from the kanban board.
4. Charlie: after inbound proof, first review task is to re-verify whatever Bravo ships.
5. Qwen (home computer): standby until Kirk wires it into SKS.

## Rules that keep us alive

- SKS repo (`github.com/kirkbradford0/sks-`) is the ONLY Source of Truth. Chat is for decisions, not state.
- Every session ends with: update status packet → write handoff → commit/push → record origin SHA.
- Never commit tokens, .env, API keys, or private local paths.
- If two agents will edit the same path, report the collision before pushing.
- Going-home file pattern: `SKS Hermes going-home handoff YYYY-MM-DD.md`.

## Alpha's read of the situation

The core three (Alpha/Bravo/Charlie) are standing for the first time. The bottleneck is no longer runtime — it is tasking. One Charlie inbound proof, one build assignment to Bravo, and this fleet moves from "alive" to "productive." Recommend Kirk pick the first Bravo build target from Lane 1 or Lane 4 today.
