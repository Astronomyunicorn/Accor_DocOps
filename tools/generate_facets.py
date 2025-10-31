import os
import re
import subprocess
from datetime import datetime
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


def scan_docs(docs_root: Path) -> tuple[dict[str, list[Path]], dict[Path, list[str]]]:
    mapping: dict[str, list[Path]] = defaultdict(list)
    doc_to_tags: dict[Path, list[str]] = {}
    for md_path in docs_root.rglob("*.md"):
        # Skip generated facet pages and tag index to avoid feedback loop
        if any(part in {"by-audience", "by-type", "by-owner"} for part in md_path.parts):
            continue
        fm = read_frontmatter(md_path)
        if not fm:
            continue
        tags = extract_tags(fm)
        doc_to_tags[md_path] = tags
        for tag in tags:
            if ":" in tag:
                mapping[tag].append(md_path)
    return mapping, doc_to_tags


def get_last_modified(filepath: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%ai", str(filepath)],
            capture_output=True,
            text=True,
            cwd=".",
            check=False,
        )
        if result.returncode == 0 and result.stdout.strip():
            date_str = result.stdout.strip().split()[0]
            return date_str
    except Exception:
        pass
    mtime = os.path.getmtime(filepath)
    return datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")


def slug_to_title(slug: str) -> str:
    return re.sub(r"\s+", " ", slug.replace("-", " ")).title()


def generate_page(namespace: str, value: str, docs: list[Path], base_dir: Path, page_dir: Path, doc_to_tags: dict[Path, list[str]]) -> str:
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
        rel = os.path.relpath(doc, page_dir).replace("\\", "/")
        name = slug_to_title(doc.stem)
        last = get_last_modified(doc)
        # Show key tags for context
        tags = doc_to_tags.get(doc, [])
        key_tags = [t for t in tags if t.startswith("audience:") or t.startswith("doc-type:")]
        if key_tags:
            tags_str = ", ".join(f"`{t}`" for t in key_tags)
            lines.append(f"- [{name}]({rel}) — Updated: {last} | {tags_str}")
        else:
            lines.append(f"- [{name}]({rel}) — Updated: {last}")
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

    mapping, doc_to_tags = scan_docs(base_dir)

    generated = 0
    for ns, out_dir in out_map.items():
        values: dict[str, list[Path]] = defaultdict(list)
        for tag, files in mapping.items():
            if tag.startswith(f"{ns}:"):
                values[tag.split(":", 1)[1]].extend(files)
        for value, files in values.items():
            page_path = out_dir / f"{value}.md"
            content = generate_page(ns, value, files, base_dir, page_path.parent, doc_to_tags)
            page_path.write_text(content, encoding="utf-8")
            generated += 1

    print(f"Generated {generated} facet pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


