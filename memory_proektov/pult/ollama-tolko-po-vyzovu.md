---
name: ollama-tolko-po-vyzovu
description: "Ollama (Hermes, ollama launch claude, любые её модели) — только по её прямому вызову; в заданиях вкладкам Hermes не предлагать"
metadata:
  node_type: memory
  type: feedback
  originSessionId: d1ccf544-efd6-41b5-a871-3d2edbded42f
  modified: 2026-10-25T19:40:34.629Z
---

Ollama не вызывать и не вписывать в задания вкладкам («отдай Hermes»), пока она сама не попросит. Её вызов — подхватить.

**Why:** 25.10.2026 её слово: «у меня там очень мало лимитов в ламе… только как подстраховщик… если будешь бездумно использовать — когда потребуется важное, их не будет, и придётся на ерунду тратить твои лимиты».
**How to apply:** правило внесено в `~\.claude\CLAUDE.md` (строка про Ollama) и в скилл hermes (раздел «ГЛАВНОЕ с 25.10»). Скрипты knigi_kupleno\hermes_*.py запускать только по её слову.
