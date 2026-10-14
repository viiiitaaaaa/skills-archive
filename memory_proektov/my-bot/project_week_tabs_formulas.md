---
name: project-week-tabs-formulas
description: reports-formulas.js — week tabs pull from «История отчетов» by period; column map and what must NOT be formula-driven
metadata: 
  node_type: memory
  type: project
  originSessionId: c254b122-50de-4a36-985b-a74e9c575ffb
  modified: 2026-07-31T00:17:55.150Z
---

`reports-formulas.js` fills the per-week tabs of spreadsheet
`12OLxU8EDwN6nJQGySGEczKe0wflJN1dr4-4Y1Dynyxw` with SUMIFS formulas reading
«История отчетов», filtered by that tab's period. Tab names equal the period
string in column A of the archive, so the filter is exact.

**Column map.** «История отчетов» = the 84 report columns shifted one right
(column A is Период):
`A` Период · `G` Артикул поставщика · `L` Обоснование для оплаты
(«Продажа»/«Возврат») · `O` Кол-во · `P` Цена розничная · `Q` ВБ реализовал ·
`U` Цена розн. с уч. согласованной скидки · `AI` К перечислению Продавцу ·
`AL` Услуги по доставке · `BI` Хранение.

Week-tab columns filled: E,F (кол-во прод/возвр), G=E−F, H,I (выручка), J
(выручка с уч. скидки, продажа−возврат), K,L (реализ), M=K−L, N,O (к перечисл),
P=N−O, T (логистика). Row after the last data row is «ИТОГО» → `=SUM(col2:colN)`.
Data is rows 2..(ИТОГО−1) — do not write formulas into the ИТОГО row itself.

**Column U «Хранение» — УСТАРЕЛО, теперь заполняется формулами.** Раньше здесь
стояло «не гнать формулами»: в отчёте реализации хранение идёт ~10 строками с
**пустым артикулом**, разнести по SKU нельзя. Но с 30.07.2026 источник другой —
отчёт по номенклатурам платного хранения, там есть «Артикул продавца». Колонку U
ставит `storage-upload.js` через SUMIFS из листа «История хранения»
(см. [[project-storage-pipeline]]). Итоги сошлись: 7 382,43 ₽ за 13–19.07 и
8 637,16 ₽ за 20–26.07.

Verification method that caught everything: back up `A1:U400` display values of
both tabs first, then diff old vs new after writing (see scratchpad
`backup-weeks.js` / `verify-weeks.js`). Result 4647/4648 cells matching.

The one remaining delta is ИТОГО for логистика: 74 047 before vs 73 792 now. The
255 ₽ difference is a WB row literally named «неопознанный товар» which has no
SKU and therefore belongs to no row of a per-SKU tab. Everything else reconciles
(SUMIFS matches article names case-insensitively, which is why
`jk-577-aroma-avto/черный` is counted even though a naive exact-match check in
Node says it is missing from the tab list).

**Книга вычищена 31.07.2026:** удалены «Sheet1», «Лист1 (1)» (старая связка
сырьё+сводная, заменена недельными вкладками) и «История остатков» (заменена
«Историей воронки»). Остались: 4 недельные вкладки, 4 листа «История …»,
«Динамика финансы», «Себестоимость», «Export» (ничем не используется, но
владелец просил оставить). reports-upload.js переведён на WRITE_SHEET1=false.
Удаление листа — только через UI: контекстное меню ярлыка (правый клик через
CDP Input.dispatchMouseEvent по координатам .docs-sheet-tab) → «Удалить».
**Apps Script-эндпоинт удалять НЕ умеет и на неизвестный payload ({del},
{remove}…) отвечает 'ok', СОЗДАВАЯ пустой лист** — не пробовать вслепую.

