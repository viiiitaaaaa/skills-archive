---
name: gemini-po-klyuchu
description: Что даёт ключ Gemini (AI Studio): только быстрые текстовые модели; картинки по ключу — 429, нужна оплата; подписка Pro — только сайт/приложение
metadata:
  type: project
---

Проверено 15.10.2026 скриптами `C:\Users\User\komputer\gemini\gemini_modeli.py` (список и проверка моделей,
`python gemini_modeli.py <модель> ...`) и `gemini_kartinka.py <модель> <файл.png>`. Ключ — переменная Windows
GEMINI_API_KEY (User), скрипты читают её через winreg и не печатают.

- Отвечают: gemini-3.8-flash, gemini-3.5-flash-lite, gemini-flash-lite-latest, gemini-flash-latest.
- gemini-2.5-flash — 404 (закрыта для новых); gemini-pro-latest, gemini-3.1-pro-preview — 429.
- Картинки: все 4 модели (gemini-3.1-flash-image, gemini-nano-banana-2.1, gemini-2.5-flash-image,
  gemini-3.1-flash-lite-image) — 429: бесплатных картинок по ключу нет.
- У неё платная Google AI Pro — НЕ называть Gemini бесплатным; Pro работает только на сайте/в приложении и NotebookLM.

**Не доделано:** она выбрала цель «картинки» — не работает. Предложено: картинки руками в Gemini (Pro),
ComfyUI Cloud (скиллы product-scenes, site-mockups) или оплата API. Ждём её решения; правило «зачем Gemini во
вкладках» в CLAUDE.md записать после решения. Текстовые flash можно было бы дать вместо [[hermes-limit-3-nedeli]] — только по её слову.
Старый ключ, попавший в чат, она удаляет в AI Studio (в её «Мои дела»). Подробнее — старая память gemini-cli-otklyuchen-antigravity.
