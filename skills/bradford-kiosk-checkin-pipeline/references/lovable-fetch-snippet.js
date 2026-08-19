// Lovable Code Mode — fetch call to add on the "Estimate ready" (step 6) screen.
// The compiled bundle obfuscates names; read the REAL source in Code Mode and
// map these keys to the app's actual state object. Do not guess the names.

// The app's form state (from decompiling the live bundle) holds these fields:
//   name, phone, year, make, model, mileage, plate, state, color,
//   symptoms (array), words, priority, bracket, signed
// The computed estimate exposes: labor, parts, total.

const NODE_URL = "https://script.google.com/macros/s/__PASTE_NODE_URL_HERE__/exec";

// Fire-and-forget on the estimate screen. Never block the customer.
const payload = {
  timestamp: new Date().toISOString(),
  name, phone, year, make, model, mileage, plate, state, color,
  symptoms, words, priority, bracket, signed,
  estimate: { labor, parts, total },
};

fetch(NODE_URL, {
  method: "POST",
  headers: { "Content-Type": "text/plain" }, // text/plain avoids CORS preflight
  body: JSON.stringify(payload),
}).catch(() => { /* ignore errors — never break the kiosk */ });
