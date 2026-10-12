---
name: fashion-trend-radar-parsing
description: Парсинг трендов Google Trends для нового магазина (профиль 3) через кастомный краулер Bright Data — рабочий рецепт
metadata: 
  node_type: memory
  type: project
  originSessionId: 9701aebe-fdb4-407d-83c5-2ec198924e37
  modified: 2026-09-12T16:26:15.391Z
---

Проект `C:\Users\User\fashion-trend-radar\fashion-trend-radar` — сбор трендов Google Trends по ключевым словам одежды (config/keywords.csv) для нового магазина, см. [[novyy-magazin-shopify-profil3]]. Считает score по интересу за 12 месяцев (`src/processors/scoring.py`), результат — `data/exports/trends_summary_*.csv`.

**Как это устроено (заработало 12.09.2026):** не SERP API-зона Bright Data (она только для обычного google-поиска, без произвольных URL) и не AI-конструктор напрямую — а **кастомный Web Scraper IDE краулер** `collector=c_mtyj2z3e14ur8nhivi`, собранный через диалог с AI-ассистентом Bright Data. Вызов асинхронный:
1. `POST https://api.brightdata.com/dca/trigger?collector=c_mtyj2z3e14ur8nhivi&queue_next=1` с телом `[{"url": "<trends.google.com/trends/explore?...>"}]` → возвращает `collection_id`.
2. Поллинг `GET https://api.brightdata.com/dca/dataset?id=<collection_id>` каждые ~10с, статусы `collecting` → `building` → готовый JSON (или пустое тело = 0% успеха, значит сбор провалился).
3. Успешный запуск занимает от ~45с до нескольких минут — это нормально, не зависание.

Реализовано в `src/clients/brightdata_client.py` (`trigger`/`fetch_result`/`fetch_url`, max_wait=300с).

**Главные грабли:**
- **Параметр `cat` в URL Google Trends должен быть числовым кодом категории** (например 185 = Apparel), а не текстовым словом. Наш `config/keywords.csv` использует `category`/`style` как свои лейблы для группировки — их **нельзя** подставлять в `cat` URL, иначе страница Trends не рендерит график и краулер падает по таймауту (`waiting for selector ".fe-line-chart-directive table tbody tr" failed`) — именно это было причиной всех сбоев 11-12.09. Решение: `google_trends_collector.py` больше не добавляет `cat` в URL вообще.
- Даты в JSON-ответе краулера содержат невидимые unicode-символы направления текста (U+200E/U+202A-E) вокруг текста — `normalize.py` их вырезает регэкспом перед парсингом.
- `regional_interest` в ответе краулера — это на самом деле три разных списка подряд (регионы с `interest_score`, топики без него, похожие запросы без него) — `normalize_brightdata_geo_map` берёт только записи с `interest_score`.
- Bright Data SERP-зона (`serp_api1`) в принципе не поддерживает открытие произвольных URL типа `trends.google.com/...` — только структурированный google-поиск (домен, gl/hl, tbm). Не пытаться чинить через неё для Trends.

**How to apply:** запускать `./.venv/Scripts/python.exe run.py` из `fashion-trend-radar/fashion-trend-radar` (venv уже настроен, `pip install -r requirements.txt` уже сделан). Токен Bright Data в `.env` (`BRIGHTDATA_API_TOKEN`).
