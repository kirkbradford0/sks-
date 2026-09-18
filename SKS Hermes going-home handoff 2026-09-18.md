# SKS Hermes handoff 2026-09-18 — DABS airlock, runtime guards, rotation doctrine

Written by Hermes/Alpha for the fleet: Bravo, Charlie, and the next Patriarch hat.

## THE LAST TWO DAYS (2026-09-17 → 2026-09-18), THE SKINNY

**2026-09-17 — Patriarch doctrine landed.** Committed `PATRIARCH-ROUTING.md`
(SHA 5225492): the swarm got its control layer. Patriarch is a hat, not a
daemon — observer, router, record-keeper, optimizer around the shared State.
Escalation ladder: routine → local GLM, specialized → the right worker
(Alpha/Bravo/Charlie by role), stuck-2x or high-impact → frontier model.
Learning loop: lessons land in `lessons/LESSON-<slug>-YYYY-MM-DD.md` —
symptom, playbook, who verified. Knowledge flows downhill; local models get
cheaper every cycle. Same day: Charlie burn-desk exists locally, books off
SKS; Google OAuth confirmed still dead (invalid_grant — Kirk has not yet
clicked the fresh auth link; Gmail auto-sort + gws CLI remain down).

**2026-09-18 — the anti-hallucination day.** Kirk ordered a quarantine layer
before Discord wiring, and it's now built and committed:

1. **DABS airlock (d7ab153).** New repo **kirkbradford0/dabs** (local clone
   `~/dabs-repo-work`, initialized commit 3c0c455). Rule: no agent message,
   claim, or status change enters SKS directly. It files a card in
   `pending/`, sits **72 hours**, gets verified by a **different agent than
   the one that wrote it**, then graduates to `verified/` and into SKS with
   provenance (card ID + verifier stamped on the SKS entry). Bad data is
   never deleted — marked SUPERSEDED with a correction link; every slip
   becomes a lesson. Hot lane: prices, stops, alerts, auth-expiry flow
   direct to SKS tagged `[UNVERIFIED-HOT]` with a same-session cross-check.
2. **Discord wiring is formally gated** on the airlock standing (161dc40).
   No bot connects to the swarm until the flow above is live.
3. **Runtime guard #1 — circuit breaker (4bf75c5).**
   `tools/agent_circuit_breaker.py`: stops a stuck agent BEFORE it burns
   tokens repeating itself. Sliding-window detection catches consecutive
   AND alternating loops (A,B,A,B trips); canonical JSON hashing; bounded
   history; trip audit; supervisor override prunes context and injects a
   forced backtrack objective. 6/6 tests pass.
4. **Runtime guard #2 — backoff + cost kill switch (df71351).**
   `tools/agent_backoff.py`: stops a FAILURE loop and walls off recursive
   work so a runaway can never produce a surprise bill. Exact attempt
   budget (max_retries=3 means exactly 3 calls, never N+1), wall-clock
   kill, **spend kill via cost hook** (broken meter fails safe = assume
   worst), jitter so fleet retries don't sync-hammer a rate limit. 8/8
   tests pass.

Both tools are standalone, zero dependencies, drop-in for any agent.

## WHERE TO PUT UPDATES — BRAVO & CHARLIE READ THIS

**Daily status:** each agent keeps its `SKS <name> status packet.json` in
sks- current, and commits a dated handoff file when it goes home
(`SKS <name> handoff YYYY-MM-DD.md`).

**Claims and facts:** anything you want the fleet to believe goes through
**dabs**, not straight into SKS. File
`pending/DABS-YYYYMMDD-<agent>-<seq>.md` using the card template in the
dabs README (one claim per card: claim, evidence, sks_target, dwell date).
After 72h unchallenged, a *different* agent stamps VERIFIED, moves it to
`verified/`, logs one line in `VERIFICATION-LOG.md`, and only then copies
the content into SKS citing the card ID.

**Hot data (prices/stops/alerts/machine-down):** straight to SKS tagged
`[UNVERIFIED-HOT]`, cross-checked same session by a second agent or Kirk.
Never use the hot lane for status changes or facts.

**Discord board (when it connects):** the board is a VIEW of SKS + dabs, not
a third source of truth. Post pointers, not copies: card IDs, task IDs,
handoff filenames. If it isn't committed to sks- or dabs, it doesn't exist.
Kirk's Discord server '--SKS---' is the venue; wiring happens only after
the airlock proves itself.

## ANTI-DRIFT PLAN — PATRIARCH OVERSIGHT + ROTATION

**The drift problem:** an agent holding the Patriarch hat too long starts
optimizing for its own lane and stops seeing the whole board; too short and
nobody accumulates the judgment the role exists to build. Kirk's call,
which is now doctrine: **one job, then rotate.** Nobody does the same job
long enough to decay. Nobody audits their own work — same rule as the
builder/verifier split, applied to the controller seat.

**Rotation mechanics:**
- The Patriarch hat rotates per session or per day — whoever wears it runs
  routing, record-keeping, and the learning loop for that shift, using
  `PATRIARCH-ROUTING.md` + `tools/agent_circuit_breaker.py` +
  `tools/agent_backoff.py` as the standing kit.
- **Verifier is always someone else.** Charlie does not verify Charlie;
  Alpha does not verify Alpha. This applies to dabs cards, builds, and the
  controller seat alike.
- **Next rotation:** Kirk expects Alpha (this agent) to take the Judge hat
  next. When that happens, routing and optimization stay light on whoever
  is wearing the worker hats — nobody sweats the optimizer job; that's what
  the Judge is for. Bravo keeps building, Charlie keeps verifying, and the
  judge does the cross-checking.
- Drift check: every handoff file ends with one line — what did I do that
  nobody else checked? That answer is what the next hat verifies first.

**Standing boundaries (unchanged):** Patriarch routes and recommends; Kirk
confirms anything touching money, reputation, broker unlock, auto-submit,
or deleting another agent's state. Broker stays LOCKED until UNLOCK.txt
says UNLOCK in Kirk's writing.

## FLEET STATUS: EVERYONE IS DOING GREAT

Kirk says so directly, and the record backs it: Bravo building, Charlie
verifying, Alpha routing — the builder/verifier split is holding, the
handoff discipline is holding, and the last two days turned Kirk's two
patterns into tested, committed tools in under a day. Keep it up. The
rotation exists so it stays that way.

## OPEN ITEMS

- [ ] dabs dwell-sweep automation (cron or controller piece) — pending/ cards
      past dwell get flagged for verify. The 3-day rule should self-enforce.
- [ ] Discord wiring — GATED on airlock proving itself. Server '--SKS---'
      (ID 1546468280343072808), invite expires 2026-10-07.
- [ ] Google OAuth — dead since 2026-09-11. Kirk needs to click a fresh
      auth link from setup.py --auth-url before Gmail auto-sort works again.
- [ ] Alpha takes Judge hat next rotation; verify pass on whatever the last
      session unchecked.
- [ ] Wire both runtime tools into each agent's execute_step path as they
      come up for rotation — they're standalone, no integration blockers.

— Hermes/Alpha, 2026-09-18, sks- commits d7ab153..518b62a
