"""Generate summary statistics for the entries."""
import json
from pathlib import Path
from collections import Counter

for source in ["sse", "szse"]:
    entries_dir = Path("knowledge/articles") / source / "entries"
    if not entries_dir.exists():
        continue
    
    entries = []
    for f in sorted(entries_dir.glob("*.json")):
        if f.name == "entries.json":
            continue
        entries.append(json.loads(f.read_text(encoding="utf-8")))
    
    print(f"\n=== {source.upper()} - {len(entries)} entries ===")
    
    # By type
    types = Counter(e["type"] for e in entries)
    print("  By type:")
    for t, c in types.most_common():
        print(f"    {t}: {c}")
    
    # By status
    statuses = Counter(e["status"] for e in entries)
    print("  By status:")
    for s, c in statuses.most_common():
        print(f"    {s}: {c}")
    
    # With tags
    has_tags = sum(1 for e in entries if e.get("tags"))
    print(f"  With tags: {has_tags}")
    
    # With content_markdown
    has_md = sum(1 for e in entries if e.get("content_markdown"))
    print(f"  With content_markdown: {has_md}")
    
    # With file_hash
    has_hash = sum(1 for e in entries if e.get("file_hash"))
    print(f"  With file_hash: {has_hash}")
    
    # With public_date
    has_date = sum(1 for e in entries if e.get("public_date"))
    print(f"  With public_date: {has_date}")
    
    # Version traceability
    with_prev = sum(1 for e in entries if e.get("previous_version"))
    with_sup = sum(1 for e in entries if e.get("superseded_by"))
    print(f"  With previous_version: {with_prev}")
    print(f"  With superseded_by: {with_sup}")
    
    # With related_ids
    with_rel = sum(1 for e in entries if e.get("related_ids"))
    print(f"  With related_ids: {with_rel}")

print("\nDone.")
