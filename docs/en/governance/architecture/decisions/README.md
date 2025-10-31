---
title: "Architecture Decision Records (ADRs)"
summary: "All important architecture decisions for the platform"
owner: "DocOps/Platform"
tags:
  - audience:developer
  - doc-type:reference
  - owner:platform
  - topic:architecture
  - topic:adr
  - lifecycle:approved
  - sensitivity:internal
last_review: "2025-01-15"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---

# Architecture Decision Records (ADRs)

All important architecture decisions for Accor DocOps platform.

## Current Decisions

| # | Decision | Status | Date |
|---|----------|--------|------|
| [001](./0001-use-mkdocs.md) | Use MkDocs for documentation generation | ✅ Accepted | 2025-01-15 |
| [002](./0002-github-pages.md) | Deploy to GitHub Pages | ✅ Accepted | 2025-01-15 |
| [003](./0003-tag-system.md) | Namespace-based tag system | ✅ Accepted | 2025-01-15 |
| [004](./0004-ci-cd-pipeline.md) | GitHub Actions for CI/CD | ✅ Accepted | 2025-01-15 |
| [005](./0005-pre-commit-hooks.md) | Pre-commit hooks for validation | ✅ Accepted | 2025-01-15 |
| [006](./0006-documentation-standards.md) | Documentation standards and templates | ✅ Accepted | 2025-01-15 |

## Quick Stats

- **Total ADRs:** 6
- **Accepted:** 6
- **Proposed:** 0
- **Deprecated:** 0

## How to Add New ADR

1. Take next number (e.g., ADR-007)
2. Copy template (see below)
3. Fill all sections (Context, Decision, Alternatives, Consequences)
4. Get approval in PR (at least 1 reviewer)
5. Merge to main
6. Update this README with new entry

## ADR Template

```markdown
---
title: "ADR-NNN: Decision Title"
summary: "Brief summary of the decision"
owner: "DocOps/Platform"
tags:
  - audience:developer
  - doc-type:reference
  - owner:platform
  - topic:architecture
  - lifecycle:approved
  - sensitivity:internal
last_review: "YYYY-MM-DD"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---

# ADR-NNN: Decision Title

## Status

✅ Accepted / ⏳ Proposed / ❌ Deprecated

## Context

[What problem were we trying to solve?]
[Why do we need to make this decision?]

## Decision

[What did we decide? State clearly and concisely.]

## Alternatives Considered

### Alternative A: [Name]
- Pros: ...
- Cons: ...
- Why not chosen: ...

### Alternative B: [Name]
- Pros: ...
- Cons: ...
- Why not chosen: ...

### Our Choice: [Chosen Option]
Why we chose this: ...

## Consequences

### Positive ✅

- Benefit 1
- Benefit 2

### Negative ❌

- Drawback 1
- Drawback 2

## Related Decisions

- ADR-XXX: Related decision
- ADR-YYY: Another related decision

---

**Date:** YYYY-MM-DD  
**Author:** Name  
**Approved By:** Reviewer
```

## Questions?

- Slack: #docops-architecture
- GitHub Issues: Tag with `architecture`
- PR Review: Discuss in pull requests

---

**Last Updated:** 2025-01-15

