# LESSON: long-lived local helper servers die silently on reboot

Date: 2026-09-29 (found by SKS running tasks cron pass 0015)
Severity: medium — silently blocks OAuth paste-back lane (campaign test volley + Gmail recovery)

## What happened
Pass 0014 (2026-09-29 00:02) verified `oauth_catcher_server.py` (PID 8216) as the sole
port-80 listener and marked the port-80 consolidation done. By the next pass (06:00),
the process was gone — machine had rebooted (uptime shows boot 09-23 19:29, i.e. the
process died some time after 00:02, not at boot; either way it was not self-healing).
Nothing surfaced the death: no cron check, no log, the capture file just sat stale.

## Rule going forward
1. Anything that must survive (OAuth catcher on port 80, HIL-DECK on 8799, GEV on 4173)
   needs a start-on-login wrapper — START-DECK.bat exists for 8799 but nothing auto-runs it.
2. The SKS running tasks cron pass should re-check port-80 listener + approval page
   HTTP 200 each run before declaring the OAuth lane "waiting on Kirk" — a dead catcher
   makes Kirk's click bounce to nothing.
3. Verify a "done" service with a live probe (curl 200), not just a past PID.

## Fix applied THIS pass (2026-09-29 06:02)
- Restarted catcher: repo copy at C:/Users/bradf/AppData/Local/hermes/oauth_catcher_server.py
- Verified: netstat 0.0.0.0:80 LISTENING (PID 19268); approval page
  http://192.168.1.253/Felon%20Melon_Kirk/hermes-approval.html → HTTP 200;
  embedded accounts.google.com auth URL state == pending verifier state
  (Qj0Sz562VkmpE5mMczt0fkLyLcxY102U); capture path writes google_oauth_captured.txt.