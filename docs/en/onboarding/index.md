---
title: "Getting Started with Accor DocOps"
summary: "Complete guide for newcomers to understand and contribute to the documentation platform"
owner: "DocOps/Platform"
tags:
  - audience:developer
  - doc-type:tutorial
  - owner:platform
  - topic:onboarding
  - lifecycle:approved
  - sensitivity:internal
last_review: "2025-01-15"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---

# Getting Started with Accor DocOps

Welcome! This guide will help you understand the Accor DocOps platform and start contributing.

## What is Accor DocOps?

Accor DocOps is a **documentation-as-code platform** that centralizes all IT documentation in one place:
- 📚 ITIL process guides
- 🔧 Runbooks and operational procedures
- 📖 Knowledge base articles
- 🏛️ Governance and policies
- 🚀 DevOps pipeline documentation

**Key features:**
- Version controlled (Git)
- Automated validation and deployment
- Multi-language support (EN/FR)
- Tagged and searchable
- Owner-driven with review cycles

## Quick Navigation

**New here?** Start with:
1. [Local Setup](#local-setup) — Get the site running on your machine
2. [Creating Your First Document](#creating-your-first-document) — Write your first page
3. [Contribution Workflow](../contributing.md) — How to submit changes

**Looking for specific information?**
- [FAQ](./faq.md) — Common questions
- [Architecture Overview](../governance/architecture/README.md) — How the platform works
- [Tagging Guide](../governance/taxonomy.md) — How to tag documents

## Local Setup

### Requirements

- Python 3.8 or higher
- Git
- Code editor (VS Code, PyCharm, etc.)

### Windows (Easiest Way)

Double-click `dev.bat` or run:
```cmd
dev.bat
```

The script automatically:
- Creates virtual environment
- Installs dependencies
- Starts local server

Open http://127.0.0.1:8000 in your browser.

### Manual Setup (All Platforms)

```bash
# 1. Clone repository
git clone <repository-url>
cd Accor_DocOps

# 2. Create virtual environment
python -m venv .venv

# 3. Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Start local server
mkdocs serve

# 6. Open http://127.0.0.1:8000
```

### Production Build

To build static site (for testing):
```bash
mkdocs build
# Output in site/ folder
```

## Creating Your First Document

### Step 1: Choose a Template

Templates are in `templates/` directory:
- `how-to.md` — Step-by-step guides
- `runbook.md` — Operational procedures
- `policy.md` — Policies and procedures
- `architecture.md` — System documentation
- `incident-report.md` — Incident postmortems

### Step 2: Copy Template

```bash
cp templates/how-to.md docs/en/kb/my-first-guide.md
```

### Step 3: Fill Front Matter

Every document needs front matter (YAML at top):

```yaml
---
title: "My First Guide"
summary: "Brief description"
owner: "Your Team/Your Name"
tags:
  - audience:developer  # Who reads this?
  - doc-type:howto       # What type?
  - owner:platform       # Who owns?
  - topic:example        # What topic?
  - lifecycle:draft      # Status
  - sensitivity:internal # Access level
last_review: "2025-01-15"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---
```

**Required fields:**
- `title`, `summary`, `owner`, `tags`, `last_review`, `locale`, `service`, `version`

### Step 4: Write Content

Use Markdown:
```markdown
## Introduction
This is my guide.

### Steps
1. Do this
2. Then that
3. Verify result
```

### Step 5: Preview Locally

```bash
mkdocs serve
# Open http://127.0.0.1:8000/kb/my-first-guide/
```

### Step 6: Validate

Before committing:
```bash
# Validate tags
python tools/validate_tags.py docs/en/kb/my-first-guide.md

# Check links (if any)
python tools/check_links.py docs/en/kb/my-first-guide.md
```

### Step 7: Commit and Push

```bash
git checkout -b docs/my-first-guide
git add docs/en/kb/my-first-guide.md
git commit -m "Add my first guide"
git push origin docs/my-first-guide
```

Then create a Pull Request on GitHub.

## Understanding the Structure

### Directory Structure

```
docs/en/
├── itil/          # ITIL process documentation
├── kb/            # Knowledge base (how-tos)
├── ops/           # Runbooks (operational procedures)
├── devops/        # DevOps pipeline docs
├── governance/    # Policies, taxonomy, architecture
├── by-audience/   # Auto-generated facet pages
├── by-type/       # Auto-generated facet pages
└── by-owner/      # Auto-generated facet pages
```

### Document Types

| Type | Location | Purpose |
|------|----------|---------|
| **Runbook** | `ops/` | Operational procedures (3 AM scenarios) |
| **How-to** | `kb/` | Step-by-step guides |
| **Reference** | Various | Documentation references |
| **Policy** | `governance/` | Policies and procedures |
| **Architecture** | `governance/architecture/` | System architecture |

### Tags Explained

Tags use **namespace:value** format:
- `audience:developer` — For developers
- `doc-type:howto` — How-to guide
- `owner:platform` — Owned by platform team
- `topic:kubernetes` — About Kubernetes

See [Taxonomy](../governance/taxonomy.md) for complete list.

## Contribution Workflow

1. **Create branch:** `docs/feature/<topic>`
2. **Make changes:** Edit Markdown files
3. **Preview locally:** `mkdocs serve`
4. **Validate:** Run validation tools
5. **Commit:** Follow commit message conventions
6. **Push:** Push branch to GitHub
7. **Create PR:** Pull Request with description
8. **Review:** Get approval from reviewer
9. **Merge:** Changes go live automatically

See [Contributing Guide](./contributing.md) for details.

## Common Tasks

### Adding Images

1. Save image to `docs/media/`
2. Reference in Markdown:
   ```markdown
   ![Description](../media/image.png)
   ```
3. Use relative paths from document location

### Linking Between Documents

Use relative paths:
```markdown
See [another document](../ops/example.md)
```

### Tagging Documents

Always include:
- `audience:` — Who reads this?
- `doc-type:` — What type?
- `owner:` — Who owns?
- `topic:` — What topic? (1-3)
- `lifecycle:` — Status
- `sensitivity:` — Access level

See [Taxonomy](../governance/taxonomy.md) for allowed values.

## Tools and Scripts

**Validation:**
- `tools/validate_tags.py` — Check tags
- `tools/check_links.py` — Check links
- `tools/docs_health_check.py` — Front matter validation

**Generation:**
- `tools/generate_facets.py` — Generate facet pages
- `tools/generate_statistics.py` — Generate statistics

**Help:**
```bash
python tools/validate_tags.py --help
```

## Getting Help

- **Slack:** #docops channel
- **GitHub Issues:** Create issue with question
- **FAQ:** See [FAQ](./faq.md)
- **Architecture:** See [Architecture Docs](../governance/architecture/README.md)

## Next Steps

1. ✅ Set up local environment
2. ✅ Read [Contributing Guide](./contributing.md)
3. ✅ Create your first document
4. ✅ Review [FAQ](./faq.md)
5. ✅ Explore [Architecture](../governance/architecture/README.md)

---

**Last Updated:** 2025-01-15

