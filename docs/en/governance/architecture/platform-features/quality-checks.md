---
title: "Quality Checks"
summary: "Automated quality assurance for documentation"
owner: "DocOps/Platform"
tags:
  - audience:developer
  - doc-type:reference
  - owner:platform
  - topic:architecture
  - topic:quality
  - lifecycle:approved
  - sensitivity:internal
last_review: "2025-01-15"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---

# Quality Checks

Automated quality assurance ensures documentation meets standards.

## Overview

Quality checks run at two stages:
1. **Pre-commit** (local) — Catch errors before commit
2. **CI/CD** (server) — Final validation before merge

## Check Types

### 1. Tag Validation

**Script:** `tools/validate_tags.py`

**Checks:**
- ✅ Required namespaces present (`audience`, `doc-type`, `owner`, `topic`, `lifecycle`, `sensitivity`)
- ✅ Tag format: `namespace:value` (kebab-case)
- ✅ Values match allowlist (`tools/tags-allowlist.json`)
- ✅ Tag count: 3-10 tags per document
- ✅ No duplicate tags

**Failure:** PR blocked if invalid tags found

**Example:**
```bash
$ python tools/validate_tags.py docs/en/governance/
✅ All tags valid
```

### 2. Link Checking

**Script:** `tools/check_links.py`

**Checks:**
- ✅ Internal links resolve to existing files
- ✅ External links are accessible (HTTP status check)
- ✅ No broken image references
- ✅ No orphaned files (files not linked from anywhere)

**Failure:** Warning in PR (non-blocking), can be merged with approval

**Example:**
```bash
$ python tools/check_links.py docs/en/
⚠️  Broken link: docs/en/example.md -> docs/en/missing.md
```

### 3. Front Matter Validation

**Script:** `tools/docs_health_check.py`

**Checks:**
- ✅ Required fields present: `title`, `summary`, `owner`, `tags`, `last_review`, `locale`, `service`, `version`
- ✅ `last_review` format: YYYY-MM-DD
- ✅ `outdated` flag: boolean (true/false)
- ✅ `locale` matches file location (e.g., `locale: en` for `docs/en/`)

**Failure:** PR blocked if critical fields missing

**Example:**
```yaml
# ❌ Missing required field
---
title: "Example"
# Missing: summary, owner, tags, etc.
---

# ✅ Valid front matter
---
title: "Example"
summary: "Brief description"
owner: "Platform"
tags: [...]
last_review: "2025-01-15"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---
```

### 4. Media Validation

**Script:** `tools/check_media.py`

**Checks:**
- ✅ Referenced images exist in `docs/media/`
- ✅ No orphaned images (images not referenced anywhere)
- ✅ Image format: PNG, SVG, or JPG

**Failure:** Warning in PR

**Example:**
```bash
$ python tools/check_media.py docs/en/
⚠️  Orphaned image: docs/media/unused.png
```

### 5. Markdown Linting (Optional)

**Tool:** `mdformat` or `markdownlint`

**Checks:**
- ✅ Consistent formatting
- ✅ No trailing whitespace
- ✅ Proper heading hierarchy
- ✅ Code block formatting

**Status:** Optional, can be enabled in pre-commit

## Pre-commit Hooks

**Setup:**
```bash
pip install pre-commit
pre-commit install
```

**Runs:**
- Automatically on `git commit`
- Can skip: `git commit --no-verify` (not recommended)

**Hooks:**
1. Tag validation (quick check)
2. Front matter check (quick check)
3. Trailing whitespace removal
4. Markdown formatting (optional)

**Benefits:**
- ✅ Fast feedback (errors before commit)
- ✅ Reduces CI load
- ✅ Teaches correct format

## CI/CD Validation

**Location:** `.github/workflows/docs.yml`

**Runs:**
- On every push to `main`
- On every Pull Request

**Checks:**
1. Full tag validation (all files)
2. Link checking (all internal/external links)
3. Front matter validation (all files)
4. Media validation (all images)
5. Build check (MkDocs builds successfully)

**Output:**
- ✅ Pass: Green checkmark in PR
- ❌ Fail: Red X with error details

## Quality Metrics

### Coverage

- **Tag validation:** 100% of documents
- **Link checking:** 100% of links
- **Front matter:** 100% of documents
- **Media:** All referenced images

### Metrics Dashboard (Future)

Potential enhancements:
- Documentation freshness (by `last_review` date)
- Tag usage statistics
- Link health over time
- Build success rate

## Bypassing Checks

### When to Bypass

**Never bypass these:**
- Tag validation (required for navigation)
- Front matter validation (required for automation)

**Can bypass with approval:**
- External link failures (may be temporary)
- Media warnings (if intentional)

### How to Bypass

1. Fix the issue (preferred)
2. Document reason in PR description
3. Get explicit approval from reviewer
4. Merge with understanding that issue will be tracked

## Continuous Improvement

**Monthly Review:**
- Review validation failures
- Update allowlists as needed
- Enhance checks based on common errors
- Document patterns and solutions

## Related Documentation

- [ADR-005: Pre-commit Hooks](../decisions/0005-pre-commit-hooks.md)
- [ADR-006: Documentation Standards](../decisions/0006-documentation-standards.md)
- [Tools README](../../../devops/TOOLS_README.md)

---

**Last Updated:** 2025-01-15

