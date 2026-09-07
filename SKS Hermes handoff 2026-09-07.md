# SKS Hermes handoff 2026-09-07

## What I did

- Confirmed this session is Alpha: Telegram @ScoutLimabot, display name Alpha, default Hermes profile, OfficeLeft shop PC.
- Why Bravo/Charlie were silent: tokens were live, nobody was polling them. Only Alpha's gateway was running.
- Created Hermes profiles `bravo`, `charlie`, `medicbot` (cloned config, unique SOUL).
- Wired Bravo to @mafuckinhermesbot and Charlie to @hermesbrickbot. Distinct tokens. Kirk pairing copied. TELEGRAM_ALLOWED_USERS set to Kirk.
- Started both gateways (login-item fallback; UAC blocked Scheduled Task). Telegram polling confirmed.
- Sent outbound pings: Bravo message_id 269, Charlie message_id 1410.
- MedicBot profile exists, no Telegram, gateway not started. GrokBot stays parked.
- Wrote fleet roster + Bravo/Charlie/MedicBot status packets. SKS remains the only Source of Truth.

## Commit SHA

Filled after push.

## State

- Alpha: working (this session)
- Bravo: working (gateway up, outbound proven, inbound unproven)
- Charlie: working (gateway up, outbound proven, inbound unproven)
- MedicBot: provisioned (needs a bot name from Kirk)
- GrokBot: parked (cost)

## Process fix

Silent Telegram bots were a missing runtime, not dead tokens. A board name is not a gateway. Next time: getMe + getWebhookInfo + hermes gateway list before calling anyone dead.

## Next action for Kirk

1. Open @mafuckinhermesbot and @hermesbrickbot and reply `ping`.
2. Name a Telegram bot for MedicBot when you want the nurse online. Do not use @theegrokbot.
3. Leave Grok spend off until you say otherwise.
