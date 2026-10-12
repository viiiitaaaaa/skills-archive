---
name: reddit-cherez-google-ai
description: Reddit напрямую недоступен (WebFetch и расширение Chrome блокируют) — смотреть обсуждения через Google AI Mode (udm=50) в Chrome
metadata:
  node_type: memory
  type: reference
  originSessionId: 918f5935-fcac-4c45-bb60-0438bdbda7cf
  modified: 2026-09-25T21:23:53.877Z
---

Reddit: WebFetch «unable to fetch», claude-in-chrome — «not allowed due to safety restrictions». Обход, который
подсказала пользователь 26.09.2026: открыть в Chrome `https://www.google.com/search?q=<запрос>+reddit&udm=50`
(режим ИИ Google/Gemini), подождать ~15 с, `get_page_text` — там пересказ веток Reddit и ссылки на них.

**How to apply:** для отзывов о сервисах/товарах сначала этот путь. Учитывать, что ИИ обобщает и подмешивает
маркетинг самой компании — отделять «реальные посты» от общих фраз и говорить пользователю, если конкретных постов нет.
