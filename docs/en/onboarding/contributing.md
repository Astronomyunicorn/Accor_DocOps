---
title: "Contributing to Accor DocOps"
summary: "How to contribute documentation changes"
owner: "DocOps/Platform"
tags:
  - audience:developer
  - doc-type:reference
  - owner:platform
  - topic:contributing
  - lifecycle:approved
  - sensitivity:internal
last_review: "2025-01-15"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---

# Contributing to Accor DocOps

How to contribute changes to the documentation platform.

## Branching Strategy

**Use feature branches:**
```bash
git checkout -b docs/feature/<topic>
```

**Examples:**
- `docs/feature/api-gateway-runbook`
- `docs/feature/kubernetes-howto`
- `docs/feature/governance-update`

## PR Checklist

Before submitting a Pull Request, ensure:

- [ ] **Front matter present** — All required fields (`title`, `summary`, `owner`, `tags`, `last_review`, `locale`, `service`, `version`)
- [ ] **Links are valid** — No broken internal or external links
- [ ] **Template used** — Used appropriate template from `/templates` if applicable
- [ ] **Images stored correctly** — Images in `docs/media/` (PNG/SVG) and properly referenced
- [ ] **Tags validated** — Tags match allowlist and format
- [ ] **Previewed locally** — Site builds and renders correctly (`mkdocs serve`)
- [ ] **Owner assigned** — Document has clear owner

## Local Validation (Optional but Recommended)

```bash
# Validate tags
python tools/validate_tags.py docs/en/your-file.md

# Check links
python tools/check_links.py docs/en/your-file.md

# Health check
python tools/docs_health_check.py docs/en/your-file.md
```

## Commit Message Format

**Good:**
```
docs: Add API Gateway restart runbook
```

**Better:**
```
docs: Add API Gateway restart runbook

- Includes health check steps
- Covers rollback procedure
- Links to monitoring dashboard
```

## PR Process

1. **Create branch** from `main`
2. **Make changes** to Markdown files
3. **Commit** with descriptive message
4. **Push** branch to GitHub
5. **Create Pull Request** with:
   - Clear description
   - Link to issue (if applicable)
   - Screenshots (if UI changes)
6. **Wait for review** — At least 1 reviewer (SME or DocOps team)
7. **Address feedback** — Update PR based on comments
8. **Merge** — After approval and CI passes

## Definition of Done

PR is ready to merge when:

- ✅ **PR approved** — At least 1 reviewer approved
- ✅ **CI green** — All validation checks pass
- ✅ **Staging preview OK** — Site renders correctly
- ✅ **Owner assigned** — Document has owner
- ✅ **Links working** — No broken links
- ✅ **Tags valid** — All tags match allowlist

## Review Process

**Who reviews?**
- Subject Matter Expert (SME) for content
- DocOps team for structure/format
- At least 1 approval required

**Review focuses on:**
- Content accuracy
- Tag correctness
- Link validity
- Front matter completeness
- Formatting consistency

## After Merge

- Changes automatically deploy to GitHub Pages
- Site updates within 1-2 minutes
- No manual steps required

## Questions?

- **Slack:** #docops channel
- **GitHub Issues:** Create issue with `contributing` tag
- **See also:** [FAQ](../onboarding/faq.md)

---

**Last Updated:** 2025-01-15

