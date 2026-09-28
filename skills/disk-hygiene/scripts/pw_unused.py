"""Печатает папки ms-playwright, которые не нужны ни одному установленному playwright/patchright (по browsers.json)."""
import os, sys
from pathlib import Path
sys.path.insert(0, os.path.dirname(__file__))
from report import playwright_needed

pw = Path(os.environ["LOCALAPPDATA"]) / "ms-playwright"
need = playwright_needed()
if pw.exists() and need:
    for d in pw.iterdir():
        if d.is_dir() and d.name.startswith(("chromium", "webkit", "firefox")) and d.name not in need:
            print(d)
