#!/usr/bin/env python3
"""
Независимая сверка юнит-экономики.

Считает показатели питоном прямо из листа-приёмника и сравнивает с тем,
что показывает сводная. Расхождение почти всегда означает артикул, которого
нет в списке сводной, — такие деньги теряются молча, без единой ошибки формул.

    python3 reconcile.py файл.xlsx                 # автоопределение площадки
    python3 reconcile.py файл.xlsx --platform wb
    python3 reconcile.py файл.xlsx --pivot Лист1 --source Sheet1

Запускай ПОСЛЕ recalc.py — иначе сравнишь со старыми закешированными значениями.
"""

import argparse
import sys
from collections import defaultdict

try:
    import openpyxl
except ImportError:
    sys.exit("Нужен openpyxl: pip install openpyxl --break-system-packages")


# ─── раскладки отчётов ────────────────────────────────────────────────────────
# Колонки заданы по ЗАГОЛОВКУ, а не по букве: буквы съезжают между выгрузками.

WB_SPEC = {
    "source": "Sheet1",
    "header_row": 1,
    "article": "Артикул поставщика",
    "metrics": [
        # (подпись, колонка-источник, {колонка-условия: значение}, столбец сводной)
        ("КОЛ ПРОДАЖ",     "Кол-во",        {"Обоснование для оплаты": "Продажа"}, 2),
        ("КОЛ ВОЗВРАТ",    "Кол-во",        {"Обоснование для оплаты": "Возврат"}, 3),
        ("ВЫРУЧКА ПРОДАЖ", "Цена розничная", {"Обоснование для оплаты": "Продажа"}, 4),
        ("ВЫРУЧКА ВОЗВРАТ","Цена розничная", {"Обоснование для оплаты": "Возврат"}, 5),
        ("РЕАЛИЗ ПРОДАЖ",  "Вайлдберриз реализовал Товар (Пр)", {"Обоснование для оплаты": "Продажа"}, 6),
        ("РЕАЛИЗ ВОЗВРАТ", "Вайлдберриз реализовал Товар (Пр)", {"Обоснование для оплаты": "Возврат"}, 7),
        ("ПЕРЕЧИСЛ ПРОДАЖ","К перечислению Продавцу за реализованный Товар", {"Обоснование для оплаты": "Продажа"}, 8),
        ("ПЕРЕЧИСЛ ВОЗВРАТ","К перечислению Продавцу за реализованный Товар", {"Обоснование для оплаты": "Возврат"}, 9),
        ("ЛОГИСТИКА",      "Услуги по доставке товара покупателю", {}, 10),
    ],
}

OZON_SPEC = {
    "source": "Начисления",
    "header_row": 2,          # строка 1 занята текстом "Период: ..."
    "article": "Артикул",
    "metrics": [
        ("КОЛ ПРОДАЖ",     "Количество",       {"Группа услуг": "Продажи",  "Тип начисления": "Выручка"}, 2),
        ("КОЛ ВОЗВРАТ",    "Количество",       {"Группа услуг": "Возвраты", "Тип начисления": "Возврат выручки"}, 3),
        ("ВЫРУЧКА ПРОДАЖ", "Цена продавца",    {"Группа услуг": "Продажи",  "Тип начисления": "Выручка"}, 4),
        ("ВЫРУЧКА ВОЗВРАТ","Цена продавца",    {"Группа услуг": "Возвраты", "Тип начисления": "Возврат выручки"}, 5),
        ("РЕАЛИЗ ПРОДАЖ",  "Сумма итого, руб.", {"Группа услуг": "Продажи",  "Тип начисления": "Выручка"}, 6),
        ("РЕАЛИЗ ВОЗВРАТ", "Сумма итого, руб.", {"Группа услуг": "Возвраты", "Тип начисления": "Возврат выручки"}, 7),
        ("КОМИССИЯ",       "Сумма итого, руб.", {"Группа услуг": "Вознаграждение Ozon"}, 8),
        ("ЛОГИСТИКА",      "Сумма итого, руб.", {"Группа услуг": "Услуги доставки"}, 9),
    ],
    # отдельные отчёты: (лист, строка заголовков, колонка-артикул, колонка-сумма, столбец сводной)
    "extra": [
        ("РЕКЛАМА",  "Реклама",  2, "Название кампании", "Расход, ₽", 10),
        ("ХРАНЕНИЕ", "Хранение", 1, "Артикул", "Начисленная стоимость размещения", 11),
    ],
}



