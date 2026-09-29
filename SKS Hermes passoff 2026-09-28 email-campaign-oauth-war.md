# SKS Hermes handoff — 2026-09-28/29 (night: campaign model, email lanes, OAuth war)

Agent: Hermes (Hermes v0.20.6, ollama-cloud / glm-5.3-flash) on OfficeLeft (shop PC).
Scope: this passoff covers 2026-09-20 → 2026-09-28 as requested by Kirk ("complete handoff, one sentence per paragraph, something's fucked up but I don't know where").
Sources: this Telegram thread (Sep 20–29), repo passoffs 09-25/09-27, campaign checklist, Honcho observations.

## Narrative — what happened, in order (one sentence per paragraph)

Snow Strike doctrine went formal on 09-26: Kirk defined a two-role loop — PATRIARCH supervises/verifies/sequences, MITCH executes bounded tasks and returns evidence — with a hard scoreboard of 100 real Felons Melon users and a 10-sales-per-100 conversion hypothesis behind the $19 kit.
Kirk approved the campaign 100x100 test volley plan as 10 emails (2 Kirk seeds + West Coast orgs), sent from felonsmelon@gmail.com, drafted into the Gmail DRAFT queue, with Kirk pressing send on each (HITL).
Kirk's notepad model for the campaign was locked: ONE constant first email to everyone, no city/persona variation in the message, variation lives at the HYPERLINK (three landing pages — start-a-case intake, "AI that knows recovery", parole-organization help — all funneling to felonsmelon.com), tracker counts replies at day 7, then adjust and repeat.
Kirk approved LOCAL OLLAMA Sparky (Qwen 2.5 7B or Llama 3.1 8B at localhost:11434, $0/mo, data never leaves the machine) instead of a DeepSeek cloud key for the FM website's /api/sparky route; adapter pattern (SPARKY_PROVIDER env) keeps the swap trivial later.
The DeepSeek lane is documented but parked: login kirkbradford1@icloud.com (password in his password note file), key-drop folder is on Kirk's OTHER profile (C:/Users/kirkb/OneDrive/APIs purchased for App Specific Use) which does NOT sync to the shop PC.
Kirk's mental model of ownership got corrected twice: Patriarch = shop-PC agent (Codex lane) that went silent when the shop box was down, and Hermes (this Telegram DM) = Sparky = runs on OfficeLeft; Kirk approved the deepseek-provider.ts plan Patriarch drafted but chose local-first.
A gift zip (D:/KinloaSlate/Dewey/KinloaSlate/Memory_Bank KH-1b/FELONS MELON Front End Paths.zip — "a present to suit the website up") could NOT be received: the shop PC has no D: drive; Kirk must copy it into OneDrive/Desktop/Felon Melon_Kirk or the viking-go-between folder.
Patriarch went dark during the session (shop computer), which is why Kirk asked "why is patriarch not responding lol wtf".

## The Google OAuth war (the "something's fucked up" thread)

Stored google_token.json (Sep 1) died with invalid_grant; the campaign has NEVER sent an email (volley staged since 09-25, still zero sends).
A fresh PKCE flow was armed (verifier in hermes/google_oauth_pending.json, client 511609326141-k98gpok7acbb4gtkglobn86l1eu4090j, scope mail.google.com + gmail.modify + gmail.readonly, prompt=consent to force refresh token).
Hermes built a mobile-friendly approval page (OneDrive/Desktop/Felon Melon_Kirk/hermes-approval.html) with one big green "Approve Hermes" button, served from the shop PC Desktop via http.server on port 80.
First blocker: 127.0.0.1 on the PHONE points at the phone — fixed by serving via the shop PC's LAN address; http://192.168.1.253/Felon Melon_Kirk/hermes-approval.html (verified 200).
Second blocker: Google blocked consent with "app has not completed verification" because project felonsmelonsparkpost is in External/Testing mode; Kirk navigated the console (got lost once in an iOS client creation screen — redirected to the Audience page) and SUCCEEDED adding felonsmelon@gmail.com to Test users (confirmed on-screen).
Third fix: the catcher was upgraded to a custom server (hermes/oauth_catcher_server.py on port 80) that returns a big green "CAPTURED - DONE" page AND logs the code to google_oauth_captured.txt; end-to-end tested with a fake code and cleaned up after.
Current blocker at pause time: Kirk could not get the Google auth page to load anywhere on his phone ("can't get the google auth to even come up"), though the URL is verified live (302 from accounts.google.com); the raw PKCE url was sent for direct paste, and the catcher remains armed.
The catch file currently holds only junk (/favicon.ico); NO OAuth code has been captured; token file remains the dead Sep 1 one.

