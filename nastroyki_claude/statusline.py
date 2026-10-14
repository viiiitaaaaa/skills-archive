# Строка состояния Claude Code (statusLine в ~/.claude/settings.json).
# Claude Code передаёт на stdin JSON сессии; печатаем одну строку по-русски:
# модель · усилия · контекст % · кэш тёплый/остыл · лимит 5 ч и неделя.
# Источник: https://code.claude.com/docs/en/statusline (изучено 07.10.2026).
import json
import sys
import time

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

try:
    d = json.loads(sys.stdin.read() or "{}")
except Exception:
    d = {}


def g(*path, default=None):
    cur = d
    for p in path:
        if not isinstance(cur, dict) or p not in cur:
            return default
        cur = cur[p]
    return cur


def hhmm(ts):
    try:
        return time.strftime("%H:%M", time.localtime(float(ts)))
    except Exception:
        return "?"


# Во вкладке Пульта агентов (её просьба 14.10): всё это показывает шапка пульта —
# отдаём данные файлом ~/pult/status/<сессия>.json, а в терминале строку не печатаем.
_pult = __import__("os").environ.get("PULT_SESSION")
if _pult:
    try:
        from pathlib import Path
        sdir = Path.home() / "pult" / "status"
        sdir.mkdir(parents=True, exist_ok=True)
        (sdir / f"{_pult}.json").write_text(json.dumps({
            "model": g("model", "display_name"),
            "effort": g("effort", "level"),
            "ctx": g("context_window", "used_percentage"),
            "ts": time.time(),
        }, ensure_ascii=False), "utf-8")
    except Exception:
        pass
    sys.exit(0)

parts = []
model = g("model", "display_name") or "?"
effort = g("effort", "level")
parts.append(model + (f" · {effort}" if effort else ""))

ctx = g("context_window", "used_percentage")
if ctx is not None:
    mark = "🟢" if ctx < 50 else ("🟡" if ctx < 80 else "🔴 /compact")
    parts.append(f"контекст {round(ctx)}% {mark}")

warm = g("prompt_cache", "warm")
exp = g("prompt_cache", "expires_at")
if warm is True:
    left = ""
    if exp:
        mins = int((float(exp) - time.time()) // 60)
        if mins >= 0:
            left = f" ещё {mins} мин"
    parts.append(f"кэш тёплый{left}")
elif warm is False:
    parts.append("кэш остыл ❄ (длинная сессия — дешевле новая)")

print(" | ".join(parts))

# вторая строка (её просьба 13.10): сессия 5 ч · неделя · ЦП · память
row = []
five = g("rate_limits", "five_hour", "used_percentage")
if five is not None:
    row.append(f"сессия 5 ч {round(five)}% (сброс {hhmm(g('rate_limits', 'five_hour', 'resets_at'))})")
week = g("rate_limits", "seven_day", "used_percentage")
if week is not None:
    row.append(f"неделя {round(week)}%")
try:
    import psutil
    cpu = psutil.cpu_percent(interval=0.2)
    vm = psutil.virtual_memory()
    row.append(f"ЦП {round(cpu)}%" + (" 🔴" if cpu >= 90 else ""))
    row.append(f"память {vm.used / 2**30:.1f} из {vm.total / 2**30:.0f} ГБ ({round(vm.percent)}%)"
               + (" 🔴" if vm.percent >= 90 else ""))
except Exception:
    pass
if row:
    print(" | ".join(row))

# вторая и следующие строки — табло задач агентов (Claude и Hermes), см. agent_status.py
try:
    sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
    from agent_status import lines as agent_lines
    for l in agent_lines():
        print(l)
except Exception:
    pass
