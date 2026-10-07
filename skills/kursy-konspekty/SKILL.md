---
name: kursy-konspekty
description: "Конспекты бесплатных курсов, которые она приняла к сведению, — Anthropic Academy (Claude Code, субагенты, скиллы, MCP, Cowork, Claude API, AI Fluency), Vercel «обвязка ИИ-агента с нуля», CMU 11-768 «AI Agents», Stanford CS329Z «Engineering AI Agents», Gábor Békés «Data Analysis with AI» — программа, ключевые идеи простыми словами и что применяем у нас (скиллы, субагенты, проверка качества, таблицы отбора 1688, сборщики). Используй, когда спрашивают «что было в курсе», «конспект курса», «чему учит anthropic academy», «как по курсу правильно сделать субагента/скилл/проверку», и когда строим нового агента, скилл или анализ таблицы и нужен приём из курса. Триггеры: \"конспект курса\", \"что было в курсе\", \"anthropic academy\", \"claude academy\", \"курс vercel\", \"обвязка агента\", \"harness\", \"cmu агенты\", \"stanford cs329z\", \"data analysis with ai\", \"габор\", \"курсы по агентам\"."
---

# Конспекты курсов (скилл `kursy-konspekty`)

Курсы из новостей, которые она приняла к сведению, пройдены целиком 07.10.2026: тексты уроков, транскрипты видео,
слайды, задания, ключевые чтения. По файлу на курс в `references\`. Учебник микроэкономики (Oregon State, Emerson) —
**не здесь**: он уже целиком в скилле `knowledge-library` (`references\microeconomics\`).

## Оглавление

| Курс | Файл | Открыть, когда |
|---|---|---|
| Anthropic Academy — Claude Code 101, Claude Code in Action, Agent Skills, Subagents, MCP, Cowork | `references\anthropic-academy-claude-code.md` | пишем/чиним скилл, субагента, хук, CLAUDE.md, подключаем MCP |
| Anthropic Academy — Building with the Claude API, Platform 101, AI Fluency (4D), малый бизнес, команды человек+агент | `references\anthropic-academy-api-fluency.md` | промпт в Python-сборщике, оценка промпта (evals), выбор схемы workflow/agent, кэш, структурированный вывод |
| Vercel Academy — Build Your Own AI Coding Agent Harness (38 уроков) | `references\vercel-agent-harness.md` | надёжность скилла: описания инструментов, подтверждения, проверка итога, вывод скриптов, explorer/executor |
| CMU 11-768 AI Agents (Neubig, Fried) — 13 лекций слайдами, 9 видео, задания 1–2 | `references\cmu-11-768-ai-agents.md` | устройство агента: контекст, память и скиллы, планирование, deep research, безопасность браузера |
| Stanford CS329Z Engineering AI Agents — слайды 1–4, задание 1, чтения Anthropic/OpenHands | `references\stanford-cs329z.md` | оценка агентов, долгие задачи (файл прогресса), context engineering, RAG, data flywheel |
| Gábor Békés — Data Analysis with AI (5 недель + проект) | `references\gabor-data-analysis-ai.md` | таблицы отбора 1688, сверка PDD↔1688, радар, скоринг текстов через LLM, где ИИ ошибается в данных |

Ранее (29.09) записанное по CMU/Stanford — три задачи агента, тест из 4 частей, pass@k/pass^k, чек-лист «Ревизия
скилла» — в `knowledge-library\references\agents-prompts-2026-09.md`; здесь — глубже, из самих лекций.

## Главные приёмы для нас (сводка; подробности — в файлах)

ГЛАВНЫЕ_ПРИЁМЫ

## Как пользоваться

1. Найти курс в оглавлении → открыть один файл (не все сразу — каждый до ~300 строк).
2. В файле раздел «Что применяем у нас и где» — готовые привязки к нашим скиллам.
3. Новый курс из новостей → тот же формат: `references\<курс>.md` (шапка, программа, идеи, «что применяем», «не для нас»)
   + строка в оглавлении + короткая отсылка в рабочий скилл.

## Грабли при изучении курсов

- academy.claude.com — приложение на JS, но текст и транскрипт урока есть в HTML страницы урока
  (`/courses/<курс>/<урок>`); без входа открыто всё, кроме квизов и сертификатов.
- cmu-agents.com — пустая страница без JS; расписание, слайды (`/slides/lecture-NN-*.pdf`) и ссылки на видео лежат
  в JS-бандле `/assets/index-*.js`. Субтитры YouTube — `youtube-transcript-api` в отдельном venv.
- vercel.com/academy — каждый урок отдаётся в markdown по адресу урока + `.md`; curl на Windows — с `--ssl-no-revoke`.
- Слайды PDF → текст: `pypdf` (картинки слайдов не читаются, только текст).
- Скрипты скачивания — `scripts\`: `dl_academy.py <папка> <курс1> <курс2>…` (все уроки курса Academy в .md),
  `dl_pages.py <папка> <url…>` (страницы → текст, PDF как есть, raw GitHub как .md),
  `yt_pdf.py pdf <папка>` (PDF → .txt) и `yt_pdf.py yt <папка> <id видео…>` (субтитры). Для `yt_pdf.py` нужен venv
  с `youtube-transcript-api pypdf`. Сырьё класть в scratchpad, не в скилл.