def get_column_letter_simple(n):
    """Номер колонки → буква (1 → A, 27 → AA)."""
    out = ""
    while n:
        n, r = divmod(n - 1, 26)
        out = chr(65 + r) + out
    return out


def header_index(ws, header_row):
    """Заголовок → номер колонки."""
    idx = {}
    for c in range(1, ws.max_column + 1):
        v = ws.cell(row=header_row, column=c).value
        if v is not None:
            idx[str(v).strip()] = c
    return idx


def num(v):
    return v if isinstance(v, (int, float)) else 0


def collect(ws, spec):
    """Считает показатели по артикулам напрямую из листа-приёмника."""
    idx = header_index(ws, spec["header_row"])
    missing = [spec["article"]] if spec["article"] not in idx else []
    for label, src, crit, _ in spec["metrics"]:
        for name in [src, *crit]:
            if name not in idx and name not in missing:
                missing.append(name)
    if missing:
        print(f"  ⚠ не найдены колонки: {', '.join(missing)}")
        return None

    art_c = idx[spec["article"]]
    per_article = defaultdict(lambda: defaultdict(float))

    for r in range(spec["header_row"] + 1, ws.max_row + 1):
        art = ws.cell(row=r, column=art_c).value
        if art is None or str(art) == "":
            continue
        key = str(art).lower()          # СУММЕСЛИМН регистронезависим
        for label, src, crit, _ in spec["metrics"]:
            ok = all(ws.cell(row=r, column=idx[cc]).value == want
                     for cc, want in crit.items())
            if ok:
                per_article[key][label] += num(ws.cell(row=r, column=idx[src]).value)
    return per_article


def collect_extra(wb, sheet, header_row, art_h, val_h):
    """Отдельный отчёт (реклама, хранение) — сумма по артикулу."""
    if sheet not in wb.sheetnames:
        return None
    ws = wb[sheet]
    idx = header_index(ws, header_row)
    if art_h not in idx or val_h not in idx:
        print(f"  ⚠ лист «{sheet}»: не найдены колонки {art_h!r} / {val_h!r}")
        return None
    out = defaultdict(float)
    for r in range(header_row + 1, ws.max_row + 1):
        art = ws.cell(row=r, column=idx[art_h]).value
        if art:
            out[str(art).lower()] += num(ws.cell(row=r, column=idx[val_h]).value)
    return out


