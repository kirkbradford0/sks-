# SKS AlphaBot Shop Kiosk Solution — 2026-08-21

**Owner:** AlphaBot (builder) · **Governor:** Kirk Bradford · **Observer:** Hermes · **Inspector:** Sparky/Codex
**Pairs with:** `SKS AlphaBot shop kiosk mission target package 2026-08-21.md` (run `ALPHA-KIOSK-20260821`)

This is the "how." The target package is the "what." Read both before writing code.

---

## 1. Current state (verified)

| Piece | State | Location |
|---|---|---|
| Kiosk frontend | Built (6-step check-in + estimate) but **discards all data** | Lovable `bradfordautosolutionscheckin` |
| Receiving node | **Written, not confirmed deployed** | `kiosk_checkin_receiver.gs` (Apps Script) |
| Wiring guide | Written (3 one-time setups) | `README-kiosk-wiring.txt` |
| AlphaBot status packet | **Missing** | must publish `SKS AlphaBot status packet.json` |
| AlphaBot machine | **Down** — Kirk fixing 2026-08-22 | — |

---

## 2. Target architecture

```
Customer (touchscreen)
   │  6-step check-in + estimate + signature
   ▼
Kiosk frontend (Lovable / target repo)
   │  on "Estimate ready" -> POST JSON, Content-Type text/plain, background, non-blocking
   ▼
Google Apps Script web app  (.../exec)   <- the "node"
   │  parse JSON -> email Kirk instantly
   ├─► Gmail  (kirkbradford0@gmail.com)
   └─► Google Sheet log  (optional, SHEET_ID blank by default)
         │
         ▼  (later lane, NOT this sortie)
      CRM / customer-front-load management
```

## 3. Data contract (exact — matches the receiver)

The kiosk must POST a JSON body with these fields. Names are case-sensitive and already locked by `kiosk_checkin_receiver.gs`:

```json
{
  "name": "string",
  "phone": "string",
  "year": "string",
  "make": "string",
  "model": "string",
  "mileage": "number|string",
  "plate": "string",
  "state": "string",
  "color": "string",
  "symptoms": ["string"],
  "words": "string",
  "priority": "string",
  "bracket": "number",        // call-first ceiling in dollars
  "signed": "boolean",
  "timestamp": "ISO string",
  "estimate": { "labor": "number", "parts": "number", "total": "number" }
}
```

**Transport rules:** `Content-Type: text/plain`, raw JSON string in body, fire-and-forget (ignore errors, never block or error the customer screen).

## 4. Frontend component breakdown

1. **Customer info** — name, phone.
2. **Vehicle** — year, make, model, mileage, plate, state, color.
3. **Symptoms** — multi-select array + free-text "in their words."
4. **Scope / priority** — priority label + call-first ceiling (`bracket`).
5. **Estimate** — labor + parts + total; surface the **$149 diagnostic authorization**.
6. **Signature + submit** — capture signature (`signed`), then fire the POST, then show "Estimate ready."

Every step keeps its state locally so a failed send never erases the customer's screen.

## 5. Build plan (ordered)

1. Confirm target location: Lovable project, or a real repo/branch if the frontend has moved. Record it in the status packet.
2. Ensure the 6-step flow persists the full field set above (especially `symptoms[]`, `bracket`, `signed`, and the nested `estimate`).
3. Add the on-complete POST using the exact transport rules in §3.
4. Verify the receiver is deployed (ask Kirk for the `/exec` URL, or flag it as the top blocker).
5. Run one real test check-in → confirm the email arrives.
6. Return the carrier SITREP + publish the SKS summary.

## 6. Verification / acceptance criteria

- [ ] All 6 steps collect every field in §3 (none dropped).
- [ ] POST fires in background; a kill of the network does **not** freeze or crash the screen.
- [ ] A real test check-in produces a real email in Kirk's inbox within ~2 seconds.
- [ ] Signature status is reported correctly (`signed: true/false`).
- [ ] `SKS AlphaBot status packet.json` is committed to `kirkbradford0/sks-`.

## 7. Risks / blockers

- **Top blocker:** the `/exec` receiver may not be deployed yet. If missing, the sortie is `partial` — frontend complete, data path unverified — until Kirk completes the ~15-min one-time setup in `README-kiosk-wiring.txt`.
- **Machine down** is assumed resolved by Kirk 2026-08-22. Do not proceed to build until confirmed.

## 8. Rollback note

This sortie is frontend-only + a POST. No shared doctrine, billing, or production DB changes. Rollback = republish the previous Lovable version.
