---
name: project-photo-color-collection
description: "How photo-fix.js fills both photo and color caches in one page visit, and why card.json is the right color source"
metadata: 
  node_type: memory
  type: project
  originSessionId: c254b122-50de-4a36-985b-a74e9c575ffb
  modified: 2026-07-30T13:51:39.915Z
---

`photo-fix.js` fills **both** `photo-cache.json` and `color-cache.json` in a
single visit per article — it already had to open each WB product card for the
photo, so the color is scraped from the same visit. The user explicitly pushed
back on doing a second pass ("ты нагружаешь лишней работой себя").

Sources and gotchas:
- It scans competitor articles from **both** `excel/` (per-product Evirma
  exports) and `excel-keys/` (key-phrase search exports, see
  [[project-keyword-search-collection]]). Missing the second directory was why
  search-found competitors had no photos.
- Color comes from the **`…/info/ru/card.json`** the product page loads itself,
  field `options[] where name == "Цвет"` → `value`. Captured via
  `page.on('response')` — no extra request.
- Do **not** use WB's internal `/__internal/card/cards/v4/detail` `colors[]`
  field: it returns WB's *normalized* color ("серый") while card.json returns the
  *seller-declared* one ("серебристый"). `colorFamilies()` in `compare.js` puts
  those in different families, so the normalized value silently breaks the color
  filter against mkeeper-collected data. That batch endpoint is also 403 unless
  called with WB's signed headers — plain fetch and same-origin fetch both fail.
- Existing non-empty colors (collected by `colors.js` from the mkeeper "Полки"
  table on *our* product pages) are never overwritten — only blanks are filled.
  A visit that finds no color writes `''` so it isn't retried every run.
- `colors.js` cannot cover search-found competitors at all: it reads colors off
  *our* product pages' mkeeper table, which only lists competitors WB shows there.

Why color matters: it is a real filter (`colorMatch`), and unknown color means
"don't filter". Filling colors cut the sheet from 710 → 414 rows (color rejects
went 1098 → 1683) by removing wrong-color straps that had been slipping through.

`compare.js` prints "Строк конкурентов без фото: N | без цвета: N" each run as a
coverage check. After the first full pass: 0 without photo, 26 without color
(sellers who left the Цвет characteristic empty).

**Tried and rejected:** deriving the missing colors from the product *name* via
`colorFamilies()`. Measured result was **0 of 26** — those names contain no color
word at all («Ароматизатор в машину автоматический», «Сменный флакон для
автомобильного ароматизатора», «Ремешок для часов Samsung Galaxy Fit3»). Roughly
half are air fresheners where colour is not a meaningful attribute anyway. The
change was reverted: zero benefit, and guessing a colour risks filtering out a
legitimate competitor. Don't re-attempt without new evidence.