def pivot_data(ws_p):
    """Артикулы сводной и строка «Общий итог»."""
    articles, total_row = {}, None
    for r in range(1, ws_p.max_row + 1):
        a = ws_p.cell(row=r, column=1).value
        if a is None:
            continue
        if str(a).strip() in ("Общий итог", "ИТОГО", "Итого"):
            total_row = r
            break
        if r >= 4:
            articles[str(a).lower()] = r
    return articles, total_row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--platform", choices=["wb", "ozon"], help="по умолчанию — автоопределение")
    ap.add_argument("--pivot", default="Лист1")
    ap.add_argument("--source", help="переопределить лист-приёмник")
    args = ap.parse_args()

    wb = openpyxl.load_workbook(args.path, data_only=True)

    platform = args.platform
    if not platform:
        platform = "ozon" if "Начисления" in wb.sheetnames else "wb"
    spec = dict(OZON_SPEC if platform == "ozon" else WB_SPEC)
    if args.source:
        spec["source"] = args.source

    print(f"Площадка: {'Ozon' if platform == 'ozon' else 'Wildberries'}")

    for name in (spec["source"], args.pivot):
        if name not in wb.sheetnames:
            sys.exit(f"Нет листа «{name}». Есть: {', '.join(wb.sheetnames)}")

    ws_src, ws_p = wb[spec["source"]], wb[args.pivot]

    # автоподстройка строки заголовков — Ozon иногда присылает без строки "Период"
    idx = header_index(ws_src, spec["header_row"])
    if spec["article"] not in idx:
        for probe in (1, 2, 3):
            if spec["article"] in header_index(ws_src, probe):
                print(f"  заголовки найдены в строке {probe} (ожидалась {spec['header_row']})")
                spec["header_row"] = probe
                break

    raw = collect(ws_src, spec)
    if raw is None:
        sys.exit("Не удалось разобрать лист-приёмник — проверь заголовки.")

    extras = {}
    for label, sheet, hrow, art_h, val_h, col in spec.get("extra", []):
        got = collect_extra(wb, sheet, hrow, art_h, val_h)
        if got is not None:
            extras[label] = (got, col)

    articles, total_row = pivot_data(ws_p)
    if total_row is None:
        sys.exit(f"В листе «{args.pivot}» нет строки «Общий итог».")

    # ── сверка итогов ────────────────────────────────────────────────────────
    print(f"\n{'Показатель':<20}{'отчёт':>15}{'сводная':>15}   ")
    print("-" * 56)
    all_ok = True
    for label, _, _, col in spec["metrics"]:
        rv = sum(v[label] for v in raw.values())
        pv = num(ws_p.cell(row=total_row, column=col).value)
        ok = abs(rv - pv) < 0.02
        all_ok &= ok
        print(f"{label:<20}{rv:>15,.2f}{pv:>15,.2f}   {'OK' if ok else 'РАСХОЖДЕНИЕ'}")

    for label, (data, col) in extras.items():
        rv = sum(data.values())
        pv = num(ws_p.cell(row=total_row, column=col).value)
        ok = abs(rv - pv) < 0.02
        all_ok &= ok
        print(f"{label:<20}{rv:>15,.2f}{pv:>15,.2f}   {'OK' if ok else 'РАСХОЖДЕНИЕ'}")

    # ── пропущенные артикулы ─────────────────────────────────────────────────
    known = set(articles)
    lost = []
    for key, vals in raw.items():
        if key not in known and any(abs(x) > 0.01 for x in vals.values()):
            lost.append((key, vals))
    for label, (data, _) in extras.items():
        for key, v in data.items():
            if key not in known and abs(v) > 0.01 and not any(k == key for k, _ in lost):
                lost.append((key, {label: v}))

    if lost:
        print(f"\nЕсть в отчёте, но НЕТ в сводной — деньги теряются ({len(lost)}):")
        for key, vals in lost:
            detail = ", ".join(f"{k}={v:,.2f}" for k, v in vals.items() if abs(v) > 0.01)
            print(f"  {key}: {detail}")
        print("\n  Добавь эти артикулы строками в сводную.")

    # ── остатки: товары без продаж в юнит не попадают ────────────────────────
    if "Остатки" in wb.sheetnames:
        ws_o = wb["Остатки"]
        # шапка двухуровневая, а ширина отчёта меняется между выгрузками:
        # колонки ищем по заголовку, иначе «Дней до конца остатка» уедет (X → Z)
        idx_o = {**header_index(ws_o, 2), **header_index(ws_o, 1)}
        art_h, qty_h = "Артикул", "Остаток на складах, шт"
        if "Дней до конца остатка" in idx_o:
            col = get_column_letter_simple(idx_o["Дней до конца остатка"])
            print(f"\n«Дней до конца остатка» — колонка {col}. "
                  f"Проверь, что формулы на листе юнита ссылаются именно на неё.")
        if art_h in idx_o and qty_h in idx_o:
            stock, stock_missing = 0.0, {}
            for r in range(3, ws_o.max_row + 1):
                a = ws_o.cell(row=r, column=idx_o[art_h]).value
                q = num(ws_o.cell(row=r, column=idx_o[qty_h]).value)
                if a and q:
                    stock += q
                    if str(a).lower() not in known:
                        stock_missing[str(a)] = q
            print(f"\nОстатки по отчёту: {stock:,.0f} шт")
            if stock_missing:
                print(f"Лежат на складе, но НЕТ в юните — {len(stock_missing)} арт., "
                      f"{sum(stock_missing.values()):,.0f} шт:")
                for a, q in sorted(stock_missing.items(), key=lambda x: -x[1])[:15]:
                    print(f"  {a[:50]:<52}{q:>7,.0f}")
                if len(stock_missing) > 15:
                    print(f"  … ещё {len(stock_missing) - 15}")
                print("\n  Продаж в периоде не было, поэтому строки не появились.")
                print("  Добавь их — прибыль не изменится, но станут видны замороженные деньги.")
                all_ok = False

    # ── дубли по регистру ────────────────────────────────────────────────────
    seen, dupes = {}, []
    for r in range(4, total_row):
        a = ws_p.cell(row=r, column=1).value
        if a:
            k = str(a).lower()
            if k in seen:
                dupes.append((seen[k], r, a))
            else:
                seen[k] = r
    if dupes:
        print(f"\nДубли артикулов (двойной счёт в итоге!):")
        for r1, r2, a in dupes:
            print(f"  строки {r1} и {r2}: {a}")

    print()
    if all_ok and not lost and not dupes:
        print("Сводная сходится с отчётом.")
        return 0
    print("Есть расхождения — см. выше.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
