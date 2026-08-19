---
name: bradford-kiosk-checkin-pipeline
description: "Wire the Bradford Auto lobby kiosk (https://bradfordautosolutionscheckin.lovable.app) so every completed vehicle check-in emails Kirk instantly and Microsoft Clarity records session/tap activity. Self-contained kill chain for Codex to execute with chrome/browser plugs. Trigger when Kirk says 'wire the kiosk', 'check-in email', 'kiosk traffic', or 'Falcon 9 launch'."
---

# Bradford Auto Kiosk — Check-In Pipeline (Kill Chain)

## Mission
The kiosk is a Lovable-hosted React SPA that collects a customer's name, phone,
vehicle, complaint, dollar ceiling, and signature — then builds an estimate and
THROWS IT ALL AWAY (state resets on "NEXT CUSTOMER", no backend, no save).

Two deliverables:
1. **Email node** — every finished check-in POSTs to a Google Apps Script web app
   that emails Kirk (kirkbradford0@gmail.com) immediately.
2. **Session tracking** — Microsoft Clarity (free) records sessions + tap heatmaps
   so Kirk can see where customers stall. (Touchscreen: no mouse cursor, use taps.)

Traffic numbers are already covered by Lovable's built-in Analytics
(More -> Analytics). Do NOT build a traffic counter — it exists.

## Plug inventory (what's available to execute this)
- `chrome@openai-bundled` / `browser@openai-bundled` — drive web UI (Lovable, Apps Script, Clarity).
- `spreadsheets@openai-primary-runtime` — optional: create the check-in log Sheet.
- `documents@openai-primary-runtime` — not needed.

## KILL CHAIN

### STAGE 0 — PREFLIGHT (verify access before doing anything)
Gate: all three must pass or STOP and report which one failed.
1. Open https://bradfordautosolutionscheckin.lovable.app — must render
   "Check your vehicle in yourself." (Lovable app is live.)
2. Open https://script.google.com — must be signed in as kirkbradford0@gmail.com.
   If a different account is signed in, STOP and tell Kirk; do not proceed.
3. Open https://clarity.microsoft.com — signed in (any Microsoft account) or create one.

### STAGE 1 — DEPLOY THE EMAIL NODE (Apps Script web app)
1. script.google.com -> "New project" -> select-all and DELETE the starter code.
2. Paste the full contents of `references/receiver.gs` (in this skill) into the editor.
3. Save (Ctrl+S). Name the project "Bradford Auto Kiosk Receiver".
4. Deploy -> "New deployment" -> gear icon -> "Web app".
   - Execute as: **Me**
   - Who has access: **Anyone**
5. Deploy -> Google asks to authorize -> Review permissions -> pick kirkbradford0@gmail.com
   -> Advanced -> "Go to Bradford Auto Kiosk Receiver (unsafe)" -> Allow.
   ("unverified app" warning is normal for a personal script — it is Kirk's own code.)
6. Copy the URL ending in `/exec`. This is the NODE URL.
7. Gate — test it responds (run in terminal, substituting the URL):
   curl -s -X POST -H "Content-Type: text/plain" \
     --data '{"name":"TEST","phone":"555","year":"2020","make":"Test","model":"Car","timestamp":"2026-08-18T00:00:00Z"}' \
     "<NODE URL>"
   Expected: `{"ok":true,"message":"received"}` AND an email lands in Kirk's Gmail.
   If you get an HTML redirect page instead of JSON, the deployment was not set to
   "Anyone" — redeploy. If no email, the receiver's MailApp authorization failed —
   redo steps 4-5.

### STAGE 2 — WIRE THE KIOSK (Lovable)
Goal: on the final "Estimate ready" screen, fire a background POST of the check-in
to the NODE URL. Use Lovable's AI chat (simplest — it knows its own code).

1. Open the kiosk project in Lovable.
2. In the chat box, paste EXACTLY (swap in the NODE URL):

   On the final "Estimate ready" screen, when the customer finishes, send the
   check-in data to this URL using fetch with a POST request and a JSON body:
     <NODE URL>
   Send these fields: name, phone, year, make, model, mileage, plate, state,
   color, symptoms (array), words, priority, bracket, signed, timestamp, and
   the estimate (labor, parts, total). Use header Content-Type text/plain and
   put the JSON in the body. Fire it in the background, ignore errors, and do
   not block the customer's screen.

3. If the AI chat is unreliable, use Lovable **Code Mode** instead: locate the
   component that renders step 6 (the "Estimate ready" screen) and add a
   `fetch` call. See `references/lovable-fetch-snippet.js` for the shape — map
   the field names to the app's actual state (the compiled bundle obfuscates
   variable names; read the real source in Code Mode, do not guess).

4. Publish (top right) to push it live.
5. Gate: run a fake check-in on a phone/desktop (fake name, any data, go to the
   end). Kirk must receive an email within a couple seconds. No email -> re-check
   the NODE URL was pasted exactly and the deployment is "Anyone".

CRITICAL: use `Content-Type: text/plain` for the request body. A JSON content type
triggers a CORS preflight (OPTIONS) that Apps Script web apps do not handle. The
receiver parses `e.postData.contents` as JSON regardless of declared type.

### STAGE 3 — CLARITY SESSION/HEATMAP TRACKING
1. clarity.microsoft.com -> New project -> name "Bradford Auto Kiosk" ->
   URL https://bradfordautosolutionscheckin.lovable.app -> Create.
2. Copy the project ID (short alphanumeric in the tracking snippet).
3. In Lovable chat, paste:
   Add Microsoft Clarity tracking to this app by adding the Clarity script to the
   <head>. The Clarity project ID is <PROJECT ID>.
   (Or: paste the full snippet and say "add this script to the head".)
4. Publish.
5. Gate: after a few minutes, Clarity -> Recordings and Heatmaps show the test visit.
   If no data, confirm the script actually made it into the published <head>
   (view-source on the live URL and grep for "clarity").

### STAGE 4 — END-TO-END VERIFY (report only when all green)
- [ ] Test check-in produces an email with name/phone/vehicle/estimate/signature.
- [ ] A second test check-in from a DIFFERENT device also emails (confirms it's not cached).
- [ ] Clarity shows both sessions with tap heatmaps.
- [ ] Lovable Analytics (More -> Analytics) shows visitors increasing (traffic baseline).

## Pitfalls
- **CORS preflight**: never send `Content-Type: application/json` to Apps Script.
  Use `text/plain`. This is the #1 reason the POST silently fails.
- **Deployment "Anyone" access**: a web app restricted to the deploying account
  returns an HTML login/redirect, not JSON. Always test with the curl gate.
- **Unverified app warning**: expected. It's Kirk's own script on his own account.
- **Lovable must be PUBLISHED** after each edit — the live URL does not update
  until you click Publish.
- **Do not** build a page-view counter, uptime monitor, or visitor dashboard —
  Lovable Analytics already does that for free.

## Files in this skill
- `references/receiver.gs` — the Apps Script email node (deploy as web app).
- `references/lovable-fetch-snippet.js` — the fetch call shape for Lovable Code Mode.

## Abort / rollback
- To stop emails: in Apps Script, Deploy -> Manage deployments -> remove the
  deployment, or change "Who has access" to "Only myself".
- To stop tracking: Lovable -> Project settings -> General -> Publishing ->
  toggle "Visitor analytics" off; and remove the Clarity script (re-publish).
