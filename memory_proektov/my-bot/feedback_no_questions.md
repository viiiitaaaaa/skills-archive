---
name: feedback-no-questions
description: User wants no confirmation questions or choice prompts during active work sessions — just execute directly.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8efa34c8-8e5f-427f-911f-321d37e7434f
  modified: 2026-07-30T00:52:36.293Z
---

Do not ask the user confirmation questions ("Запустить?", "Хотите, чтобы я...?") or present multiple-choice options while doing hands-on work (running scripts, editing files, automating the browser/sheet, etc.). Just proceed and do the task, then report the result.

**Why:** User explicitly said (twice, with increasing frustration) during a session of iterative debugging/automation on `my-bot`/`compare.js`: "больше не спрашивай меня!! просто молча делай и все" and "в этом процессе, вообще и за сегодня не задавай мне вопросы и выбор ответа. просто делай". This came after several turns where I asked "Прогнать снова?" / "Хотите чтобы я...?" before each action.

**How to apply:** Default to executing the next logical step without a check-in, especially for continuing/iterating on a task the user already set in motion (e.g. re-running a script after a code fix, retrying a failed UI step, applying an obvious follow-up fix). Still use judgment for genuinely irreversible/high-blast-radius actions (force-push, deleting data, sending external communications) per the standing safety guidance — but routine iteration, verification, and retries should not be gated behind a question. Only ask when truly blocked on a decision only the user can make.
