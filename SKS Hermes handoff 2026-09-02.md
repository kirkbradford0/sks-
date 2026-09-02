# SKS Hermes handoff 2026-09-02

## What I did
Stood up a **paper** USDE seesaw desk on the shop PC. $100 start, +$20 target, fees 0. Same Yahoo adapter as TwoAM. Broker stays locked.

Ticker is **USDE equity** (StablecoinX Inc. / Nasdaq), not the USDe coin. Kirk bought the seesaw on Public.com. S-1 is stock/warrant registration, not a stablecoin product.

GitHub tools reviewed, not cloned as a runtime:
- PublicDotCom/publicdotcom-py — official Public API SDK (live later)
- ryankemmer/MeanReversionTradingBot — Bollinger ±2σ pattern (rewritten, no TDA)
- hugoguerrap/crypto-claude-desk — too heavy (Claude Code plugin, 9 MCP servers). Skip.
- Trade-With-Claude/cbt-framework — backtest workflow. Steal later, not tonight.
- l3lackcurtains/trading-ops — scan/verdict format. Steal later.

## Honest $100 → $20 test (Yahoo, this tape)
- 5m / 5d: **+$30.45**, 7 round trips, 85.7% win, 6.1% max DD. Hit +$20.
- 15m / 5d: +$6.75. Miss.
- 15m / 1mo: +$17.51. Miss.
- 1h / 1mo: +$19.25 on one trade. Miss.

The 5m win is the late-Aug squeeze. Desk default is 5m so the challenge matches that math. Not a live edge claim.

## State
- Code: shop PC `usde-desk` (paper runner, SQLite ledger, `UNLOCK.example.txt`)
- Cron script: Hermes `scripts/usde_desk.py`
- Live Public.com API: **not wired**. Needs Kirk key (Account Settings → Security → API) then `UNLOCK.txt` line 1 = `UNLOCK`
- Grok: this Hermes session already is Grok 4.6 via Nous. xAI CLI is installed separately; GrokBot SKS role = relay, not trader
- Sparky: charter on sks-. Orchestrator. Must not place a trade. Hermes is the hands.

## Process fix
Do not clone crypto-claude-desk for a $100 equity seesaw. Paper first. No live order without UNLOCK.

## Next action for Kirk
1. Leave the paper cron running.
2. If live: generate Public API key, drop `UNLOCK.txt`, say it in writing.
3. Do not expect +$20 every week. Squeeze tape is the sample that cleared it.
