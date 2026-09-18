# SKS Charlie handoff 2026-09-18

## What I did

- Alpha brief: verify the three tools Alpha wrote (`tools/agent_pbft.py`, `agent_circuit_breaker.py`, `agent_backoff.py`) at SHA `56005ad`. Nobody else had checked them.
- Did not silently repair. Did not stamp VERIFIED. Did not promote findings into SKS as fact.
- Ran an independent attack suite on OfficeLeft (not the author `__main__`). Bravo already filed happy-path card `DABS-20260918-bravo-001`. Charlie challenged it.

## Findings (intake only — live in dabs, dwell 72h)

Pointers, not copies:

- `pending/DABS-20260918-charlie-001` — pBFT is in-process theater, not a quorum
- `pending/DABS-20260918-charlie-002` — `root_signed` is a caller boolean, not Kirk
- `pending/DABS-20260918-charlie-003` — replay poisons REJECTED ids; COMMITTED keyed on action_id not digest
- `pending/DABS-20260918-charlie-004` — backoff doomed-sleep after last fail; spend kill overshoots
- Challenge on `pending/DABS-20260918-bravo-001` — self-test observation ≠ council/HITL proof

Breaker consecutive + alternating loops do trip. Hash is order-independent. Exact N calls holds. Wall-clock kill between attempts holds. Broken cost meter fail-closes. Those are observations, not a green stamp.

Alpha going-home claims breaker 6/6 and backoff 8/8. Those test files are not in `sks-/tools/`.

## Commit SHA

(this file's SHA fill rides the following commit)

## State

- Charlie: working. Host OfficeLeft. profile charlie. @hermesbrickbot.
- SKS packet: `SKS Charlie status packet.json`
- Left Alpha uncommitted cron-notes / cron_pass_notes untouched.
- Broker locked. Did not push FM main. Council seat: will not isolate/revoke/mutate alone.

## Process fix

Builder-run `ALL 5 TESTS PASS` is not verification. A local object that returns COMMITTED is not 2f+1. Status packet is not a certify.

## Next action for Kirk

1. Leave charlie-001..004 in dwell. A different agent stamps them — not Charlie.
2. Do not wire `agent_pbft.py` into isolate/revoke/mutate until 001–003 are resolved.
3. Money / broker unlock / deletes / submits still Kirk. Boolean flags do not count.

## Unchecked by anyone else

Charlie's attack suite and the four dabs cards — Bravo ran the self-test, not the attack.
