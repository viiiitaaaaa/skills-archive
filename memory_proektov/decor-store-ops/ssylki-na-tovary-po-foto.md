---
name: ssylki-na-tovary-po-foto
description: Скилл поиска ссылок на товары AliExpress по фото и импорта их в Dsers
metadata: 
  node_type: memory
  type: project
  originSessionId: 01751d72-549c-49dc-8269-5150f5435db9
  modified: 2026-08-18T12:32:04.399Z
---

Ссылки на товары AliExpress по картинкам и импорт в Dsers — скилл `product-links`
(`C:\Users\User\.claude\skills\product-links\`), рабочие копии скриптов в
`C:\Users\User\dolphin_anty\`: `match_folder.py` (папка → Excel, основной режим),
`match_products.py` (один магазин → CSV), `dsers_add.py` (жать «Add To DSers»).

Основной сценарий пользователя: даёт путь к папке с вырезками → магазин определяется
из имени файла → ссылка из `state_tabs.json` → обход каталога → **Excel** со ссылками.

**Why:** пользователю нужен именно Excel и именно по сборной папке из разных магазинов;
плюс присланный им скрипт листал каталог через `&page=N` — так AliExpress отдаёт одну
и ту же страницу, и ссылки выходили мусорные при нормальном на вид логе.

**How to apply:** цепочка — [[narezka-kartochek-tovarov]] → [[kollektsii-po-stilyam]] →
этот скилл. Профили Dolphin — [[dolphin-profile-id]]. Кнопку «Add all to DSers» никогда
не жать: она тянет рекламные товары чужих продавцов.
