---
name: arhiv-skillov
description: Архив всех скиллов и промтов — C:\Users\User\claude-skills = git-репозиторий viiiitaaaaa/claude-skills (приватный); обновлять при каждом новом или переписанном скилле
metadata:
  node_type: memory
  type: feedback
  originSessionId: 7d08801d-9fab-4181-8e23-bee1a2c82936
  modified: 2026-09-28T00:59:07.017Z
---

Все скиллы и промты дублируются в архив `C:\Users\User\claude-skills` — это git-репозиторий
**viiiitaaaaa/claude-skills** (приватный): `skills\` (полная копия `.claude\skills`), `promty\` (вынутые файлы
с промтами), `ОПИСАНИЕ_СКИЛЛОВ.txt` (текстовый док «кто чем занимается»), `sync_skills.ps1`, `last_sync.txt`.
Заведено 19.08.2026 (в Downloads); 28.09.2026 по её слову перенесено в git, с Google Диска удалено
(«на гугл диске не нужен»).

**Why:** она хочет видеть все наработки в одном месте обычными файлами и читать описание без Claude;
хранить — на GitHub, не на Google Диске.

**How to apply:** после создания или переписывания скилла — запустить
`powershell -ExecutionPolicy Bypass -File "C:\Users\User\claude-skills\sync_skills.ps1"` (скрипт сам
пересобирает skills\ и promty\, убирает вложенные .git, коммитит и пушит) и дописать/поправить раздел
в `ОПИСАНИЕ_СКИЛЛОВ.txt` (потом снова запустить скрипт или сделать commit+push). Правки — в оригинале
`.claude\skills`. Новый скилл с промтами — добавить в `$promptFiles`. .ps1/.txt с кириллицей — UTF-8 **с BOM**.
Личные правила `rules.local.json` в git не попадают (.gitignore). Связано: [[karta-skillov]], [[google-drive-struktura]].
