import os
from pathlib import Path
from collections import defaultdict


def extract_frontmatter_and_body(md_path: Path):
    text = md_path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, text
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return None, text
    frontmatter = parts[1]
    body = parts[2]
    meta = {}
    for line in frontmatter.splitlines():
        s = line.strip()
        if s.startswith("tags:"):
            meta["tags"] = []
        elif s.startswith("-") and "tags" in meta and isinstance(meta["tags"], list):
            meta["tags"].append(s[1:].strip())
    return meta, body


def generate_stats(docs_dir: Path):
    total = 0
    by_lifecycle = defaultdict(int)
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if not file.endswith(".md"):
                continue
            path = Path(root) / file
            meta, _ = extract_frontmatter_and_body(path)
            if meta is None:
                continue
            total += 1
            lifecycle = [t for t in meta.get("tags", []) if t.startswith("lifecycle:")]
            if lifecycle:
                status = lifecycle[0].split(":", 1)[1]
                by_lifecycle[status] += 1
    return total, by_lifecycle


def render_stats_md(total: int, by_lifecycle: dict) -> str:
    approved = by_lifecycle.get("approved", 0)
    review = by_lifecycle.get("review", 0)
    draft = by_lifecycle.get("draft", 0)
    deprecated = by_lifecycle.get("deprecated", 0)

    pct = lambda n: f"{round((n/total)*100):d}%" if total else "0%"

    lines = [
        "**\ud83d\udcda Total Documents:** " + str(total) + "  ",
        f"**\u2705 Approved:** {approved} ({pct(approved)})  ",
        f"**\ud83d\udd04 In Review:** {review} ({pct(review)})  ",
        f"**\ud83d\udccb Draft:** {draft} ({pct(draft)})  ",
        f"**\u26a0\ufe0f Deprecated:** {deprecated}",
        "",
        "---",
        "",
        "## Quick Navigation",
        "",
        "- [Browse by Audience](by-audience/index.md)",
        "- [Browse by Type](by-type/index.md)",
        "- [Browse by Owner](by-owner/index.md)",
        "",
    ]
    return "\n".join(lines)


def update_homepage(home_path: Path, stats_md: str) -> None:
    text = home_path.read_text(encoding="utf-8")
    marker_start = "<!-- STATS:BEGIN -->"
    marker_end = "<!-- STATS:END -->"
    block = f"{marker_start}\n\n# Documentation Hub\n\n{stats_md}\n{marker_end}"
    if marker_start in text and marker_end in text:
        pre, _mid, post = text.partition(marker_start)
        _old, _mid2, post2 = post.partition(marker_end)
        new_text = pre + block + post2
    else:
        # Insert after front matter
        if text.startswith("---\n"):
            parts = text.split("---\n", 2)
            new_text = parts[0] + "---\n" + parts[1] + "---\n\n" + block + "\n\n" + parts[2]
        else:
            new_text = block + "\n\n" + text
    home_path.write_text(new_text, encoding="utf-8")


def main() -> int:
    docs_dir = Path("docs/en")
    total, by_lifecycle = generate_stats(docs_dir)
    stats_md = render_stats_md(total, by_lifecycle)
    update_homepage(docs_dir / "index.md", stats_md)
    print("Updated homepage with statistics.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


