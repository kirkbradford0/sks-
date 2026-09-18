# DABS QUARANTINE PROTOCOL — dabs → SKS promotion doctrine

Committed 2026-09-18 by Hermes (Alpha session, Kirk-directed).
Status: DOCTRINE. Every agent loads this before touching SKS shared state.

## Why this exists

One hallucinated message from any agent must not be able to contaminate
the SKS source of truth. kirkbradford0/dabs is the quarantine tier: claims
enter the fleet there first, sit out a dwell period, and only graduate to
SKS after surviving verification + time.

## The flow

1. **INTAKE → dabs.** Any message, claim, status, or handoff produced by an
   agent lands in dabs as a card: `DABS-<YYYYMMDD>-<agent>-<seq>.md`.
   Required fields: source agent, date (UTC), what is claimed, evidence or
   "unverified", and the SKS target it is asking to enter.
2. **DWELL — 72 hours minimum.** Nothing promotes before 3 days from its
   card date. During dwell, any other agent may file a CHALLENGE note on the
   card. A challenged card does not promote until the challenge is resolved.
3. **PROMOTION — verify + time.** After 72h unchallenged, the verifying
   agent (Charlie by default, or whoever holds the Patriarch controller role
   that session) stamps the card VERIFIED and moves the content into SKS
   (running tasks list, status packets, handoffs). The SKS entry must cite
   the dabs card ID and the verifier.
4. **NO SELF-CERTIFICATION.** An agent never verifies its own card. Bravo
   builds, Charlie verifies — same rule at the message layer.

## Fast lane (hot data)

Time-critical operational data — price alerts, stop levels, auth expiring,
machine-down — flows direct to SKS without dwell, but MUST be tagged
`[UNVERIFIED-HOT]` and requires a same-session cross-check by a second
agent or Kirk. Hot lane is for prices and alerts, never for facts, claims,
or status changes.

## Fallback: when bad data still reaches SKS

- Every SKS entry carries provenance: dabs card ID + verifier.
- Bad entries are never deleted. Mark `SUPERSEDED`, link the correction,
  keep the audit trail.
- File a lesson: `lessons/LESSON-<slug>-YYYY-MM-DD.md` — symptom, how it
  got promoted, who verified, what the dwell/verify rule change is.
- Fix at the source agent. The same lie must not be able to promote twice.

## Human-in-the-loop boundary (unchanged)

Patriarch routes and recommends. Kirk confirms anything touching money,
reputation, broker unlock, auto-submit, or deletion of another agent's
state — regardless of dwell status.

## One-line summary

**dabs is the airlock. Three days or a verifier's stamp — both, before
anything touches SKS. Hot data runs direct but tagged and cross-checked.**
