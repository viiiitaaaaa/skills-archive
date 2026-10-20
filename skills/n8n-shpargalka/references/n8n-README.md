# n8n — оркестратор (этап 4)

n8n связывает Shopify с тем, что снаружи. Правило разделения простое:
**действие целиком внутри Shopify — это Flow, вышло наружу — это n8n.**

Установлен глобально через npm, версия 2.36.7, панель — http://localhost:5678.
База — SQLite в `C:\Users\User\.n8n`.

## Запуск

```powershell
.\n8n\start-n8n.ps1
```

Скрипт подставляет `SHOPIFY_CLIENT_ID` и `SHOPIFY_CLIENT_SECRET` из файла с
ключами на рабочем столе и поднимает n8n. **Ключи в репозиторий не попадают** —
воркфлоу читают их как `{{ $env.SHOPIFY_CLIENT_ID }}`.

Голая команда `n8n start` тоже работает, но воркфлоу без переменных окружения
не получат токен.

## Проверка, что всё живо

```powershell
.\n8n\selftest.ps1
```

Гоняет `00-selftest-token.json`: выпускает токен и спрашивает у Shopify имя
магазина и число товаров. Ожидаемый ответ — `ARTMELLIO`, `PLN`, `131`.
Прогнано 26.08.2026 — связь есть.

## Как решена проблема токена

Токен Admin API выпускается по client credentials и **живёт 24 часа**. Для
круглосуточного оркестратора это означало бы остановку через сутки.

Вместо постоянного токена (его пришлось бы заводить через админку за
Cloudflare) **каждый воркфлоу первым шагом сам выпускает свежий токен** —
узел «Выпустить токен» POST-ит на `/admin/oauth/access_token`. Дальше токен
подставляется в заголовок `X-Shopify-Access-Token` через
`{{ $('Выпустить токен').item.json.access_token }}`.

Плюс: браузер не нужен вообще, ничего не протухает.
Минус: один лишний запрос на запуск — на наших объёмах не имеет значения.

**Узел Shopify из коробки не используем** — он требует OAuth, а OAuth открывает
системный Chrome, который для этого магазина запрещён. Везде обычный HTTP Request.

## Воркфлоу

Все три импортированы и **выключены** — включать осознанно.

| Файл | Что делает |
|---|---|
| `exports/05-error-alert.json` | **Error Workflow**: срабатывает, когда падает любой другой воркфлоу (у всех в `settings.errorWorkflow` стоит `artmErrAlert001`) → уведомление в панель (`kind: error`) и сообщение в Telegram с названием сценария из `registry.json`, узлом и текстом ошибки. Ручные запуски из редактора сюда не попадают — только боевые |
| `exports/10-products-update-gaps.json` | вебхук `products/update` → смотрит `artmellio.style/material/room/palette` → вешает тег `needs:data`, если чего-то нет, и снимает его, когда дозаполнили |
| `exports/20-daily-catalog-report.json` | каждое утро в 9 (и кнопка) → считает по каталогу, сколько карточек без метаполей, без картинки, без `pairs_with` → **полная таблица** по одному товару на строку уходит в панель `POST /api/report` → `data/reports/catalog-gaps-<дата>.xlsx` и `.csv`; по расписанию ещё и короткая сводка в Telegram (кнопка в Telegram не пишет) |
| `exports/30-collections-update.json` | вебхук `collections/update` → опубликованная коллекция без баннеров помечается как требующая внимания |
| `exports/40-orders-recent.json` | кнопка в панели → 20 последних заказов по-русски: номер, дата, сумма, оплата, доставка, страна, позиции |
| `exports/50-orders-create.json` | вебхук `orders/create` → короткое уведомление → две ветки: `POST 127.0.0.1:8787/api/notify` в панель и `sendMessage` в Telegram (если есть ключи) |
| `exports/55-telegram-test.json` | кнопка в панели → тестовое сообщение от бота; без ключей отвечает «связь: нет» и что поправить |
| `exports/70-markup-tag-all.json` | кнопка в панели → весь каталог → сверка тега `needs:data` с метаполями: пусто → tagsAdd, всё есть → tagsRemove, иначе ничего. Повторы при ECONNRESET/429, пауза каждые 20 мутаций |
| `exports/80-supplier-check.json` | каждый день в 9:30 (и кнопка) → **Execute Command** `py -3.13 scripts/suppliers/check_suppliers.py --json` → скрипт читает My Products в Dsers через профиль Dolphin «Shopify», ставит метаполя `artmellio.supplier_check` / `supplier_cost` / `supplier_checked_at`, тег `supplier:unavailable` → таблица в `data/reports/suppliers-<дата>.xlsx`, уведомление в панель, в Telegram — если что-то изменилось. **`--auto-draft`** (решение владелицы 04.09.2026): недоступные активные → черновик с тегом `supplier:auto-drafted`, вернувшиеся с этим тегом → снова активны; ручные черновики без тега не трогает. Идёт 10–15 минут |
| `exports/85-supplier-draft.json` | кнопка в панели (с подтверждением) → `check_suppliers.py --draft-unavailable` → активные товары со статусом `unavailable` по последнему снимку `data/suppliers/latest.json` переводятся в черновик |
| `exports/90-reshoot-run.json` | кнопка в панели → Execute Command `scripts/comfy/reshoot_products.py --limit 5 --json` → до 5 товаров с тегом `reshoot` пересъёмка в Comfy Cloud без браузера (Qwen-Image-Edit, рецепт product-scenes), новое фото первым в карточке, `content_status = photo_ready`, тег `reshoot:done`. Ключи Comfy — `comfy cloud.txt` рядом с ключами Shopify, см. panel/README |
| `exports/95-reshoot-queue.json` | кнопка в панели → `reshoot_products.py --list --json` → очередь пересъёмки и сцена для каждого |
| `exports/60-markup-queue.json` | кнопка в панели → весь каталог (active + draft) → первые 20 товаров с пустыми `artmellio.style/material/room/palette`, ссылки в админку, счётчик «осталось / готово» |

