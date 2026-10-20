---
name: notfair-gde-nuzhen
description: "NotFair (скиллы seo-/ads- из notfair-plugin, поставлены 20.10.2026) — подключать только где нужен (реклама), остальное делать своими силами"
metadata:
  node_type: memory
  type: project
  originSessionId: ce2476cd-94b0-4cdd-9675-4eca39ac4efa
  modified: 2026-10-20T19:31:00.745Z
---

Её решение 20.10.2026: «где он нужен, мы его ставим, где не нужен, мы обходимся своими силами». Делиться данными с NotFair она не против.

- SEO (seo-analysis, seo-page, seo-content-planner) — без NotFair: прямой путь к Google Search Console через gcloud (`notfair-common\seo-shared\preamble.md`, `seo-analysis\references\gsc_setup.md`), по ссылке и по выгрузке — без входа. Яндекса у NotFair нет — Вебмастер и Директ (скилл yandex-direct) делаем сами.
- Реклама (ads-*) — NotFair MCP подключать, когда она запустит рекламу в Google/Meta/TikTok/LinkedIn: у них есть разрешения площадок на чтение и правку кабинетов. До этого — разбор выгрузок.

**Why:** не платить посреднику там, где Google/Яндекс дают доступ напрямую; посредник — только где без него долго (developer token Google Ads, проверка приложения Meta).
**How to apply:** подключение NotFair MCP — новое подключение, перед ним сказать ей, какие данные уйдут (🟡), и войти она должна сама. Общие справочники — `C:\Users\User\.claude\notfair-common` (в архив идут через sync_skills.ps1).
