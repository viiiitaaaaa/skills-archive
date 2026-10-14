---
name: project-keyword-search-collection
description: How keywords.js collects extra competitors from WB search results and merges them into the Сравнение sheet
metadata: 
  node_type: memory
  type: project
  originSessionId: c254b122-50de-4a36-985b-a74e9c575ffb
  modified: 2026-08-04T19:10:08.143Z
---

**Три прохода сбора конкурентов в `compare.js`** (04.08.2026). Если после всех
фильтров группа пуста, она пересобирается без фильтра по цвету, а если и это не
помогло — ещё и без фильтра «дешевле нас больше чем на 30 %». Проверка модели по
названию остаётся всегда. Без этого 16 товаров из 121 вообще не попадали в лист:
у редких цветов (медь, графит, перламутр, лавандовый) конкурентов того же цвета
нет, а у дорогих (blok-redmi-w-3, 1 210 ₽) под ценовой фильтр уходила вся
выдача. `node compare.js --why` печатает разбор по каждому товару без записи.

Second competitor source added 2026-07-30 (`keywords.js`), on top of the
per-product Evirma exports that `pipeline.js` already downloads into `excel/`.

How it works:
- A **key phrase** is derived from each of our product names by stripping
  material/property words (металлический, силиконовый, нейлоновый, миланская
  петля, …). Names that mention neither "ремеш" nor "браслет" (e.g. "Ароматизатор
  в машину автоматический") are left completely untouched — the user asked for
  that explicitly.
- Two regex gotchas that were actual bugs, keep them fixed:
  1. `\w` does NOT match Cyrillic in JS, so `металлическ\w*` left a stray "ий".
     Endings must use `[а-яё]*`.
  2. Product names mix Latin lookalikes into Cyrillic words ("**C**иликоновый"
     with a Latin C). `fixLatin()` converts a Latin char to Cyrillic only when a
     Cyrillic char is adjacent, so brand names (Huawei, Xiaomi) stay intact.
     Same trick as `norm()` in `compare.js`.
- Phrases are **deduplicated before searching**: 122 products collapse to 29
  unique queries (one phrase often covers 4–5 of our articles). `keys.json` maps
  each phrase → `{phrase, file, arts[]}`. Plus `SKIP_DONE` skips any phrase whose
  file already exists in `excel-keys/`. The user cares about this — never issue
  the same search query twice.
- For each phrase: WB search URL → the Evirma panel's **"Реклама на странице"**
  block → its "Экспорт в Excel" button (the only such button on a search page) →
  saved to `excel-keys/<slug>.xlsx`. Column layout is **identical** to the
  product-page exports, so `e[0]`=артикул, `e[2]`=название, `e[8]`=цена,
  `e[11]`=рейтинг work unchanged.
- `compare.js` merges both sources per product via a shared `collect()` closure
  applying the existing filters (own brand, name match, color, MAX_CHEAPER), then
  dedupes **within that product's group** by article (`seen` Set) — the same
  competitor may legitimately appear under different products of ours.

Result of the first full run: 309 → 710 rows, 84 → 110 groups, 375 competitors
added from key-phrase search, 46 skipped as duplicates.

`run.bat` now has 8 steps, with `node keywords.js` as step 7 before `compare.js`.
See [[project-compare-sheet-formatting]] for the sheet formatting/highlighting.
