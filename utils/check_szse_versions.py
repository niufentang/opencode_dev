"""Quick check SZSE interface versions."""
import json
from pathlib import Path

for f in sorted(Path("knowledge/articles/szse/entries").glob("szse-iface*.json")):
    if f.name == "entries.json":
        continue
    d = json.loads(f.read_text(encoding="utf-8"))
    title = d.get("title", "")
    print(f'{d["id"]}: version={d.get("version")}, title_end={title[-30:]}')
