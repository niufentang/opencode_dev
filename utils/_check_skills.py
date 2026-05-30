"""Validate all ls_* skill files."""
import re
from pathlib import Path

required_sections = ["使用场景", "执行步骤", "注意事项", "输出", "质量检查"]

for f in sorted(Path(".opencode/skills").rglob("ls_*/SKILL.md")):
    content = f.read_text("utf-8")
    errors = []

    # Check YAML frontmatter
    m = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not m:
        errors.append("MISSING frontmatter")
        print(f"\n{f.parent.name}: FAIL")
        continue

    fm = m.group(1)
    name = re.search(r"^name:\s*(.+)", fm, re.M)
    desc = re.search(r"^description:\s*(.+)", fm, re.M)
    tools = re.search(r"^allowed-tools:\s*\[(.+)\]", fm, re.M)
    body = content[m.end():]

    if not name:
        errors.append("name missing")
    elif name.group(1).strip() != f.parent.name:
        errors.append(f"name mismatch: {name.group(1)} != {f.parent.name}")

    if not desc:
        errors.append("description missing")
    if not tools:
        errors.append("allowed-tools missing")
    if len(m.group(1).strip()) < 10:
        errors.append("frontmatter too short")

    for sec in required_sections:
        if sec not in body:
            errors.append(f"section missing: {sec}")

    status = "OK" if not errors else "FAIL"
    print(f"\n{f.parent.name}: [{status}] name={name.group(1) if name else '?'}")
    for e in errors:
        print(f"  - {e}")
