---
name: project-weekly-reports-pipeline
description: "reports.js / reports-upload.js — WB weekly settlement reports into the \"1\" spreadsheet's Sheet1"
metadata: 
  node_type: memory
  type: project
  originSessionId: c254b122-50de-4a36-985b-a74e9c575ffb
  modified: 2026-07-30T13:50:59.593Z
---

Second pipeline in `my-bot`, unrelated to the Сравнение sheet. Built 2026-07-30.

Source: `seller.wildberries.ru/suppliers-mutual-settlements/reports-implementations/reports-weekly-new`.
No API is involved — everything goes through Playwright over CDP on port 9222.

**`reports.js`**
- Table rows match `[class*="Reports-table-row"]`; each row's innerText splits into
  `номер | продавец | "с DD.MM.YYYY по DD.MM.YYYY" | дата формирования | тип`.
- Every week has exactly **two** reports: **«Основной»** and **«По выкупам»** —
  that is the pair the user means by "2 отчёта", NOT two different weeks.
- Groups by period, newest first; `PERIODS` arg (default **1** = current period
  only) picks how many weeks. Prints whether each period falls in the current month.
- Downloads via the **«Скачать Excel»** button (Russian UI) on
  `.../report/<номер>`. The download is a **ZIP containing one real .xlsx** even
  though the button implies Excel — saved as `reports/<num>.zip`, inner file
  extracted to `reports/extracted/<num>.xlsx` (PowerShell
  `System.IO.Compression`, since Node has no built-in unzip).
- Writes `reports/manifest.json` with `{num, type, period, start, end, file}`.
- Already-extracted reports are skipped.

**`reports-upload.js`** → target spreadsheet
`12OLxU8EDwN6nJQGySGEczKe0wflJN1dr4-4Y1Dynyxw`, sheet **`Sheet1`**.
- All report files share the same **84 columns**, so merging a period's pair is a
  plain concatenation: one header + data rows of both.
- `Sheet1` is the raw landing area — `Лист1 (1)` states "Источник — Sheet1
  (вставляешь отчёт реализации как есть)" and computes everything with
  `СУММЕСЛИМН(ДВССЫЛ("Sheet1!N:N");…)`. The per-week tabs and «Динамика финансы»
  are formula-driven off it, so **never dump raw data into the week tabs** and
  **never delete Sheet1** — use `wipe` (clearContents), not `clear`.
- Uploads in chunks of 300 rows, each with an explicit **`at`** row number.
  This matters: a chunk once timed out client-side while Apps Script had already
  written it, and the append-based retry duplicated 200 rows. Explicit `at` makes
  retries idempotent.
- `Ctrl+End` may still report a stale last cell (e.g. CF6510 when data ends at
  6310) because `clearContents()` leaves formatting — not a duplicate-row bug.

**History archive** — sheet «История отчетов», column A = period, then the same 84
columns. Periods are **appended**, never overwritten. It exists as a separate
sheet precisely because accumulating in `Sheet1` would make the `СУММЕСЛИМН`
pivot add different weeks together. Append position and already-loaded periods
are tracked locally in `reports/history-log.json` (`{periods[], nextRow}`), so
each chunk is written with an explicit `at` — a re-run of the same period is
refused, and an interrupted run just rewrites the same rows. `--hist` appends to
the archive without touching Sheet1 (used to backfill older weeks):
`node reports-upload.js 13.07 --hist`.

`run-reports.bat` runs the whole thing: Chrome → reports.js → reports-upload.js.

**Apps Script** bound to that spreadsheet: project
`1eLiR9T4TRklcHFhd8sTpGzSiXXJAim2VHWvY0fgkR9O09H5Mw8VkQn90`, exec URL
`AKfycbygfctg0GocMygEuyZv6MMWyEaIZJ7Kc2bnS6Qa3-osSPuCADM1gcldKaeGg35e93Gn`.
It was originally deployed with an **empty** script (`function myFunction(){}`),
so POSTs failed with "Script function not found: doPost". Code now supports
`sheet`, `rows`, `clear`, `wipe`, `at`. Updating the existing deployment with a
new version keeps the URL stable; the user must click through the OAuth consent
themselves — do not do that for them.

Note: the tab «с 13.07.2026 по 19.07.**2027**» has a typo in the year (should be
2026); left as-is, it is the user's sheet.
