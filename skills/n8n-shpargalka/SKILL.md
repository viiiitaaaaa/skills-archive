---
name: n8n-shpargalka
description: "Шпаргалка для повтора: как у нас стоял n8n (оркестратор связки ARTMELLIO, этап 4) — установка, запуск, токен Shopify, 14 цепочек, панель кнопок :8787, грабли. Сам n8n удалён 20.10.2026; копии воркфлоу и скриптов — в references\\. Используй, когда она просит «поставь n8n заново», «верни n8n», «как мы делали n8n», «автоматизация на n8n», «воркфлоу n8n», «панель кнопок». Триггеры: \"n8n\", \"н8н\", \"оркестратор\", \"воркфлоу\", \"поставить n8n заново\", \"панель сценариев\"."
---

# n8n — шпаргалка для повтора

**Состояние:** n8n и его база удалены 20.10.2026 по её слову («удаляй, сохрани как шпаргалку»).
ARTMELLIO — не её магазин, он ведётся в Claude Desktop (`decor-store-ops`). Здесь — как всё было,
чтобы поставить заново за час. Ничего не ставить без её «да».

**Правило:** действие целиком внутри Shopify → Shopify Flow. Выходит наружу (Telegram, файлы, скрипты,
другие сайты) → n8n.

## Что лежит в references\

