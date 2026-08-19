# SKS Hermes article pipeline built - 2026-08-18

## Status: SHIPPED

## What was built
Two skills, authored by Hermes (DeepSeek V4), now live both locally and in this repo under `skills/`.

### 1. kirk-writing-voice
- **Purpose:** write in Kirk Bradford's authentic voice (journalism, opinion, kiosk, Felons Melon).
- **Source corpus:** Muck Rack portfolio (https://muckrack.com/kirk-bradford-1) + local `Kirks Booksmarts` folder ("Kirks Chapter One" docx = book voice; "The Price of a Phone Call" html = journalism voice).
- **Voice DNA:** short declaratives, rhetorical-question hooks, first-person lived experience, moral clarity + reform lens, concrete stats, bookending, aphorisms. Motto: "Stay Curious."

### 2. felons-melon-article-pipeline
- **Purpose:** end-to-end article production — draft, self-revise, format, stage — then STOP before the click. Kirk posts via the browser harness.
- **Target formats:** kiosk article (300-600 words, skimmable) and Felons Melon article (mission piece, justice-impacted lens).

## What's available now
- Kirk can say **"Hermes article for the kiosk"** + 3-5 topics (or an outline) and get a publish-ready piece in his voice, staged one click from live.
- Any future Hermes / helper agent can pull both skills from `skills/` in this repo.

## Location
- **Local:** `~/AppData/Local/hermes/skills/sks/`
- **Repo:** `sks-/skills/{kirk-writing-voice, felons-melon-article-pipeline}/SKILL.md`

## Next
- Wire browser-harness handoff (editor open + content loaded + stop at Post).
- Stand up daily/weekly cron jobs + daily task board (`board/NOW.md`) — pending Kirk's confirmation.
