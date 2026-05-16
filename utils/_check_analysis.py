"""Quick quality check on analysis output."""
import json
from pathlib import Path

analyzed = list(Path("knowledge/articles").rglob("analyzed/**/*_analysis.json"))
all_data = [(json.loads(f.read_text("utf-8")), f) for f in analyzed]
all_data.sort(key=lambda x: len(x[0].get("changes", [])), reverse=True)

for data, f in all_data[:5]:
    changes = data.get("changes", [])
    doc_id = data["doc_id"]
    print(f"\n{doc_id} ({f.name}): {len(changes)} changes")
    for c in changes[:5]:
        print(f"  [{c['type']}] {c['summary'][:80]}")
    if len(changes) > 5:
        print(f"  ... and {len(changes)-5} more")

# Overall stats
with_changes = sum(1 for d, _ in all_data if d.get("changes"))
total_entries = sum(len(d.get("changes", [])) for d, _ in all_data)
print(f"\n--- Stats ---")
print(f"Total docs: {len(all_data)}")
print(f"With changes: {with_changes}")
print(f"Total change entries: {total_entries}")
print(f"Avg per doc (with changes): {total_entries/with_changes:.1f}")
