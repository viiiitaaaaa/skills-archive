---
name: trends-mcp-trend-radar
description: "Trends MCP (trendsmcp.ai) для trend-radar — ключ в .env, клиент src/clients/trendsmcp_client.py готов, бесплатно 100 запросов/мес и 90 дней истории"
metadata: 
  node_type: memory
  type: project
  originSessionId: 3381c894-1f85-495d-903f-a4cbfcbe648b
  modified: 2026-09-22T14:18:16.059Z
---

Trends MCP (trendsmcp.ai, кабинет trendsmcp.ai/account) — сторонний сервис трендов: Google Search/Shopping/Images, YouTube, TikTok (хэштеги), Amazon, Reddit (подписчики сабреддитов), live-топы (TikTok Trending, Amazon Best Sellers и др.). Ключ `TRENDSMCP_API_KEY` лежит в `.env` fashion-trend-radar (на 22.09.2026 ключ tmcp_live_… тот же, что пользователь прислала повторно).

Клиент `src/clients/trendsmcp_client.py` ведёт журнал расхода `data/logs/trendsmcp_usage.csv` и стоп на 100/мес; сырые ответы в `data/raw/trendsmcp/`. На 22.09 потрачен 1 запрос (time_series google search «roll neck sweater»). 22.09 исправлен `growth()`: поле `percent_growth`, окна 7D/30D/3M/12M… Скрипты радара клиент пока не вызывают. Ответ приходит как `{"statusCode","body": "<JSON-строка>","note"}` — body надо парсить отдельно.

**Сверка 22.09.2026** (`compare_trendsmcp.py`, отчёт в data/reports/): google search у trendsmcp почти совпадает с нашим Google Trends — корреляция 0.99 (roll neck sweater), 0.94 (plaid skirt), 0.82 (faux fur coat; у мелких запросов шаг грубый: 44/56/67). Грабля: trendsmcp подписывает неделю её **концом** (суббота), Google — **началом** (воскресенье), поэтому сдвиг −6 дней. Со сдвигом +1 выходило ложное отставание на неделю. После сверки потрачено 3/100.

**Подключено в радар 22.09.2026:** `run_trendsmcp.py` (ручной запуск, кэш 7 дней, проверка квоты) → `data/processed/trendsmcp.csv` → `candidate_matrix.build_matrix(trendsmcp=...)`: check_tiktok / check_amazon засчитываются также при росте ≥15% (MIN_YOY) «последний период к предыдущему». Грабли: Amazon у сервиса **помесячный** (4 точки + объём поисков/мес), TikTok **подневный** за 30 дней и только для крупных хэштегов (plaidskirt, tennisskirt, sweaterdress → no_data; falloutfit есть). Ответ no_data приходит с внутренним statusCode 404 и квоту не тратит. 22.09 полный прогон по 22 кандидатам: квота 22/100 (действует до конца сентября), Amazon-данные есть у 17, TikTok только у fall outfit inspo. Решения радара не поменялись (TEST — только roll neck sweater; у fall outfit inspo +1 проверка, всё равно REJECT). Ценность сервиса — объём поисков Amazon в месяц, а не голоса. Копия таблицы до подключения: data/reports/radar_candidates_before_trendsmcp.csv.

**Why:** закрывает TikTok/Amazon/Reddit без своих API-ключей (Etsy забанен, Reddit не одобрен). Но бесплатно только 90 дней истории, а радару нужно 2 года (это тариф Pro), и источник данных сервис не раскрывает.
**How to apply:** каждый запрос тратит квоту — запускать только по команде ([[trend-radar-bez-avtozapuska]]), сначала сверять с нашим Google Trends. Связано с [[etsy-api-trend-radar]], [[reddit-api-registration]], [[fashion-trend-radar-parsing]].
