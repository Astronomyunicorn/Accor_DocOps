---
title: "Tagging System"
summary: "How documents are organized and filtered using namespace-based tags"
owner: "DocOps/Platform"
tags:
  - audience:developer
  - doc-type:reference
  - owner:platform
  - topic:architecture
  - topic:taxonomy
  - lifecycle:approved
  - sensitivity:internal
last_review: "2025-01-15"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---

# Tagging System

How documents are organized and filtered using namespace-based tags.

## Overview

Accor DocOps uses a **namespace-based tagging system** to classify documents across multiple dimensions. This enables faceted navigation and powerful filtering.

## Tag Structure

Tags follow the format: `namespace:value`

### Required Namespaces

Every document must have tags in these namespaces:

| Namespace | Purpose | Example Values |
|-----------|---------|---------------|
| `audience:` | Who reads this? | `audience:developer`, `audience:l1-support`, `audience:manager` |
| `doc-type:` | What format? | `doc-type:runbook`, `doc-type:howto`, `doc-type:reference` |
| `owner:` | Who owns this? | `owner:platform`, `owner:security`, `owner:network` |
| `topic:` | What is it about? | `topic:kubernetes`, `topic:api-gateway` (1-3 topics) |
| `lifecycle:` | Document status | `lifecycle:draft`, `lifecycle:approved`, `lifecycle:deprecated` |
| `sensitivity:` | Access level | `sensitivity:internal`, `sensitivity:confidential` |

### Optional Namespaces

| Namespace | Purpose | Example Values |
|-----------|---------|---------------|
| `region:` | Geography | `region:emea`, `region:amer`, `region:apac` |
| `incident-priority:` | For runbooks | `incident-priority:p0`, `incident-priority:p1` |

## Example

```yaml
---
tags:
  - audience:l1-support
  - doc-type:runbook
  - owner:platform
  - topic:api-gateway
  - topic:restart
  - lifecycle:approved
  - sensitivity:internal
  - incident-priority:p1
---
```

## Faceted Navigation

Tags enable automatic generation of facet pages:

- `/by-audience/` — Filter by role
- `/by-type/` — Filter by document type
- `/by-owner/` — Filter by owning team

Users can browse by these facets to find relevant documentation quickly.

## Validation

Tags are validated in two places:

1. **Pre-commit hooks** — Local validation before commit
2. **CI/CD** — Automated validation on every PR

Validation checks:
- ✅ Format: `namespace:value` (kebab-case)
- ✅ Required namespaces present
- ✅ Values match allowlist (`tools/tags-allowlist.json`)
- ✅ Total tags: 3-10 per document

## Tag Allowlist

Valid tag values are defined in `tools/tags-allowlist.json`. To add new values:

1. Update `tools/tags-allowlist.json`
2. Justify in PR description
3. Get approval
4. Merge to main

## Benefits

1. **Consistency** — Namespaces prevent tag conflicts
2. **Multi-dimensional** — Documents can be classified by multiple facets
3. **Automation** — Enables automated navigation generation
4. **Discoverability** — Better search and filtering
5. **Validation** — Automated checks ensure quality

## Related Documentation

- [ADR-003: Namespace-based Tagging](../decisions/0003-tag-system.md)
- [Taxonomy](../../taxonomy.md)

---

**Last Updated:** 2025-01-15

