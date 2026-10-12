---
name: dolphin-profile-id
description: "Dolphin{anty}: у пользователя ВСЕГДА только один профиль — 859648353 (AliExpress, магазин, радар — всё в нём); 828976678 больше не существует"
metadata:
  node_type: memory
  type: project
  originSessionId: 918f5935-fcac-4c45-bb60-0438bdbda7cf
  modified: 2026-09-25T21:39:25.252Z
---

**Единственный профиль Dolphin — 859648353** (пользователь 26.09.2026: «у нас всегда только один профиль!!!»).
AliExpress, магазин Shopify, радар трендов — всё в нём. Не спрашивать, какой профиль, и не искать другие.
Старый 828976678 («Ремешки») в Dolphin больше не существует («basic browser profile not found»), папки других
профилей в %APPDATA%\dolphin_anty\browser_profiles — мусор, их не трогать и не запускать.

Подключение без перезапуска (вкладки пользователя остаются): порт из
`%APPDATA%\dolphin_anty\browser_profiles\859648353\data_dir\DevToolsActivePort` → connect_over_cdp
(функция `cdp_endpoint()` в fashion-trend-radar/run_retailers.py). Playwright есть только в .venv радара.

**Why:** я полезла в несуществующий профиль и переспрашивала — пользователя это разозлило.
**How to apply:** всегда 859648353. Связано: [[dolphin-anty-scripts]], [[dolphin-profil3-dlya-trend-radar]].
