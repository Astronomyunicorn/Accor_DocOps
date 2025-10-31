---
title: "ADR-004: GitHub Actions for CI/CD"
summary: "Decision to use GitHub Actions for continuous integration and deployment"
owner: "DocOps/Platform"
tags:
  - audience:developer
  - doc-type:reference
  - owner:platform
  - topic:architecture
  - topic:ci-cd
  - lifecycle:approved
  - sensitivity:internal
last_review: "2025-01-15"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---

# ADR-004: GitHub Actions for CI/CD

## Status

✅ **Accepted** (Date: 2025-01-15)

## Context

**Problem:**
- Manual deployment is error-prone and time-consuming
- Need automated quality checks (tag validation, link checking)
- Want to prevent broken links and invalid content from reaching production
- Need automatic deployment on merge to main branch
- Want PR previews for documentation changes

**Why this matters:**
- Documentation quality depends on automated validation
- Manual steps introduce human error
- Fast feedback loop improves developer experience
- PR previews help reviewers see actual rendered output

## Decision

**Use GitHub Actions for all CI/CD workflows.**

GitHub Actions will:
- Validate tags on every PR
- Check for broken links
- Run health checks (front matter, structure)
- Generate facet pages and statistics
- Build MkDocs site
- Deploy to GitHub Pages automatically
- Create PR previews for review

## Alternatives Considered

### Alternative A: Jenkins
- **Pros:** Mature, feature-rich, self-hosted
- **Cons:** Requires infrastructure, complex setup, maintenance overhead
- **Why not chosen:** Overkill for documentation, adds infrastructure burden

### Alternative B: GitLab CI
- **Pros:** Integrated with GitLab, powerful YAML-based config
- **Cons:** We use GitHub, not GitLab
- **Why not chosen:** Wrong platform

### Alternative C: CircleCI / Travis CI
- **Pros:** Good features, widely used
- **Cons:** External service, costs, additional configuration
- **Why not chosen:** GitHub Actions is free and integrated

### Alternative D: Manual Deployment
- **Pros:** Simple, no setup needed
- **Cons:** Error-prone, time-consuming, no validation, no previews
- **Why not chosen:** Doesn't solve any problems

### Our Choice: GitHub Actions
**Why we chose this:**
- ✅ **Free** for public repos (and included in GitHub Enterprise)
- ✅ **Integrated** — No external services needed
- ✅ **Simple** — YAML-based workflow files in `.github/workflows/`
- ✅ **Fast** — Runs on GitHub's infrastructure
- ✅ **Preview Support** — Can deploy PR previews
- ✅ **Matrix Support** — Can test multiple Python versions if needed

## Consequences

### Positive ✅

1. **Automated Quality Checks** — Tags, links, front matter validated automatically
2. **Fast Feedback** — Developers see issues immediately in PR
3. **No Manual Steps** — Deployment happens automatically on merge
4. **PR Previews** — Reviewers can see rendered documentation
5. **Consistency** — Every change goes through same validation pipeline
6. **Cost** — Free for GitHub-hosted repos

### Negative ❌

1. **GitHub Dependency** — Locked to GitHub platform
   - **Mitigation:** Acceptable trade-off, GitHub is our platform
2. **YAML Complexity** — Workflow files can become complex
   - **Mitigation:** Keep workflows simple, extract to scripts when needed
3. **Build Time** — Adds ~1-2 minutes to PR checks
   - **Mitigation:** Acceptable for documentation, parallel jobs possible

## Implementation Details

**Workflow Steps:**
1. Checkout code
2. Set up Python environment
3. Install dependencies (`requirements.txt`)
4. Run validation scripts:
   - `validate_tags.py` — Check tag format and allowlist
   - `check_links.py` — Validate internal/external links
   - `docs_health_check.py` — Front matter and structure checks
5. Generate facets (`generate_facets.py`)
6. Generate statistics (`generate_statistics.py`)
7. Build MkDocs site (`mkdocs build`)
8. Deploy to GitHub Pages (on merge to main)

**PR Previews:**
- Use GitHub Actions to deploy preview to temporary location
- Comment on PR with preview link
- Automatically cleaned up after PR closes

**Workflow Files:**
- `.github/workflows/docs.yml` — Main CI/CD workflow
- Can add more workflows as needed (e.g., monthly health reports)

## Related Decisions

- [ADR-001: Use MkDocs](./0001-use-mkdocs.md)
- [ADR-002: Deploy to GitHub Pages](./0002-github-pages.md)
- [ADR-005: Pre-commit Hooks](./0005-pre-commit-hooks.md)

## References

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [MkDocs GitHub Actions](https://github.com/marketplace?type=actions&query=mkdocs)

---

**Date:** 2025-01-15  
**Author:** DocOps Team  
**Approved By:** Platform Lead

