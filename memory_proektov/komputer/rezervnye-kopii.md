---
name: rezervnye-kopii
description: "Состояние резервных копий на 15.10.2026 — отчёт komputer\\rezerv\\otchet.html; что на GitHub, что нет, выключатели в sync_skills.ps1, тема магазина связана с живым Shopify"
metadata:
  node_type: memory
  type: project
  originSessionId: d3ede0b1-b4cb-4725-9bba-f85e77ebdbbd
  modified: 2026-10-14T21:15:18.096Z
---

Аудит 15.10.2026, отчёт `C:\Users\User\komputer\rezerv\otchet.html` (план восстановления на новом ПК, 11 шагов).
- 11 папок проектов — в приватных репозиториях viiiitaaaaa (сохранено и выгружено 15.10). Без GitHub: **pult** (git есть, remote нет), **komputer** (нет git), my-bot, my, store3, dolphin_anty, pc_check.
- **decor-store-theme: main связан с живым Shopify** («Update from Shopify» коммиты) — в main не пушить; локальная работа лежит в ветке `backup/local-2026-10-15`.
- `skills-archive\sync_skills.ps1`: добавлены блоки «память проектов» и «настройки Claude» за выключателями `$vklMemProektov`, `$vklNastroyki` = `$false` — включать только после её «да» (классификатор остановил выгрузку памяти проектов как личные данные).
- `settings.local.json` содержит ключ бота Telegram — наружу не копировать.
- Переписки .jsonl 2,9 ГБ, копии нет; совет — не копировать (🔴).
- C: свободно 7,9 ГБ (96%); AppData 58 ГБ.

**Why:** Вита хочет, чтобы при поломке всё было сохранено и можно было поднять.
**How to apply:** ждём её ответы на 6 вопросов в конце отчёта; после ответа — создать репозитории / включить выключатели / чистка. Связано со старой памятью [[arhiv-skillov]], [[spoki-sohranit-vse]].