## Kirk's explicit direction changes (09-28, same day — all Kirk's calls)

App-Password lane KILLED by Kirk ("definitely not trying to put a two step authorization on there") — App Passwords require 2FA first, so that path is abandoned.
Kirk pivoted AWAY from Gmail toward a non-Google, highest-security, flexible email stack; research (DDG lane; Firecrawl bill ran dry) produced: Proton Mail (Swiss, Proton Foundation majority owner, CERN founders, optional 2FA, no phone required, free 150/day but SMTP/Bridge paid-only) = security/receive lane; Brevo (300/day free, plain signup, SMTP key, real bounce/spam reports) = send lane — recommendation approved as $0/mo two-lane pattern.
BCC rule (final): every outbound BCCs kirkbradford1@icloud.com + kinloaslate@gmail.com (NOT kirkbradford0); sender felonsmelon@gmail.com; reply-to kirkbradford0@gmail.com.
Campaign repo split (Kirk order 09-27): ALL campaign code/logs go to kirkbradford0/Operation-Mer-ki, never mixed into sks-/dabs/sparkpost.

## Worked & verified (machine-side, all green)

Himalaya v2.1.0 installed at ~/bin/himalaya.exe (verified running, Windows build) as the keyless terminal email client.
Catcher (oauth_catcher_server.py) live on port 80 with CAPTURED confirmation page + watcher pattern; fake-code test passed and was scrubbed.
Approval page verified 200 from LAN address; draft outreach-email-ORGS-draft.md verified CLEAN (zero plural felonsmelons.com).
Checklist staked: campaign-100x100/BATCH-0-CHECKLIST-2026-09-28.md (5 steps: OAuth → token verify → 10 drafts queued w/ Kirk-copy BCC + landing-page variants → Kirk sends → tracker loop).
SKS running tasks updated pass 0013 (26ab6e6) — pre-send blockers reduced to ONE (OAuth code).

## Where it's probably fucked (Kirk asked; ranked)

1. Phone-side rendering of the Google auth URL (Safari/one-tap-wifi/DNS on the phone) — the exact URLs are alive from the shop PC, so the page itself is fine; anything that can't load it is device/network side.
2. Multiple http.server instances on port 80 (two python processes were found listening) — harmless for capture but should be consolidated to the custom catcher only.
3. The "fire in the hole" screenshot was the Test-users screen, not the consent flow — Kirk may believe approval is done when only the whitelist is done; the consent screen never rendered for him.
4. If nothing loads on ANY device, re-issue the OAuth url fresh (state/verifier are from 09-26 and still armed, but a fresh pair costs nothing).

## Next actions for whoever picks this up (in order)

1. Get the PKCE url rendered for Kirk on ANY device (phone Chrome, shop PC, Lenovo) — the link is in this thread; approval as felonsmelon@gmail.com → code lands in google_oauth_captured.txt automatically.
2. Exchange code → verify granted account == felonsmelon@gmail.com via getProfile BEFORE building drafts.
3. Stage 10 Batch 0 drafts (landing-page link variants across 10, BCC rule, reply-to) into Gmail DRAFT queue → Kirk sends → trace.
4. Parallel: Proton (identity/receive) + Brevo (send) signup walk-through for the non-Google stack Kirk wants — Brevo SMTP key can back up himalaya.py config directly.
5. Still owed: FELONS MELON Front End Paths.zip hand-delivery via OneDrive; local Ollama Sparky install; deepseek-provider.ts build when Sparky goes live; Sunday metrics cron.

## What did nobody else check?

- The approval page itself was never re-tested after the whitelist change — worth a 30-second cold reload from a different device before blaming the phone.
- The Brevo deliverability claim (bounce/spam reporting) is from vendor marketing pages — needs a live smoke test before relying on it for the health gates.

— Hermes (OfficeLeft), 2026-09-29 03:15 MDT