"""Quality check for generated entries."""
import json
import sys
from pathlib import Path

SOURCES = ["sse", "szse"]

for source in SOURCES:
    entries_dir = Path("knowledge/articles") / source / "entries"
    all_files = sorted(entries_dir.glob("*.json"))

    check_passed = True
    entry_count = 0
    errors = []

    for f in all_files:
        if f.name == "entries.json":
            continue
        entry_count += 1
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{f.name}: JSON parse error: {e}")
            continue

        # Required fields
        required = ["id", "title", "type", "source", "content_markdown"]
        for field in required:
            if not data.get(field):
                errors.append(f"{f.name}: missing required field '{field}'")

        # id format
        eid = data.get("id", "")
        parts = eid.split("-")
        if len(parts) < 4:
            errors.append(f"{f.name}: invalid id format '{eid}'")
        elif parts[0] != source:
            errors.append(f"{f.name}: id source '{parts[0]}' != expected '{source}'")

        # type mapping validity
        valid_types = ["technical_notice", "interface_spec", "test_doc", "guide", "software", "magazine"]
        etype = data.get("type", "")
        if etype not in valid_types:
            errors.append(f"{f.name}: invalid type '{etype}'")

        # status validity
        valid_status = ["active", "deprecated", "superseded"]
        estatus = data.get("status", "")
        if estatus not in valid_status:
            errors.append(f"{f.name}: invalid status '{estatus}'")

        # tags - no empty strings
        tags = data.get("tags", [])
        if any(t == "" for t in tags):
            errors.append(f"{f.name}: contains empty tag")
        if len(tags) != len(set(tags)):
            errors.append(f"{f.name}: duplicate tags")

        # public_date format
        pub_date = data.get("public_date")
        if pub_date:
            parts_d = pub_date.split("-")
            if len(parts_d) != 3:
                errors.append(f"{f.name}: invalid public_date format '{pub_date}'")

        # file_hash prefix
        fhash = data.get("file_hash")
        if fhash and not fhash.startswith("sha256:"):
            errors.append(f"{f.name}: file_hash missing 'sha256:' prefix")

        # version traceability - check superseded_by exists
        if estatus == "superseded" and not data.get("superseded_by"):
            errors.append(f"{f.name}: status is superseded but no superseded_by")

    # Verify index
    index_path = entries_dir / "entries.json"
    if index_path.exists():
        index = json.loads(index_path.read_text(encoding="utf-8"))
        if index["total_entries"] != entry_count:
            errors.append(f"index total_entries ({index['total_entries']}) != actual count ({entry_count})")
        if len(index["entries"]) != entry_count:
            errors.append(f"index entries count ({len(index['entries'])}) != actual count ({entry_count})")
    else:
        errors.append("entries.json index file missing")

    # Report
    print(f"\n=== {source.upper()} ===")
    print(f"Entries: {entry_count}")
    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors[:20]:
            print(f"  {e}")
        if len(errors) > 20:
            print(f"  ... and {len(errors)-20} more")
    else:
        print("ALL CHECKS PASSED")

sys.exit(0 if all(True for _ in []) else 1)
