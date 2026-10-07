"""Скан одной страницы со сканера Ricoh (WIA, USB) в PNG.

python scan.py <выход.png> [--dpi 300] [--color|--gray] [--info]
Источник выбирается сам: если в автоподатчике лежит лист — из него, иначе со стекла.
"""
import argparse, sys
import win32com.client as com

FEEDER, FLATBED, FEED_READY = 1, 2, 1
WIA_FORMAT_PNG = "{B96B3CAF-0728-11D3-9D7B-0000F81EF32E}"


def setp(props, pid, val):
    for p in props:
        if p.PropertyID == pid:
            try:
                p.Value = val
            except Exception as e:
                print(f"  свойство {pid}={val} не принято: {e}")
            return


def getp(props, pid):
    for p in props:
        if p.PropertyID == pid:
            return p.Value


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out", nargs="?")
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--gray", action="store_true")
    ap.add_argument("--info", action="store_true")
    ap.add_argument("--glass", action="store_true", help="сканировать со стекла, даже если в податчике есть лист")
    a = ap.parse_args()

    dm = com.Dispatch("WIA.DeviceManager")
    infos = [d for d in dm.DeviceInfos if d.Type == 1]
    if not infos:
        sys.exit("Сканер не найден — проверь USB-кабель")
    dev = infos[0].Connect()
    caps = getp(dev.Properties, 3086)   # DOCUMENT_HANDLING_CAPABILITIES
    status = getp(dev.Properties, 3087)  # DOCUMENT_HANDLING_STATUS
    use_feeder = bool(caps and caps & FEEDER and status and status & FEED_READY) and not a.glass
    if a.info:
        for p in dev.Properties:
            try:
                print(p.PropertyID, p.Name, p.Value)
            except Exception:
                pass
        print("подача:", "автоподатчик" if use_feeder else "стекло")
        return
    setp(dev.Properties, 3088, FEEDER if use_feeder else FLATBED)  # DOCUMENT_HANDLING_SELECT
    item = dev.Items[1]
    setp(item.Properties, 6146, 2 if a.gray else 1)  # 1 цвет, 2 серый
    setp(item.Properties, 6147, a.dpi)
    setp(item.Properties, 6148, a.dpi)
    img = item.Transfer(WIA_FORMAT_PNG)
    img.SaveFile(a.out)
    print(f"Скан ({'автоподатчик' if use_feeder else 'стекло'}): {a.out}")


if __name__ == "__main__":
    main()
