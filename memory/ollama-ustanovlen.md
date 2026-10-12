---
name: ollama-ustanovlen
description: "09.10.2026 по её просьбе установлен Ollama 0.40.2 (локальные нейросети), сервер 127.0.0.1:11434; моделей пока нет, на C: ~13 ГБ"
metadata:
  node_type: memory
  type: project
  originSessionId: 845a11c9-6dda-497f-bdbd-bf8282b86758
  modified: 2026-10-09T14:24:27.611Z
---

09.10.2026 она дала команду `irm https://ollama.com/install.ps1 | iex` — скрипт прочитан (качает OllamaSetup.exe с ollama.com,
проверяет подпись Ollama Inc.) и запущен. Стоит в %LOCALAPPDATA%\Programs\Ollama, сервер http://127.0.0.1:11434, стартует с Windows.
Моделей не скачано; на C: свободно ~13 ГБ — модели 2–10 ГБ, класть в OLLAMA_MODELS на другой диск, если место кончается.

09.10 поставлен Hermes Desktop (`ollama launch hermes-desktop`): агент в %LOCALAPPDATA%\hermes, модель gpt-oss:120b-cloud
(облако Ollama, её аккаунт, бесплатный тариф — платить не нужно, ссылку Stripe не оплачивать). Грабли: обрыв SSL к GitHub при
установке — докачать `git -C %LOCALAPPDATA%\hermes\hermes-agent fetch` + `reset --hard origin/main`; «binary not found on PATH» —
окно со старым PATH, перечитать PATH из реестра; без меню запускать `--yes --model <модель>`.

**How to apply:** локальная модель — запасной вариант, когда кончился лимит Claude, и для данных 🟡/🔴 (не уходят в облако) —
см. [[dannye-komu-mozhno]].
