---
title: "Frequently Asked Questions (FAQ)"
summary: "Common questions about Accor DocOps platform"
owner: "DocOps/Platform"
tags:
  - audience:developer
  - audience:manager
  - doc-type:reference
  - owner:platform
  - topic:faq
  - lifecycle:approved
  - sensitivity:internal
last_review: "2025-01-15"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---

# Frequently Asked Questions (FAQ)

Common questions about Accor DocOps platform.

## General

### What is Accor DocOps?

Accor DocOps is a **documentation-as-code platform** that centralizes IT documentation.
It replaces scattered Confluence pages, SharePoint sites, and wikis with a single, version-controlled,
searchable documentation hub.

### Why do we need this?

- **Single source of truth** — All docs in one place
- **Version control** — Full history, PR reviews
- **Automation** — Automatic validation and deployment
- **Search** — Find documents quickly
- **Ownership** — Clear ownership model with review cycles

### Who uses Accor DocOps?

- **Developers** — Technical documentation, architecture
- **L1/L2 Support** — Runbooks, troubleshooting guides
- **Managers** — Policies, governance, processes
- **Everyone** — Knowledge base, how-tos

## Technical

### How do I set up local development?

See [Getting Started](../onboarding/index.md#local-setup).

Quick version:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
```

### How do I add a new document?

1. Copy template from `templates/`
2. Fill front matter (YAML header)
3. Write content in Markdown
4. Preview locally (`mkdocs serve`)
5. Commit and create PR

See [Getting Started](../onboarding/index.md#creating-your-first-document).

### What's the difference between runbook and how-to?

- **Runbook** (`ops/`) — Operational procedure, used during incidents (e.g., "Restart API Gateway at 3 AM")
- **How-to** (`kb/`) — Step-by-step guide for common tasks (e.g., "How to reset VPN")

### How do I tag documents?

Use **namespace:value** format:

```yaml
tags:
  - audience:developer
  - doc-type:runbook
  - owner:platform
  - topic:kubernetes
  - lifecycle:approved
  - sensitivity:internal
```

See [Taxonomy](../governance/taxonomy.md) for allowed values.

### What happens when I push changes?

1. GitHub Actions validates tags, links, front matter
2. Builds MkDocs site
3. Deploys to GitHub Pages (if on `main` branch)
4. Site updates within 1-2 minutes

See [CI/CD Workflow](../governance/architecture/platform-features/ci-cd-workflow.md).

### How do I add images?

1. Save to `docs/media/`
2. Reference: `![Description](../media/image.png)`
3. Use relative paths from document location

### Can I edit documents in the browser?

No. Accor DocOps uses **documentation-as-code**:

- Edit Markdown files locally
- Commit to Git
- Changes deploy via CI/CD

This ensures version control and quality checks.

## Structure & Organization

### Where should I put my document?

| Content Type | Location |
|-------------|----------|
| Operational procedure | `docs/en/ops/` |
| How-to guide | `docs/en/kb/` |
| ITIL process | `docs/en/itil/<process>/` |
| Policy | `docs/en/governance/` |
| Architecture | `docs/en/governance/architecture/` |
| DevOps | `docs/en/devops/` |

### What are facet pages?

Auto-generated pages that filter documents by tags:

- `/by-audience/` — Filter by role (developer, manager, etc.)
- `/by-type/` — Filter by document type (runbook, howto, etc.)
- `/by-owner/` — Filter by owning team

Generated automatically during build.

### How does multilingual work?

- Each language has own folder: `docs/en/`, `docs/fr/`
- Documents must have `locale: en` or `locale: fr` in front matter
- Set `outdated: true` if translation lags behind English
- Images shared in `docs/media/`

See [Localization](../devops/localization.md).

## Quality & Validation

### Why did my PR fail validation?

Common reasons:

- **Missing front matter** — Required fields not present
- **Invalid tags** — Tags don't match allowlist or format
- **Broken links** — Links point to non-existent files
- **Build failure** — MkDocs can't build site

Check PR comments for details.

### How do I validate locally?

```bash
# Tags
python tools/validate_tags.py docs/en/your-file.md

# Links
python tools/check_links.py docs/en/your-file.md

# Front matter
python tools/docs_health_check.py docs/en/your-file.md
```

### What is the tag allowlist?

Valid tag values are defined in `tools/tags-allowlist.json`. To add new values:

1. Update allowlist file
2. Justify in PR description
3. Get approval

## Troubleshooting

### Site doesn't build locally

**Check:**

- Python version (3.8+)
- Virtual environment activated
- Dependencies installed (`pip install -r requirements.txt`)
- Front matter valid (YAML syntax)

**Common errors:**

- `ModuleNotFoundError` → Install dependencies
- YAML syntax error → Check front matter formatting

### Images not showing

**Check:**

- Image in `docs/media/`
- Correct relative path (e.g., `../media/image.png` from `kb/`)
- Image format (PNG, SVG, JPG)

### Links broken

**Check:**

- File exists at target path
- Correct relative path
- File extension included (`.md`)

### Pre-commit hooks failing

**Options:**

1. Fix the issue (recommended)
2. Skip with `git commit --no-verify` (not recommended)

CI will still validate, but local validation is faster.

## Architecture

### Why MkDocs?

See [ADR-001: Use MkDocs](../governance/architecture/decisions/0001-use-mkdocs.md).

**Key reasons:**

- Python-based (team expertise)
- Simple configuration
- Excellent Markdown support
- Rich plugin ecosystem

### Why GitHub Pages?

See [ADR-002: Deploy to GitHub Pages](../governance/architecture/decisions/0002-github-pages.md).

**Key reasons:**

- Free for organization repos
- Integrated with GitHub
- Automatic HTTPS
- Simple deployment

### How does the tagging system work?

See [ADR-003: Namespace-based Tagging](../governance/architecture/decisions/0003-tag-system.md).

**Key points:**

- Namespace prevents conflicts
- Multi-dimensional classification
- Enables faceted navigation
- Automated validation

## Still Have Questions?

- **Slack:** #docops channel
- **GitHub Issues:** Create issue with `faq` tag
- **Architecture Docs:** See [Architecture Overview](../governance/architecture/README.md)

---

**Last Updated:** 2025-01-15

