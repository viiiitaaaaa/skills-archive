---
name: sessiya-13-10-hermes-knigi
description: "Сессия 13.10 — Hermes чинили и связали с Claude, 13 книг через Hermes, табло задач, бот разрешений; хвосты — привязка бота и 4 недокачанные книги"
metadata:
  node_type: memory
  type: project
  originSessionId: e994540f-d5ab-4cfe-8186-497676e3e8a3
  modified: 2026-10-13T13:16:19.605Z
---

13.10.2026:
- Hermes «waiting for the provider» = Ollama была выключена ([[ollama-ustanovlen]]). Правило: лёгкое → Hermes, сложное → Claude ([[hermes-legkie-zadachi]]), скилл `hermes`.
- 13 книг обработаны: модель Hermes пересказала, агенты Claude сверили → `knigi\novye13\`, 841 приём по 21 скиллу, панель, GitHub ([[kuplennye-knigi]]).
  Урок: hermes -z с чтением файла выдумывает — текст давать в запросе; полная сверка Opus дорогая (38% сессии) → в следующий раз Sonnet + выборочно.
- Табло задач и вторая строка статуса (сессия/неделя/ЦП/память) — [[tablo-zadach-agentov]].
- Hermes подключён ею к Telegram; бесплатный Ollama — максимум 3 одновременных, мне 2 потока.
- Бот разрешений @vita_claude_ok_bot создан, токен в .env ([[razresheniya-cherez-telegram]]).

- 16:00–16:12 бот «Дела» не получал сообщения из-за ошибки «Conflict: terminated by other getUpdates request», к боту подключилась вторая программа. Она удалила Telegram-бота Hermes, я перезапустила start_bot.bat в 16:15, ошибок больше нет. Если «Дела» молчит, первым делом смотреть case-bot\bot.log на Conflict.

**Хвосты:** (1) она перезапускает «Claude с Telegram.cmd» → pair-код → allowlist; если бот молчит — разбираться (Windows не проверен).
(2) Битые книги — закрыто, она велела забыть (см. [[kuplennye-knigi]]).
(3) Из книг ждут её «да»: поиск по смыслу в znaniya (локальная модель эмбеддингов).
