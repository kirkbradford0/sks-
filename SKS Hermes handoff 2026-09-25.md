# SKS Hermes handoff 2026-09-25 (evening — war drum + HIL-DECK)

## What landed
1. **Crons fixed + pinned to war-drum chat.** Both live jobs were drift-skip failing (created under nous, config moved to ollama-cloud). Pinned both via `hermes cron edit --provider ollama-cloud --model glm-5.3-flash`, flipped deliver to `telegram`, acked 5 stale incidents, test-fired: SparkPost heartbeat ran clean (ledger check, sorter, PII-safe push f080621). SKS running tasks (d0bf85c6789b, 6-hourly) next fires 00:00. TwoAM + USDE crons remain paused (as left 09-07).
2. **HIL-DECK built and live** at sparkpost/hil-deck/ (commit e9b6336 on origin/main):
   - `deck_server.py` serves `current.html` at http://127.0.0.1:8799 — START-DECK.bat launches + opens browser.
   - Finish button POSTs the decisions log straight to `hil-deck/done/` (gitignored; smoke-test file cleaned after verify).
   - SparkPost heartbeat prompt updated: reads done/ logs, executes APPROVED cards in order (HITL hard gates still hold — no sends/purchases/submissions), renames `processed-`.
   - First deck live with 6 real cards: D1 test volley (VOLLEY, confirm), D2 Pinterest batch (confirm), D3 $19 kit price (confirm), D4 FB engine-vs-Marketplace, D5 Discord briefs (confirm), D6 Amazon gating (Kirk-only).
3. **Campaign 100x100 test volley** — plan locked via Kirk's clarify answers: 10 emails = Kirk seeds (kirkbradford0@gmail + kirkbradford1@icloud) + 5 real West Coast orgs; plain text + hyperlinks; from felonsmelon@gmail.com; Gmail DRAFT queue, Kirk presses send; then trace paths/links/rendering.
   - **Domain bug caught:** draft linked felonsmelons.com (plural) = DNS dead. felonsmelon.com (singular) live (HTTP 200). Draft corrected. Memory updated.
   - **BLOCKER:** Gmail OAuth dead (invalid_grant on both stored tokens; leftover file = 213-row message cache, not a token). Fresh PKCE link issued to Kirk in Telegram (verifier saved in hermes/google_oauth_pending.json). Kirk approves as felonsmelon@gmail.com and pastes back the localhost?code= URL.

## Open threads (next session picks up)
- Kirk's OAuth paste-back → exchange code → build 10 drafts → Kirk sends → trace report.
- Deck logs flow through heartbeat at 08:00; verify first deck execution.
- Server proc_3171505fae6b currently serving 8799 on OfficeLeft (dies on reboot — START-DECK.bat is the launcher).

## What did nobody else check?
- The deck server's finish-capture path was smoke-tested by me (GET 200 + POST filed + cleaned). Per no-self-certify, Charlie should run a cold verify against hil-deck/ before we call the deck lane hardened.