---
name: fonovye-zadachi-planirovshchik
description: 25.10.2026 механические дела перенесены на Планировщик Windows через komputer\raspisanie\zapusk.py; радар выключен, пока не нужен
metadata:
  type: project
---

Дело d8b3d4df сделано 25.10.2026. Задачи Планировщика идут через `komputer\raspisanie\zapusk.py <имя>` (pythonw, без окна,
табло `agent_status --glob`, итог в `raspisanie\itogi\<имя>.txt`, строка в `zhurnal.txt`). Создаёт/правит их `sozdat_zadachi.ps1`
(файл с BOM, иначе PowerShell 5.1 ломает русский). Задачи: TG_Monitor 9:00, Фон_вакансии пн 10:30, Фон_сайт_СмартЛюкс 12:00 (check_links),
Фон_копия_GitHub 23:30 (`nochnaya_kopiya.py`: сначала proverka_klyuchey, чужие origin и разошедшиеся истории пропускает), ChistkaMesta раз в час.
Фон_радар_неделя создана ВЫКЛЮЧЕННОЙ; её слово 25.10: пока не нужен, поднимет сама. decor-store-theme перенесена в C:\Users\User\arhiv\ (пока не нужна).

**Why:** лимит Claude тратился на механику (n8n удалён [[n8n-udalen]]); ChistkaMesta до этого молча не работала — «не запускать на батарее» давало код 0x800710E0.
**How to apply:** новую фоновую задачу — добавить в ZADACHI в zapusk.py и в sozdat_zadachi.ps1; в настройках всегда AllowStartIfOnBatteries, WakeToRun выключен.
Ключи только в .env. Радар включать только по её слову.
