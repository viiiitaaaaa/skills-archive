---
name: harness2-wsl
description: "Harness2 (Google Research) проверен 🟢 и стоит в tools\\harness2; на Windows не идёт (fcntl) — 22.10 поставлен WSL+Ubuntu, ждёт перезагрузки"
metadata:
  node_type: memory
  type: project
  originSessionId: dae77a1e-ecc9-437e-919d-154ceb1f6bec
  modified: 2026-10-22T19:51:06.389Z
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

После перезагрузки она скажет «Linux после перезагрузки» — сразу доделывать по шагам выше, итог ей + проверить место на C:.
