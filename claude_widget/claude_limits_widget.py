"""
Виджет лимитов Claude над панелью задач Windows.

Показывает, сколько израсходовано из лимита 5-часовой сессии и недельного лимита,
и когда они сбросятся. Данные — те же, что в /usage в Claude Code.
Токен входа берётся из ~/.claude/.credentials.json (его обновляет сам Claude Code)
и отправляется только на api.anthropic.com.

Запуск без чёрного окна:  pythonw claude_limits_widget.py
Перетащить — левой кнопкой мыши. Правая кнопка — меню «Обновить / Закрыть».
"""
import ctypes
import json
import threading
import tkinter as tk
from datetime import datetime
from pathlib import Path

import requests

CRED = Path.home() / ".claude" / ".credentials.json"
URL = "https://api.anthropic.com/api/oauth/usage"
REFRESH_MS = 3 * 60 * 1000
SYS_MS = 2000          # загрузка компьютера — каждые 2 с
TOP = 36               # высота строки «ЦП · Память · Диск · Сеть» (в точках при масштабе 100%)
W, H = 250, 92 + TOP
FOLLOW_MS = 250        # как часто сверяться с окном Claude Desktop
STRIP_W, STRIP_H = 620, 28                 # полоса в заголовке Claude (точки при 100%)
DEF_OFF = {"r": 150, "t": 4}               # отступ от правого края (кнопки окна) и от верха
POS = Path(__file__).with_name("widget_pos.json")

BG, FG, MUTED, TRACK = "#1E1F1C", "#ECEAE0", "#9B9A8B", "#34352F"
GOOD, WARN, BAD = "#6CC49A", "#E0A857", "#E5876F"
DAYS = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]


def fetch():
    tok = json.loads(CRED.read_text(encoding="utf-8"))["claudeAiOauth"]["accessToken"]
    r = requests.get(URL, timeout=20, headers={"Authorization": f"Bearer {tok}",
                                               "anthropic-beta": "oauth-2025-04-20"})
    if r.status_code == 401:
        raise RuntimeError("вход устарел — откройте Claude Code")
    r.raise_for_status()
    return r.json()


def when(iso, with_day):
    if not iso:
        return ""
    t = datetime.fromisoformat(iso).astimezone()
    return f"{DAYS[t.weekday()]} {t:%H:%M}" if with_day else f"{t:%H:%M}"


def color(p):
    return GOOD if p < 60 else WARN if p < 85 else BAD


