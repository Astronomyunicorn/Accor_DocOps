---
title: "CI/CD Workflow"
summary: "Automated deployment pipeline for documentation"
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

# CI/CD Workflow

Automated deployment pipeline for Accor DocOps documentation.

## Overview

Every change to documentation goes through an automated CI/CD pipeline that validates, builds, and deploys the site.

## Workflow Stages

### 1. Trigger

**Events:**
- Push to `main` branch → Full build and deploy
- Pull Request → Validation and preview build
- Manual trigger (GitHub Actions UI)

**Workflow file:** `.github/workflows/docs.yml`

### 2. Checkout

```yaml
- uses: actions/checkout@v3
  with:
    fetch-depth: 0  # Full history for statistics
```

### 3. Setup Python

```yaml
- uses: actions/setup-python@v4
  with:
    python-version: '3.9'
```

### 4. Install Dependencies

```yaml
- run: pip install -r requirements.txt
```

Includes:
- MkDocs and plugins
- Validation tools dependencies

### 5. Validation

Runs quality checks:

| Check | Script | Purpose |
|-------|--------|---------|
| Tag validation | `tools/validate_tags.py` | Ensures tags match allowlist |
| Link checking | `tools/check_links.py` | Verifies no broken links |
| Health check | `tools/docs_health_check.py` | Validates front matter |
| Media check | `tools/check_media.py` | Ensures images exist |

**Failures:** PR fails if validation errors found

### 6. Generation

Generates additional content:

| Generator | Script | Output |
|-----------|--------|--------|
| Facet pages | `tools/generate_facets.py` | `/by-audience/`, `/by-type/`, etc. |
| Statistics | `tools/generate_statistics.py` | Home page stats |

### 7. Build

```yaml
- run: mkdocs build --clean
```

Builds static site to `site/` directory.

**Output:**
- HTML pages
- CSS/JavaScript assets
- Search index
- Media files

### 8. Deploy (Main Branch Only)

**Condition:** Only runs on push to `main` branch

```yaml
- name: Deploy
  if: github.ref == 'refs/heads/main'
  uses: peaceiris/actions-gh-pages@v3
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}
    publish_dir: ./site
    cname: # Custom domain if configured
```

**Process:**
1. Pushes `site/` contents to `gh-pages` branch
2. GitHub Pages automatically serves from `gh-pages`
3. Site updates within 1-2 minutes

## PR Workflow

For Pull Requests:

1. ✅ **Validation runs** — Same checks as main branch
2. ⚠️ **Build runs** — But does NOT deploy
3. 📝 **Status reported** — Success/failure in PR comments

**Benefits:**
- Catch errors before merge
- No broken content in production
- Fast feedback loop

## Preview Deployments (Optional)

Can be enhanced to create preview deployments:

```yaml
- name: Deploy Preview
  if: github.event_name == 'pull_request'
  # Deploy to temporary URL
  # Comment preview link on PR
```

## Workflow Timeline

**Typical run time:** 2-3 minutes

```
0:00 - Checkout code
0:10 - Setup Python
0:20 - Install dependencies
0:30 - Run validation
1:00 - Generate facets/statistics
1:30 - Build MkDocs site
2:00 - Deploy to GitHub Pages
2:30 - Complete
```

## Error Handling

### Validation Failures

- ❌ Tag validation fails → PR blocked, error message shown
- ❌ Link check fails → Warning in PR, can be merged with approval
- ❌ Build fails → PR blocked, MkDocs error shown

### Deployment Failures

- Retry logic: GitHub Actions retries automatically (3 attempts)
- Rollback: Previous version remains live (gh-pages branch history)
- Notification: GitHub Actions sends email on failure (if configured)

## Manual Triggers

Workflow can be triggered manually:

1. Go to **Actions** tab in GitHub
2. Select **Documentation** workflow
3. Click **Run workflow**
4. Choose branch and run

## Secrets & Variables

Currently used:
- `GITHUB_TOKEN` — Auto-provided, no setup needed

Future (if needed):
- Custom domain certificate
- External service API keys
- Deployment credentials

## Monitoring

- **Status badges:** Add to README to show build status
- **Notifications:** GitHub sends email on workflow failures
- **History:** All runs visible in Actions tab

## Related Documentation

- [ADR-004: GitHub Actions for CI/CD](../decisions/0004-ci-cd-pipeline.md)
- [GitHub Actions Workflow](../../../../.github/workflows/)

---

**Last Updated:** 2025-01-15

