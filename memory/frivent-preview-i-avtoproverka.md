---
name: frivent-preview-i-avtoproverka
description: Публичная ссылка на сайт Frivent без входа в Claude (GitHub Pages) и автопроверка багов сайта — с 12.10.2026
metadata:
  type: project
---
12.10 по её просьбе («ссылку, чтобы любой открыл на телефоне без входа в Claude») — https://viiiitaaaaa.github.io/frivent-preview/
(открытый репозиторий viiiitaaaaa/frivent-preview, только готовые страницы, noindex). Обновление: `python site/build.py` →
`powershell -File site/publish_preview.ps1`. Её «устала сама искать баги» → после правок сайта прогонять `python site/qa_site.py
<адрес> site` (все страницы × 3 ширины) и смотреть скрины телефона, не ждать её скринов. Агент design-review (OneRedOak) +
Playwright MCP установлены 12.10, заработают после перезапуска.
**Why:** она хочет показывать сайт людям и не искать баги вручную.
**How to apply:** после каждой правки сайта — build → publish_preview → qa_site; см. [[lead-engine-proekt]], [[sessiya-10-10-sayt-frivent]].

**С 12.10 (вечер):** сайт для людей — https://frivent-site.frivent-dom.workers.dev (Cloudflare, её аккаунт), выкладка site/deploy_cf.ps1; GitHub-превью выключено и закрыто (её «скрыть мой аккаунт, не отдавать код»).