**03.09.2026:** у `00`, `20`, `40` есть узел «Кнопка в панели» (вебхук
`panel/<имя>`, `responseMode: lastNode`), они и `50` включены. `20` теперь
читает весь каталог постранично через Code-узел с `this.helpers.httpRequest`.
Панель — `panel/README.md`.

Первый и третий закрывают ровно то, чего **Flow не умеет**: у него нет триггера
«товар изменён» и нет триггеров по коллекциям вообще.

### Почему теги, а не удаление

`needs:data` только добавляется и снимается. **Остальные теги не трогать** — на
`room:*` держатся автоматические коллекции, а условие по списочному метаполю
Shopify не принимает.

## Telegram-бот для уведомлений

Ключи бота, как и ключи Shopify, **вне репозитория**:
`C:\Users\User\Desktop\Новая папка (4)\telegram bot.txt` — строка 1 токен от
@BotFather, строка 2 `chat_id`. `start-n8n.ps1` читает файл и отдаёт воркфлоу
`TELEGRAM_BOT_TOKEN` и `TELEGRAM_CHAT_ID`; файла нет — ветка «В Telegram»
молча пропускается, уведомления идут только в панель.

Первичная настройка один раз:

1. В Telegram у @BotFather: `/newbot`, имя, юзернейм с `bot` на конце → токен.
2. Токен первой строкой в `telegram bot.txt`.
3. Открыть своего бота, нажать Start (иначе Telegram не отдаёт chat_id).
4. `python scripts\telegram\setup_telegram.py` — найдёт chat_id, допишет в файл,
   пришлёт тестовое сообщение.
5. Перезапустить `.\n8n\start-n8n.ps1`, в панели нажать «Проверить Telegram».
6. Сбои сценариев приходят в тот же чат сами — через Error Workflow
   `05-error-alert.json`, отдельное окно для этого не нужно.

Библиотек не нужно: Bot API — обычный HTTPS, из n8n это HTTP Request на
`https://api.telegram.org/bot<токен>/sendMessage`. Текст заказа собирается в
Code-узле с экранированием `<`, `>`, `&` — иначе Telegram отвечает 400 на
названии товара с угловыми скобками.

## Чтобы вебхуки заработали: туннель Cloudflare

n8n стоит локально, Shopify до `localhost` не достучится. Решение без
денег, аккаунта и домена — быстрый туннель Cloudflare (`cloudflared`,
ставится `winget install --id Cloudflare.cloudflared -e`):

```powershell
.\n8n\start-tunnel.ps1                       # только orders/create
.\n8n\start-tunnel.ps1 -Topics ORDERS_CREATE,PRODUCTS_UPDATE,COLLECTIONS_UPDATE
```

