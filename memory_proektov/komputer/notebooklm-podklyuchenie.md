---
name: notebooklm-podklyuchenie
description: Можно ли подключить NotebookLM (Gemini Notebook) к Claude Code — разобрано 15.10.2026, ждёт её решения
metadata:
  type: project
---

15.10.2026 Вита спросила, можно ли подключить NotebookLM (переименован в Gemini Notebook) — дёшево разбирать купленные книги.
Разобрано (ничего не ставили):
- Официального API для обычного NotebookLM нет. Есть только Gemini Notebook Enterprise API в Google Cloud (v1alpha):
  нужен платёжный аккаунт Cloud и Enterprise-лицензии (по блогам ~9 $/лицензия/мес, мин. 15); в документации — создание
  блокнотов и загрузка источников, метода «задать вопрос» не нашла. Официального MCP нет.
- Неофициальные MCP через браузер — чужой непроверенный код (только с её слова) + риск для Google-аккаунта, как с Perplexity.
- Страна: NotebookLM работает там, где Gemini API; России в списке нет. Её аккаунт gokjhfrr уже «не в той стране»
  для Antigravity ([[gemini-cli-otklyuchen-antigravity]]) — вероятно, не пустит и сюда; проверить, открывается ли у неё сайт.
- Безопасный путь: она сама грузит книгу в NotebookLM и сохраняет конспект/заметку в Google Docs, мы читаем файл с Диска.
Связано: [[perplexity-poisk]].
