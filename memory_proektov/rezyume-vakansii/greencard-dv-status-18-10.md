---
name: greencard-dv-status-18-10
description: "Лотерея грин-карты — на 22.10.2026: суд велел открыть DV-2027 до 1.11 (обжалуют); сторож greencard-storozh пишет в бот; greencard.html обновлён"
metadata:
  node_type: memory
  type: project
  originSessionId: 5fdd0b86-6051-4293-83ea-f94cee8e30da
  modified: 2026-10-22T19:18:33.286Z
---

18.10.2026 она попросила подготовить участие в лотерее Green Card → rezyume-vakansii\greencard.html (чеклист, фото + проверка файла, поля DS-5501, источники).

22.10.2026 (сверено с первоисточниками): дело Red Eagle Law v. Rubio (S.D. Cal., судья Ohta), поправка от 14.10 — объявить до 29.10.2026, открыть приём DV-2027 не позже 1.11.2026 (30 дней), результаты до 3.12.2026; правительство подало апелляцию и просит остановить решение. DV-2028 — дат нет. Правило FR 2026-04737: скан паспорта JPEG до 5 МБ, не PDF. Фото DV — ровно 600×600, до 240 КБ. Собеседование для живущих в России — Варшава. Исследование Perplexity — greencard_perplexity_2026-10-22.md.

Сторож (её просьба 22.10): rezyume-vakansii\greencard_storozh (свой приватный репозиторий viiiitaaaaa/greencard-storozh; в .gitignore родителя). Worker greencard-storozh (Cloudflare, cron ежедневно, проверяет сам, если 72 ч никто не запускал): Federal Register (+ ранние публикации) и GDELT; суть по-русски — Workers AI, без Claude. ПК: pk_pomoshnik.py, Планировщик «Сторож грин-карты» раз в 3 дня в 10:00 (с догоном) — Google News site:travel.state.gov / dvprogram.state.gov + новости → POST /run. Пишет в @adocs657412bot (секреты BOT_TOKEN, OWNER_ID, KEY в Cloudflare; run.key на ПК). Тест без отправки: `python pk_pomoshnik.py --test`.
22.10 добавлено по её слову: канал юриста t.me/aya_baltabek (открытый просмотр, посты про лотерею) и чаты American_Pathway, teachBK — через своё окно Telegram Web сторожа (chaty.py, Playwright, профиль tg_profil в .gitignore; читает как tg_web_reader.js). my.telegram.org для неё закрыт навсегда (её слово 22.10 — не предлагать). Копировать вход из её Chrome запрещает защита Claude Code. Вход по её QR сделан 22.10 — работает (первый запуск: 385 сообщений, отобрано 33). Слетит вход — снова vhod_telegram.bat. Отбор сообщений чатов — Workers AI по её профилю (PROFIL в index.js): Россия, A2, без сильного кейса, без партнёра из США, без денег на учёбу → лотерея DV, удалёнка, мошенники, советы россиянам; брак/учёба/инвест/убежище/таланты — мимо.
Сайты travel.state.gov и dvprogram.state.gov блокируют любые программы (и с ПК из России, и из облака, и headless Chrome); Google News не отвечает облаку Cloudflare (503) — поэтому часть на ПК.
**Why:** Она подаёт сама; мы готовим данные заранее и не пропускаем открытие.
**How to apply:** Пришло объявление — сверить greencard.html с инструкцией DV-2027 (есть ли Россия, формат фото/скана), по её «да» вести по полям; паспортные данные в файлы не писать. Связано: [[vakansii-prioritet-ssha]].
