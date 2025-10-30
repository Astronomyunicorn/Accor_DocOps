import re
from pathlib import Path


def collect_media(media_dir: Path) -> set[str]:
    names: set[str] = set()
    for f in media_dir.rglob('*'):
        if f.is_file():
            names.add(f.name)
    return names


def collect_used_media(docs_dir: Path) -> set[str]:
    used: set[str] = set()
    img_re = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
    for f in docs_dir.rglob('*.md'):
        content = f.read_text(encoding='utf-8', errors='ignore')
        for m in img_re.finditer(content):
            path = m.group(1)
            name = Path(path).name
            if name:
                used.add(name)
    return used


def main() -> int:
    docs_dir = Path('docs/en')
    media_dir = Path('docs/media')
    media = collect_media(media_dir)
    used = collect_used_media(docs_dir)
    orphans = sorted(media - used)
    if orphans:
        print('Orphan media files:')
        for name in orphans:
            print(f"  - {name}")
        return 1
    print('No orphan media files found')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())


