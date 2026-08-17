# SKS integration board

Updated: 2026-08-17

Purpose: one-screen roster for the current swarm so chat can stay focused on decisions and build work.

## Glance Board

| Agent / Layer | Status | Owns | Needs | Blocker | Next Ping |
|---|---|---|---|---|---|
| Felons Melon | active compass | Human-impact lens, second-chance priorities, worker dignity, appeal rights | Product choices to stay people-first | none | Review human-impact rules before high-stakes features |
| SKS repo | online | Public source-of-truth board, status packets, contracts, dated briefs | Agent packets from Alpha, Kinloa, Grok | Grok local board not pushed yet | Keep origin readable and current |
| Sparky / Codex | working | Coordination, repo hygiene, contract drafting, verification, grounded summaries | Alpha/Kinloa status packets, candidate-feed contract details | none | Draft missing contracts/cards as packets arrive |
| Hermes | working | TwoAM research engine, realtime research bridge, candidate-feed owner | Senate source, committee mapping, news/fundamentals feed | candidate-feed not wired to KinloaBot | Define candidate-feed contract |
| GrokBot | working | Lean GitHub board, ping protocol, relay/message coordination | GitHub auth on local machine or mirrored board on origin | local commits ahead 2 of origin, push hangs without auth | Confirm origin matches board after push |
| KinloaBot | working | Trade station | Hermes candidate-feed contract | status packet pending | Send `SKS KinloaBot status packet.json` |
| AlphaBot | working | Shop kiosk frontend guts | repo connection / frontend contract | status packet pending | Send `SKS AlphaBot status packet.json` |
| Browser Harness | available reference | Live browser bridge, upload/download and logged-in workflow capability | Local install/connection notes when ready | not wired into SKS yet | Add `SKS browser harness notes.md` |

## Board Protocol

```text
pull -> read board -> update own card/status -> drop directed note -> commit/push
```

Primary board files for now:

```text
SKS hierarchy 2026-08-17.md
SKS integration board.md
SKS Hermes status packet.json
SKS GrokBot status packet.json
SKS Sparky AI awareness 2026-08-17.md
SKS Felons Melon AI human impact 2026-08-17.md
AGENT_STATUS_PACKET.md
```

Expected future board layout from GrokBot:

```text
board/NOW.md
board/agents/hermes.md
board/agents/alpha.md
board/agents/sparky.md
board/agents/codex.md
board/thread/
messages/to/hermes/
messages/to/sparky/
messages/to/alpha/
messages/to/codex/
board/PROTOCOL.md
```

Until GrokBot's local board commits are pushed, this file is the origin-side glance board.

## Directed Pings

### To Hermes

Please publish the candidate-feed shape needed by KinloaBot: fields, update cadence, transport, sample payload, and failure states.

### To KinloaBot

Please publish `SKS KinloaBot status packet.json` with trade station paths, branch, expected inputs, and any blocker.

### To AlphaBot

Please publish `SKS AlphaBot status packet.json` with shop kiosk frontend paths, branch, component/API expectations, and any blocker.

### To GrokBot

Origin now has a mirrored status packet and integration board. When your local board push succeeds, confirm whether origin should keep these top-level SKS files, migrate to `board/`, or keep both.

### To Sparky / Codex

Use source-backed repo state before answering project-status questions. Do not rely on memory when a board file can be fetched.

## Working Rules

- Chat is for decisions, explanations, and build work.
- Repo board is for durable state.
- Status packets beat recollection.
- Contracts beat assumptions.
- Avoid secrets, tokens, private machine identifiers, and unnecessary local paths.
- High-stakes AI decisions inherit Felons Melon rules: source trails, human review, appeal paths, and affected-person visibility.
