---
name: github-skilly-ustanovleno-2610
description: "26.10 скиллы с GitHub — что проверено, что поставлено в skills, что в карантине; хуки чужих не ставим; своя строка состояния остаётся"
metadata:
  node_type: memory
  type: project
  originSessionId: 3d69a9be-6434-4132-8034-8aca5059d36b
  modified: 2026-10-25T22:20:46.288Z
---

Её слова: 25.10 «найди на GitHub скиллы, которые улучшают тебя, безопасные, много звёзд»; 26.10 «хуки допишем сами по примеру из хуков чужого репозитория», «оставить свою [строку состояния]», «читай все» (тексты), «ставь» №1–11.

Сделано 26.10: 26 репозиториев оценено (`komputer/skilly_github_2510.html`), 17 клонировано в `~\.claude\karantin\gh-*`, весь код прочитан (875 из 875 файлов, `skilly_polnoe_chtenie_2610.html`; сканер `proverki/skan_karantin.py`). Скрытой отправки данных нет; 🔴 — dev-browser (качает бинарник), часть Composio в awesome-claude-skills.

Поставлено в `~\.claude\skills` (с правками: без хуков, без субагентов, коммит только по её просьбе; записано в `pult/razresheniya/chuzhie.json`): context-* (6+12 из Context Engineering), security-audit (Cloudflare), self-learning и llm-council (с правкой: спрашивать/только по фразе «council this»), 5 из superpowers, 5 из agent-skills, kaizen, root-cause-tracing, planning-with-files (хуки вырезаны), book-to-skill, cangjie-skill, design-taste-frontend (звёзды taste-skill подозрительны).

Не ставили: claude-hud (у неё своя statusline.py — её слово «оставить свою»), claude-code-memory-setup (Obsidian, вторая память), SkillOpt, Vercel skills, dev-browser, awesome-claude-skills, archify (её отказ загрузки).

**Why:** хуки чужих — риск; её правила: лимит, новые скиллы только по её «да», сначала каркас сайта.
**How to apply:** новые чужие скиллы — только через карантин и чтение; не ставить хуки из чужих репо; archify в карантине нет. См. [[uchim-claude-resheniya]], [[ne-zapuskat-bez-sprosa]].

**Переписано нами 26.10 (её слово «берём, но переписываем, как будто мы написали сами»; дела 42e066fd и 518cbea8):** сканер `skan_karantin.py` (+шаблоны SkillSpector), `drift_agentov.py`, скиллы `uluchshit-skill`, `scheta-ip`, `pravila-kod-iz-knig`, `otsenka-skilla`, `proverka-claude-md`, помощники `bezopasnik` и `otladchik`, советы — `claude-code-priemy/references/sovety_tips_2610.md`. Оригиналы остаются в карантине как черновики. Не взяли: хуки/cron/сеть SkillOpt, Composio, DDD-книги, ленту уведомлений и подписи clawsec, плагин dx. Остаётся: `clawsec`-проверки Windows 10/ESU, журналы Защитника, брандмауэр (защита ПК).