Скрипт поднимает туннель, ловит выданный адрес вида
`https://xxx.trycloudflare.com` и **сам перерегистрирует вебхуки Shopify**
на него через `scripts/webhooks/register_shopify_webhooks.py`. Адрес
меняется при каждом запуске — поэтому перерегистрация автоматическая.
Туннель живёт, пока открыто окно и включён компьютер; заказы при этом не
теряются, они в Shopify.

Регистрировать только темы, чьи воркфлоу **включены**: на выключенный n8n
отвечает 404, и Shopify после серии неудач удаляет подписку. С 03.09.2026
включены `orders/create` и `products/update` (по умолчанию в скрипте);
`collections/update` выключен.

`10-products-update-gaps` **идемпотентен**: меняет тег только если он не в
нужном состоянии (`action: add | remove | none`). Иначе tagsAdd сам бы
вызывал `products/update`, и получился бы круг.

Посмотреть / снести вебхуки:

```powershell
python scripts\webhooks\register_shopify_webhooks.py --list
python scripts\webhooks\register_shopify_webhooks.py --delete-all
```

Проверено 03.09.2026: пример заказа через публичный адрес дошёл до панели.
VPS или n8n Cloud — когда появятся регулярные заказы (см.
`docs/operations-system-map.md`).

## Версионирование

Экспорт каждого рабочего воркфлоу класть сюда и коммитить — иначе они живут
только в локальной базе и теряются вместе с ней.

```powershell
n8n export:workflow --id=<id> --output=n8n\exports\<имя>.json
n8n import:workflow --input=n8n\exports\<имя>.json
```

## Грабли, проверенные на практике

- **Импорт падает** с `NOT NULL constraint failed: workflow_entity.id`, если в
  JSON нет поля `id`. У наших оно проставлено.
- **`access to env vars denied`** — в n8n 2.x доступ к переменным окружения из
  узлов закрыт по умолчанию. Лечится `N8N_BLOCK_ENV_ACCESS_IN_NODE=false`,
  это уже стоит в `start-n8n.ps1` и `selftest.ps1`.
- **`n8n execute` умеет запускать только воркфлоу с узлом Execute Workflow
  Trigger.** Расписание и вебхуки из командной строки не гоняются — поэтому
  дымовой тест сделан отдельным воркфлоу с нужным триггером.
- **`read ECONNRESET` в долгом Code-узле** — Shopify рвёт соединение
  посреди сотен запросов. В `this.helpers.httpRequest` встроенных повторов
  нет, оборачивать в цикл с паузой (см. `70-markup-tag-all`).
- **`connect EACCES ::1:8787`** из HTTP Request на `localhost` — n8n берёт
  IPv6, а локальный сервер слушает IPv4. Писать `127.0.0.1`.
- **После `publish:workflow` n8n нужно перезапустить**, и первую минуту он
  отдаёт 503 «Database is not ready» — ждать строку «Editor is now accessible».
- **Порт брокера 5679 занят**, если n8n уже запущен: для разовой прогонки
  поднимать `N8N_RUNNERS_BROKER_PORT` и `N8N_PORT`.
- **Execute Command в n8n 2.x выключен по умолчанию** (`NODES_EXCLUDE` содержит
  `n8n-nodes-base.executeCommand`). Воркфлоу с этим узлом импортируется, но при
  включении молча падает — панель показывает «Сбой… сценарий не смог включиться»,
  а вебхук отвечает 404. Лечится `NODES_EXCLUDE='[]'` в `start-n8n.ps1` (уже стоит).
- **`require('fs')` в Code-узле** закрыт по умолчанию — `NODE_FUNCTION_ALLOW_BUILTIN=fs`
  в `start-n8n.ps1`; без него сценарий сбоя берёт имя воркфлоу из n8n, а не из реестра.
- **Панель ждёт ответ вебхука ограниченное время** (`RUN_TIMEOUT` в `panel/server.py`,
  1500 с). Если сценарий дольше — панель напишет «не ответил», но воркфлоу
  доработает, результат будет в «Истории» и в уведомлениях.
- Node на машине **24**, n8n официально поддерживает 20 и 22. Запускается и
  работает, но в логе висит предупреждение про запуск вне контейнера.
- Ошибка `Error fetching from Strapi API (api.n8n.io)` в логе старта —
  это реестр MCP-серверов не достучался наружу. На работу не влияет.

## Что дальше

- Очередь пересъёмки фото: метка «нужна пересъёмка» → задача в ComfyUI →
  готовая картинка обратно в Shopify. Это уже этап 5.
- В процессе Flow «Email notification for approved products» до сих пор стоит
  заглушка `staff@example.com`.
