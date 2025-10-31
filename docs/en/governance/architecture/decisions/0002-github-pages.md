---
title: "ADR-002: Deploy to GitHub Pages"
summary: "Decision to use GitHub Pages for hosting the documentation site"
owner: "DocOps/Platform"
tags:
  - audience:developer
  - doc-type:reference
  - owner:platform
  - topic:architecture
  - topic:github-pages
  - lifecycle:approved
  - sensitivity:internal
last_review: "2025-01-15"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---

# ADR-002: Deploy to GitHub Pages

## Status

✅ **Accepted** (Date: 2025-01-15)

## Context

**Problem:**
- Need reliable, free hosting for documentation site
- Must integrate with GitHub repository workflow
- Requires automatic deployment from CI/CD
- Should support custom domains (if needed in future)

**Why this matters:**
- Documentation needs to be publicly accessible (or within org)
- Manual deployment is error-prone and time-consuming
- Cost is a factor (no budget for dedicated hosting)
- GitHub is already our repository host

## Decision

**Use GitHub Pages for hosting the static documentation site.**

GitHub Pages will:
- Host the built static site from MkDocs
- Deploy automatically via GitHub Actions
- Provide HTTPS by default
- Support custom domains
- Offer free hosting for public repos (and private repos with GitHub Enterprise)

## Alternatives Considered

### Alternative A: Self-Hosted Web Server
- **Pros:** Full control, custom configuration
- **Cons:** Requires infrastructure, maintenance overhead, costs, SSL management
- **Why not chosen:** Too much overhead for documentation site

### Alternative B: AWS S3 + CloudFront
- **Pros:** Scalable, CDN benefits, enterprise-grade
- **Cons:** Setup complexity, costs (even if low), need to manage AWS resources
- **Why not chosen:** Overkill for internal documentation, adds complexity

### Alternative C: Netlify / Vercel
- **Pros:** Excellent DX, automatic deployments, free tier
- **Cons:** External dependency, potential vendor lock-in, may hit free tier limits
- **Why not chosen:** GitHub Pages integrates better with our workflow

### Alternative D: GitLab Pages
- **Pros:** Similar to GitHub Pages, integrated
- **Cons:** We use GitHub, not GitLab
- **Why not chosen:** Not applicable (wrong platform)

### Our Choice: GitHub Pages
**Why we chose this:**
- ✅ **Zero cost** for organization repositories
- ✅ **Native integration** with GitHub Actions
- ✅ **Automatic HTTPS** — no certificate management
- ✅ **Simple setup** — just enable Pages in settings
- ✅ **Custom domains** supported (if needed)
- ✅ **Reliable** — GitHub's infrastructure
- ✅ **PR previews** possible with GitHub Actions

## Consequences

### Positive ✅

1. **Zero Cost** — Free hosting for organization repos
2. **Simple Deployment** — Push to `gh-pages` branch or use GitHub Actions
3. **Automatic HTTPS** — Secure by default
4. **Reliability** — GitHub's proven infrastructure
5. **Integration** — Works seamlessly with GitHub Actions CI/CD

### Negative ❌

1. **Public Repos Only** — Free tier limited to public repos (private repos need Enterprise)
   - **Mitigation:** Use GitHub Enterprise for private repos
2. **Limited Customization** — Fewer options than self-hosted
   - **Mitigation:** Sufficient for documentation needs
3. **Rate Limits** — Very high limits, unlikely to hit for documentation
   - **Mitigation:** Not a concern for our use case

## Implementation Details

**Deployment Strategy:**
- Use GitHub Actions to build MkDocs site
- Deploy built `site/` folder to `gh-pages` branch
- GitHub Pages serves from `gh-pages` branch automatically

**Configuration:**
- Repository Settings → Pages → Source: `gh-pages` branch
- Custom domain: Can be configured if needed
- HTTPS: Enabled by default

**Workflow:**
1. Developer pushes to `main` branch
2. GitHub Actions builds site
3. GitHub Actions pushes to `gh-pages` branch
4. GitHub Pages automatically serves new version

## Related Decisions

- [ADR-001: Use MkDocs](./0001-use-mkdocs.md)
- [ADR-004: GitHub Actions for CI/CD](./0004-ci-cd-pipeline.md)

## References

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Actions for Pages](https://github.com/actions/deploy-pages)

---

**Date:** 2025-01-15  
**Author:** DocOps Team  
**Approved By:** Platform Lead

