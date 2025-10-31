---
title: "ADR-006: Documentation Standards and Templates"
summary: "Decision to establish documentation standards and use templates for consistency"
owner: "DocOps/Platform"
tags:
  - audience:developer
  - doc-type:reference
  - owner:platform
  - topic:architecture
  - topic:standards
  - lifecycle:approved
  - sensitivity:internal
last_review: "2025-01-15"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---

# ADR-006: Documentation Standards and Templates

## Status

✅ **Accepted** (Date: 2025-01-15)

## Context

**Problem:**
- Documentation from different teams lacks consistency
- Missing metadata (owner, review dates, tags)
- Inconsistent structure makes navigation difficult
- Hard to find documents due to missing front matter
- No clear templates for common document types

**Why this matters:**
- Inconsistent docs reduce trust and usability
- Missing metadata prevents automation (tagging, search, ownership)
- Review cycles are unclear without dates
- New contributors don't know where to start

## Decision

**Establish documentation standards with required front matter and templates.**

Every document must have:
- **Required front matter:**
  - `title` — Document title
  - `summary` — Brief description
  - `owner` — Responsible team/person
  - `tags` — Namespace-based tags (see ADR-003)
  - `last_review` — Last review date (YYYY-MM-DD)
  - `locale` — Language code (en, fr, etc.)
  - `service` — Service/system name
  - `version` — Document version
  - `outdated` — Boolean flag if translation is stale

- **Templates provided for:**
  - Architecture documents
  - How-to guides
  - Incident reports
  - Policies
  - Runbooks

## Alternatives Considered

### Alternative A: No Standards (Free-form)
- **Pros:** Maximum flexibility, no constraints
- **Cons:** Inconsistent structure, missing metadata, hard to automate
- **Why not chosen:** Doesn't solve consistency and automation problems

### Alternative B: Strict Schema (XML/JSON)
- **Pros:** Validatable, structured
- **Cons:** Too rigid, harder to write, not Markdown-friendly
- **Why not chosen:** Overkill, reduces writer productivity

### Alternative C: Guidelines Only (No Templates)
- **Pros:** Flexible, encourages creativity
- **Cons:** Inconsistent application, hard to enforce
- **Why not chosen:** Standards without templates are hard to follow

### Alternative D: Separate Metadata Files
- **Pros:** Clean separation, validatable
- **Cons:** Extra files to maintain, easy to get out of sync
- **Why not chosen:** Front matter keeps metadata with content

### Our Choice: Front Matter + Templates
**Why we chose this:**
- ✅ **Consistent Structure** — Templates ensure uniformity
- ✅ **Automation-Friendly** — Front matter enables automated checks
- ✅ **Writer-Friendly** — Markdown is easy to write
- ✅ **Validation** — Can validate front matter automatically
- ✅ **Searchable** — Metadata enables faceted search

## Consequences

### Positive ✅

1. **Consistency** — All documents follow same structure
2. **Automation** — Front matter enables automated checks and features
3. **Ownership** — Clear ownership model
4. **Review Cycles** — Review dates visible and trackable
5. **Templates** — New contributors know where to start
6. **Validation** — Can validate front matter in CI/CD

### Negative ❌

1. **Boilerplate** — Every document needs front matter
   - **Mitigation:** Templates reduce copy-paste, can use snippets
2. **Learning Curve** — Team needs to learn front matter format
   - **Mitigation:** Clear documentation, templates, validation errors
3. **Maintenance** — Need to keep templates updated
   - **Mitigation:** Templates are version controlled, easy to update

## Implementation Details

**Front Matter Format:**
```yaml
---
title: "Document Title"
summary: "Brief description"
owner: "Team/Person"
tags:
  - audience:developer
  - doc-type:reference
  - owner:platform
  - topic:example
  - lifecycle:approved
  - sensitivity:internal
last_review: "2025-01-15"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---
```

**Templates Location:** `templates/` directory
- `architecture.md`
- `how-to.md`
- `incident-report.md`
- `policy.md`
- `runbook.md`

**Validation:**
- Pre-commit hooks check for required fields
- CI/CD validates front matter on every PR
- Missing fields cause build warnings

**Documentation:**
- [DOCUMENTATION_STYLE.md](../../../../DOCUMENTATION_STYLE.md) — Style guide
- [STYLEGUIDE.md](../../../../STYLEGUIDE.md) — Writing guidelines
- [Taxonomy](../taxonomy.md) — Tag definitions

## Related Decisions

- [ADR-003: Namespace-based Tagging](./0003-tag-system.md)
- [ADR-005: Pre-commit Hooks](./0005-pre-commit-hooks.md)

## References

- [Templates Directory](../../../../templates/)
- [Documentation Style Guide](../../../../DOCUMENTATION_STYLE.md)

---

**Date:** 2025-01-15  
**Author:** DocOps Team  
**Approved By:** Platform Lead