class SysLoad:
    """Загрузка компьютера как в Диспетчере задач: ЦП, память, диск, сеть в %.
    Счётчики Windows (PDH) по английским именам — работают и в русской Windows, без psutil."""
    PDH_FMT_DOUBLE = 0x200

    class _FMT(ctypes.Structure):
        _fields_ = [("CStatus", ctypes.c_ulong), ("doubleValue", ctypes.c_double)]

    class _ITEM(ctypes.Structure):
        pass

    def __init__(self):
        self._ITEM._fields_ = [("szName", ctypes.c_wchar_p), ("FmtValue", self._FMT)]
        self.pdh = ctypes.windll.pdh
        self.q = ctypes.c_void_p()
        self.pdh.PdhOpenQueryW(None, 0, ctypes.byref(self.q))
        self.c = {}
        for key, path in [("cpu", r"\Processor Information(_Total)\% Processor Utility"),
                          ("idle", r"\PhysicalDisk(_Total)\% Idle Time"),
                          ("net", r"\Network Interface(*)\Bytes Total/sec"),
                          ("bw", r"\Network Interface(*)\Current Bandwidth")]:
            h = ctypes.c_void_p()
            if self.pdh.PdhAddEnglishCounterW(self.q, path, 0, ctypes.byref(h)) == 0:
                self.c[key] = h
        self.pdh.PdhCollectQueryData(self.q)   # первое чтение — точка отсчёта для «за секунду»

    def _one(self, key):
        v = self._FMT()
        if key not in self.c or self.pdh.PdhGetFormattedCounterValue(self.c[key], self.PDH_FMT_DOUBLE, None, ctypes.byref(v)):
            return None
        return v.doubleValue

    def _many(self, key):
        """Счётчик с (*) — значение по каждому сетевому адаптеру: {имя: число}."""
        if key not in self.c:
            return {}
        size, n = ctypes.c_ulong(0), ctypes.c_ulong(0)
        self.pdh.PdhGetFormattedCounterArrayW(self.c[key], self.PDH_FMT_DOUBLE, ctypes.byref(size), ctypes.byref(n), None)
        if not size.value:
            return {}
        buf = ctypes.create_string_buffer(size.value)
        if self.pdh.PdhGetFormattedCounterArrayW(self.c[key], self.PDH_FMT_DOUBLE, ctypes.byref(size), ctypes.byref(n), buf):
            return {}
        items = ctypes.cast(buf, ctypes.POINTER(self._ITEM))
        return {items[i].szName: items[i].FmtValue.doubleValue for i in range(n.value)}

    @staticmethod
    def _memory():
        class MS(ctypes.Structure):
            _fields_ = [("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong)] + \
                       [(f"f{i}", ctypes.c_ulonglong) for i in range(7)]
        m = MS(); m.dwLength = ctypes.sizeof(MS)
        ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
        return m.dwMemoryLoad

    def read(self):
        """-> {'ЦП': %, 'Память': %, 'Диск': %, 'Сеть': %}"""
        self.pdh.PdhCollectQueryData(self.q)
        cpu, idle = self._one("cpu"), self._one("idle")
        net, bw = self._many("net"), self._many("bw")
        nets = [net[k] * 8 / bw[k] * 100 for k in net if bw.get(k)]   # как в Диспетчере: самый загруженный адаптер
        clip = lambda x: None if x is None else max(0, min(100, x))
        return {"ЦП": clip(cpu), "Память": self._memory(),
                "Диск": clip(100 - idle) if idle is not None else None, "Сеть": clip(max(nets)) if nets else 0}


class RECT(ctypes.Structure):
    _fields_ = [("l", ctypes.c_long), ("t", ctypes.c_long), ("r", ctypes.c_long), ("b", ctypes.c_long)]


u32 = ctypes.windll.user32
u32.SetWindowLongPtrW.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
u32.SetWindowLongPtrW.restype = ctypes.c_void_p
WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)


def exe_of(hwnd):
    pid = ctypes.c_ulong()
    u32.GetWindowThreadProcessId(ctypes.c_void_p(hwnd), ctypes.byref(pid))
    h = ctypes.windll.kernel32.OpenProcess(0x1000, False, pid.value)   # PROCESS_QUERY_LIMITED_INFORMATION
    if not h:
        return ""
    buf, n = ctypes.create_unicode_buffer(520), ctypes.c_ulong(520)
    ctypes.windll.kernel32.QueryFullProcessImageNameW(h, 0, buf, ctypes.byref(n))
    ctypes.windll.kernel32.CloseHandle(h)
    return buf.value


def find_claude():
    """Главное окно Claude Desktop (Claude.exe из WindowsApps / Program Files) — самое большое видимое."""
    found = []

    def cb(hwnd, _):
        if u32.IsWindowVisible(ctypes.c_void_p(hwnd)) and u32.GetWindowTextLengthW(ctypes.c_void_p(hwnd)):
            exe = exe_of(hwnd).lower()
            if exe.endswith("\\claude.exe") and "\\app\\" in exe:
                rc = RECT()
                u32.GetWindowRect(ctypes.c_void_p(hwnd), ctypes.byref(rc))
                found.append(((rc.r - rc.l) * (rc.b - rc.t), hwnd))
        return True

    u32.EnumWindows(WNDENUMPROC(cb), 0)
    return max(found)[1] if found else None


def frame_of(hwnd):
    """Видимая рамка окна без невидимых краёв (DWMWA_EXTENDED_FRAME_BOUNDS)."""
    rc = RECT()
    if ctypes.windll.dwmapi.DwmGetWindowAttribute(ctypes.c_void_p(hwnd), 9, ctypes.byref(rc), ctypes.sizeof(rc)):
        u32.GetWindowRect(ctypes.c_void_p(hwnd), ctypes.byref(rc))
    return rc


def work_area():
    """Прямоугольник рабочего стола без панели задач (SPI_GETWORKAREA)."""
    class RECT(ctypes.Structure):
        _fields_ = [("l", ctypes.c_long), ("t", ctypes.c_long), ("r", ctypes.c_long), ("b", ctypes.c_long)]
    rc = RECT()
    ctypes.windll.user32.SystemParametersInfoW(0x0030, 0, ctypes.byref(rc), 0)
    return rc.r, rc.b


class Widget:
    def __init__(self):
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except (AttributeError, OSError):
            pass
        self.root = tk.Tk()
        global W, H
        self.s = s = self.root.winfo_fpixels("1i") / 96   # масштаб экрана Windows (200% -> 2.0)
        W, H = round(250 * s), round((92 + TOP) * s)
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg=BG)
        right, bottom = work_area()
        self.root.geometry(f"{W}x{H}+{right - W - round(12 * s)}+{bottom - H - round(8 * s)}")

        self.c = tk.Canvas(self.root, width=W, height=H, bg=BG, highlightthickness=0)
        self.c.pack()
        self.c.bind("<ButtonPress-1>", self._start_drag)
        self.c.bind("<B1-Motion>", self._drag)
        self.c.bind("<ButtonRelease-1>", self._end_drag)
        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="Обновить", command=self.refresh)
        menu.add_command(label="Закрыть", command=self.root.destroy)
        self.c.bind("<Button-3>", lambda e: menu.tk_popup(e.x_root, e.y_root))

        try:
            self.load = SysLoad()
        except Exception:        # счётчики Windows недоступны — виджет работает как раньше
            self.load = None
        self.sys = {}
        self.data, self.msg = None, "Claude · загрузка…"
        # привязка к окну Claude Desktop: полоса в строке заголовка, справа перед кнопками окна
        self.mode, self.claude, self.hidden = "card", None, False
        self.off = self._load_off()
        menu.add_separator()
        menu.add_command(label="Вернуть полосу на место", command=self._reset_off)
        self.redraw()
        self._tick()
        self._sys_tick()
        self._keep_on_top()
        self._follow()

    # ---------- привязка к Claude Desktop ----------
    def _load_off(self):
        try:
            return json.loads(POS.read_text(encoding="utf-8"))
        except Exception:
            return dict(DEF_OFF)

    def _reset_off(self):
        self.off = dict(DEF_OFF)
        POS.write_text(json.dumps(self.off), encoding="utf-8")

    def _hwnd(self):
        return u32.GetParent(self.root.winfo_id()) or self.root.winfo_id()

    def _set_mode(self, mode):
        if mode == self.mode:
            return
        self.mode = mode
        global W, H
        s = self.s
        if mode == "strip":
            W, H = round(STRIP_W * s), round(STRIP_H * s)
            self.root.attributes("-topmost", False)
        else:
            W, H = round(250 * s), round((92 + TOP) * s)
            u32.SetWindowLongPtrW(self._hwnd(), -8, None)      # отцепить от окна Claude
            self.root.attributes("-topmost", True)
            right, bottom = work_area()
            self.root.geometry(f"+{right - W - round(12 * s)}+{bottom - H - round(8 * s)}")
        self.c.config(width=W, height=H)
        self.root.geometry(f"{W}x{H}")
        self.redraw()

    def _follow(self):
        """4 раза в секунду: найти окно Claude, встать в его заголовок; свёрнуто — спрятаться."""
        try:
            if not (self.claude and u32.IsWindow(ctypes.c_void_p(self.claude))
                    and u32.IsWindowVisible(ctypes.c_void_p(self.claude))):
                self.claude = find_claude()
                if self.claude:
                    # окно-«хозяин»: виджет всегда над Claude, но под другими программами
                    u32.SetWindowLongPtrW(self._hwnd(), -8, ctypes.c_void_p(self.claude))
            if not self.claude:
                self._show(True)
                self._set_mode("card")
            elif u32.IsIconic(ctypes.c_void_p(self.claude)):
                self._show(False)
            else:
                self._set_mode("strip")
                self._show(True)
                if not self._dragging:
                    rc = frame_of(self.claude)
                    x = rc.r - round(self.off["r"] * self.s) - W
                    y = rc.t + round(self.off["t"] * self.s)
                    if (x, y) != (self.root.winfo_x(), self.root.winfo_y()):
                        self.root.geometry(f"+{x}+{y}")
        except Exception:
            pass
        self.root.after(FOLLOW_MS, self._follow)

    def _show(self, on):
        if on and self.hidden:
            self.root.deiconify()
            self.hidden = False
        elif not on and not self.hidden:
            self.root.withdraw()
            self.hidden = True

    def _sys_tick(self):
        if self.load:
            try:
                self.sys = self.load.read()
            except Exception:
                pass
            self.draw_sys()
        self.root.after(SYS_MS, self._sys_tick)

    def draw_sys(self):
        """Строка сверху, как шапка Диспетчера задач: крупный % и подпись."""
        s = self.s
        if self.mode == "strip":
            if self.data:
                self.draw_strip(self.data)
            return
        self.c.delete("sys")
        if not self.sys:
            return
        cols = list(self.sys.items())
        step = (W - 24 * s) / len(cols)
        for k, (name, v) in enumerate(cols):
            x = 12 * s + step * (k + 0.5)
            txt = "—" if v is None else f"{round(v)}%"
            self.c.create_text(x, 12 * s, text=txt, fill=FG if v is None else color(v),
                               font=("Segoe UI Semibold", 11), tags="sys")
            self.c.create_text(x, 27 * s, text=name, fill=MUTED, font=("Segoe UI", 7), tags="sys")
        self.c.create_line(12 * s, (TOP - 2) * s, W - 12 * s, (TOP - 2) * s, fill=TRACK, tags="sys")

    def _keep_on_top(self):
        """Развёрнутые окна иногда перекрывают topmost-окно Tk — раз в 5 с поднимаем себя снова.
        Только для карточки: полоса в Claude держится над ним как «подчинённое» окно."""
        if self.mode == "card":
            # HWND_TOPMOST=-1, SWP_NOSIZE|SWP_NOMOVE|SWP_NOACTIVATE = 0x1|0x2|0x10
            u32.SetWindowPos(self._hwnd(), -1, 0, 0, 0, 0, 0x13)
        self.root.after(5000, self._keep_on_top)

    def _tick(self):
        self.refresh()
        self.root.after(REFRESH_MS, self._tick)

    _dragging = False

    def _start_drag(self, e):
        self._dx, self._dy = e.x, e.y
        self._dragging = True

    def _drag(self, e):
        self.root.geometry(f"+{e.x_root - self._dx}+{e.y_root - self._dy}")

    def _end_drag(self, e):
        """Полосу сдвинули — запомнить место относительно окна Claude."""
        self._dragging = False
        if self.mode == "strip" and self.claude:
            rc = frame_of(self.claude)
            self.off = {"r": round((rc.r - self.root.winfo_x() - W) / self.s),
                        "t": round((self.root.winfo_y() - rc.t) / self.s)}
            POS.write_text(json.dumps(self.off), encoding="utf-8")

    def redraw(self):
        if self.data:
            self.show(self.data)
        else:
            self.draw_text(self.msg)

    def draw_text(self, msg):
        self.msg = msg
        self.c.delete("all")
        y = H // 2 if self.mode == "strip" else (TOP * self.s + H) // 2
        x = W - 12 * self.s if self.mode == "strip" else 12 * self.s
        self.c.create_text(x, y, text=msg, fill=MUTED, anchor="e" if self.mode == "strip" else "w",
                           font=("Segoe UI", 9))
        self.draw_sys()

    def draw_strip(self, d):
        """Одна строка: ЦП 5% · Память 52% · Диск 0% · Сеть 0% │ Сессия 8% ▬ 21:29 │ Неделя 25% ▬ вт 12:59"""
        s, c, y = self.s, self.c, H / 2
        c.delete("all")
        x = 10 * s
        for name, v in self.sys.items():
            short = {"Память": "Пам"}.get(name, name)
            c.create_text(x, y, text=short, fill=MUTED, anchor="w", font=("Segoe UI", 8))
            x += 4 * s + c.bbox(c.find_all()[-1])[2] - c.bbox(c.find_all()[-1])[0]
            txt = "—" if v is None else f"{round(v)}%"
            c.create_text(x, y, text=txt, fill=FG if v is None else color(v), anchor="w",
                          font=("Segoe UI Semibold", 9))
            x += 10 * s + c.bbox(c.find_all()[-1])[2] - c.bbox(c.find_all()[-1])[0]
        if not d:
            return
        for label, part, day in (("Сессия", d.get("five_hour") or {}, False), ("Неделя", d.get("seven_day") or {}, True)):
            c.create_line(x, 6 * s, x, H - 6 * s, fill=TRACK)
            x += 10 * s
            p = max(0, min(100, round(part.get("utilization") or 0)))
            c.create_text(x, y, text=f"{label} {p}%", fill=FG, anchor="w", font=("Segoe UI Semibold", 9))
            x += 6 * s + c.bbox(c.find_all()[-1])[2] - c.bbox(c.find_all()[-1])[0]
            c.create_rectangle(x, y - 2.5 * s, x + 50 * s, y + 2.5 * s, fill=TRACK, width=0)
            if p:
                c.create_rectangle(x, y - 2.5 * s, x + 50 * s * p / 100, y + 2.5 * s, fill=color(p), width=0)
            x += 56 * s
            c.create_text(x, y, text=when(part.get("resets_at"), day), fill=MUTED, anchor="w", font=("Segoe UI", 8))
            x += 10 * s + c.bbox(c.find_all()[-1])[2] - c.bbox(c.find_all()[-1])[0]

    def bar(self, y, label, p, reset):
        s = self.s   # координаты заданы для масштаба 100% и умножаются на масштаб экрана
        p = max(0, min(100, round(p)))
        self.c.create_text(12 * s, y * s, text=label, fill=FG, anchor="w", font=("Segoe UI Semibold", 9))
        self.c.create_text(W - 12 * s, y * s, text=f"{p}%  · сброс {reset}", fill=MUTED, anchor="e", font=("Segoe UI", 8))
        x0, x1, yb = 12 * s, W - 12 * s, (y + 12) * s
        self.c.create_rectangle(x0, yb, x1, yb + 5 * s, fill=TRACK, width=0)
        if p:
            self.c.create_rectangle(x0, yb, x0 + (x1 - x0) * p / 100, yb + 5 * s, fill=color(p), width=0)

    def show(self, d):
        self.data = d
        if self.mode == "strip":
            self.draw_strip(d)
            return
        self.c.delete("all")
        s, w = d.get("five_hour") or {}, d.get("seven_day") or {}
        self.bar(TOP + 14, "Сессия 5 ч", s.get("utilization") or 0, when(s.get("resets_at"), False))
        self.bar(TOP + 46, "Неделя", w.get("utilization") or 0, when(w.get("resets_at"), True))
        self.c.create_text(W - 12 * self.s, H - 9 * self.s, text=f"обновлено {datetime.now():%H:%M}",
                           fill=MUTED, anchor="e", font=("Segoe UI", 7))
        self.draw_sys()

    def refresh(self):
        def work():
            try:
                d = fetch()
                self.root.after(0, self.show, d)
            except Exception as e:  # сеть, файл, 401 — показываем текстом, не падаем
                msg = str(e) if isinstance(e, RuntimeError) else "нет связи — повторю позже"
                self.root.after(0, self.draw_text, f"Claude · {msg}")
        threading.Thread(target=work, daemon=True).start()


if __name__ == "__main__":
    Widget().root.mainloop()
