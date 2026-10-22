---
name: harness2-wsl
description: "Harness2 (Google Research) проверен 🟢 и стоит в tools\\harness2; на Windows не идёт (fcntl) — 22.10 поставлен WSL+Ubuntu, ждёт перезагрузки"
metadata:
  node_type: memory
  type: project
  originSessionId: dae77a1e-ecc9-437e-919d-154ceb1f6bec
  modified: 2026-10-22T21:25:47.234Z
---

22.10.2026: github.com/google-research/harness2 (самоулучшение обвязки агента) проверен по proverka_chuzhogo.md — 🟢
(официальная org, 17,9k звёзд, сеть только github/npm/Vertex, ключи для демо не нужны). Копия в
`~\.claude\karantin\harness2`, установка — `C:\Users\User\tools\harness2\.venv` (Python 3.13, 44 МБ).
Демо на Windows падает: `No module named 'fcntl'` (только Linux).

Её «ставь Linux» 22.10: `wsl --install -d Ubuntu --web-download` (с правами админа) — компоненты и Ubuntu поставлены,
нужна перезагрузка. Задача ей в «Мои дела».

**Как доделать после перезагрузки:** пользователь в Ubuntu без пароля через `wsl -d Ubuntu -u root` (useradd,
sudo без пароля), в Linux — uv + Python 3.12, клон harness2 в домашнюю папку Linux (не /mnt/c — медленно),
`harness2-demo --output runs/demo --k 2`. Настоящие бенчмарки — платный Google Cloud Vertex: без её «да» не трогать.

Google Cloud 22.10: она пробовала завести оплату — отказ `OR_BACR2_59` (проверка Google, массово в сент–окт 2026,
решения нет, только поддержка Billing). Мой совет ей — не бороться, Vertex нам не нужен (прикидка $5–15 за задачу
Harness2). Берём из Harness2 приёмы для пульта (предложи правку → проверь на той же задаче → оставь лучшее; уроки
после задачи).

**Доделано 22.10 после перезагрузки:** WSL 3.0.3, дистрибутив `Ubuntu` (первое окно «имя/пароль» закрыла сама),
пользователь `vita` без пароля, sudo без пароля, по умолчанию (`/etc/wsl.conf`, systemd=true). uv + Python 3.12,
`~/harness2` (тот же коммит 1cfe254, что в карантине), демо: 2 из 2 задач ok. Диск Linux —
`%LOCALAPPDATA%\wsl\{bc9d…}\ext4.vhdx` ~1,7 ГБ. C: свободно было 12,4 → стало 7,2 ГБ.
Копия `C:\Users\User\tools\harness2` (Windows, не работает) — лишняя, удалять только по её слову.
Из Harness2 взято (22.10): агент-проверяльщик `~\.claude\agents\proverka.md` — правила его выбора ответа
(доставка → только то, что просили → сверка с источником → согласованность → годность → доделано) и записи урока
(«когда / делать», не «будь внимательна» и не цифры одной задачи; один неясный случай — «урок неясен»).
Других учебных задач в Harness2 нет: только демо (2 таблицы); бенчмарки — скачивание + платные модели.
Проверяльщик опробован 23.10 на отчёте про Linux: совпало 9 из 9 (C: на деле 7,0 ГБ, не 7,2; vhdx будет расти).
В той же вкладке 23.10 — красная метка «разрешить?» в пульте (main.js pollPerm, app.js permSess/isPerm, style.css .perm,
хук razreshenie_tg.py пишет transcript и правит сообщение бота на «ekran»); проверено на копии; ждёт перезапуска пульта
(в её делах). Описание — скилл pult, раздел «Красная метка». Не закоммичено: в тех же файлах пульта чужие правки других вкладок.
Не доделано: удалить `C:\Users\User\tools\harness2` (44 МБ) — только по её «удали».
Запуск: `wsl -d Ubuntu -- bash -lc "cd ~/harness2 && .venv/bin/harness2-demo ..."`.

23.10: карта «где учиться harness engineering» (Perplexity, глубокое исследование) — `komputer\hermes_obuchenie.html`; выжимка — kursy-konspekty/references/learn-harness-engineering.md. Статья Harness²: arXiv 2610.14224.
