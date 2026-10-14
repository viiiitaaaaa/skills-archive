---
name: etsy-api-trend-radar
description: "Etsy Open API v3 для trend-radar — 22.09.2026 ключ приложения «vi» забанен (Banned), канал Etsy закрыт"
metadata: 
  node_type: memory
  type: project
  originSessionId: 3381c894-1f85-495d-903f-a4cbfcbe648b
  modified: 2026-09-22T13:44:44.513Z
---

22.09.2026 Etsy перевёл приложение «vi» (ключи `ETSY_API_KEY`, `ETSY_SHARED_SECRET` в `.env` fashion-trend-radar) в статус **Banned**. До этого был Pending Personal Approval и ответ 403 «key not active». Пользователь заранее ожидала бан.

**Why:** Etsy вручную одобряет ключи и отказывает в коммерческих/аналитических сценариях; парсить сайт в обход нельзя (антибот-защита, обход запрещён правилами).
**How to apply:** Etsy исключён из радара. Не предлагать новые заявки/новые аккаунты под тот же сценарий — это нарушает правила Etsy. Тренды площадок теперь берём через Trends MCP ([[trends-mcp-trend-radar]]). Связано с [[reddit-api-registration]], [[trend-radar-bez-avtozapuska]].
