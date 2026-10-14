---
name: plan-razbor-deshevo
description: "План 15.10.2026 — как дёшево разбирать книги: Hermes читает, NotebookLM учит, Claude редактор; ждёт её выбора"
metadata:
  node_type: memory
  type: project
  originSessionId: 2d71350b-9e08-4473-a8d0-43184d164d23
  modified: 2026-10-14T21:26:03.008Z
---

15.10.2026 сделан план `razbor_deshevo.html`: способ 1 (рекомендован, 0 ₽) — Hermes делает «карту главы» и самопроверку,
скрипт собирает конспект и схему, Claude читает только итог и делает 20–30 карточек, учёба — NotebookLM (одна книга = один блокнот).
Способ 2 — платный пакетный запрос (Batch API), ≈ $1–12 за 70 книг, только по её слову.
Причина ошибок 429 в прогоне 14.10 (81 из 144 кусков): на бесплатном Ollama Cloud, по сторонним источникам, — 1 одновременный запрос к облачной модели.

**Why:** Вита: разбор книг «очень дорого и долго».
**How to apply:** ждём её выбора способа; дальше — поправить hermes_vse.py (1 поток, повтор после 429), пробная книга. См. [[knigi-primenyat-na-praktike]], [[kuplennye-knigi]].

15.10 позже: бесплатный лимит Ollama у неё кончился (ждать ~3 недели). Предложены замены той же модели/бесплатные: Gemini Flash-Lite free (~1000 запросов/день), Cerebras gpt-oss-120b (~1 млн токенов/день, возможно нужна карта), Groq gpt-oss-120b (~200 тыс. токенов/день). Hermes переключается на другого поставщика командой `hermes model` (config: %LOCALAPPDATA%\hermes\config.yaml, сейчас provider ollama-launch). Ключи она заводит сама. Второй аккаунт Ollama — не предлагать (обход правил).

15.10: ключ Gemini лежит в knigi_kupleno\.env (в git не идёт). Скрипт gemini_vse.py (модель gemini-flash-lite-latest = gemini-3.5-flash-lite) — те же куски и задание, что hermes_vse.py, итог в pereskaz_vse; проба на Claude_Code_Полное_pdf_02 сверена — цитаты и страницы верны. Запущен на все куски, лог gemini_vse.log, табло gemini-knigi. Hermes на Gemini не переключали — ждём её решения (её личные чаты Telegram пошли бы в Google).
