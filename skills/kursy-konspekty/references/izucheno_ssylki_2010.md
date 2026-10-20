# Изученные ссылки из принятых новостей — 20.10.2026

Ссылки из постов, которые она приняла к сведению (notes.json, скилл `kursy-konspekty`). Помощники открыли каждую;
пересказ чужого — «пишут», не проверенный факт. Код GitHub только прочитан — ничего не ставили.
Вердикт кода: 🟢 безопасно, 🟡 с оговорками, 🔴 опасно.

## Агенты и обвязка

- **Статья Anthropic про устройство обвязки для долгих задач агента: отдельный проверяющий агент, критерии «готово», управление контекстом.** Для нас: Для Пульта: проверяющая вкладка с критериями «готово» и порогом; проверять, нужны ли усложнения. Приёмы: Генератор и оценщик отдельно: сам себя агент хвалит; Критерии с порогом: ниже одного — задача не принята; примеры оценок для калибровки; Три агента: планировщик, исполнитель, проверяющий; общение через файлы. — https://www.anthropic.com/engineering/harness-design-long-running-apps (пост projplus/4939)

## Курс Claude Code для новичков

- **Docker-контейнер с заданиями курса «Claude Code для непрограммистов»: VS Code в браузере, Claude Code, 20 скиллов и 33 демо-проекта. Работает на моделях GLM через z.ai.** Для нас: Можно подсмотреть список скиллов и демо-проектов курса для новичков. Ставить целиком не нужно: у нас уже свои скиллы и Claude Code. Приёмы: Запуск: .env с PASSWORD и GLM_API_KEY, затем ./run.sh, вход на localhost:8080; Внутри: LibreOffice, Playwright, Pandoc, Tesseract OCR, FFmpeg, pandas; docker compose down -v удаляет работу студента. Код: 🟡 Запросы идут на z.ai (модели GLM) с вашим ключом; ставит много программ; скилы сторонние, у каждого своя лицензия. — https://github.com/miolamio/cc-for-non-coders-dev-container (пост aiwizards/469)

## Изучено раньше (07–14.10), итог из прошлых разборов

- **** — https://vercel.com/academy/build-ai-agent-harness (пост vibecoding_tg/3738)
- **** — https://www.youtube.com/playlist?list=PLSN0qpDfUvTM (пост vibecoding_tg/3833)
- **** — https://cs329z.stanford.edu/ (пост vibecoding_tg/3833)

## Ещё не изучены

- https://github.com/walkinglabs/learn-harness-engineering — пост projplus/4939 — курс/видео — позже: Бесплатный курс из 14 лекций и 8 проектов о том, как строить «обвязку» вокруг ИИ-агента (инструкции, состояние, проверка, границы задачи, жизненный цикл сессии). Целиком не проходи
- http://z.ai/ — пост aiwizards/469 — курс/видео — позже: Среда с заданиями курса «Claude Code для не программистов»; это учебная платформа, не проходила.
- https://cmu-agents-ru.gitverse.site — пост vibecoding_community/235381 — курс/видео — позже: Курс CMU по ИИ-агентам с русской озвучкой; не проходила.
- https://docs.google.com/presentation/d/1NkPzpuSQt6Esbnr2-EnxM9007TL6ebSPFwITyVY-QxU/edit?slide=id.g38439ee0243_0_111#slide=id.g38439ee0243_0_111 — пост max_about_ai/100 — курс/видео — позже: Презентация из курса Stanford CS146S про код-ревью; часть курса.
- https://drive.google.com/file/d/1MZ0Qx68Vzw4x5x_XcV8XiPLp7fFDe1LJ/view — пост max_about_ai/100 — курс/видео — позже: Файл design_doc_template.md (шаблон дизайн-документа) из курса Stanford; требует входа, содержимое не видно.
- https://themodernsoftware.dev/ — пост max_about_ai/100 — курс/видео — позже: Сайт курса Stanford CS146S осени 2026: разработка софта с ИИ-агентами (MCP, скиллы, spec-driven, software factory). Курс не проходила.
- https://walkinglabs.github.io/learn-harness-engineering/en/ — пост PushEnter/13549 — курс/видео — позже: Бесплатный курс learn-harness-engineering про настройку Claude Code и Codex; не проходила.
- https://www.automatica.io/courses/claude-code — пост aiwizards/469 — курс/видео — позже: Страница курса «Claude Code для не программистов»; не проходила.
- https://www.cmu-agents.com/ — пост vibecoding_tg/3833 — курс/видео — позже: Университетский курс CMU по разработке ИИ-агентов; не проходила.
- https://youtu.be/072eNztI06k?si=l6gOtmnE8VN_aAAF — пост vibecoding_tg/3700 — курс/видео — позже: Бесплатный 30-минутный курс про память ИИ-агентов
