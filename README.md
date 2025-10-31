
# 📚 Accor DocOps — Your Centralized Documentation Hub

Documentation as a product: transparent, ITIL-aligned, role-based accountability. No more "document swamps" of outdated pages!

![Accor DocOps hero](docs/media/hero.png)

## 🎯 Why This Matters

- **One entry point**: Stop hunting across six different systems — everything is here in one place.
- **ITIL-structured**: Incidents, problems, changes, CMDB, and service catalog — each section where it belongs.
- **Clear accountability**: Every page has an owner and review date — you always know who's responsible.
- **Automated delivery**: Changes go through CI/CD — updates hit the site without manual effort.
- **Painless bilingual**: English and French stay synchronized; outdated translations are flagged automatically.

## 🧩 Documentation Architecture

```
Accor_DocOps/
├─ docs/
│  ├─ en/                  # English documentation
│  │  ├─ itil/             # ITIL processes
│  │  ├─ kb/               # Knowledge base (how-to guides)
│  │  ├─ ops/              # Operational runbooks
│  │  ├─ devops/           # CI/CD practices
│  │  ├─ governance/       # Policies, RACI, glossary
│  │  └─ media/            # All images & assets
│  ├─ fr/                  # French documentation (mirror)
│  └─ templates/           # Shared templates
├─ .github/workflows/docs.yml  # CI/CD automation
├─ mkdocs.yml                  # Site configuration
└─ requirements.txt            # Dependencies
```

**What makes this work:**

- **ITIL roadmap**: Navigate by process — impossible to get lost.
- **Templated & tagged**: All pages follow the same structure; search and maintenance are effortless.
- **Scales cleanly**: Add a language or new section — just a few minutes of setup.

## ✨ Key Features

- **Single source of truth**: Git history, PR reviews, transparent change log.
- **Real bilingual support**: EN ↔ FR, translation status always visible.
- **ITIL by the book**: Processes, artifacts, shared glossary — standards built in.
- **Ownership & cadence**: Each document shows its owner, status, and next review date — accountability is visible.
- **CI/CD included**: Markdown linting, link checking, PR previews, auto-deploy.
- **Built to grow**: Add RACI, policies, Jira/ServiceNow integrations — everything supported.

## 🧭 Faceted Navigation + Fresh Content

- **Smart filtering**: Browse by Audience, Document Type, or Owner — find what you need instantly.
- **Last updated**: Facet pages display when each document was last modified (pulled from Git).
- **Live statistics**: Homepage shows document count and lifecycle coverage — auto-updated during CI/CD runs.

## 🌍 Localization (i18n)

- **Two languages supported**: EN/FR (ready to add: DE, ES, RU, etc.).
- **Folder-based structure**: Each locale gets its own folder: `docs/<locale>/`.
- **Translation status**: Pages out of sync with English are marked `outdated` automatically.
- **Shared assets**: All images live in `docs/media/` — no duplication.
- **Built-in technology**: Uses `mkdocs-static-i18n` — add a new language in the config and you're done.

## 🚀 Quick Start

### Windows (Easiest Way)

```cmd
dev.bat
```

That's it! The script will:

- Create virtual environment (if needed)
- Install dependencies
- Start the dev server on http://127.0.0.1:8000

### Any OS

```bash
git clone <repository-url>
cd Accor_DocOps
python -m venv .venv
.venv\Scripts\activate    # Windows
source .venv/bin/activate # macOS/Linux
pip install -r requirements.txt
mkdocs serve
```

Open http://127.0.0.1:8000 in your browser.

### Content Quality Toolkit

Run any of these commands to validate your documentation:

- **Validate tags**: `python tools/validate_tags.py docs/en/...`
- **Generate facets**: `python tools/generate_facets.py`
- **Update statistics**: `python tools/generate_statistics.py`
- **Health check**: `python tools/docs_health_check.py`
- **Link validation**: `python tools/check_links.py`
- **Find orphan media**: `python tools/check_media.py`

Setup pre-commit hooks (local validation before every commit):

```bash
pip install pre-commit
pre-commit install
```

Now every commit runs checks automatically — catch errors before they hit the repo!

## 🛠️ Document Templates

Each template includes required metadata: author, owner, tags, version, and review dates.

- **Architecture** — System diagrams, components, data flows
- **How-to Guide** — Step-by-step instructions + troubleshooting section
- **Incident Report** — ITIL post-mortem (RCA + corrective actions)
- **Policy** — Policies & procedures with ownership and review cycles
- **Runbook** — "What to do at 3 a.m. when things are on fire"

## 🖼️ Visual Examples

ITIL Process Tiles:

- — Incident Management
- — Problem Management
- — Change Enablement

*(All visual assets are stored in `docs/media/` — keeps everything organized.)*

## 🤝 Contributing Guidelines

- **All changes via pull/merge requests** — no direct pushes to main.
- **Review process**: Quick turnaround for minor fixes; full review for new pages.
- **Keep EN/FR synchronized** — update both versions and fill front-matter metadata.
- **Asset management**: Store all images in `docs/media/` with descriptive names and alt text.

## 🌍 Auto-Publishing to GitHub Pages

1) Push to GitHub  
2) Enable GitHub Actions in repository settings  
3) Pages → **Deploy from a branch** → choose `gh-pages`  
4) Done! Every push to `main` automatically builds and deploys.

**What happens in each CI/CD run:**

- ✅ Markdown linting & validation
- ✅ Internal link checking
- ✅ Facet generation
- ✅ Statistics update
- ✅ Site build
- ✅ Deploy to GitHub Pages
- ✅ PR preview (optional)

## ✅ Why This Works

Accor DocOps is a mature documentation platform where content lives, updates predictably, and helps teams stay aligned.

You can see the thoughtfulness in the architecture:

- **Roles & accountability** — every page has a clear owner
- **Review cycles** — nothing gets stale
- **Bilingual first** — EN/FR aren't an afterthought
- **Automation** — CI/CD takes the pain out of publishing

**Result?** Documentation that actually stays current and useful.

## 📘 Full Documentation

Everything else — see [FAQ.md](FAQ.md).

That's where you'll find:

- Setup instructions
- Tagging rules
- Troubleshooting
- Best practices
- All other questions answered

Ready to get started?

Pick your platform above ⬆️ and follow the Quick Start steps. Questions? Check [FAQ.md](FAQ.md) or open an issue.

