---
name: vidzhet-limitov-claude
description: "Виджет лимитов Claude над панелью задач — C:\\Users\\User\\claude_widget\\claude_limits_widget.py, автозапуск ярлыком «Лимиты Claude» в папке Startup"
metadata:
  node_type: memory
  type: project
  originSessionId: 3381c894-1f85-495d-903f-a4cbfcbe648b
  modified: 2026-09-25T19:43:37.779Z
---

22.09.2026 сделан виджет (Python/tkinter, pythonw): плашка в правом нижнем углу над панелью задач, поверх окон; полоски «Сессия 5 ч» и «Неделя» с % и временем сброса, обновление раз в 3 мин. Данные — `GET https://api.anthropic.com/api/oauth/usage` (заголовок `anthropic-beta: oauth-2025-04-20`) с токеном из `~/.claude/.credentials.json` → поля `five_hour` / `seven_day` (`utilization`, `resets_at`). Пользователь хотела только лимиты Claude (Apify/Bright Data/Trends MCP — не нужно).

25.09.2026 добавлена строка сверху «ЦП · Память · Диск · Сеть» в %, как в Диспетчере задач, раз в 2 с (класс SysLoad):
счётчики Windows PDH по английским именам (PdhAddEnglishCounterW) — `% Processor Utility`, `PhysicalDisk % Idle Time`,
`Network Interface Bytes Total/sec ÷ Current Bandwidth`; память — GlobalMemoryStatusEx. psutil в C:\Python314 нет — не нужен.

Автозапуск: ярлык `Лимиты Claude.lnk` в `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup` (удалить ярлык = выключить).

Грабли: экран 2880×1800 с масштабом 200% — размеры умножаются на `winfo_fpixels("1i")/96`; `-alpha` делает окно layered, и обычный снимок экрана его не видит (убрано); topmost переустанавливается раз в 5 с через SetWindowPos.

14.10.2026 (её «постоянно передвигаю, неудобно»): виджет прицеплен к окну Claude Desktop — полоса 620×28 в строке
заголовка справа перед кнопками окна (find_claude: Claude.exe из WindowsApps\…\app; окно-«хозяин» через GWLP_HWNDPARENT,
без topmost; свёрнут Claude — прячется; нет Claude — прежняя карточка в углу). Сдвинуть мышкой — место запоминается
в widget_pos.json; правая кнопка → «Вернуть полосу на место». Встроенного постоянного индикатора лимитов в Desktop нет
(только Settings → Usage).