| Файл | Что это |
|---|---|
| `exports\*.json` | 14 воркфлоу (цепочек), готовы к импорту |
| `map\*.json` | «карты» скиллов в виде схем n8n (просто картинки-схемы из пустых узлов, не работали) |
| `n8n-README.md` | полное старое описание с граблями |
| `start-n8n.ps1` | запуск: читает ключи из файла на рабочем столе, ставит переменные, `n8n start` |
| `selftest.ps1` | проверка связи с Shopify (ответ ARTMELLIO / PLN / 131) |
| `start-tunnel.ps1` | туннель Cloudflare для вебхуков Shopify + перерегистрация вебхуков |
| `panel\` | панель кнопок на http://127.0.0.1:8787: `server.py`, `index.html`, `registry.json`, `reports.py`, `start-panel.ps1`, README |

Ключей и токенов в копиях нет (проверено grep'ом 20.10.2026). Ключи лежали в
`C:\Users\User\Desktop\Новая папка (4)\` (`shopy api.txt`, `telegram bot.txt`, `comfy cloud.txt`) — их не трогали.
Скрипты, которые вызывали цепочки (`scripts\suppliers\check_suppliers.py`, `scripts\comfy\reshoot_products.py`,
`scripts\webhooks\register_shopify_webhooks.py`, `scripts\telegram\setup_telegram.py`), остались в `decor-store-ops\scripts`.
Сами папки `n8n\` и `panel\` — в git-истории `decor-store-ops` (до 20.10.2026).

## Как ставили

```powershell
npm install -g n8n@2.36.7     # npm = магазин программ для Node.js; -g = для всего компьютера
n8n start                     # редактор на http://localhost:5678
```

- База — SQLite (один файл-база) в `C:\Users\User\.n8n`.
- Node на ПК — 24, n8n официально хочет 20 или 22. Работало, но с предупреждением.
- Запускать через `start-n8n.ps1`, а не голым `n8n start` — иначе цепочки не видят ключей.
- Импорт цепочки: `n8n import:workflow --input=exports\<имя>.json`; экспорт: `n8n export:workflow --id=<id> --output=...`.
  Экспорт каждой рабочей цепочки — сразу в git, иначе живёт только в базе.

Переменные в `start-n8n.ps1` (без них не работает):
`N8N_BLOCK_ENV_ACCESS_IN_NODE=false` (узлам видно переменные), `NODES_EXCLUDE='[]'` (включает узел Execute Command),
`NODE_FUNCTION_ALLOW_BUILTIN=fs` (Code-узлу можно читать файлы), `PYTHONUTF8=1`, `N8N_DIAGNOSTICS_ENABLED=false`.

## Токен Shopify на 24 часа

Токен Admin API (ключ доступа к магазину) по client credentials живёт 24 часа. Поэтому **каждая цепочка
первым узлом «Выпустить токен» сама берёт свежий** (POST `/admin/oauth/access_token`), дальше он идёт в заголовок
`X-Shopify-Access-Token`. Готовый узел Shopify не брали — он хочет OAuth через системный Chrome. Везде HTTP Request.

## 14 цепочек

| Файл | Что делала |
|---|---|
| 00-selftest-svyaz (было 00-selftest-token) | проверка связи: токен → имя магазина, валюта, число товаров |
| 05-error-alert | упала любая цепочка → сообщение в панель и Telegram (узел, текст ошибки) |
| 10-products-update-gaps | товар изменён → нет стиля/материала/комнаты/палитры → тег `needs:data`, дозаполнили → снять |
| 20-daily-catalog-report | каждый день в 9:00 → таблица пробелов каталога (xlsx/csv) + сводка в Telegram |
| 30-collections-update | коллекция опубликована без баннеров → пометка |
| 40-orders-recent | кнопка → 20 последних заказов по-русски |
| 50-orders-create | новый заказ → уведомление в панель и Telegram |
| 55-telegram-test | кнопка → тест бота |
| 60-markup-queue | кнопка → первые 20 товаров без разметки, ссылки в админку |
| 70-markup-tag-all | кнопка → весь каталог: сверить тег `needs:data` с метаполями |
| 80-supplier-check | каждый день в 9:30 → скрипт проверяет поставщиков в Dsers, недоступные — в черновик |
| 85-supplier-draft | кнопка (с подтверждением) → недоступные по последнему снимку — в черновик |
| 90-reshoot-run | кнопка → до 5 товаров с тегом `reshoot` пересняты в Comfy Cloud |
| 95-reshoot-queue | кнопка → очередь пересъёмки |

Вебхуки Shopify (сигналы «что-то случилось») доходили через бесплатный туннель Cloudflare
(`cloudflared`, адрес `*.trycloudflare.com` меняется при каждом запуске — `start-tunnel.ps1` перерегистрирует сам).
Регистрировать только темы включённых цепочек: на выключенную n8n отвечает 404, и Shopify удаляет подписку.

## Панель кнопок :8787

`panel\start-panel.ps1` → http://127.0.0.1:8787. Чистый Python без библиотек. Читает базу n8n (только чтение),
по кнопке дёргает вебхук `panel/<имя>`, пишет журнал. Сценарии и их человеческие названия — `registry.json`.
Ждёт ответа до 1500 с (`RUN_TIMEOUT`), дольше — результат в «Истории». Окон было три: start-n8n, start-tunnel, start-panel.

## Грабли

- **`127.0.0.1`, а не `localhost`** в HTTP-узлах: n8n лезет по IPv6 и ловит `EACCES ::1:8787`.
- **503 «Database is not ready»** первую минуту после старта — ждать строку «Editor is now accessible».
- **После `n8n publish:workflow` — перезапустить n8n**, иначе не подхватит.
- `access to env vars denied` → `N8N_BLOCK_ENV_ACCESS_IN_NODE=false`.
- Execute Command выключен по умолчанию → `NODES_EXCLUDE='[]'`; без этого цепочка молча не включается.
- Импорт падает `NOT NULL constraint failed: workflow_entity.id` — в JSON нужно поле `id`.
- `n8n execute` запускает только цепочки с Execute Workflow Trigger; при работающем n8n — другие порты
  (`N8N_PORT=5691`, `N8N_RUNNERS_BROKER_PORT=5690`).
- `ECONNRESET` / 429 от Shopify в длинном Code-узле — повторять с паузой (см. 70-markup-tag-all).
- Текст в Telegram экранировать `< > &`, иначе ошибка 400.
- `Error fetching from Strapi API` в логе старта — не мешает.

## Если ставить заново

1. Спросить её «да» (новая установка). 2. `npm install -g n8n@<версия>` (Node 22 лучше). 3. Скопировать
`start-n8n.ps1` и поправить пути. 4. Импортировать нужные цепочки из `exports\`. 5. `selftest.ps1`. 6. Включать
по одной. Для наших дел без Shopify сперва сравнить с Cloudflare Workers — там уже живут боты и не нужен включённый ПК.
