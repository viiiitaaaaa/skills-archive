# Операционная панель (MVP по ТЗ «Art Melio Operations System»)

Пульт для человека, не для программиста: список сценариев, статусы, кнопка
«Запустить», история и журнал. Вся логика живёт в n8n, панель — тонкая витрина
над ним. Требования — `docs/operations-system-spec.md`, сверка с тем, что уже
есть, — `docs/operations-system-map.md`.

## Запуск

```powershell
.\n8n\start-n8n.ps1        # окно 1: оркестратор
.\panel\start-panel.ps1    # окно 2: панель на http://localhost:8787
```

Зависимостей нет — только Python из коробки.

## Как устроено

| Файл | Роль |
|---|---|
| `registry.json` | реестр сценариев: человеческое название, что делает, когда запускать, id воркфлоу, путь вебхука для кнопки |
| `server.py` | HTTP-сервер: отдаёт страницу, читает базу n8n (SQLite, только чтение), дёргает вебхуки, пишет журнал |
| `index.html` | сама страница: дашборд, карточки сценариев, история, журнал |
| `journal.jsonl` | журнал действий сотрудника, создаётся сам, в репозиторий не идёт |

Состояние сценария (включён / последний запуск / ошибки за неделю) берётся
напрямую из `~/.n8n/database.sqlite`, таблицы `workflow_entity` и
`execution_entity`. API-ключ n8n для этого не нужен.

## Кнопка «Запустить»

Кнопка бьёт в `POST http://localhost:5678/webhook/panel/<имя>`. Чтобы воркфлоу
на неё отзывался, в нём должен стоять узел Webhook «Кнопка в панели» с таким
путём и `responseMode: lastNode` — тогда результат последнего узла
возвращается на экран. Сейчас кнопка есть у:

- `00-selftest-token` → `panel/selftest`
- `20-daily-catalog-report` → `panel/daily-catalog-report`
- `40-orders-recent` → `panel/orders-recent`
- `60-markup-queue` → `panel/markup-queue` — очередь разметки: 20 товаров с
  пустыми метаполями и ссылками в админку (открывать в Dolphin)
- `70-markup-tag-all` → `panel/markup-tag-all` — разовая сверка тега
  `needs:data` по всему каталогу; `changes_data: true`, панель спрашивает
  подтверждение. Идёт 2–4 минуты, таймаут ожидания в панели 600 с.

Результат сценария панель рисует сама: массив объектов — таблицей, ссылки
`http…` — кликабельными, остальное строками «ключ: значение».

## Уведомления из n8n в панель

Панель принимает `POST http://127.0.0.1:8787/api/notify` с телом
`{"kind": "order", "title": "...", "text": "..."}` и показывает это в блоке
«Уведомления» наверху. Так работает `50-orders-create`. Адрес именно
`127.0.0.1`, не `localhost`: n8n резолвит localhost в IPv6, а панель слушает
только IPv4, получится `connect EACCES ::1:8787`.

Проверить без Shopify — послать пример заказа прямо в вебхук:

```powershell
Invoke-RestMethod -Method Post -ContentType 'application/json' `
  -Uri http://localhost:5678/webhook/shopify-orders-create `
  -Body '{"name":"#1001","total_price":"49.90","currency":"USD","line_items":[{"title":"Curved Moon Statue","quantity":1}]}'
```

Уведомления копятся в `notifications.jsonl` (в репозиторий не идёт).

**Продакшн-вебхук отвечает только у включённого воркфлоу.** Выключенный
даёт 404, панель переводит это в «сценарий выключен в n8n». Включать:

```powershell
n8n publish:workflow --id=artmDailyRep001
n8n publish:workflow --id=artmSelfTest001
```

Сценарии по событию (`products/update`, `collections/update`) кнопки не
имеют: им нужен настоящий payload от Shopify и публичный адрес.

## Отчёты в файл (таблица)

Воркфлоу присылает готовые строки на `POST http://127.0.0.1:8787/api/report`
с телом `{"name": "catalog-gaps", "title": "…", "rows": [{...}, ...]}`. Панель
пишет `data/reports/<name>-<дата>.csv` (разделитель `;`, чтобы Excel открывал
без мастера импорта) и `.xlsx` (собирается без сторонних библиотек, см.
`panel/reports.py`), отвечает ссылками `xlsx_url` / `csv_url` и добавляет строку
в «Уведомления». Блок «Отчёты» на странице показывает последние файлы со
ссылками на скачивание (`GET /reports/<файл>`). Папка `data/reports/` в
`.gitignore`: отчёты генерируются каждый день.

Сейчас так работают «Сводка пробелов в каталоге» (`catalog-gaps`) и
«Проверить поставщиков» (`suppliers`).

## Раздел «Поставщики»

Два сценария поверх `scripts/suppliers/check_suppliers.py` (запускается из n8n
узлом Execute Command, Python 3.13 — в нём playwright):

