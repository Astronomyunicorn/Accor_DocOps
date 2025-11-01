---
title: "ADR-005: Pre-commit Hooks for Local Validation"
summary: "Decision to use pre-commit hooks for local validation before pushing"
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

# ADR-005: Pre-commit Hooks for Local Validation

## Status

✅ **Accepted** (Date: 2025-01-15)

## Context

**Problem:**

- Developers push invalid changes (broken tags, missing front matter)
- CI/CD catches errors, but feedback is delayed (after push)
- Wasted CI minutes on preventable errors
- Reviewers spend time on PRs with basic validation failures
- Need to catch errors locally before commit

**Why this matters:**

- Fast feedback improves developer experience
- Reduces CI load and costs
- Prevents broken content from being committed
- Teaches developers correct format immediately

## Decision

**Use pre-commit hooks to validate documentation locally before commit.**

Pre-commit hooks will:

- Validate tag format and allowlist
- Check for required front matter fields
- Validate Markdown syntax (optional)
- Check for common issues (broken links, missing images)
- Run before commit, preventing invalid commits

## Alternatives Considered

### Alternative A: CI/CD Only (No Local Validation)

- **Pros:** Simple, no local setup needed
- **Cons:** Delayed feedback, wasted CI resources, developers learn slowly
- **Why not chosen:** Too slow, doesn't solve developer experience issue

### Alternative B: Git Hooks (Manual Setup)

- **Pros:** Native Git, no external dependencies
- **Cons:** Manual setup per developer, harder to maintain, version control issues
- **Why not chosen:** Hard to maintain, inconsistent across team

### Alternative C: IDE Plugins

- **Pros:** Integrated with development environment
- **Cons:** Different IDEs, not all developers use same IDE, harder to enforce
- **Why not chosen:** Not universal, harder to enforce

### Alternative D: Pre-push Hooks Only

- **Pros:** Catches issues before pushing
- **Cons:** Still allows invalid commits, wastes time fixing after commit
- **Why not chosen:** Too late in the workflow

### Our Choice: Pre-commit Framework
**Why we chose this:**

- ✅ **Fast Feedback** — Errors caught before commit
- ✅ **Version Controlled** — Hook config in `.pre-commit-config.yaml`
- ✅ **Easy Setup** — `pre-commit install` one command
- ✅ **Extensible** — Can add custom hooks easily
- ✅ **Consistent** — Same validation across all developers
- ✅ **Optional** — Can be skipped with `--no-verify` if needed (emergency)

## Consequences

### Positive ✅

1. **Fast Feedback** — Developers see errors immediately
2. **Reduced CI Load** — Fewer validation failures in CI
3. **Education** — Developers learn correct format quickly
4. **Consistency** — Same checks for everyone
5. **Version Controlled** — Hook config is in repo, easy to update

### Negative ❌

1. **Setup Required** — Developers need to install pre-commit
   - **Mitigation:** One-time setup, documented in onboarding
2. **Commit Delay** — Validation adds ~5-10 seconds to commit
   - **Mitigation:** Acceptable trade-off, can be cached
3. **Can Be Bypassed** — `git commit --no-verify` skips hooks
   - **Mitigation:** CI still validates, bypass is discouraged

## Implementation Details

**Framework:** [pre-commit](https://pre-commit.com/) — Python-based hook framework

**Configuration:** `.pre-commit-config.yaml` in repository root

**Hooks:**

- `validate_tags.py` — Tag format and allowlist validation
- `check_links.py` — Internal link validation (quick check)
- Markdown formatter (optional) — Consistent formatting
- Trailing whitespace — Code quality

**Setup:**

```bash
pip install pre-commit
pre-commit install
```

**Usage:**

- Runs automatically on `git commit`
- Can run manually: `pre-commit run --all-files`
- Can skip if needed: `git commit --no-verify` (not recommended)

**CI Integration:**

- CI also runs same checks (pre-commit hooks can run in CI)
- Ensures consistency even if developer bypasses hooks

## Related Decisions

- [ADR-003: Namespace-based Tagging](./0003-tag-system.md)
- [ADR-004: GitHub Actions CI/CD](./0004-ci-cd-pipeline.md)
- [ADR-006: Documentation Standards](./0006-documentation-standards.md)

## References

- [Pre-commit Framework](https://pre-commit.com/)
- [Pre-commit Hooks Repository](https://github.com/pre-commit/pre-commit-hooks)

---

**Date:** 2025-01-15  
**Author:** DocOps Team  
**Approved By:** Platform Lead

