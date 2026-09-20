# SKS Hermes handoff 2026-09-19

## SnowStrike repo buildout (evening, Kirk at shop)

**What I did**
- Kirk created github.com/kirkbradford0/operation_snow_strike; I cloned it to C:/Users/bradf/snowstrike and built the full Operation SnowStrike marketing campaign machine (100 FM users by Dec 25, 2026; harden date Oct 1).
- OPERATION.md: locked 10-step daily loop (SCRAPE -> FIND NARRATIVE -> VERIFY -> REPORT -> OUTREACH -> PUBLISH -> DISTRIBUTE -> OBSERVE -> CONTRAST -> NEXT VOLLEY) + daily output table.
- TEAM.md: five-seat SaaS marketing team (Editor-in-Chief, Intelligence Analyst, Staff Journalist, Growth Lead, Fact-Checker/Analytics) with seat rotation; verifier never certifies own claim.
- docs/FILE-SCHEMA.md: volley file naming volleys/YYYY-MM-DD/NN-step.md, mandatory frontmatter, [UNVERIFIED-HOT] quarantine, open-case content banned repo-wide.
- docs/DAILY-SKILL-PROMPT.md: self-contained daily runner prompt for SPARKY/any Hermes profile.
- docs/CHANNELS.md: 5 legitimate vectors (journalism/employer/reentry/economics/lived-experience), 3-5 channels max per story.
- docs/FUNNEL.md: math to 100 users (~95 firing days, ~475 packets, placeholder rates to be replaced by measured SIGNAL-LOG rates).
- templates/volley/: all 10 step templates; learning/ seeded (SIGNAL-LOG, CONTACTS, LESSONS); inbox/ seeded.
- Committed and pushed: operation_snow_strike main @ 2590444.

**State**
- Loop starts 2026-09-21. Not yet scheduled as cron; docs/DAILY-SKILL-PROMPT.md is the runbook.
- Byline model enforced in templates: story stands alone, only mention is "Brought to you courtesy of FelonsMelon.com".

**Process fix**
- Outreach gate baked into every artifact: agents stage packets, Kirk clicks Send. Never automate the send.

**Next action for Kirk**
- None required tonight. From 9/21, say "run the SnowStrike volley" (or we wire the daily cron) and the loop fires from the repo.
