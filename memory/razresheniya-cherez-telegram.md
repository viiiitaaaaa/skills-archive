---
name: razresheniya-cherez-telegram
description: "13.10 вопросы «разрешить?» Claude Code — в Telegram через официальный канал (plugin telegram@claude-plugins-official, Bun 1.4.3); запуск «C:\\Users\\User\\Claude с Telegram.cmd»"
metadata:
  node_type: memory
  type: project
  originSessionId: e994540f-d5ab-4cfe-8186-497676e3e8a3
  modified: 2026-10-13T12:28:53.032Z
---

Её просьба 13.10: вопросы да/нет из командной строки получать в Telegram, отвечать там, а Claude Code отмечает ответ.
Сделано: Bun (winget Oven-sh.Bun), плагин telegram@claude-plugins-official (scope user), ярлык `C:\Users\User\Claude с Telegram.cmd`
(= `claude --channels plugin:telegram@claude-plugins-official`). Нужен ОТДЕЛЬНЫЙ бот от @BotFather (не «Дела» и не бот Hermes —
у одного токена может быть только один приёмник). Токен → `~/.claude/channels/telegram/.env` (TELEGRAM_BOT_TOKEN=…, 🟡 только на ПК).
13.10 создан бот **@vita_claude_ok_bot** («Claude разрешения»), токен уже в .env (getMe проверен).
**Грабля 13.10:** в Windows (уровень пользователя) задан TELEGRAM_BOT_TOKEN бота «Дела» (id 8728523381), а плагин берёт его раньше .env →
слушал @adocs657412bot, 409 ×8 и замолкал. Ярлык теперь сам подставляет ключ из .env (только в своём окне). Переменную Windows не трогать — она нужна «Делам».
Проверка «слушает ли кто бота»: getUpdates?timeout=0 — 409 = слушает, список = никто. /mcp Reconnect не поможет: окружение наследуется от окна.
**13.10 привязка сделана:** её Telegram ID 1388664660 в allowFrom, политика `allowlist` (чужим бот не выдаёт код).
Нового человека: `/telegram:access allow <ID>` или временно `policy pairing` → `pair <код>` → обратно `policy allowlist`.

**Why:** она отходит от компьютера, а работа стоит на вопросе «разрешить?».
**How to apply:** relay только для инструментов (Bash/Write/Edit), работает пока окно открыто; на Windows плагин официально не проверен —
при сбое смотреть сообщения плагина. Перезапуск сессии с флагом обрывает фоновые задачи — делать между задачами. См. [[razresheniya-ne-sprashivat]].
