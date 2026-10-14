---
name: project-storage-pipeline
description: "storage.js/storage-upload.js — платное хранение по артикулам, колонка U недельных вкладок"
metadata: 
  node_type: memory
  type: project
  originSessionId: a3c1d32e-112f-4457-ad82-459b33a0533d
  modified: 2026-07-30T19:43:12.513Z
---

Платное хранение в разрезе SKU берётся из отчёта по номенклатурам:
https://seller.wildberries.ru/analytics-reports/paid-storage/nomenclature-report
Это **единственный** источник хранения с артикулами — в отчёте реализации оно
идёт строками с пустым артикулом.

**Порядок на сайте** (`storage.js` повторяет его через CDP): период →
«Создать Excel» → модалка с именем файла → «Сформировать» → ждать `SUCCESS` в
списке → «Скачать» → клик по размеру файла в строке нужного отчёта.

**Ключевые факты:**
- Файл приходит **zip**, внутри один xlsx. Лист «Детальная информация»,
  первая строка — заголовок отчёта, шапка во **второй** строке
  (`findIndex(r => r.includes('Артикул продавца'))`).
- Нужные колонки: «Дата», «Артикул продавца», «Сумма хранения, руб».
- Артикул совпадает с колонкой A недельных вкладок один в один.
- **Скачать по `downloadUrl` напрямую нельзя**: домен
  downloads-content-analytics отдаёт 403 и на куки домена, и на
  AuthorizeV3/Wb-Seller-Lk. Файл забирает сам Chrome через
  `Browser.setDownloadBehavior` после клика по панели «Скачать».
- Список отчётов (`/file-manager/downloads?report_types=PAID_STORAGE_NM_REPORT`
  на seller-content) заголовки принимает: `AuthorizeV3` =
  localStorage `wb-eu-passport-v2.access-token`, `Wb-Seller-Lk` =
  localStorage `wb-eu-portal.seller-token`.
- Инпут периода под React — нужен нативный сеттер + событие `input`.

Колонка U в таблице отформатирована с округлением до рубля, поэтому сумма
отображаемых ячеек расходится с точным итогом на 1–2 ₽. Сверять надо по ИТОГО.

Связано: [[project-week-tabs-formulas]], [[project-ads-expenses-pipeline]].
