---
name: cloudflare-razbor-2610
description: "26.10 разбор «кончился лимит Cloudflare» — ни один лимит не исчерпан, гостья любви потратила ~2 ответа; lyubov-bot правлен (один KV.list)"
metadata:
  node_type: memory
  type: project
  originSessionId: 4c76a494-972b-454e-8614-f17a0f694285
  modified: 2026-10-26T11:48:27.727Z
---

26.10.2026 Вита: «на Cloudflare закончился лимит». Цифры GraphQL за 24–26.10: запросы Workers ~2500/сутки из 100 000, KV чтения ≤12 350 (doki-bot), записи ≤186, списки lyubov-bot 569 (лимит 1000), Workers AI 578 нейронов из 10 000, D1 мелочь, ошибок нет. Точный лимит, который она видела, НЕ найден — ждём снимка плашки (todo 72fd6379).
Гостья в lyubov-bot (chat 305588518, пущена 25.10) писала ~2 сообщения 25.10 10:28 UTC, нагрузка ничтожна.
Правка по её «да» 26.10: checkStale в lyubov-bot делает один KV.list вместо двух (коммит 9592c0d, версия a375a67a).

**Why:** чтобы при новом «лимит кончился» не гонять заново, а сразу спросить слово с плашки.
**How to apply:** токен wrangler в `%APPDATA%\xdg.config\.wrangler\config\default.toml`, GraphQL работает (workersInvocationsAdaptive, kvOperationsAdaptiveGroups, d1AnalyticsAdaptiveGroups, aiInferenceAdaptiveGroups); журнал запросов (observability) токену недоступен. См. [[cloudflare-limity]].
