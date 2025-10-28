# Contributing

## Branching
- Use feature branches: `docs/feature/<topic>`
- All changes go via Pull Request (PR) with at least 1 reviewer (SME or DocOps).

## Checklist for PRs
- [ ] Front matter present (`title, summary, owner, tags, last_review, locale, service, version`)
- [ ] Links are valid (no broken links)
- [ ] Uses a template from `/templates` where applicable
- [ ] Images are stored in `docs/media` (PNG/SVG) and properly referenced

## Local Lint (optional)
```bash
mdformat --check docs
```

## Definition of Done
- PR approved and CI green
- Staging preview renders OK
- Owner assigned
