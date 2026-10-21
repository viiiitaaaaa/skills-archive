---
name: rezervnye-kopii
description: "Резервные копии (15.10.2026) — всё на приватном GitHub, память проектов и настройки в skills-archive, ключи никогда наружу, проверка ключей при «споки», переписки 90 дней, чистку только по её слову"
metadata:
  node_type: memory
  type: project
  originSessionId: d3ede0b1-b4cb-4725-9bba-f85e77ebdbbd
  modified: 2026-10-14T22:03:28.482Z
---

Отчёт и план восстановления на новом ПК: `C:\Users\User\komputer\rezerv\otchet.html`.

Её решения 15.10.2026:
- **Всё на GitHub, приватно.** 26 хранилищ viiiitaaaaa, все PRIVATE. 15.10 добавлены pult, komputer, my-bot, wb-scripts-my (папка my), store3, dolphin-anty-scripts, pc-check, claude-widget, golos-konec, newton1688. tools не копируем (программы).
- **Ключи — никогда никуда** (ни GitHub, ни Диск, ни флешка пока): «если ломается, я выпущу». Проверять постоянно (её довод: новость о программах, которые ищут ключи на GitHub). Проверка `komputer\rezerv\proverka_klyuchey.py` (все папки + вся история + открытые хранилища) — сама идёт в конце `sync_skills.ps1`; перед выгрузкой архива `--staged` останавливает отправку. Общий git-хук `rezerv\git-hooks\pre-commit` включён ею 15.10 (`git config --global core.hooksPath`), проверен: файл с ключом не коммитится. Ложное срабатывание — `git commit --no-verify` только после проверки глазами.
- `sync_skills.ps1` теперь копирует память всех проектов (`memory_proektov\`) и настройки (`nastroyki_claude\`: settings.json, statusline, agent_status, агенты, звуки, `mcp_servers.json` без ключей через `rezerv\eksport_mcp.py`). settings.local.json не берём — там ключ бота.
- **Переписки** — только на ПК, `cleanupPeriodDays: 90` в settings.json (старше 3 месяцев удаляются сами). Выводы из них — в память/скиллы → GitHub.
- Флешка и единый менеджер паролей — потом, вместе; 15.10 попросила напоминать (пункт «НАПОМНИТЬ» в глобальном CLAUDE.md: при каждом «споки» и в разговорах о паролях/ключах/резерве).
- **Чистить место — ничего, пока она не скажет.** Поставлен TreeSize Free (`AppData\Local\Programs\JAM Software\TreeSize Free\TreeSizeFree.exe`) — смотрим дерево вместе.
- Google Диск пока не проверять. Claude Desktop — «забудь, ничем не поможет»; тема магазина: ветка `backup/local-2026-10-15`, в main не пушить (main = живой Shopify).

**Why:** «чтобы в случае, если не повезло, всё было сохранено и задокументировано и можно было в любой момент поднять».
**How to apply:** новая папка проекта → сразу приватное хранилище + .gitignore с блоком ключей; при «споки» смотреть итог проверки ключей. Связано: [[arhiv-skillov]], [[spoki-sohranit-vse]].

Копии по дням на ПК (22.10.2026): [[kopii-po-dnyam]].
