# BUILD SPEC — APPLY LIGHT HARNESS (for Claude Code)

Version 1.0 — 2026-09-07. Written by Alpha (Hermes) for Kirk Bradford. Builder: Claude. Operator: Hermes (any profile). Human: Kirk.

## What this is (one paragraph)

A local job-application harness with three parts: (1) a **scraper** that pulls live job postings from company ATS boards, (2) an **apply engine** that scores jobs against Kirk's profile, pre-fills application forms in a real browser, and (3) a **Light Board** — a fullscreen window that shows only a color. GREEN means the agent is working / everything is safe to proceed. RED means the agent is blocked and needs Kirk. Zero words. Zero UI chrome. Kirk sees color, walks over, fixes the thing, light goes back to green.

This exists because Kirk processes information as alerts, not prose. The harness must never require him to read anything to know the state.

## Hard rules (violating any of these = build rejected)

1. **No auto-submit.** The final "Submit application" click is ALWAYS a RED light event. The agent may fill every field, attach every file, and stage the click — but a human clicks submit. (Config flag `allow_auto_submit=false` by default. If Kirk later flips it in writing, that's his call — build the flag, ship it false.)
2. **No PII outside the machine.** The harness runs 100% locally. Nothing posts to any remote repo, API, or log service. Profile data (name, email, phone, work history, background) lives in a local `profile/` folder that is gitignored by default.
3. **Respect rate limits.** Max 1 application flow at a time. Max 20 board polls/hour. Backoff on 429s. No CAPTCHA solving — a CAPTCHA is a RED light, not a puzzle to beat.
4. **Every action logged.** SQLite journal: timestamp, job id, action, result, screenshot path. If the light turned red, the log must say why (append-only).
5. **The agent drives via files/CLI, not the UI.** Hermes never touches the Light Board UI directly — it calls the harness API. The UI is for Kirk's eyes only.

## Architecture

```
C:\Users\bradf\apply-light-harness\
├── harness\
│   ├── scraper.py        # ATS board pollers (Greenhouse, Lever, Ashby, Workday)
│   ├── scorer.py         # scores jobs vs profile, 0-100, class 1-4
│   ├── applier.py        # Playwright browser: open form, fill, stage
│   ├── lights.py         # state machine: GREEN / AMBER / RED
│   ├── server.py         # localhost HTTP API (FastAPI) + serves the Light Board
│   └── db.py             # SQLite journal + job queue
├── profile\              # GITIGNORED — PII lives here
│   ├── resume.docx
│   ├── answers.json      # reusable field answers
│   └── settings.json     # allow_auto_submit, poll limits, board list
├── queue\                # drop folder: Hermes drops job JSONs here, harness picks up
├── board.html            # the Light Board (fullscreen color, polling /api/light)
├── requirements.txt
└── README.md
```

## Component details

### 1. Scraper (`scraper.py`)
- Input: list of ATS board URLs in `profile/settings.json` (format: `{"board_url": "...", "company": "...", "ats": "greenhouse|lever|ashby|workday"}`).
- Greenhouse: hit `boards-api.greenhouse.io/v1/boards/<co>/jobs?content=true` — JSON, no scraping needed. Same pattern for Lever (`api.lever.co/v0/postings/<co>`) and Ashby (`api.ashbyhq.com/posting-api/board/<co>`). Workday needs real scraping — Playwright, last resort.
- Output per job: `{id, title, company, location, remote:boolean, url, posted_date, description_text, source_ats}`.
- Dedup by (company, title, url). New jobs go into SQLite with status `NEW`.
- Filter out: commission-only, MLM, pay-to-work, crypto-scheme keywords. Mark them `REJECTED_RISK` in the journal.

### 2. Scorer (`scorer.py`)
- Score 0–100. Dimensions (weights): hire probability 30, speed to paycheck 20, schedule fit 15, skill relevance 15, career value 10, comp 10.
- Read the resume text + answers from `profile/` to compute skill relevance. Keep scoring dumb and deterministic — keyword/requirement matching against the description, not vibes. An LLM pass is optional and only runs when Hermes calls the API with a job id; the batch scorer stays rule-based.
- Class: 1 = strong fit, 2 = adjacent fit, 3 = income-first, 4 = stretch. Class 4 needs RED confirmation before any apply flow starts.

### 3. Applier (`applier.py` — Playwright, chromium)
- Takes a job id, opens the ATS form URL in a headful (visible) browser window so Kirk can watch.
- Fill order: identification fields → resume upload (path from profile) → short answers → long-form answers → review screen. Screenshots at every step into `journal/screenshots/`.
- Field matching: match form labels to `profile/answers.json` keys with fuzzy match. Any field it cannot fill → record it and continue.
- At the review screen: STOP. Set light to RED with reason `READY_FOR_SUBMIT`. Do not click submit. (See Hard Rule 1.)
- Login walls, CAPTCHAs, payment, or "sign in with X" → RED immediately with reason. Never guess credentials.

### 4. Lights (`lights.py` — the state machine)
- States: `GREEN` (agent working or idle-and-clear), `AMBER` (transitions, <30s, e.g. switching jobs), `RED` (blocked, needs Kirk).
- Red carries a machine-readable reason code (shown in log + API, never on the wall): `READY_FOR_SUBMIT`, `CAPTCHA`, `LOGIN_WALL`, `CANNOT_FILL_FIELD`, `CLASS4_CONFIRM`, `SCRAPER_ERROR`, `RATE_LIMITED`, `UNKNOWN`.
- Kirk resolution: pressing SPACE on the Light Board window (or clicking it) acknowledges the red, executes the staged submit if reason is `READY_FOR_SUBMIT` (because the human just clicked, satisfying Rule 1), and returns to GREEN. Any other reason opens the browser window for Kirk to fix by hand; when he's done he presses SPACE to go green.
- Persist state to SQLite so a crash never loses a staged application.

### 5. Light Board (`board.html`)
- One fullscreen page, one giant rectangle, polling `GET /api/light` every 2s.
- GREEN #00c853 / AMBER #ffd600 / RED #d50000. Whole window. Nothing else. No text, no icons, no clock.
- Optional (settings.json flag, default ON): 1 short beep on state change to RED — color plus audio cue. Still zero words.
- SPACE or click = acknowledge/resolve (per lights.py behavior above).

### 6. API (`server.py` — FastAPI on 127.0.0.1:8765, no external binding)
Hermes drives everything through these:
```
POST /queue/job        {job payload}        -> enqueue
GET  /queue/next                            -> highest-scoring NEW job
POST /apply/{job_id}                        -> start apply flow (async)
GET  /light                                 -> {state, reason_code, current_job}
POST /light/ack                             -> same as SPACE press (for scripted ack)
GET  /journal?since=...                     -> action log
POST /mark/{job_id}  {applied|rejected|dead} -> manual ledger mark
```
Plus CLI mirror: `python -m harness scan`, `python -m harness next`, `python -m harness apply <job_id>`.

## Integration with the existing desk

- The harness's SQLite journal is the machine ledger; a `harness export` command appends a Markdown table to `C:\Users\bradf\Job Applications\ledger.md` (applied date, company, role, url, status). Do not duplicate — export, don't fork.
- Hermes drops scraped jobs into `/queue` or calls `POST /queue/job`. Hermes reads `/light` before every apply action and after any RED to know whether to proceed or stand by.
- SKS: harness status lines (no PII) go in the daily Hermes handoff like any other desk.

## Build order (ship in this sequence, verify each)

1. `lights.py` + `board.html` + `server.py` with hardcoded light states — **the light works end-to-end before anything else.** Verify: curl `/light` returns green; force red via test endpoint; window turns red; SPACE returns green.
2. `db.py` journal + queue + `POST /queue/job`.
3. `scraper.py` for Greenhouse only (best-documented API) with one real board configured. Verify: 10+ live postings pulled, deduped, journaled.
4. `scorer.py` rule-based pass. Verify: sample job scores deterministically, same input = same score twice.
5. `applier.py` against a Greenhouse test form. Verify: fills fields, uploads resume, screenshots each step, stops at review with RED `READY_FOR_SUBMIT`, and SPACE-triggered submit actually goes through on the test form.
6. Lever + Ashby pollers, Workday scraper last (if it fights back, leave it and note it in README).
7. `export` to ledger.md + README.

## Acceptance test (the whole harness, end to end)

1. Start server → window is GREEN.
2. Hermes queues 3 jobs (one good, one class-4, one with a login wall).
3. Apply the class-4 job → light goes RED with `CLASS4_CONFIRM` before any browser opens. Ack → proceeds.
4. Apply the login-wall job → RED `LOGIN_WALL`. Ack → opens browser, Kirk logs in manually, presses SPACE → GREEN, flow resumes.
5. Apply the good job → fills everything, RED `READY_FOR_SUBMIT` at review. Kirk presses SPACE → submits, journal records it, ledger.md gets the row, light GREEN.
6. Kill the server mid-apply, restart → staged state survives, light restores.

## Non-goals (do not build)

- No cover-letter generation (Hermes does that already).
- No multi-user, no auth, no cloud anything.
- No CAPTCHA solving, no credential storage beyond what Kirk pastes manually.
- No scraping Indeed/LinkedIn aggregators (dead-listing hell; ATS-direct only).

## Environment

- Windows 11, Python 3.11 (`python` on PATH), `uv` available. Playwright: `pip install playwright && playwright install chromium`.
- Everything runs on Kirk's machine. No accounts, no API keys needed beyond the ATS public board endpoints.
