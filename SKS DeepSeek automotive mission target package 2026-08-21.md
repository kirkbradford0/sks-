# SKS DeepSeek Automotive Mission Target Package — 2026-08-21

**Run ID:** `FM-20260821-1949`  
**Status:** READY FOR BUILDER  
**Risk:** LOW for content production / MEDIUM for shared-repo mutation  
**Governor:** Kirk Bradford  
**Builder:** DeepSeek V4 Pro via Hermes  
**Observer:** Hermes run log + artifact manifest  
**Inspector:** Sparky or Codex independent verification  

## Mission
Finish the interrupted Bradford Auto Solutions automotive-content sortie. Do not stop at another outline. Produce the complete deliverable set, verify it, return a concise carrier SITREP, and post the final shared SKS mission summary for the rest of the swarm.

## Source of truth already established

1. The campaign is **24 automotive articles** centered on the thesis that the robotics wave in automotive repair may arrive much faster than many shop owners expect. Treat the "6–12 months" position as a thesis to investigate and argue, **not an unsupported factual guarantee**.
2. Required subject territory includes concrete repair questions such as oil changes and timing belts, what the modern mechanic may look like in 2027, AI/robotics adoption in small shops, and the operational problem of language translation / Spanish-speaking customer communication.
3. The commercial path is journalism/content → Bradford Auto Solutions bolt-on kiosk → useful customer/vehicle data → later CRM/customer-front-load management. The product should be framed as **digital scaffolding around a shop that already knows how to repair cars**, not another login-heavy dashboard replacing the shop's operating identity.
4. Brand stance: transparent, customer-focused, practical. If the customer understands the repair and feels treated fairly, the shop is allowed to make money. Do not fabricate live capabilities, customer counts, savings, integrations, or deployment status.
5. Existing SKS writing infrastructure already exists: `skills/kirk-writing-voice/` and `skills/felons-melon-article-pipeline/`. Use those contracts rather than inventing a new writing system.

## Rules of engagement

- **No more clarification loop unless truly blocked.** Use best judgment, record assumptions, keep moving.
- **Finish all 24 pieces.** An outline alone is not mission complete.
- Use the existing Kirk writing voice + article pipeline skills.
- Ground time-sensitive robotics claims in current sources when research tools are available. Record source URLs/titles and access date in the working evidence or article notes. Never manufacture citations.
- Separate **fact**, **reasonable forecast**, and **Kirk's thesis/opinion** in the prose.
- Audience priority: independent repair-shop owners/technicians first, with driver-friendly hooks when useful.
- Keep the articles useful even for a reader who never buys anything. The Bradford Auto Solutions CTA should be earned, not stapled on.
- Do not delete Google Drive folders, reorganize Drive, alter credentials, change billing, modify production databases, or deploy a live site during this sortie. Those are separate missions.
- Do not put secrets, tokens, private machine identifiers, personal data, or private local paths into GitHub.

## Coverage map

Across the 24 pieces, ensure the campaign collectively covers at least these lanes:

- first realistic robotic oil-change workflows
- why a timing-belt job is a different robotics problem
- the 2027 mechanic: technician, diagnostician, robot wrangler, customer translator
- computer vision / inspection and where humans still beat it
- tool changing, dexterity, access constraints, rust, broken fasteners, real-shop messiness
- diagnostics and sensor data versus physical wrenching
- safety, liability, calibration and human sign-off
- economics for independent shops versus dealership groups
- robotics-as-a-service / lease / retrofit possibilities
- workflow redesign before robot purchase
- customer intake as the near-term automation beachhead
- why AI translation is an operational capability, not a decorative chatbot feature
- Spanish-speaking customer communication and interpreter/human escalation
- estimate transparency and "closing" the repair without manipulation
- data ownership, consent and useful longitudinal customer records
- kiosk → captured context → follow-up → CRM progression
- parts-room / inventory organization and machine-readable work orders
- teleoperation / remote expert support
- technician labor shortage claims only when sourced
- what shop owners should measure before buying automation
- why brilliant auto-tech demos fail inside ugly real workflows
- small-shop competitive advantage if adoption stays bolt-on and reversible
- what should **not** be automated yet
- a practical 30/60/90-day readiness path for a shop that wants to prepare now

## Deliverables

1. **24 publish-ready article files** in the existing local article staging location already established by the Hermes session/pipeline.
2. **Campaign manifest** listing all 24 titles, filenames, primary audience, thesis, major source(s), and CTA lane.
3. **Research/evidence note** containing current-source references used for time-sensitive technical or market claims.
4. **Validation pass** confirming:
   - exactly 24 articles exist;
   - no placeholder/TODO sections remain;
   - no duplicate titles or substantially duplicate articles;
   - no invented citations or product capabilities;
   - each article fits the established writing-pipeline contract;
   - every article has a clear useful takeaway;
   - every local file opens successfully.
5. **Carrier SITREP** in the format below.
6. **Final SKS shared summary** committed to `kirkbradford0/sks-` after the deliverables and validation are complete.

## Carrier return: required SITREP

Return this exact structure when the sortie is over:

```yaml
run_id: FM-20260821-1949
governing_unit: SKS-DEEPSEEK-AUTOMOTIVE-CONTENT
unit_version: 1.0.0
builder: DeepSeek V4 Pro via Hermes
role: builder
task_category: content
status: success | partial | blocked | error | aborted | unverified
risk_level: low | medium | high | critical
what_changed:
  - ""
artifacts:
  article_count: 0
  manifest: ""
  evidence_note: ""
  local_output_location: "REDACTED_FROM_GITHUB"
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

Then add a **five-line human-readable summary**:

1. Mission status.
2. What actually shipped.
3. What was verified.
4. What remains uncertain/blocked.
5. The single next human decision or action.

## SKS post-flight summary contract

Create one new Markdown file in `kirkbradford0/sks-` named along the pattern:

`SKS DeepSeek automotive content SITREP YYYY-MM-DD.md`

It must contain:

- run ID and final status
- builder/model
- what changed
- artifact manifest or safe pointers (no private local path)
- verification results
- assumptions / forecasts that remain unverified
- blockers
- next action
- rollback note if any shared file was modified
- commit SHA from the mission summary post if available

Do not rewrite shared doctrine merely to make the mission look successful. Report `partial`, `blocked`, or `unverified` when that is what the evidence supports.

## Definition of DONE

The sortie is complete only when **all 24 articles are written, the manifest exists, research claims have evidence where required, validation has run, the carrier SITREP is returned, and the SKS summary has been committed**. Execution without errors is not proof of completion.
