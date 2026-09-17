# SKS Charlie handoff 2026-09-17

## What I did

- Kirk sent a handwritten runway napkin plus later sitrep/app screenshots and asked for a burn-rate engine.
- Checked SKS + local desks first. No existing burn/runway tracker. Did not invent a second board.
- Built a **private local engine** (shop box only). Personal amounts, account numbers, and snapshots stay off SKS.
- Verified the napkin math: the ~7.8-month figure is net ÷ monthly nut. That is an output, not an input. Treating brokerage as rent cash is theater.
- Engine splits cash / invested / debt, reports three runways, flags incomplete nut and zero income, and refuses to annualize a 2-day cash drop.
- 8 unit tests pass on the shop box. Charlie built it — Charlie does not certify the books. Kirk owns money decisions.
- Broker still locked. Did not push FM main. Left Alpha/cron uncommitted notes untouched.

## Commit SHA

(this file's SHA fill rides the following commit)

## State

- Charlie: working. Host OfficeLeft. profile charlie. @hermesbrickbot.
- SKS packet: `SKS Charlie status packet.json`
- Private desk exists locally; SKS only records that it exists.

## Process fix

A circular model that feeds the napkin's output months back in as Time_Allocated is not a burn engine. Daily_Burn = nut / days is a tautology. Observed cash between dated snapshots is the check. Chat is not state.

## Next action for Kirk

1. Next snapshot: paste or photo the same three piles (bank cash, brokerage total, debt). Engine will compute. Do not treat invested as liquid.
2. If you want this on a schedule, say so. No cron unless you ask.
3. Charlie still does not certify own work. Money clicks stay Kirk.
