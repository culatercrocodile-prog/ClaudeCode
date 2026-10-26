"""南高の英単語レベル1〜3.xlsx から、シス単トレーナーを元にした独立アプリ3つを生成する。"""
import json
import re
import sys
from pathlib import Path

import openpyxl

sys.stdout.reconfigure(encoding="utf-8")
here = Path(__file__).parent
tpl = (here.parent / "シス単ソフト" / "index.html").read_text(encoding="utf-8").split("\n")
# シス単固有のStage4機能の行(1始まり: 84, 89, 97-99, 106)を除く
drop = {84, 89, 97, 98, 99, 106}
tpl = "\n".join(l for i, l in enumerate(tpl, 1) if i not in drop)

for n in (1, 2, 3):
    ws = openpyxl.load_workbook(here / f"南高の英単語レベル{n}.xlsx").worksheets[0]
    words = [
        [int(no), str(w).strip(), str(m).strip()]
        for no, w, m in ws.iter_rows(min_row=2, values_only=True)
        if no is not None and w
    ]
    data = json.dumps(words, ensure_ascii=False, separators=(",", ":"))
    html = re.sub(r"/\*DATA\*/.*?/\*END\*/", lambda _: "/*DATA*/" + data + "/*END*/", tpl, flags=re.S)
    html = html.replace("シス単トレーナー", f"南高英単語レベル{n}トレーナー")
    html = html.replace("sisutan-v1", f"nanko-level{n}-v1")
    html = html.replace("STAGE4_FROM=1701", "STAGE4_FROM=1e9")
    out = here.parent / f"minatan{n}"
    out.mkdir(exist_ok=True)
    (out / "index.html").write_text(html, encoding="utf-8")
    print(f"レベル{n}: {len(words)}語 -> {out.name}/index.html")
