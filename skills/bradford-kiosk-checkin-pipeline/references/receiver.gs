/**
 * Bradford Auto — Lobby Kiosk check-in receiver ("the node").
 *
 * Deploy as a Google Apps Script WEB APP:
 *   Execute as:   Me
 *   Who has access: Anyone
 *
 * The kiosk POSTs the finished check-in here as JSON. This script:
 *   1) emails Kirk the full check-in, the moment a customer finishes
 *   2) (optional) appends a row to a Google Sheet log
 */

const RECIPIENT = "kirkbradford0@gmail.com"; // Kirk's Gmail
const SHEET_ID  = "";                        // OPTIONAL: spreadsheet ID for the log
const SHEET_TAB = "Check-ins";               // OPTIONAL: tab name

/** Simple helper so the kiosk's fetch() gets a clean response. */
function out(ok, msg) {
  return ContentService.createTextOutput(JSON.stringify({ ok: ok, message: msg }))
    .setMimeType(ContentService.MimeType.TEXT);
}

function doPost(e) {
  var payload;
  try {
    payload = JSON.parse(e.postData.contents);
  } catch (err) {
    return out(false, "bad json: " + err.message);
  }

  var subject = "Kiosk check-in: " + (payload.name || "No name") +
    " - " + [payload.year, payload.make, payload.model].filter(Boolean).join(" ");

  try {
    MailApp.sendEmail({
      to: RECIPIENT,
      subject: subject,
      body: buildEmail(payload)
    });
  } catch (err) {
    return out(false, "email failed: " + err.message);
  }

  if (SHEET_ID) {
    try { logToSheet(payload); } catch (err) { /* log quietly, don't fail */ }
  }

  return out(true, "received");
}

function money(n) {
  return "$" + Number(n || 0).toLocaleString("en-US", { maximumFractionDigits: 0 });
}

function buildEmail(p) {
  var L = [];
  L.push("NEW CHECK-IN - BRADFORD AUTO");
  L.push("Time: " + (p.timestamp || new Date().toISOString()));
  L.push("");
  L.push("CUSTOMER");
  L.push("Name:  " + (p.name || "-"));
  L.push("Phone: " + (p.phone || "-"));
  L.push("");
  L.push("VEHICLE");
  L.push([p.color, p.year, p.make, p.model].filter(Boolean).join(" ") +
         (p.mileage ? "  |  " + Number(p.mileage).toLocaleString() + " mi" : ""));
  L.push("Plate: " + (p.plate || "-") + (p.state ? " (" + p.state + ")" : ""));
  L.push("");
  L.push("WHAT IT'S DOING");
  (p.symptoms || []).forEach(function (s) { L.push("  - " + s); });
  if (p.words) { L.push("In their words: \"" + p.words + "\""); }
  L.push("");
  L.push("SCOPE");
  L.push("Priority: " + (p.priority || "-"));
  L.push("Call-first ceiling: " + (p.bracket === null || p.bracket === undefined ? "-" : money(p.bracket)));
  L.push("");
  L.push("ESTIMATE");
  L.push("Labor: " + money(p.estimate && p.estimate.labor) +
         "   Parts: " + money(p.estimate && p.estimate.parts) +
         "   Total: " + money(p.estimate && p.estimate.total));
  L.push("Diagnostic authorized ($149) - signature " + (p.signed ? "on file" : "MISSING"));
  L.push("");
  L.push("(Sent automatically by the lobby kiosk)");
  return L.join("\n");
}

function logToSheet(p) {
  var ss = SpreadsheetApp.openById(SHEET_ID);
  var sh = ss.getSheetByName(SHEET_TAB);
  if (!sh) { sh = ss.insertSheet(SHEET_TAB); }
  sh.appendRow([
    p.timestamp || new Date().toISOString(),
    p.name || "",
    p.phone || "",
    [p.year, p.make, p.model].filter(Boolean).join(" "),
    p.mileage || "",
    p.plate || "",
    p.state || "",
    p.color || "",
    (p.symptoms || []).join(", "),
    p.words || "",
    p.priority || "",
    p.bracket === null || p.bracket === undefined ? "" : p.bracket,
    p.signed ? "yes" : "no",
    p.estimate ? p.estimate.total : ""
  ]);
}
