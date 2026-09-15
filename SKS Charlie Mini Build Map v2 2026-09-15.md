# SKS Charlie — Mini Build Map v2 2026-09-15

Pointing note. **Not a second SKS board.** `kirkbradford0/sks-` stays the only Source of Truth.

## What landed

Kirk named the schema (Telegram): one sidecar = one card. Columns are workflow only:

`INBOX → READY → BUILDING → BLOCKED → VERIFIED`

Card face: WHAT / WHERE / DEPENDS ON / BUILD / NEXT / PRIORITY.

v1 (seven attribute-columns, same item in multiple places) was rejected. There was no shipped prototype — ChatGPT/Claude handed the spec around. Charlie built the runnable map so Alpha/Bravo can use it. Charlie reviews **their cards**, not this tool.

## Where

Local sidecar on OfficeLeft, folder name `mini-build-map` (shop home). Not in this repo. Open `index.html` or serve it on loopback. Schema file: `types/build-map.ts`.

## Loop evidence (logic, not certify)

Headless dump of `?autotest=1` returned:

```
over: true
ok: true
cards: 1
finalStatus: VERIFIED
columns: INBOX 0 / READY 0 / BUILDING 0 / BLOCKED 0 / VERIFIED 1
unique: true
```

Parse of inline script: OK. Intro dump had title, + CARD, five columns, three seed cards.

## Do not paint green

- Charlie built it. VERIFY → CERTIFY needs a different owner. This file is a review candidate for the **tool**, not a certify.
- Map column VERIFIED ≠ SKS certify. A card sitting in VERIFIED is still uncertified until a different actor reviews it.
- Seed cards (Intro Submit, FM live-vs-git) are reminders, not board mutations. Sept NOW / running-tasks were not rewritten.
- Do not push FM `main`. Broker still locked.

## Next

1. Kirk: open the map, add a real sidecar if this is the sortie.
2. Alpha/Bravo: put builds on the map. Charlie reviews those cards.
3. Someone who did **not** write `index.html` signs the tool off — or Kirk says ship.
