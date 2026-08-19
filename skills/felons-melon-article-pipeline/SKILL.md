---
name: felons-melon-article-pipeline
description: End-to-end article production for Felons Melon and the kiosk — draft, self-revise, format, and stage for posting, then STOP right before the click so Kirk posts it himself via the browser harness. Trigger on "Hermes article for the kiosk," "Felons Melon article," "wire it to go," or any request to produce a publish-ready piece.
---

# Felons Melon Article Pipeline

## When to use
- "Hermes article for the kiosk" or "Felons Melon article"
- Kirk wants a piece fully produced and staged, ready for him to click Post
- Any publish workflow where Kirk does the final human action

## The one rule
**Kirk clicks Post. You do everything else.** Never click Publish/Post/Send. The handoff is the deliverable.

## Pipeline (run all steps silently; don't make Kirk repeat context)
1. **Confirm target** — kiosk or Felons Melon. Default to whatever Kirk said; ask only if it's genuinely ambiguous (max ONE question).
2. **Load the voice** — apply the `kirk-writing-voice` skill. If the topic is new, pull one fresh sample from Muck Rack or the local corpus before drafting.
3. **Draft** — follow the recipe (one thread -> image/question open -> declaratives + lived experience + data -> counterargument -> fix).
4. **Self-revise** — strip AI-isms, tighten rhythm, verify numbers, confirm a clear point. Read it aloud mentally; if it sounds like a memo, restart.
5. **Format for target** — kiosk: 300-600 words, headline + deck + one pull quote + 1-2 stats. Felons Melon: mission piece, data + lived experience + reform call.
6. **Stage** — write the final copy to a file, plus headline, deck, byline, pull quote, and stat block as separate fields.
7. **Browser harness handoff** — open the target editor/CMS, load the content, position at the Publish button — then STOP.
8. **Kirk clicks Post.**

## Task-switching discipline (so Kirk never gets frustrated)
- Do all loading/context-gathering yourself. Never ask Kirk to re-explain a topic he already gave you.
- Batch the steps. Report only the result ("ready to post"), not the process.
- Ask at most one question per article, and only for a real decision.
- Kirk's only job is the click. Everything before it is yours.

## Browser harness notes
- Per the SKS hierarchy, `browser-harness` is the live browser bridge (real browser state, logged-in workflows, uploads/downloads).
- When wired: open the CMS, use the existing logged-in session, paste the staged article, and stop at Post.
- If the harness isn't connected yet: save the staged file and tell Kirk exactly where it is and what's left (one click).
- Reuse the existing session; don't log in fresh unless the session is dead.

## Verification (before handing off)
- Reads in Kirk's voice (see `kirk-writing-voice`).
- All stats are real or explicitly flagged as placeholders.
- Staged copy is complete and in the correct format.
- Handoff state is clean: editor open, content loaded, one click from live.

## Pitfalls
- **Don't post.** The entire design is Kirk's human click.
- Don't leave the editor half-loaded or the draft unsaved.
- Don't ask Kirk to re-provide context or topic details.
- Don't run this pipeline for content outside Felons Melon / kiosk scope.
