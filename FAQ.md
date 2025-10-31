# 📚 Accor DocOps — Frequently Asked Questions (FAQ)

> Complete reference guide combining all project documentation, onboarding instructions, and common questions in one place.

---

## 📖 Table of Contents

1. [About Accor DocOps](#about-accor-docops)
2. [Getting Started](#getting-started)
3. [Project Structure](#project-structure)
4. [ITIL Framework](#itil-framework)
5. [Creating & Editing Documents](#creating--editing-documents)
6. [Contribution Workflow](#contribution-workflow)
7. [Technical Setup](#technical-setup)
8. [Installing External Tools](#installing-external-tools)
9. [Quality & Validation](#quality--validation)
10. [Architecture & Design Decisions](#architecture--design-decisions)
11. [Troubleshooting](#troubleshooting)
12. [Localization (i18n)](#localization-i18n)

---

## About Accor DocOps

### What is Accor DocOps?

**Accor DocOps** is a **documentation-as-code platform** that centralizes all IT documentation in one place. It replaces scattered Confluence pages, SharePoint sites, and wikis with a single, version-controlled, searchable documentation hub.

**Key features:**
- 📚 ITIL process guides
- 🔧 Runbooks and operational procedures
- 📖 Knowledge base articles
- 🏛️ Governance and policies
- 🚀 DevOps pipeline documentation
- 🏷️ Flexible tagging system
- 🔍 Full-text search
- 🚀 Automated deployment (CI/CD)
- ✅ Document quality checks
- 👥 Audience-based navigation

### Why do we need this?

- **Single source of truth** — All docs in one place, no more hunting through seven different spaces
- **ITIL logic** — Incidents, problems, changes, service catalog, CMDB — every section where it belongs
- **Ownership & cadence** — Each page has an owner and a review date — transparency over "nobody's"
- **Automation** — Every change goes through CI/CD and lands on the site without manual heroics
- **Version control** — Full history, PR reviews, full transparency
- **Real bilingual** — EN/FR stay in sync; lagging translations are clearly flagged
- **Pain-free bilingual** — One-to-one EN/FR structure with "stale translation" flags

### Who uses Accor DocOps?

- **Developers** — Technical documentation, architecture, DevOps guides
- **L1/L2 Support** — Runbooks, troubleshooting guides, incident procedures
- **Managers** — Policies, governance, processes, ITIL documentation
- **Everyone** — Knowledge base, how-tos, reference documentation

### What makes this platform special?

- **Single source of truth** — Git history, PR reviews, full transparency
- **ITIL-friendly** — Process sections, artifacts, and a shared glossary — by the book
- **Built-in responsibility** — Owner, status, next review date — right in front-matter
- **CI/CD out of the box** — Markdown linter, link checker, PR preview, auto-deploy
- **Ready to grow** — From RACI & policies to Jira/ServiceNow links when needed
- **Faceted navigation** — Browse by Audience, Type, and Owner
- **Freshness tracking** — Facet pages show last modified dates from Git for each document

---

## Getting Started

### Quick Start (Windows - Easiest Way)

Just double-click `dev.bat` or run it from terminal:
```cmd
dev.bat
```

That's it! The script will:
- Create virtual environment (if needed)
- Install dependencies
- Start the development server

Open http://127.0.0.1:8000 in your browser.

### Manual Setup (All Platforms)

**Requirements:** Python 3.8+, Git, Code editor (VS Code, PyCharm, etc.)

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

### Pre-commit Hooks Setup

For local validation before committing:
```bash
pip install pre-commit
pre-commit install
```

---

## Project Structure

### Directory Structure

```
Accor_DocOps/
├─ docs/
│  ├─ en/                      # English
│  │  ├─ itil/
│  │  │  ├─ incident/          # Incident Management
│  │  │  ├─ problem/           # Problem Management
│  │  │  ├─ change/            # Change Enablement
│  │  │  ├─ cmdb/              # Configuration Management
│  │  │  └─ service-catalog/   # Service Catalog
│  │  ├─ kb/                   # Knowledge base (how-to)
│  │  ├─ ops/                  # Runbooks
│  │  ├─ devops/               # Pipelines & practices
│  │  ├─ governance/           # Policies, RACI, glossary
│  │  │  └─ architecture/      # Architecture docs, ADRs
│  │  ├─ onboarding/          # Getting started guides
│  │  ├─ by-audience/          # Auto-generated facet pages
│  │  ├─ by-type/              # Auto-generated facet pages
│  │  ├─ by-owner/             # Auto-generated facet pages
│  │  └─ media/                # Images & assets
│  ├─ fr/                      # French (mirror)
│  └─ templates/               # Shared document templates
├─ .github/workflows/docs.yml  # CI/CD for build & publish
├─ mkdocs.yml                  # Site config
├─ requirements.txt            # Dependencies
└─ tools/                      # Validation and generation scripts
```

### Document Types & Locations

| Content Type | Location | Purpose |
|-------------|----------|---------|
| **Runbook** | `docs/en/ops/` | Operational procedures (3 AM scenarios) |
| **How-to** | `docs/en/kb/` | Step-by-step guides |
| **Reference** | Various | Documentation references |
| **Policy** | `docs/en/governance/` | Policies and procedures |
| **Architecture** | `docs/en/governance/architecture/` | System architecture, ADRs |
| **ITIL Process** | `docs/en/itil/<process>/` | ITIL process documentation |
| **DevOps** | `docs/en/devops/` | Pipeline and deployment docs |

### Templates Available

Templates are in `templates/` directory:
- **Architecture** — System diagram, components, data flows
- **How-to Guide** — Step-by-step + "Troubleshooting" section
- **Incident Report** — ITIL post-mortem (RCA, corrective actions)
- **Policy** — Policy/procedure with owner and dates
- **Runbook** — What to do at 3 a.m. when things are on fire

Each template includes author, owner, review dates, tags, and version fields.

---

## ITIL Framework

### What is ITIL in Accor DocOps?

**Accor DocOps** is built around **ITIL-aligned structure** that organizes documentation by ITIL processes. This ensures that IT operations documentation follows industry best practices (ITIL 4) and is easy to find for different roles.

> **ITIL (Information Technology Infrastructure Library)** is a framework of best practices for delivering IT services. Accor DocOps organizes documentation following ITIL 4 practices.

### ITIL Processes in Accor DocOps

The platform includes five core ITIL practices:

| ITIL Practice | Location | Purpose | Audience |
|---------------|----------|---------|----------|
| **Incident Management** | `/itil/incident/` | Handle service interruptions | L1 Support, Service Desk |
| **Problem Management** | `/itil/problem/` | Identify root causes | L2 Support, Problem Managers |
| **Change Enablement** | `/itil/change/` | Manage changes safely | Change Managers, Developers |
| **Configuration Management (CMDB)** | `/itil/cmdb/` | Track IT assets | Infrastructure, Managers |
| **Service Catalog Management** | `/itil/service-catalog/` | Define and manage services | Service Owners, Managers |

### How ITIL Works in This Project

#### 1. Process Documentation Structure

Each ITIL process has its own section:

```
docs/en/itil/
├── incident/
│   └── index.md          # Incident Management overview
├── problem/
│   └── index.md          # Problem Management overview
├── change/
│   └── index.md          # Change Enablement overview
├── cmdb/
│   └── index.md          # CMDB overview
└── service-catalog/
    └── index.md          # Service Catalog overview
```

#### 2. Cross-Referenced Content

ITIL processes reference operational documentation:

- **Incident Management** → Links to runbooks in `/ops/`
- **Problem Management** → Links to troubleshooting guides in `/kb/`
- **Change Enablement** → Links to deployment guides in `/devops/`
- **All processes** → Link to policies in `/governance/`

#### 3. Integrated Workflows

Documentation flows follow ITIL workflows:

**Incident Flow:**
1. Incident detected → Check `/itil/incident/` for process
2. Use runbook → Follow procedure from `/ops/`
3. Escalate if needed → Reference `/itil/problem/` for problem management
4. Document incident → Use `incident-report.md` template
5. Create change if needed → Reference `/itil/change/` for change process

**Problem Flow:**
1. Problem identified → Check `/itil/problem/` for process
2. Root cause analysis → Use troubleshooting guides from `/kb/`
3. Create change → Follow `/itil/change/` process
4. Update CMDB → Update configuration in `/itil/cmdb/`

### ITIL Process Details

#### Incident Management

**Location:** `docs/en/itil/incident/`

**Purpose:** Restore normal service operation as quickly as possible

**Key Documentation:**
- Incident management process overview
- Links to operational runbooks (`/ops/`)
- Escalation procedures
- Links to problem management for recurring issues

**When to Use:**
- Service is down or degraded
- Need to restore service quickly
- During incident response

#### Problem Management

**Location:** `docs/en/itil/problem/`

**Purpose:** Identify root causes and prevent recurrence

**Key Documentation:**
- Problem management process
- Links to troubleshooting guides (`/kb/`)
- Root cause analysis procedures
- Links to change enablement for fixes

**When to Use:**
- Recurring incidents
- Need to find root cause
- Prevent future issues

#### Change Enablement

**Location:** `docs/en/itil/change/`

**Purpose:** Manage changes safely and minimize risk

**Key Documentation:**
- Change management process
- Links to deployment guides (`/devops/`)
- Change approval workflows
- Rollback procedures

**When to Use:**
- Planning a change
- Need change approval
- Deploying new features or fixes

#### Configuration Management (CMDB)

**Location:** `docs/en/itil/cmdb/`

**Purpose:** Track IT assets and their relationships

**Key Documentation:**
- CMDB structure and process
- Configuration item (CI) definitions
- Relationship mapping
- Update procedures

**When to Use:**
- Documenting infrastructure
- Tracking service dependencies
- Managing configuration items

#### Service Catalog Management

**Location:** `docs/en/itil/service-catalog/`

**Purpose:** Define and manage service offerings

**Key Documentation:**
- Service catalog structure
- Service definitions
- Service level agreements (SLAs)
- Service relationships

**When to Use:**
- Defining new services
- Updating service definitions
- Managing service portfolio

### ITIL Workflow Example

#### Complete Incident-to-Change Workflow

1. **Incident Detected**
   - Go to `/itil/incident/` → Understand process
   - Use runbook from `/ops/` → Restore service

2. **Incident Resolved**
   - Document in incident report (use `templates/incident-report.md`)
   - If recurring → Create problem in `/itil/problem/`

3. **Problem Management**
   - Investigate root cause using `/itil/problem/`
   - Use troubleshooting guides from `/kb/`

4. **Fix Identified**
   - Create change request → Follow `/itil/change/` process
   - Use deployment guide from `/devops/`

5. **Change Implemented**
   - Update CMDB → Document in `/itil/cmdb/`
   - Update service catalog if needed → `/itil/service-catalog/`

### Finding ITIL Documentation

#### By Navigation

1. Open main site
2. Click **ITIL** in navigation
3. Select process (Incident, Problem, Change, etc.)

#### By Tags

Search/filter by ITIL tags:
- `topic:itil-incident`
- `topic:itil-problem`
- `topic:itil-change`
- `topic:cmdb`
- `topic:service-catalog`

#### By Audience

- **L1 Support** → Incident Management, Runbooks
- **L2 Support** → Problem Management, Troubleshooting
- **Managers** → Change Enablement, CMDB, Service Catalog

### Creating ITIL Documentation

#### Step 1: Choose the Right Location

- **Process overview** → `/itil/<process>/`
- **Incident report** → Use `templates/incident-report.md`
- **Operational procedure** → `/ops/` (linked from ITIL)
- **Policy** → `/governance/` (linked from ITIL)

#### Step 2: Tag Correctly

Always include ITIL topic tag:
```yaml
tags:
  - topic:itil-incident    # For incident-related docs
  - topic:itil-problem     # For problem-related docs
  - topic:itil-change      # For change-related docs
```

#### Step 3: Cross-Reference

Link between ITIL processes and related documentation:
```markdown
See [Related Runbook](../../ops/runbook-example.md)
See [Change Process](../change/index.md)
See [Problem Management](../problem/index.md)
```

### Benefits of ITIL-Aligned Structure

1. **Industry Standard** — Follows ITIL 4 best practices
2. **Role Clarity** — Each process has clear audience
3. **Easy Navigation** — Processes organized logically
4. **Cross-References** — Documentation linked across processes
5. **Consistency** — Standardized structure and templates

### Integration with Other Sections

**ITIL → Operations:**
- `/itil/incident/` → `/ops/runbook-restart-apigw.md`
- `/itil/problem/` → `/kb/troubleshooting-guide.md`
- `/itil/change/` → `/devops/deployment-guide.md`

**ITIL → Governance:**
- `/itil/incident/` → `/governance/escalation-policy.md`
- `/itil/change/` → `/governance/change-policy.md`
- `/itil/service-catalog/` → `/governance/service-ownership.md`

**ITIL → Knowledge Base:**
- `/kb/how-to-reset-vpn.md` → Used in `/itil/incident/` workflows
- `/kb/troubleshooting.md` → Used in `/itil/problem/` workflows

For detailed ITIL documentation, see [ITIL Overview](docs/en/itil/README.md).

---

## Creating & Editing Documents

### Creating Your First Document

#### Step 1: Choose a Template

Copy appropriate template from `templates/`:
```bash
cp templates/how-to.md docs/en/kb/my-first-guide.md
```

#### Step 2: Fill Front Matter

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

#### Step 3: Write Content

Use Markdown:
```markdown
## Introduction
This is my guide.

### Steps
1. Do this
2. Then that
3. Verify result
```

#### Step 4: Preview Locally

```bash
mkdocs serve
# Open http://127.0.0.1:8000/kb/my-first-guide/
```

#### Step 5: Validate

Before committing:
```bash
# Validate tags
python tools/validate_tags.py docs/en/kb/my-first-guide.md

# Check links (if any)
python tools/check_links.py docs/en/kb/my-first-guide.md
```

### Adding Images

1. Save image to `docs/media/`
2. Reference in Markdown:
   ```markdown
   ![Description](../media/image.png)
   ```
3. Use relative paths from document location

**Rules:**
- Images must be in `docs/media/` (PNG/SVG/JPG)
- Use clear, descriptive names
- Include alt text for accessibility

### Linking Between Documents

Use relative paths:
```markdown
See [another document](../ops/example.md)
```

**Rules:**
- Include file extension (`.md`)
- Use relative paths from current document location
- Validate links before committing

### Tagging Documents

Always include required tags:

```yaml
tags:
  - audience:developer     # Required: Who reads this?
  - doc-type:howto          # Required: What type?
  - owner:platform          # Required: Who owns?
  - topic:kubernetes        # Required: 1-3 topics
  - topic:docker            # Optional: Additional topics
  - lifecycle:approved      # Required: Status
  - sensitivity:internal     # Required: Access level
```

**Tagging Rules:**
- Required namespaces: `audience`, `doc-type`, `owner`, `lifecycle`, `sensitivity`
- 1-3 `topic` tags required
- 3-10 tags total
- kebab-case, English only
- Format: `namespace:value`

See [Taxonomy Guide](docs/en/governance/taxonomy.md) for complete list of allowed values.

### What's the Difference Between Runbook and How-to?

- **Runbook** (`ops/`) — Operational procedure, used during incidents (e.g., "Restart API Gateway at 3 AM")
- **How-to** (`kb/`) — Step-by-step guide for common tasks (e.g., "How to reset VPN")

### Can I Edit Documents in the Browser?

**No.** Accor DocOps uses **documentation-as-code**:
- Edit Markdown files locally
- Commit to Git
- Changes deploy via CI/CD

This ensures version control and quality checks.

---

## Contribution Workflow

### Branching Strategy

**Use feature branches:**
```bash
git checkout -b docs/feature/<topic>
```

**Examples:**
- `docs/feature/api-gateway-runbook`
- `docs/feature/kubernetes-howto`
- `docs/feature/governance-update`

### Complete Workflow

1. **Create branch:** `docs/feature/<topic>`
2. **Make changes:** Edit Markdown files
3. **Preview locally:** `mkdocs serve`
4. **Validate:** Run validation tools
5. **Commit:** Follow commit message conventions
6. **Push:** Push branch to GitHub
7. **Create PR:** Pull Request with description
8. **Review:** Get approval from reviewer (at least 1)
9. **Merge:** Changes go live automatically

### PR Checklist

Before submitting a Pull Request, ensure:

- [ ] **Front matter present** — All required fields (`title`, `summary`, `owner`, `tags`, `last_review`, `locale`, `service`, `version`)
- [ ] **Links are valid** — No broken internal or external links
- [ ] **Template used** — Used appropriate template from `/templates` if applicable
- [ ] **Images stored correctly** — Images in `docs/media/` (PNG/SVG) and properly referenced
- [ ] **Tags validated** — Tags match allowlist and format
- [ ] **Previewed locally** — Site builds and renders correctly (`mkdocs serve`)
- [ ] **Owner assigned** — Document has clear owner

### Commit Message Format

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

### Definition of Done

PR is ready to merge when:

- ✅ **PR approved** — At least 1 reviewer approved (SME or DocOps team)
- ✅ **CI green** — All validation checks pass
- ✅ **Staging preview OK** — Site renders correctly
- ✅ **Owner assigned** — Document has owner
- ✅ **Links working** — No broken links
- ✅ **Tags valid** — All tags match allowlist

### Review Process

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

### After Merge

- Changes automatically deploy to GitHub Pages
- Site updates within 1-2 minutes
- No manual steps required

### Contribution Rules (Summary)

- All changes via pull/merge requests
- Minor edits → quick review; new pages → full review
- Keep EN/FR in sync and fill front-matter (owner, next review date, status)
- Store images in `media/`, use clear names, include alt text

---

## Technical Setup

### Requirements

- **Python:** 3.8 or higher
- **Git:** For version control
- **Code editor:** VS Code, PyCharm, etc. (optional but recommended)

### Local Development Setup

See [Getting Started](#getting-started) section above for detailed instructions.

### What Happens When I Push Changes?

1. **GitHub Actions** triggers CI/CD workflow
2. **Validation** runs:
   - Tag validation
   - Link checking
   - Front matter validation
   - Health checks
3. **Generation** runs:
   - Facet pages generation
   - Statistics generation
4. **Build** runs:
   - MkDocs builds static site
5. **Deploy** runs (main branch only):
   - Pushes to `gh-pages` branch
   - GitHub Pages serves new version
6. **Site updates** within 1-2 minutes

### Auto-Publish (GitHub Pages)

Setup (one-time):
1. Push repo to GitHub
2. Enable GitHub Actions
3. Pages → **Deploy from a branch** → `gh-pages`
4. Done: each push to `main` builds & deploys, PRs get a live preview

The workflow runs:
- ✅ Markdown lint & link check
- ✅ Site build
- ✅ Deploy to Pages + PR preview

### Content Quality Toolkit

**Validation tools:**
- `tools/validate_tags.py` — Validate tags against allowlist
- `tools/check_links.py` — Check for broken links
- `tools/docs_health_check.py` — Validate front matter
- `tools/check_media.py` — Check for orphaned images

**Generation tools:**
- `tools/generate_facets.py` — Generate facet pages
- `tools/generate_statistics.py` — Generate statistics

**Usage:**
```bash
# Validate tags
python tools/validate_tags.py docs/en/your-file.md

# Check links
python tools/check_links.py docs/en/your-file.md

# Health check
python tools/docs_health_check.py docs/en/your-file.md
```

### Installing External Tools

#### Vale (Style Checking)

**Vale** is an optional tool for checking writing style and grammar. It's not required for basic development but recommended for quality checks.

**Installation (Windows - Direct Download):**

1. **Download Vale:**
   - Go to: https://github.com/errata-ai/vale/releases/latest
   - Download: `vale_X.X.X_Windows_x64.zip` (e.g., `vale_v3.0.11_Windows_x64.zip`)
   - Extract the archive

2. **Add to PATH:**
   - Extract to `C:\Program Files\Vale\` (create folder if needed)
   - Add to PATH:
     - Press `Win + Pause` → Advanced system settings
     - Environment Variables → Path → Edit
     - Add → `C:\Program Files\Vale`
     - OK → OK → OK
   - **Open a NEW terminal** (PATH updates only in new sessions)

3. **Verify Installation:**
   ```cmd
   vale --version
   # Should show: vale v3.0.11 (or similar)
   ```

4. **Create Styles Directory:**
   ```cmd
   mkdir .vale\styles
   ```

5. **Test:**
   ```cmd
   vale docs/en/index.md
   ```

**Alternative Installation Methods:**

- **Chocolatey:** `choco install vale` (if Chocolatey is installed)
- **Scoop:** `scoop install vale` (if Scoop is installed)

**If Vale is Not Found:**

1. Check that you opened a **new terminal** (PATH updates require new session)
2. Use full path: `"C:\Program Files\Vale\vale.exe" --version`
3. Check PATH: `echo %PATH%` (should contain Vale path)

**Note:** Vale is optional. Scripts will skip Vale checks if it's not installed.

**For detailed setup, see:** [Vale Setup Guide](docs/en/devops/vale-setup.md)

#### Markdownlint

**Markdownlint-cli2** is a Node.js tool for Markdown linting.

**Installation:**
```bash
npm install -g markdownlint-cli2
```

**Note:** Markdownlint is optional. Scripts will skip it if not installed.

---

## Quality & Validation

### Why Did My PR Fail Validation?

Common reasons:
- **Missing front matter** — Required fields not present
- **Invalid tags** — Tags don't match allowlist or format
- **Broken links** — Links point to non-existent files
- **Build failure** — MkDocs can't build site

**Check PR comments** for detailed error messages.

### How Do I Validate Locally?

```bash
# Tags
python tools/validate_tags.py docs/en/your-file.md

# Links
python tools/check_links.py docs/en/your-file.md

# Front matter
python tools/docs_health_check.py docs/en/your-file.md
```

### What is the Tag Allowlist?

Valid tag values are defined in `tools/tags-allowlist.json`. 

**To add new values:**
1. Update allowlist file
2. Justify in PR description
3. Get approval
4. Merge to main

### Pre-commit Hooks

**Setup:**
```bash
pip install pre-commit
pre-commit install
```

**What they do:**
- Run automatically on `git commit`
- Validate tags (quick check)
- Check front matter (quick check)
- Remove trailing whitespace
- Optional: Markdown formatting

**Can be bypassed:**
- `git commit --no-verify` (not recommended)
- CI will still validate, but local validation is faster

---

## Architecture & Design Decisions

### Why MkDocs?

**Key reasons:**
- Python-based (team expertise)
- Simple configuration (single YAML file)
- Excellent Markdown support
- Rich plugin ecosystem
- Material theme provides great UX
- Native i18n support via plugins
- Easy to automate in CI/CD

See [ADR-001: Use MkDocs](docs/en/governance/architecture/decisions/0001-use-mkdocs.md) for full decision record.

### Why GitHub Pages?

**Key reasons:**
- Free for organization repos
- Integrated with GitHub
- Automatic HTTPS
- Simple deployment
- Reliable infrastructure

See [ADR-002: Deploy to GitHub Pages](docs/en/governance/architecture/decisions/0002-github-pages.md) for full decision record.

### Why Namespace-based Tagging?

**Key reasons:**
- Namespaces prevent conflicts (e.g., `audience:developer` vs `topic:developer`)
- Multi-dimensional classification
- Enables faceted navigation
- Automated validation

See [ADR-003: Namespace-based Tagging](docs/en/governance/architecture/decisions/0003-tag-system.md) for full decision record.

### Architecture Decisions (ADRs)

All important decisions are documented as ADRs:

| ADR | Decision | Status |
|-----|---------|--------|
| [0001](docs/en/governance/architecture/decisions/0001-use-mkdocs.md) | Use MkDocs for generation | ✅ Accepted |
| [0002](docs/en/governance/architecture/decisions/0002-github-pages.md) | Deploy to GitHub Pages | ✅ Accepted |
| [0003](docs/en/governance/architecture/decisions/0003-tag-system.md) | Namespace-based tagging | ✅ Accepted |
| [0004](docs/en/governance/architecture/decisions/0004-ci-cd-pipeline.md) | GitHub Actions CI/CD | ✅ Accepted |
| [0005](docs/en/governance/architecture/decisions/0005-pre-commit-hooks.md) | Local validation hooks | ✅ Accepted |
| [0006](docs/en/governance/architecture/decisions/0006-documentation-standards.md) | Documentation standards | ✅ Accepted |

See [All ADRs](docs/en/governance/architecture/decisions/README.md) for complete list.

---

## Troubleshooting

### Site Doesn't Build Locally

**Check:**
- Python version (3.8+)
- Virtual environment activated
- Dependencies installed (`pip install -r requirements.txt`)
- Front matter valid (YAML syntax)

**Common errors:**
- `ModuleNotFoundError` → Install dependencies
- YAML syntax error → Check front matter formatting

### Images Not Showing

**Check:**
- Image in `docs/media/`
- Correct relative path (e.g., `../media/image.png` from `kb/`)
- Image format (PNG, SVG, JPG)

### Links Broken

**Check:**
- File exists at target path
- Correct relative path
- File extension included (`.md`)

### Pre-commit Hooks Failing

**Options:**
1. Fix the issue (recommended)
2. Skip with `git commit --no-verify` (not recommended)

CI will still validate, but local validation is faster.

### Vale Not Found / Installation Issues

**Problem:** Vale command not recognized or installation failed.

**Solution 1: Direct Installation (Recommended)**
1. Download from: https://github.com/errata-ai/vale/releases/latest
2. Extract to `C:\Program Files\Vale\` (create folder if needed)
3. Add to PATH:
   - Press `Win + Pause` → Advanced system settings → Environment Variables
   - Edit PATH → Add → `C:\Program Files\Vale`
   - OK → OK → OK
4. **Open a NEW terminal** (PATH updates only in new sessions)
5. Verify: `vale --version`

**Solution 2: Fix Chocolatey Lock**
If Chocolatey installation failed with lock error:
```cmd
# Run PowerShell as Administrator
Remove-Item "C:\ProgramData\chocolatey\lib\6d8188623a479a68c9b2b6ef3ae860f7d58ec215" -Force
choco install vale -y
```

**Solution 3: Use Full Path**
If Vale is installed but not in PATH:
```cmd
"C:\Program Files\Vale\vale.exe" --version
```

**Note:** Vale is optional. Scripts will work without it, just skipping Vale checks.

**For detailed instructions:** See [Installing External Tools](#installing-external-tools) section.

### Validation Errors

**Tag validation:**
- Check format: `namespace:value` (kebab-case)
- Check allowlist: `tools/tags-allowlist.json`
- Ensure required namespaces present

**Link validation:**
- Verify file exists
- Check relative path
- Ensure correct file extension

**Front matter validation:**
- Check all required fields present
- Verify YAML syntax
- Check date format: YYYY-MM-DD

---

## Localization (i18n)

### Overview

The project supports multiple languages via the `mkdocs-static-i18n` plugin.

- **Default language:** `en`
- **Already available:** `en`, `fr`
- **Ready to add:** new locales can be plugged in (e.g., `de`, `es`, `ru`)

### How Multilingual Works

- Each language has own folder: `docs/en/`, `docs/fr/`
- Documents must have `locale: en` or `locale: fr` in front matter
- Set `outdated: true` if translation lags behind English
- Images shared in `docs/media/`

### Adding a New Locale

**Quick version:**
1. Create `docs/<locale>/` (e.g., `docs/ru/`)
2. Copy needed pages from `docs/en/` and translate them
3. In each page's front matter set: `locale: "<locale>"`; if not aligned with EN yet, set `outdated: true`
4. Images are shared across languages: keep them in `docs/media/` and use relative links like `../../../media/<image>.png` from nested sections
5. Update `mkdocs.yml`: add the new locale under `nav:` and include it in the language switcher `extra.alternate`
6. Build the site: `mkdocs build --clean` or preview locally with `mkdocs serve`

**Detailed guide:** See [Localization Documentation](docs/en/devops/localization.md)

### Technical Notes

- `mkdocs-static-i18n` is added in `requirements.txt`
- `i18n` plugin is enabled in `mkdocs.yml` (folder-based structure)
- Language switcher is configured via `extra.alternate`

### Translation Status

When a translation lags behind EN, mark the page `outdated: true` so readers see the status until it's updated.

---

## Additional Resources

### Navigation

- **Main Documentation Site:** [Live Site](https://example.github.io/accor-docops)
- **Getting Started:** [Onboarding Guide](docs/en/onboarding/index.md)
- **Architecture:** [Architecture Overview](docs/en/governance/architecture/README.md)
- **Contributing:** [Contributing Guide](docs/en/onboarding/contributing.md)
- **Taxonomy:** [Tag Definitions](docs/en/governance/taxonomy.md)

### Facet Pages

Auto-generated pages that filter documents by tags:
- `/by-audience/` — Filter by role (developer, manager, etc.)
- `/by-type/` — Filter by document type (runbook, howto, etc.)
- `/by-owner/` — Filter by owning team

Generated automatically during build.

### Getting Help

- **Slack:** #docops channel
- **GitHub Issues:** Create issue with appropriate tag (`faq`, `architecture`, `contributing`)
- **Documentation:** Browse [Onboarding Section](docs/en/onboarding/)

---

## Quick Reference

### Common Commands

```bash
# Setup
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Development
mkdocs serve              # Local server
mkdocs build             # Build static site

# Validation
python tools/validate_tags.py docs/en/file.md
python tools/check_links.py docs/en/file.md
python tools/docs_health_check.py docs/en/file.md

# Pre-commit
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

### Common Paths

- **Templates:** `templates/`
- **Documentation:** `docs/en/`
- **Media:** `docs/media/`
- **Tools:** `tools/`
- **Config:** `mkdocs.yml`

### Tag Examples

```yaml
# Runbook
tags:
  - audience:l1-support
  - doc-type:runbook
  - owner:platform
  - topic:api-gateway
  - lifecycle:approved
  - sensitivity:internal
  - incident-priority:p1

# How-to Guide
tags:
  - audience:developer
  - doc-type:howto
  - owner:platform
  - topic:kubernetes
  - lifecycle:approved
  - sensitivity:internal

# Policy
tags:
  - audience:manager
  - doc-type:policy
  - owner:security
  - topic:access-control
  - lifecycle:approved
  - sensitivity:internal
```

---

**Last Updated:** 2025-01-15  
**Maintained By:** DocOps/Platform Team

For detailed documentation, visit the [live site](https://example.github.io/accor-docops) or browse `docs/en/` directory.

