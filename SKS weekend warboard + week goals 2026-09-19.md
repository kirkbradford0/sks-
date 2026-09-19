# SKS Weekend Warboard + Week Goals — 2026-09-19 (Saturday)

Written by Alpha (Hermes), pencil-holder. One screen. Each card carries a **considered success** — no card is done until that line is true.

## The one sentence

**By Friday 2026-09-25 the fleet has (1) a verified statute map, (2) a named outreach list of 20, and (3) Bravo + Charlie running on local GLM — the three things the B2B pitch physically cannot ship without.** Everything else waits.

## Why this path (easiest → most effective logic)

The B2B "Re-entry as a Service" pitch needs exactly three inputs:

1. **Credible, verified legal content** → WB-01 statute map (Alpha builds, Charlie verifies)
2. **Someone to pitch** → WB-05 target list (Alpha drafts, Kirk gates sending)
3. **A fleet that actually runs** → GLM swap (Kirk, this weekend) + paying down the verification debt (Charlie, Monday)

If we only do these three this week, the Final Card (pitch emails from felonsmelon@gmail.com) is one step away. If we do anything else first, it isn't.

---

## SATURDAY–SUNDAY (the weekend board)

### CARD W1 — Alpha · WB-01 Legal Content Verifier groundwork
Map 10 Utah re-entry questions → real statutes. Each question gets: statute cite, official source URL (le.utah.gov), plain-English one-liner, and a "what the statute does NOT say" honesty line.
**Considered success:** file `SKS WB-01 Utah statute map v1 2026-09-19.md` in sks- + file a DABS card so it enters the airlock. 10/10 questions mapped, every cite has a URL that loads.

### CARD W2 — Alpha · WB-05 target list draft
10 Utah/defense-adjacent attorneys + 10 re-entry non-profits (Utah first, 2–3 national). Each row: name, org, contact email, why-them (one line), best door-in.
**Considered success:** file `SKS WB-05 outreach targets v1 2026-09-19.md` in sks-. 20 rows, no invented emails — "not found" is an acceptable value, a hallucinated email is not.

### CARD W3 — Kirk · GLM swap for Bravo + Charlie (in progress — this is the weekend's infrastructure win)
You're already on it. When done, drop one line in `AGENT_STATUS_PACKET.md`: "Bravo + Charlie on local GLM as of <date>."
**Considered success:** both profiles answer a test prompt on local GLM; status packet updated. This also completes the routing doctrine's tier:local first rung — fleet finally walks the escalation ladder it wrote.

### CARD W4 — Kirk · the two clicks (5 minutes total, highest ROI of the whole week)
1. **Click Submit on Intro Content Marketing Writer** ($50–100/hr, packet ready at `Job Applications\Intro_Content_Marketing_Writer_2026-09-12\`). Motley Fool is DEAD — do not chase it.
2. **Click a fresh Google OAuth link** — I generate it, you click it. Gmail auto-sort + gws come back from the dead (down since 09-11).
**Considered success:** ledger row for Intro moves to ✅ Submitted; a test Gmail API call returns 200.

### CARD W5 — Muse · WB-04 Constitution + Voice (nudge)
2-day deliverable was due ~09-20. Culture layer pins/rituals + "what we learned" thread.
**Considered success:** constitution v0 skeleton filed to sks- (even rough). Source of truth stays repo — Discord is a view only.

---

## MONDAY ONWARD (unlocks when the weekend lands)

### CARD M1 — Charlie · verification debt paydown (three items, one session)
1. Verify `agent_pbft.py` + circuit breakers (author-checked only — builder never certifies own work)
2. DABS cards charlie-001..004 + bravo-001 hit 72h dwell **2026-09-21** → verify/promote/SUPERSEDE
3. WB-03 harness kickoff (due 2026-10-02)
**Considered success:** verification notes filed; all five DABS cards resolved; WB-03 has a skeleton + first failing test.

### CARD M2 — Bravo (on GLM) · WB-02 drafting pipeline skeleton
One motion-support draft template with citation slots that reference WB-01 statutes only.
**Considered success:** a template renders with every citation slot filled from WB-01 v1 — and Charlie's harness can reject a bad one.

### CARD M3 — Alpha (Judge hat) · accept/flag/escalate logic live
Rotation doctrine says I take the Judge hat after Controller. First ruling: WB-01 goes through Charlie, not me.
**Considered success:** judge rules filed for WB-01 verification; routing table updated.

### STRETCH (only if W1–W4 all land) — Warboard Priority One: "Clear My Warrant Letter"
The simple-buy version of FM: one story, one fee, one letter to sign. Draft the one-page buy-page copy for felonsmelons.com. Pricing gated by Kirk.

---

## Guardrails (unchanged, standing)

- No money moves, no live broker orders (LOCKED), no spend without Kirk's signature
- No Discord wiring until the DABS intake flow is stood up — airlock first
- No pitch emails leave felonsmelon@gmail.com until WB-01 is Charlie-verified
- PII stays out of sks-; brain stays on SSD

## ⚠️ INTAKE LANDMINE — case status & privilege (Kirk, 2026-09-19)

**Rule for the inference agent's intake flow:** the FIRST thing we establish with any user is whether they have an **open case** — and open-case users are a hard special-handling class.

Why: the moment an open-case user's data sits in a third-party cloud (Supabase, any hosted DB, any cloud sync), that data is held by a third party. No attorney-client privilege attaches. It becomes discoverable — subpoena-able **by a criminal defense attorney, but also by a prosecutor**. The "process in between" (upload → cloud → back) converts protected intake into evidence.

Standing handling rules until Kirk amends:
1. Intake asks case status first: open / closed / none / prefer-not-to-say.
2. **Open-case answers stay LOCAL-ONLY.** Never leave the machine — no Supabase, no cloud, no repo, no chat dump. Tag: `[OPEN-CASE-LOCAL]`.
3. Closed/none answers can use the normal (still minimal-data) pipeline.
4. The product never claims confidentiality it can't deliver. If data isn't privileged, the UI/letters must not imply it is.
5. Attorney-tier (WB-02) work product under a licensed attorney's supervision is the only lane where privilege can ever attach — that's why the B2B lane is the gold.

DABS card: `DABS-20260919-alpha-001` (filed same day — case-status intake rule).

## The honest stall risk

Kirk's two clicks (W4) are the single point of failure — everything I can do without them I'll do this weekend anyway, but the Intro application has been "ready" since 09-12. Five minutes, Kirk. It's the highest-paid 5 minutes available this week.
