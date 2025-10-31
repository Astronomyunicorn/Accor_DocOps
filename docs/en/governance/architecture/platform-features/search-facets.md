---
title: "Search & Facets"
summary: "How users find documentation quickly using search and faceted navigation"
owner: "DocOps/Platform"
tags:
  - audience:developer
  - doc-type:reference
  - owner:platform
  - topic:architecture
  - topic:search
  - lifecycle:approved
  - sensitivity:internal
last_review: "2025-01-15"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---

# Search & Facets

How users find documentation quickly using search and faceted navigation.

## Search Functionality

### Full-Text Search

Accor DocOps includes **client-side full-text search** powered by Lunr.js.

**Features:**
- ✅ Instant search results (no server round-trip)
- ✅ Searches title, content, and tags
- ✅ Highlights matching terms
- ✅ Supports multiple languages (per locale)

**How it works:**
1. During build, MkDocs generates search index (`search/search_index.json`)
2. Index is included in static site
3. Browser loads index and performs search client-side

### Search Usage

- **Keyboard shortcut:** `Ctrl+K` (or `Cmd+K` on Mac)
- **Search box:** Top navigation bar
- **Results:** Instant filtering as you type

## Faceted Navigation

Faceted navigation allows users to browse documents by predefined dimensions.

### Available Facets

1. **By Audience** (`/by-audience/`)
   - Filter by role: Developer, L1 Support, Manager, etc.
   - Example: `/by-audience/developer/` shows all developer-focused docs

2. **By Type** (`/by-type/`)
   - Filter by document format: Runbook, How-to, Reference, Policy
   - Example: `/by-type/runbook/` shows all operational runbooks

3. **By Owner** (`/by-owner/`)
   - Filter by owning team: Platform, Security, Network, etc.
   - Example: `/by-owner/platform/` shows all platform team docs

### Facet Generation

Facet pages are automatically generated during build by `mkdocs-tags` plugin:

1. Plugin scans all documents for tags
2. Groups documents by namespace (`audience`, `doc-type`, `owner`)
3. Generates index pages for each facet value
4. Includes last-updated dates from Git

**Generation script:** `tools/generate_facets.py` (optional enhancement)

## Navigation Structure

### Main Navigation

- Home
- Tags (all tags index)
- Browse by Audience
- Browse by Type
- Browse by Owner
- ITIL sections
- KB, Ops, DevOps, Governance

### Breadcrumbs

Material theme provides breadcrumb navigation showing current location:
```
Home > Governance > Architecture > Decisions > ADR-001
```

## Finding Documentation

### Scenario 1: "I need a runbook for API Gateway"

1. Navigate to **Ops (Runbooks)** in main nav
2. Or browse **By Type → Runbook**
3. Search for "api gateway"
4. Filter by `topic:api-gateway` if available

### Scenario 2: "What documentation exists for developers?"

1. Browse **By Audience → Developer**
2. See all developer-focused documentation
3. Filter further by type or topic

### Scenario 3: "I need security policies"

1. Browse **By Type → Policy**
2. Filter by `owner:security` (if facet page exists)
3. Or search for "security policy"

## Performance

- **Search index size:** Typically 100-500 KB (depends on content)
- **Load time:** < 1 second (index loaded on page load)
- **Search speed:** Instant (client-side, no network delay)
- **Facet generation:** Fast (generated at build time, not runtime)

## Limitations

1. **Client-side only** — Search index must be loaded in browser
2. **No fuzzy matching** — Exact word matching (Lunr.js limitations)
3. **No stemming** — "run" and "running" are different terms
4. **Static generation** — Facets generated at build time, not dynamic

## Future Enhancements

Potential improvements:
- Server-side search (Algolia, Elasticsearch) for larger sites
- Advanced filtering (combine multiple facets)
- Search analytics
- Popular searches / suggestions

## Related Documentation

- [Tagging System](./tagging-system.md)
- [ADR-003: Namespace-based Tagging](../decisions/0003-tag-system.md)

---

**Last Updated:** 2025-01-15

