import sys
import json
import re
from pathlib import Path


FRONTMATTER_RE = re.compile(r"^---\n([\s\S]*?)\n---", re.MULTILINE)
TAG_LINE_RE = re.compile(r"^tags:\s*$")


def load_allowlist(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def extract_frontmatter(path: Path) -> str | None:
    content = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.search(content)
    return m.group(1) if m else None


def extract_tags_from_yaml(frontmatter: str) -> list[str]:
    # naive YAML tags extraction to avoid extra deps
    tags: list[str] = []
    lines = frontmatter.splitlines()
    in_tags = False
    for line in lines:
        if TAG_LINE_RE.match(line.strip()):
            in_tags = True
            continue
        if in_tags:
            if not line.strip().startswith("-"):
                break
            # expected format: - namespace:value
            value = line.strip()[1:].strip()
            tags.append(value)
    return tags


def validate_format(tag: str) -> tuple[bool, str | None]:
    if ":" not in tag:
        return False, "Tag must be in 'namespace:value' format"
    ns, val = tag.split(":", 1)
    if not re.fullmatch(r"[a-z][a-z0-9-]*", ns):
        return False, "Invalid namespace format"
    if not re.fullmatch(r"[a-z][a-z0-9-]*", val):
        return False, "Invalid value format"
    return True, None


def validate_against_allowlist(tag: str, allowlist: dict) -> tuple[bool, str | None]:
    ns, val = tag.split(":", 1)
    if ns not in allowlist:
        return False, f"Unknown namespace: {ns}"
    if val not in allowlist[ns]:
        return False, f"Value '{val}' not allowed for namespace '{ns}'"
    return True, None


def validate_rules(tags: list[str]) -> list[str]:
    errors: list[str] = []
    if not (3 <= len(tags) <= 10):
        errors.append("Tags must be between 3 and 10")

    required_namespaces = [
        "audience",
        "doc-type",
        "owner",
        "lifecycle",
        "sensitivity",
    ]

    for ns in required_namespaces:
        if not any(t.startswith(f"{ns}:") for t in tags):
            errors.append(f"Missing required namespace: {ns}")

    topic_count = sum(1 for t in tags if t.startswith("topic:"))
    if topic_count == 0:
        errors.append("At least 1 topic:* tag is required")
    if topic_count > 3:
        errors.append("No more than 3 topic:* tags allowed")

    return errors


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python tools/validate_tags.py <file1.md> [file2.md ...]")
        return 2

    allowlist = load_allowlist(Path(__file__).with_name("tags-allowlist.json"))
    exit_code = 0

    for path_str in sys.argv[1:]:
        path = Path(path_str)
        fm = extract_frontmatter(path)
        if fm is None:
            print(f"[FAIL] {path}: missing front matter")
            exit_code = 1
            continue

        tags = extract_tags_from_yaml(fm)
        if not tags:
            print(f"[FAIL] {path}: missing tags")
            exit_code = 1
            continue

        errors: list[str] = []

        for tag in tags:
            ok, msg = validate_format(tag)
            if not ok:
                errors.append(f"{tag}: {msg}")
                continue
            ok, msg = validate_against_allowlist(tag, allowlist)
            if not ok:
                errors.append(f"{tag}: {msg}")

        errors.extend(validate_rules(tags))

        if errors:
            print(f"[FAIL] {path}:")
            for e in errors:
                print(f"  - {e}")
            exit_code = 1
        else:
            # Additional rule: deprecated docs must include redirect
            fm_text = fm
            if any(t == "lifecycle:deprecated" for t in tags):
                if "deprecated_redirect:" not in fm_text:
                    print(f"[FAIL] {path}: Deprecated doc must have 'deprecated_redirect' in front matter")
                    exit_code = 1
                else:
                    print(f"[OK] {path} (deprecated with redirect)")
            else:
                print(f"[OK] {path}")

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())