- **Проверить поставщиков** — Dsers → статус по каждому товару (в порядке /
  мало на складе / подорожал / недоступен / нет в Dsers), метаполя
  `artmellio.supplier_check`, `supplier_cost`, `supplier_checked_at`, тег
  `supplier:unavailable`, таблица в «Отчёты», Telegram при изменениях. Цены не
  трогает; **наличие меняет сама** (с 04.09.2026, по решению владелицы): недоступные
  активные → черновик с тегом `supplier:auto-drafted`, когда поставщик снова в
  наличии — обратно в «активен» и тег снимается. Ручные черновики без тега не трогает. Нужен запущенный Dolphin и живой вход в Dsers
  в профиле «Shopify» (`836461485`); если вход слетел — сценарий упадёт с
  понятным текстом, придёт уведомление о сбое.
- **Снять с продажи недоступные** — переводит в черновик активные товары со
  статусом `unavailable` по последнему снимку `data/suppliers/latest.json`.
  Это единственное место, где меняется наличие, и оно за подтверждением.

## Раздел «Контент»: пересъёмка фото через Comfy Cloud

Два сценария поверх `scripts/comfy/reshoot_products.py`: «Очередь пересъёмки»
(товары с тегом `reshoot`, какая сцена им достанется) и «Переснять фото
(5 товаров)» — генерация в Comfy Cloud по рецепту скилла product-scenes,
новый кадр становится первым фото товара, старое остаётся, метаполе
`content_status = photo_ready`, тег `reshoot` → `reshoot:done`. Кадры
дублируются в `data/reshoot/<дата>/` (в `.gitignore`).

Очередь наполняется тегом `reshoot` в админке товара — так владелица сама
решает, что переснимать.

### Ключи Comfy Cloud (один раз)

Comfy Cloud работает без браузера по firebase-токену (`scripts/comfy/comfy_cloud.py`),
но долгоживущий refresh-токен лежит только во вкладке cloud.comfy.org. Передать
его панели нужно самой владелице — Claude токены не пересылает:

1. Запустить панель (`.\panel\start-panel.ps1`).
2. Открыть https://cloud.comfy.org (войти, если просит), нажать F12 → Console.
3. Вставить и выполнить:

```js
(async()=>{const k=Object.keys(localStorage).find(x=>x.startsWith('firebase:authUser:'));
const u=JSON.parse(localStorage.getItem(k));
const r=await fetch('http://127.0.0.1:8787/api/comfy-token',{method:'POST',headers:{'Content-Type':'application/json'},
body:JSON.stringify({api_key:u.apiKey,refresh_token:u.stsTokenManager.refreshToken})});
console.log(await r.json());})();
```

Ответ `{ok: true, saved: "…comfy cloud.txt"}` — ключи легли в файл рядом с ключами
Shopify (вне репозитория). Проверка: `py -3.13 scripts\comfy\comfy_cloud.py --check`.
Повторять только если клиент начал отвечать «Firebase не обновил токен»
(выход из аккаунта Comfy или смена пароля).

## Закладка «Коллекция» (избранное → коллекция без участия Claude)

Избранное живёт в `localStorage` браузера, с сервера его не прочитать.
Поэтому в панели есть закладка-кнопка (bookmarklet): её один раз
перетаскивают на панель закладок, а потом нажимают на
`https://www.artmellio.com/pages/wishlist`. Она шлёт список в
`POST /api/wishlist-collection`, панель запускает
`scripts/content-prep/wishlist_to_collection.py`, отвечает адресом
коллекции, закладка чистит избранное и открывает коллекцию.

Панель для этого отдаёт CORS-заголовки только для доменов витрины
(`STORE_ORIGINS` в `server.py`). Слушает по-прежнему только 127.0.0.1.

Вручную то же самое:

```powershell
python scripts\content-prep\wishlist_to_collection.py data\wishlist-ids.json
```

## Как добавить сценарий

1. Сделать воркфлоу в n8n, экспортировать в `n8n/exports/`.
2. Если нужна кнопка — добавить узел Webhook с путём `panel/<имя>` и
   `responseMode: lastNode`, соединить с первым рабочим узлом.
3. Дописать запись в `registry.json`: `id`, `workflow_id`, `section`, `name`,
   `what`, `when`, `trigger`, `changes_data`, `run` (или `null`), `result_hint`.
4. Перезапустить панель. Ничего больше править не нужно.

Если `changes_data: true`, панель перед запуском спросит подтверждение.

## Чего пока нет (по ТЗ)

- ролей и входа: панель локальная, оператор берётся из имени пользователя Windows;
- разделов «Маркетинг», «Файлы» — появятся вместе с первыми сценариями в них
  («Поставщики» и «Контент» есть с 04.09.2026);
- почтовых уведомлений и базы логов вне n8n (журнал пока в jsonl). Telegram
  есть с 03.09.2026: заказ уходит боту, кнопка «Проверить Telegram» в разделе
  «Система», настройка — `n8n/README.md`, раздел «Telegram-бот». Сбои сценариев
  с 04.09.2026 тоже уходят в панель и Telegram (Error Workflow `05-error-alert`).
