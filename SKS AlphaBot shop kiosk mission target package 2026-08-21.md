# SKS AlphaBot Shop Kiosk Mission Target Package — 2026-08-21

**Run ID:** `ALPHA-KIOSK-20260821`
**Status:** READY FOR BUILDER — HOLD until Kirk confirms AlphaBot machine is back online
**Risk:** LOW for content/frontend work / MEDIUM for any live deploy or data wiring
**Governor:** Kirk Bradford
**Builder:** AlphaBot
**Observer:** Hermes (realtime research + coordination path)
**Inspector:** Sparky or Codex (independent verification)

## Mission

Finish the Bradford Auto Solutions lobby-kiosk frontend and its real connection path, so that every completed check-in is captured and lands in Kirk's inbox (and, later, a CRM). Do not stop at a mockup. Produce a working frontend + verified data path, return a concise carrier SITREP, and post the shared SKS summary for the swarm.

This target package was authored **before** AlphaBot's machine is back. Its job is to remove all ambiguity so the sortie starts instantly once Kirk confirms the computer is fixed.

## Source of truth already established

1. **The kiosk is a Lovable app** at `bradfordautosolutionscheckin.lovable.app` — a 6-step vehicle check-in that builds a repair estimate, but today **discards all data** (no backend).
2. **A receiving node already exists and is written** — `kiosk_checkin_receiver.gs` (Google Apps Script web app). It accepts a POST, emails Kirk the full check-in instantly, and optionally appends a Google Sheet log. Local copy lives in Kirk's kiosk-node folder (path REDACTED from GitHub).
3. **The wiring instructions already exist** — `README-kiosk-wiring.txt` (3 steps: deploy the Apps Script node, wire the kiosk to POST to it, add Microsoft Clarity tap-heatmaps). Kirk has not yet confirmed these one-time setups are complete.
4. **The data contract is already fixed** by the receiver. The kiosk must POST JSON with these fields: `name, phone, year, make, model, mileage, plate, state, color, symptoms[] (array), words, priority, bracket (call-first ceiling, number), signed (bool), timestamp, estimate{labor, parts, total}`. Content-Type `text/plain`, fired in the background, non-blocking.
5. **The commercial path** is: journalism/content → Bradford Auto bolt-on kiosk → useful customer/vehicle data → later CRM / customer-front-load management. The kiosk is **digital scaffolding around a shop that already knows how to repair cars**, not a login-heavy dashboard replacing the shop's identity.
6. **AlphaBot's assigned role** (per `SKS hierarchy 2026-08-17.md`): "Shop kiosk frontend guts, UI implementation and front-end connection work." This sortie is that role, executed.

## Rules of engagement

- **No more clarification loop unless truly blocked.** Use best judgment, record assumptions, keep moving.
- **User intent wins.** Kirk reopened this lane on 2026-08-21 with a directive to prepare the target package and solution. The earlier freeze ("keep AutoFlow expansion out of NOW") is lifted **for this kiosk sortie only** once Kirk says go; do not expand into other lanes.
- Do **not** deploy a live production site, change billing, modify production databases, or touch credentials during this sortie without explicit approval.
- Do **not** put secrets, tokens, private machine identifiers, personal data, or private local paths into GitHub.
- Ground any customer-facing claim (pricing, capabilities) in what the shop actually does. Do not fabricate customer counts, savings, integrations, or deployment status.
- Separate **fact**, **reasonable design choice**, and **Kirk's thesis/opinion** in any written notes.

## Scope / coverage map

The sortie must land, end to end, at least these:

- the full 6-step check-in flow (customer info → vehicle → symptoms → scope/priority → estimate → signature)
- the estimate builder (labor + parts + total) with the **$149 diagnostic authorization** and signature-capture step
- the exact POST on completion, matching the receiver's field contract above
- a non-blocking, background fire-and-forget send that never freezes the customer's screen
- graceful handling when the receiver is unreachable (fail silently, never lose the local screen state)
- a clear "estimate ready" success state after submit
- confirmation of where the data goes next (email today, Sheet log optional, CRM later)

## Deliverables

1. **`SKS AlphaBot status packet.json`** — publish immediately on first connection. Per the AGENT_STATUS_PACKET contract: agent, repo, connection state, branch, planned paths, first-push ETA, needs-from-Codex. **This is deliverable #1 and unblocks the whole swarm.**
2. **Working kiosk frontend** in the confirmed Lovable project (or the confirmed target repo/branch if the frontend has moved off Lovable).
3. **Verified data path** — a real test check-in that produces a real email in Kirk's inbox (or a documented blocker if the Apps Script node is not yet deployed).
4. **Carrier SITREP** in the format below.
5. **Final SKS shared summary** committed to `kirkbradford0/sks-` after deliverables and verification.

## Carrier return: required SITREP

```yaml
run_id: ALPHA-KIOSK-20260821
governing_unit: SKS-ALPHABOT-SHOP-KIOSK
unit_version: 1.0.0
builder: AlphaBot
role: builder
task_category: frontend
status: success | partial | blocked | error | aborted | unverified
risk_level: low | medium | high | critical
what_changed:
  - ""
artifacts:
  status_packet: ""
  frontend_target: ""      # Lovable project or repo/branch
  data_path_verified: false
  test_checkin_email_sent: false
verification:
  checks: []
  results: []
remaining_uncertainty: []
blockers: []
github:
  repo: kirkbradford0/sks-
  summary_path: ""
  commit_sha: ""
recommended_next_action: ""
```

Then a **five-line human-readable summary**: mission status, what actually shipped, what was verified, what remains uncertain/blocked, and the single next human decision.

## SKS post-flight summary contract

Create `SKS AlphaBot shop kiosk SITREP YYYY-MM-DD.md` in `kirkbradford0/sks-` containing: run ID + final status, builder, what changed, artifact manifest (no private local paths), verification results, unverified assumptions, blockers, next action, rollback note if any shared file changed, and the commit SHA.

Report `partial`, `blocked`, or `unverified` when that is what the evidence supports. Do not rewrite doctrine to look successful.

## Definition of DONE

The sortie is complete only when: the status packet is published, the frontend is built in its confirmed target, a real test check-in traverses the full flow and the POST is verified (or a precise blocker is logged), the carrier SITREP is returned, and the SKS summary is committed. Execution without errors is not proof of completion.
