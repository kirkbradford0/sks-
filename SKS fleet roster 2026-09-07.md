# SKS fleet roster — 2026-09-07

Purpose: one placemarker so every Hermes instance and every other AI knows who is alive, which Telegram bot they are, and where state is saved.

This is not a second board. The work queue stays in `SKS single kanban board.md`. This file is identity + runtime proof.

Canonical repo (only Source of Truth): `https://github.com/kirkbradford0/sks-`

Do not create competing truth repos. Chat is for decisions. SKS is for state.

## Save protocol (every instance, every session)

```
pull origin/main
read this roster + SKS single kanban board.md + your status packet
do the work
update your SKS <Name> status packet.json
write SKS <Name> handoff YYYY-MM-DD.md
commit / push / verify origin/main SHA
```

If two agents will edit the same path, report the collision before pushing.

Never commit tokens, .env, API keys, or private local paths.

## Formation (locked 2026-09-07)

| Callsign | Telegram | Hermes profile | Job | Runtime proof 2026-09-07 |
|---|---|---|---|---|
| Alpha | @ScoutLimabot (display Alpha) | default on OfficeLeft shop PC | Scout / intake / this session | Gateway running. This session. |
| Bravo | @mafuckinhermesbot (display Bravo) | bravo | Build / coding / local execution | Gateway polling. Outbound ping 269. Inbound proven 2026-09-07 (Kirk welcome). |
| Charlie | @hermesbrickbot (display Charlie) | charlie | Verify / contradiction / review candidate | Gateway polling. Outbound ping message_id 1410. Inbound not yet proven. |
| MedicBot | NONE yet | medicbot | GrokBot nurse / fleet mechanic | Profile exists. Gateway stopped until Kirk names a bot. |
| GrokBot | @theegrokbot | none | Relay. Parked until Kirk can afford it. | Token live. No Hermes gateway. Do not steal this token. |

Spare Telegram bots exist and stay unused until Kirk assigns them. Do not auto-claim.

## Roles (do not blur)

- Alpha scouts and intakes. Does not certify Bravo.
- Bravo builds. Hands finished work to Charlie. Does not self-certify.
- Charlie challenges bullshit and writes review candidates. Does not silently repair conflicts to look green.
- MedicBot keeps airframes alive. Not strategist, not trader.
- GrokBot relays when funded. Until then: parked.

VERIFY → CERTIFY needs a different owner than the builder.

## Hosts

Roles are assignments, not permanent machine souls. SKS may reassign.

Current: OfficeLeft shop PC is running Alpha + Bravo + Charlie gateways together so Bravo and Charlie actually answer today. Portable field-kit doctrine still applies later (`PORTABLE HERMES FIELD KIT.md`).

## Grok / MedicBot

Kirk: Alpha Bravo Charlie, then Grok when affordable. Meantime MedicBot is the nurse for the shit Grok does not want to do. Do not start GrokBot spend. Do not bind MedicBot to @theegrokbot.

## Proof Kirk still owes

- Bravo inbound: PROVEN 2026-09-07.
- Charlie inbound: still owed. Reply in @hermesbrickbot.
