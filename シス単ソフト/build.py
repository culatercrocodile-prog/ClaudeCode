"""システム英単語一覧.xlsx の内容を index.html に埋め込む。"""
import json
import re
import sys
from pathlib import Path

import openpyxl

sys.stdout.reconfigure(encoding="utf-8")
here = Path(__file__).parent
ws = openpyxl.load_workbook(here / "システム英単語一覧.xlsx").worksheets[0]
words = [
    [int(n), str(w).strip(), str(m).strip()]
    for n, w, m in ws.iter_rows(min_row=2, values_only=True)
    if n is not None and w
]
data = json.dumps(words, ensure_ascii=False, separators=(",", ":"))
html_path = here / "index.html"
html = html_path.read_text(encoding="utf-8")
html, count = re.subn(
    r"/\*DATA\*/.*?/\*END\*/",
    lambda _: "/*DATA*/" + data + "/*END*/",
    html,
    flags=re.S,
)
assert count == 1, "marker not found"
html_path.write_text(html, encoding="utf-8")
print(f"embedded {len(words)} words")
