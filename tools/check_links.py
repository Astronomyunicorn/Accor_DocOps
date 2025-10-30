import os
import re
from pathlib import Path


MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def normalize_target(target: str) -> str:
    # strip anchors and query
    target = target.split('#', 1)[0].split('?', 1)[0]
    return target


def is_http(target: str) -> bool:
    return target.startswith('http://') or target.startswith('https://')


def main() -> int:
    docs_root = Path('docs/en')
    errors = 0
    for md in docs_root.rglob('*.md'):
        content = md.read_text(encoding='utf-8', errors='ignore')
        for m in MD_LINK_RE.finditer(content):
            raw = m.group(1).strip()
            if is_http(raw):
                continue  # external links handled elsewhere
            if raw.startswith('mailto:') or raw.startswith('tel:'):
                continue
            target = normalize_target(raw)
            if not target:
                continue
            # Resolve relative to current md
            target_path = (md.parent / target).resolve()
            if not target_path.exists():
                print(f"[BROKEN] {md}: -> {raw}")
                errors += 1
    if errors:
        print(f"Broken internal links: {errors}")
        return 1
    print("All internal links OK")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())


