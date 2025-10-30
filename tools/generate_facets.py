import os
import re
from pathlib import Path
from collections import defaultdict


def read_frontmatter(md_path: Path) -> str | None:
    text = md_path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return None
    return parts[1]


def extract_tags(frontmatter: str) -> list[str]:
    tags: list[str] = []
    in_tags = False
    for line in frontmatter.splitlines():
        s = line.strip()
        if s == "tags:":
            in_tags = True
            continue
        if in_tags:
            if not s.startswith("-"):
                break
            tags.append(s[1:].strip())
    return tags


def scan_docs(docs_root: Path) -> dict[str, list[Path]]:
    mapping: dict[str, list[Path]] = defaultdict(list)
    for md_path in docs_root.rglob("*.md"):
        # Skip generated facet pages and tag index to avoid feedback loop
        if any(part in {"by-audience", "by-type", "by-owner"} for part in md_path.parts):
            continue
        fm = read_frontmatter(md_path)
        if not fm:
            continue
        tags = extract_tags(fm)
        for tag in tags:
            if ":" in tag:
                mapping[tag].append(md_path)
    return mapping


def slug_to_title(slug: str) -> str:
    return re.sub(r"\s+", " ", slug.replace("-", " ")).title()


def generate_page(namespace: str, value: str, docs: list[Path], base_dir: Path) -> str:
    title = f"Documentation for {slug_to_title(value)}"
    lines = [
        "---",
        f"title: {title}",
        f"description: All documentation tagged with {namespace}:{value}",
        "tags:",
        f"  - {namespace}:{value}",
        "  - lifecycle:approved",
        "---",
        "",
        f"# {title}",
        "",
        "## All Documents",
        "",
    ]
    for doc in sorted(docs):
        rel = os.path.relpath(doc, base_dir)
        name = slug_to_title(doc.stem)
        lines.append(f"- [{name}]({rel})")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    base_dir = Path("docs/en")
    out_map = {
        "audience": base_dir / "by-audience",
        "doc-type": base_dir / "by-type",
        "owner": base_dir / "by-owner",
    }
    for p in out_map.values():
        p.mkdir(parents=True, exist_ok=True)

    mapping = scan_docs(base_dir)

    generated = 0
    for ns, out_dir in out_map.items():
        values: dict[str, list[Path]] = defaultdict(list)
        for tag, files in mapping.items():
            if tag.startswith(f"{ns}:"):
                values[tag.split(":", 1)[1]].extend(files)
        for value, files in values.items():
            content = generate_page(ns, value, files, base_dir)
            (out_dir / f"{value}.md").write_text(content, encoding="utf-8")
            generated += 1

    print(f"Generated {generated} facet pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


