---
name: hermes-delegate
description: Runs before EVERY user message, task or question. Decides whether the work goes to the Hermes executor (GPT via ChatGPT subscription) or needs no hands-on work, then writes the task card, launches Hermes on the cheapest tier and verifies only the result. Saves Claude's limits.
---

# Delegate hands-on work to Hermes

Owner's rule: Claude is the brain and judge, Hermes does the work. Claude's limits come first, ChatGPT's second.
Reply to the owner in Russian, briefly.

## 1. Classify the message (silently, in one thought)

- **Pure question / conversation, nothing to do** → answer directly and briefly. No Hermes. Done.
- **Needs only knowledge already in context** (a decision, an opinion, a short explanation) → answer directly.
- **Hands-on work** (reading many or large files, searching code, writing or editing code/scripts, running checks or tests, web search, diagnostics with more than 1–2 commands, installs, file moves) → Hermes. Continue below.
- **Exceptions Claude does itself**, saying why in ONE line: Claude's own config (skills, hooks, settings, memory, mods), launching Hermes itself, fixing the launcher, a single command that is cheaper than a card, or something Hermes cannot reach.

## 2. Check where and how Hermes can do it

- Hermes runs from Claude's shell and sees the same virtualized view. Never have it create NEW folders under `%LOCALAPPDATA%` (the desktop app hides them from the owner). Pre-existing ones (`hermes`) and `C:\Users\User\...` outside AppData are real.
- If the result must be seen or run in the owner's real session (a GUI, a shortcut, something that must outlive Claude's processes), the owner launches it, or start a `.cmd` via the user's terminal with `Start-Process .\x.cmd -WindowStyle Minimized`.
- Hermes cannot ask questions. If a choice is truly the owner's, ask the owner first, then write the card.

## 3. Write the card (English) to `C:\Users\User\hermes-tasks\<name>.md`

Contents:
- Goal in one sentence.
- Exact scope: which files/folders may be touched (full paths).
- Exact change when it is small: give the code or the precise edit, not an idea.
- Done when.
- `Verify:` commands whose output proves the result (print the changed lines, run the script, hashes, syntax checks).
- Forbidden: other files, printing secrets, starting/stopping processes unless needed, installs unless needed.

Independent tasks: one card each, launched in parallel (different files).

## 4. Launch on the cheapest tier that can do it

```powershell
& 'C:\Users\User\.claude\skills\hermes-delegate\hermes-task.ps1' -BodyFile 'C:\Users\User\hermes-tasks\<name>.md' -Tier fast -Dir '<project dir>' -Report 'C:\Users\User\hermes-tasks\reports\<name>.md' *> 'C:\Users\User\hermes-tasks\reports\<name>-run.log'
```

Run it with `run_in_background: true` and wait for the notification; do not poll.
Tiers: `fast` = gpt-6-luna (mechanical, small precise edits, lookups), `std` = gpt-6.1-terra (features, bugs, tests), `deep` = gpt-6.1-sol (only after a failure on std or truly hard). Raise the tier only after a failure. If ChatGPT session use is over 80%, go lower or wait.

## 5. Judge only the result

- Read the report (RESULT / CHANGED / VERIFIED / ASSUMPTIONS / LEFT), not logs.
- Check the key thing yourself with 1–2 cheap commands: grep the changed lines, run the check. Never trust "done" on its word: the fast tier has reported success without editing the file.
- Accepted → tell the owner in a few lines. Not accepted → a sharper card with the exact fix; after a second failure raise the tier.
- If Hermes cannot reach chatgpt.com (DNS/timeout), the cause is the network/VPN; tell the owner instead of retrying in a loop.

Emergency stop of everything: `hermes pause`; resume: `hermes resume`.
