---
title: "ADR-001: Use MkDocs for Documentation Generation"
summary: "Decision to use MkDocs static site generator for the documentation platform"
owner: "DocOps/Platform"
tags:
  - audience:developer
  - doc-type:reference
  - owner:platform
  - topic:architecture
  - topic:mkdocs
  - lifecycle:approved
  - sensitivity:internal
last_review: "2025-01-15"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---

# ADR-001: Use MkDocs for Documentation Generation

## Status

✅ **Accepted** (Date: 2025-01-15)

## Context

**Problem:**
- Documentation was scattered across Confluence, SharePoint, and various wikis
- No single source of truth
- Difficult to maintain consistency
- No version control for documentation
- Hard to automate quality checks and deployment

**Why this matters:**
- Teams spent time searching for information
- Outdated documentation caused confusion
- No clear ownership model
- Manual deployment process was error-prone

## Decision

**Use MkDocs as the static site generator for Accor DocOps platform.**

MkDocs will:
- Generate static HTML from Markdown files
- Provide built-in search functionality
- Support plugins for extended functionality (i18n, tags, etc.)
- Enable automated CI/CD deployment
- Maintain documentation as code (version controlled)

## Alternatives Considered

### Alternative A: Keep Confluence/SharePoint
- **Pros:** Team familiarity, existing content
- **Cons:** Vendor lock-in, limited automation, no version control, poor search
- **Why not chosen:** Doesn't solve the core problems of scattered docs and lack of automation

### Alternative B: Jekyll (GitHub Pages)
- **Pros:** Native GitHub Pages support, large community
- **Cons:** Ruby dependency, less intuitive for non-developers, plugin ecosystem less mature
- **Why not chosen:** MkDocs is simpler and Python-based (better fit for team)

### Alternative C: Docusaurus
- **Pros:** React-based, modern UI, built-in i18n
- **Cons:** More complex setup, requires Node.js, overkill for our needs
- **Why not chosen:** Too heavy for documentation-focused use case

### Alternative D: Hugo
- **Pros:** Fast builds, single binary
- **Cons:** Go templating less familiar, configuration more complex
- **Why not chosen:** MkDocs has better Markdown-first approach

### Our Choice: MkDocs
**Why we chose this:**
- ✅ Python-based (team expertise)
- ✅ Simple configuration (single YAML file)
- ✅ Excellent Markdown support
- ✅ Rich plugin ecosystem
- ✅ Material theme provides great UX
- ✅ Native i18n support via plugins
- ✅ Easy to automate in CI/CD

## Consequences

### Positive ✅

1. **Version Control** — All docs in Git, full history and PR workflow
2. **Automation** — CI/CD can validate, build, and deploy automatically
3. **Consistency** — Markdown format ensures consistent structure
4. **Search** — Built-in full-text search without external services
5. **Local Development** — Developers can preview changes locally with `mkdocs serve`
6. **Cost** — Free open-source tool, no licensing fees

### Negative ❌

1. **Learning Curve** — Team needs to learn Markdown (minimal, but present)
2. **Static Only** — No dynamic features (user comments, live edits)
3. **Build Step** — Requires build process (solved by CI/CD)
4. **Migration Effort** — Need to migrate existing content from other platforms

## Implementation Details

- **Configuration:** `mkdocs.yml` at project root
- **Theme:** Material for MkDocs
- **Plugins:** 
  - `mkdocs-static-i18n` (multilingual support)
  - `mkdocs-section-index` (better navigation)
  - `mkdocs-glightbox` (image galleries)
  - `mkdocs-tags` (tagging system)

## Related Decisions

- [ADR-002: Deploy to GitHub Pages](./0002-github-pages.md)
- [ADR-004: GitHub Actions for CI/CD](./0004-ci-cd-pipeline.md)

## References

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

---

**Date:** 2025-01-15  
**Author:** DocOps Team  
**Approved By:** Platform Lead

