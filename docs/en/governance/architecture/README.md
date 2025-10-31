---
title: "Architecture & Design Documentation"
summary: "Platform architecture, design decisions, and system diagrams"
owner: "DocOps/Platform"
tags:
  - audience:developer
  - audience:manager
  - doc-type:reference
  - owner:platform
  - topic:architecture
  - topic:docops
  - lifecycle:approved
  - sensitivity:internal
last_review: "2025-01-15"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---

# Architecture & Design Documentation

Architecture of Accor DocOps platform and design principles.

> 📋 **New here?** Start with [System Overview](#overview)  
> 🎯 **Looking for a decision?** See [Architecture Decisions](decisions/README.md)  
> 📊 **Need diagrams?** Open [C4 Context Diagram](c4-diagrams/context.md)

## Overview

**Accor DocOps** — centralized documentation management platform with:

- 🏷️ Flexible tagging system
- 🔍 Full-text search
- 🚀 Automated deployment (CI/CD)
- ✅ Document quality checks
- 👥 Audience-based navigation

## Architecture Decisions

All important decisions are documented as ADRs:

| ADR | Decision | Status |
|-----|---------|--------|
| [0001](./decisions/0001-use-mkdocs.md) | Use MkDocs for generation | ✅ Accepted |
| [0002](./decisions/0002-github-pages.md) | Deploy to GitHub Pages | ✅ Accepted |
| [0003](./decisions/0003-tag-system.md) | Namespace-based tagging | ✅ Accepted |
| [0004](./decisions/0004-ci-cd-pipeline.md) | GitHub Actions CI/CD | ✅ Accepted |
| [0005](./decisions/0005-pre-commit-hooks.md) | Local validation hooks | ✅ Accepted |
| [0006](./decisions/0006-documentation-standards.md) | Documentation standards | ✅ Accepted |

[All ADRs →](decisions/README.md)

## System Architecture

### High-Level Flow

```
┌─────────────┐
│ Developer  │
└──────┬──────┘
       │ pushes docs
       ▼
┌──────────────────────────────────┐
│ GitHub Repository (Markdown)     │
│ - Documentation files            │
│ - Config (mkdocs.yml)            │
│ - Scripts (tools/)               │
└──────┬───────────────────────────┘
       │ webhook
       ▼
┌──────────────────────────────────┐
│ GitHub Actions (CI/CD)           │
│ ├─ Validate tags                 │
│ ├─ Health check                  │
│ ├─ Generate facets               │
│ ├─ Build (mkdocs)                │
│ └─ Deploy                        │
└──────┬───────────────────────────┘
       │ publishes to
       ▼
┌──────────────────────────────────┐
│ GitHub Pages (Static Site)       │
│ - Live documentation             │
│ - Search index                   │
│ - Tagging facets                 │
└──────┬───────────────────────────┘
       │
       ▼
┌──────────────────────────────────┐
│ Team reads docs                  │
│ - Filtered by audience          │
│ - Filtered by doc type          │
│ - Full-text search              │
└──────────────────────────────────┘
```

For detailed diagrams, see [C4 Context Diagram](c4-diagrams/context.md) and [C4 Containers Diagram](c4-diagrams/containers.md).

## Platform Features

- **[Tagging System](./platform-features/tagging-system.md)** — How docs are organized and filtered
- **[Search & Facets](./platform-features/search-facets.md)** — Finding docs quickly
- **[CI/CD Workflow](./platform-features/ci-cd-workflow.md)** — Automated deployment
- **[Quality Checks](./platform-features/quality-checks.md)** — Ensuring doc quality

## Related Documentation

- [Taxonomy](../taxonomy.md) — Tag definitions and usage
- [Onboarding](../../onboarding/index.md) — Getting started guide for newcomers
- [Contributing](../../onboarding/contributing.md) — How to add new docs

---

**Last Updated:** 2025-01-15

