import os
from pathlib import Path


def extract_frontmatter_and_content(md_path: Path):
    text = md_path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, text
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return None, text
    frontmatter = parts[1]
    body = parts[2]
    meta = {"tags": []}
    in_tags = False
    for line in frontmatter.splitlines():
        s = line.strip()
        if s == "tags:":
            in_tags = True
            continue
        if in_tags:
            if not s.startswith("-"):
                in_tags = False
                continue
            meta["tags"].append(s[1:].strip())
    return meta, body


def check_docs_health() -> list[str]:
    issues: list[str] = []
    for root, _, files in os.walk("docs/en"):
        for file in files:
            if not file.endswith(".md"):
                continue
            path = Path(root) / file
            meta, body = extract_frontmatter_and_content(path)
            if not meta:
                issues.append(f"❌ {path}: Missing frontmatter")
                continue
            tags = meta.get("tags", [])
            required = ["audience", "doc-type", "owner", "lifecycle", "sensitivity"]
            for req in required:
                if not any(tag.startswith(f"{req}:") for tag in tags):
                    issues.append(f"⚠️  {path}: Missing '{req}' tag")
            if len(body.strip()) < 100:
                issues.append(f"⚠️  {path}: Content too short (<100 chars)")
    return issues


def main() -> int:
    issues = check_docs_health()
    for i in issues:
        print(i)
    print(f"\nTotal issues: {len(issues)}")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())


