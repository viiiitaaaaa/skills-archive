---
name: razresheniya-bez-voprosov
description: "27.10 её злость на вопросы «разрешить?» каждую секунду; решение — bypassPermissions в настройках вкладок пульта, ставит она сама"
metadata:
  node_type: memory
  type: feedback
  originSessionId: ae5ce611-4cdc-4452-a1b9-7eb8041e71d0
  modified: 2026-10-27T19:58:24.389Z
---

27.10.2026 её слова: «Я же тебе просила убрать эти постоянные разрешения, чтобы было как раньше. Я для кого перезапускала вкладки?», «Ты вообще в себе, чтобы я каждую секунду нажимала эти разрешения?», «Ты опять мне усугубляешь всю работу и усложняешь».

**Why:** добавленные 26–27.10 allow-правила не помогли: в режиме auto сложные команды Bash (с `&&`, `|`) и клики Chrome всё равно спрашивают; правило «разрешения разрешены целиком» (27.09) не было доведено до настроек.
**How to apply:** вкладки пульта запускаются с `--settings pult\golos\bez_voice_claude.json`; в нём `permissions.defaultMode: bypassPermissions` (deny-список общих настроек и хуки-сторожа остаются). Claude сам эти настройки менять не может — скрипт `pult\otklyucheno\bez_voprosov.py` запускает она. Новых allow-правил по одному больше не предлагать. Связано: [[pochinka-pulta-proveryat-vzhivuyu]].

27.10 23:24, её слово: «Вообще без разрешения. На все дают ответ „разрешаю“. Не спрашивать». bypassPermissions не спасал от вопросов расширения Chrome (mcp__claude-in-chrome__computer) — теперь хук `pult\hooks\razreshenie_tg.py` во вкладках пульта сам отвечает allow на любой PermissionRequest (кроме AskUserQuestion/планов). Не возвращать окна «разрешить?» без её слова.