Колонка D недельных вкладок подвязана к листу «Себестоимость»:
`=IFERROR(VLOOKUP(TRIM($A2);'Себестоимость'!$A:$B;2;0);0)`. Fallback обязан
быть числовым 0: текстовый "-" ломает Q (себестоимость продаж) → Q302 →
«Динамику» (#VALUE! в G/R/Y/Z/AA).

Предсуществующий мусор в «Динамике»: строки 112 и 130–132 полны #REF!
(ссылки на давно удалённые вкладки), это НЕ следствие правок.

**«Динамика финансы» ПЕРЕСТРОЕНА владельцем (31.07.2026):** колонка B теперь
содержит собственную сетку недель («26.02 - 03.03» и т.п.), а не периоды
«с ... по ...». reports-dynamics.js там ничего не найдёт и ничего не должен
трогать — НЕ запускать без явной просьбы. Также запрещено трогать: колонку C
недельных вкладок (формула владельца «дней до обнуления»
=ЕСЛИОШИБКА(ОКРУГЛВВЕРХ(B/(AP*AS/100/7);0);"-") — завязана на B, AP, AS)
и кэши photo-cache.json / color-cache.json.

**`reports-dynamics.js`** links the «Динамика финансы» rows to the week tabs.
Pattern copied from the sheet's own pre-existing row 112 (`='1'!$H$333`): each
period row references its week tab's ИТОГО row 333 —
D←H, E←I, F=D−E, G←Q, H←T, I←R, J←U, N←V, P←Z, and C/S are the existing derived
formulas. A row whose period has no week tab is **left untouched** (16 of 18 rows
today) — writing formulas there would zero out historical data.

Because «Динамика финансы» needs the true money figure, the week tab's ИТОГО for
T (логистика) is `SUMIFS(AL; period)` — the full period total — not `SUM` of the
SKU rows. Every other ИТОГО is a plain `SUM`. With that, week tabs verify
4648/4648 against the pre-change backup.

**`reports-period.js`** onboards a new period automatically: it takes the newest
period from `reports/manifest.json`, creates the week tab named exactly after it
(by duplicating the latest existing week tab via the `dup` doPost mode), and adds
the row to «Динамика финансы» with the month label in A and the period text in B.
Both steps are skipped if they already exist, so it is safe to re-run.

**УСТАРЕЛО и ОПАСНО: копию больше НЕ чистить.** Раньше dup сопровождался
очисткой Q2:S333, U2:Z333, AA2:AK333 как «ручных значений». Теперь в Q..S и
W..AK стоят ФОРМУЛЫ владельца (юнит-экономика, налоги), считающие от колонок
своей вкладки, — очистка 31.07.2026 убила их на двух новых вкладках.
Восстановлено копированием Q2:S302/W2:Z302/AA2:AK302 с вкладки-донора через
UI таблицы (поле имени #t-name-box + CDP Ctrl+C/Ctrl+V — формулы при вставке
привязываются к своей вкладке). reports-period.js исправлен: MANUAL_RANGES=[].
B, U, V, AL..AV после dup переустанавливают funnel-/storage-/ads-upload.

Month label rule (verified against 17 of 18 existing rows — the 18th only differs
because the sheet's history starts mid-March): the week belongs to the month
holding **the majority of its days**, and the index is the highest existing index
for that month plus one. So «с 27.07.2026 по 02.08.2026» → «Июль 5».

`reports-formulas.js` no longer has a hardcoded tab list — it discovers every
sheet whose name matches the period pattern, so a newly created tab is picked up
automatically. Full chain in `run-reports.bat`: reports → upload → period →
formulas → dynamics.

**Lesson — back up raw values, not display values.** The U restore used
`getDisplayValues()`, which is formatted text ("7 382" for 7 382,47), so kopecks
were lost and «Динамика финансы» row 128 drifted by 3 ₽ (J, and via it C and S).
Add a `getValues()` mode if a restore is ever needed again.

**Bug that cost real data:** `doPost` honoured `data.col` only in the `formulas`
branch, not in the `rows` (setValues) branch. A restore that passed `col: 21`
therefore wrote into **column A**, wiping the article names and breaking every
SUMIFS. Fixed — both branches now use `data.col || 1`. Always re-read after a
positional write.
