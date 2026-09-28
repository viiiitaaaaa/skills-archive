"""Список «файл → тема» для рефератов. Скопируй в рабочую папку, заполни TITLES и RULES под материалы, запусти:
python manifest_template.py "<учебная папка>" <work>
Каждый файл попадает ровно в одну тему (первое совпавшее правило). Непопавшие печатаются — их надо отнести.
Файлы «не учёба» (пароли, личное, юр. голосовые) переносятся в m["keep"][путь] = "куда" — finalize.py их сохранит."""
import json, os, re, sys

B, W = sys.argv[1], sys.argv[2]
TITLES = {  # код → название реферата (номер = порядок в папке)
    "01_WB": "Wildberries — полный курс продаж на WB",
    "02_OZON": "Ozon и зарубежные маркетплейсы",
    # ...
}
RULES = [  # (регулярка по относительному пути, код) — порядок важен, регистр не важен
    (r"WB_|lecture_wb", "01_WB"),
    (r"ozon", "02_OZON"),
]
man = {k: [] for k in TITLES}; un = []
for root, _, fs in os.walk(B):
    for f in fs:
        if f == "desktop.ini": continue
        rel = os.path.relpath(os.path.join(root, f), B)
        for pat, k in RULES:
            if re.search(pat, rel, re.I): man[k].append(rel); break
        else: un.append(rel)
json.dump({"titles": TITLES, "files": man, "keep": {}}, open(os.path.join(W, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for k in TITLES: print(k, len(man[k]), TITLES[k])
print("НЕ ОТНЕСЕНО:", un)
