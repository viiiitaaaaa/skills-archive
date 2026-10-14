---
name: project-compare-sheet-formatting
description: "Correct photo row/column sizing for the \"Сравнение\" Google Sheet fed by compare.js + Apps Script doPost"
metadata: 
  node_type: memory
  type: project
  originSessionId: c254b122-50de-4a36-985b-a74e9c575ffb
  modified: 2026-07-30T02:25:15.159Z
---

Working configuration for the "Сравнение" sheet in the Google Sheet at
`https://docs.google.com/spreadsheets/d/12Bmi7Jih3WVIhNJaQ9yBTuTd1vB_i7_1nPCtkZU-DMQ`
(bound Apps Script project `1uul3KbjfkYW1yNgn-wtBh4TK-ga3ceTrv5aeCePYVEgJ8JIGVP2iYDvk`):

- WB product photos are 246×328px. To display them in a cell at row height 150
  without distortion, column width must be **113px** (150 × 246/328 ≈ 112.5).
  `compare.js` already inserts images via `=IMAGE(url;4;150;113)` (mode 4 = fixed
  pixel size) — see `IMG_H`/`IMG_W` constants.
- The Apps Script `doPost` in the bound project has a `if (data.format) {...}`
  block that sets row heights to 150 and column A/B width to 113. **Row 1 (header
  row) must never be resized** — `setRowHeights` must start at row 2, not row 1:
  `sh.setRowHeights(2, sh.getMaxRows() - 1, 150)`. The user explicitly called
  this out after the fix was applied ("но строку 1 никогда не расширяй").
- `compare.js` did NOT originally send `format: true` to the web app, so the
  format block was dead code unless manually run via a separate `fixHeights()`
  function in the Apps Script editor. Fixed by adding a final
  `await toSheet({ rows: [], clear: false, format: true })` call at the end of
  `compare.js`'s main IIFE, so formatting is reapplied automatically every time
  the sheet is rebuilt (compare.js deletes+recreates the sheet on `data.clear`,
  wiping prior formatting).
- Deploying: editing the *same* deployment (pencil icon → new version) keeps the
  `/exec` URL stable. Creating a *new* deployment changes the URL, requiring
  `SHEET_URL` in `compare.js` to be updated to match.
- Competitor price highlighting (added 2026-07-30): `doPost` accepts a
  `paint: [{row, color}]` payload and applies backgrounds via
  `getRangeList().setBackground()` to **`H<row>` only** — the price cell, not the
  whole row (the user explicitly narrowed it from `A:J` to just column H).
  `compare.js` builds the payload while emitting competitor rows, comparing
  column H ("Цена после СПП") with a **5% tolerance** (`PRICE_TOL = 0.05`):
  - `compPrice >= ourPrice * 0.95` → pale green `#d9ead3` (`CLR_OK`) — includes
    competitors more expensive than us, and those undercutting by ≤5%
  - `compPrice <  ourPrice * 0.95` → pale red `#f4cccc` (`CLR_BAD`) — they are
    meaningfully undercutting us
  The user iterated on this rule twice (first cheaper=red/dearer=green with no
  tolerance, then this banded version) — confirm before changing the semantics
  again. Colors and the tolerance live in `compare.js`, so retuning them needs no
  Apps Script redeploy; changing *which cells* get painted does.

How to apply: if asked to touch row heights/column widths on this sheet again,
preserve the "skip row 1" rule and the 113px/150px ratio tied to WB's 246×328
photo dimensions. If the deployment URL ever changes, update `SHEET_URL` in
`C:\Users\User\my-bot\compare.js`.
