
# 📚 Accor DocOps — One Home for Documentation

> Documentation as a product: clear, predictable, ITIL‑aligned — no more swamps of stale pages.

![Accor DocOps hero](docs/media/hero.png)

**Accor DocOps** is a documentation‑as‑code platform that puts everything in one place, sets common rules, and removes chaos across Confluence, SharePoint, and scattered wikis. Two languages (EN/FR), clear owners, scheduled reviews, and a lean CI/CD wheel that ships changes automatically — so knowledge stays fresh and trustworthy.

---

## 🎯 Why this matters

- **Single entry point.** No more hunting through seven different spaces — everything is here.
- **ITIL logic.** Incidents, problems, changes, service catalog, CMDB — every section where it belongs.
- **Ownership & cadence.** Each page has an owner and a review date — transparency over "nobody's".
- **Automation.** Every change goes through CI/CD and lands on the site without manual heroics.
- **Pain‑free bilingual.** EN/FR stay in sync; lagging translations are clearly flagged.

---

## 🧭 Documentation structure

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
│  │  └─ media/                # Images & assets
│  ├─ fr/                      # French (mirror)
│  └─ templates/               # Shared document templates
├─ .github/workflows/docs.yml  # CI/CD for build & publish
├─ mkdocs.yml                  # Site config
└─ requirements.txt            # Dependencies
```

Why it's convenient:
- **Feels like a metro map:** ITIL branches with smart cross‑links — hard to get lost.
- **Templates & metadata:** consistent pages that are easy to search and maintain.
- **Scales cleanly:** add sections/languages without rewriting the world.

---

## ✨ Highlights

- **Single source of truth.** Git history, PR reviews, full transparency.
- **Real bilingual.** One‑to‑one EN/FR structure with "stale translation" flags.
- **ITIL‑friendly.** Process sections, artifacts, and a shared glossary — by the book.
- **Built‑in responsibility.** Owner, status, next review date — right in front‑matter.
- **CI/CD out of the box.** Markdown linter, link checker, PR preview, auto‑deploy.
- **Ready to grow.** From RACI & policies to Jira/ServiceNow links when needed.

### Faceted navigation and freshness
- **Facets:** Browse by Audience, Type, and Owner in the EN nav.
- **Last Updated:** Facet pages show last modified dates from Git for each document.
- **Stats on Home:** Total docs and lifecycle coverage auto-updated during CI.

---

## 🌍 Localization (i18n)

The project supports multiple languages via the `mkdocs-static-i18n` plugin.

- **Default language:** `en`
- **Already available:** `en`, `fr`
- **Ready to add:** new locales can be plugged in (e.g., `de`, `es`, `ru`)

Detailed how-to for vendors and translators: `docs/en/devops/localization.md` (site path: `/en/devops/localization/`).

How to add a new locale (short version):
1. Create `docs/<locale>/` (e.g., `docs/ru/`).
2. Copy the needed pages from `docs/en/` and translate them.
3. In each page’s front matter set: `locale: "<locale>"`; if not aligned with EN yet, set `outdated: true`.
4. Images are shared across languages: keep them in `docs/media/` and use relative links like `../../../media/<image>.png` from nested sections.
5. Update `mkdocs.yml`: add the new locale under `nav:` and include it in the language switcher `extra.alternate`.
6. Build the site: `mkdocs build --clean` or preview locally with `mkdocs serve`.

Technical notes:
- `mkdocs-static-i18n` is added in `requirements.txt`.
- `i18n` plugin is enabled in `mkdocs.yml` (folder-based structure) and the language switcher is configured.

When a translation lags behind EN, mark the page `outdated: true` so readers see the status until it’s updated.

## 🚀 Quick start

**Requirements:** Python 3.8+, Git

### Windows (Easy way)

Just double-click `dev.bat` or run it from terminal:
```cmd
dev.bat
```

That's it! The script will:
- Create virtual environment (if needed)
- Install dependencies
- Start the development server

Open http://127.0.0.1:8000 in your browser.

### Manual setup (all platforms)

```bash
# Clone
git clone <repository-url>
cd Accor_DocOps

# Virtual env
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install & run locally
pip install -r requirements.txt
mkdocs serve
# Open http://127.0.0.1:8000
```

**Production build**
```bash
mkdocs build
# Static site in the site/ folder
```

### Content quality toolkit
- Tags validator: `python tools/validate_tags.py docs/en/...`
- Facet generator: `python tools/generate_facets.py`
- Stats generator: `python tools/generate_statistics.py`
- Health check: `python tools/docs_health_check.py`
- Internal link check: `python tools/check_links.py`
- Orphan media check: `python tools/check_media.py`

Pre-commit setup:
```bash
pip install pre-commit
pre-commit install
```

Tagging rules (short):
- Required namespaces per doc: `audience`, `doc-type`, `owner`, `lifecycle`, `sensitivity`; 1–3 `topic`
- 3–10 tags total; kebab-case, english
- Deprecated docs must include `deprecated_redirect` in front matter

---

## 🌍 Auto‑publish (GitHub Pages)

1) Push the repo to GitHub  
2) Enable GitHub Actions  
3) Pages → **Deploy from a branch** → `gh-pages`  
4) Done: each push to `main` builds & deploys, PRs get a live preview.

The workflow runs:
- ✅ Markdown lint & link check  
- ✅ Site build  
- ✅ Deploy to Pages + PR preview

---

## 🛠️ Templates (in `templates/`)

- **Architecture** — system diagram, components, data flows  
- **How‑to Guide** — step‑by‑step + "Troubleshooting" section  
- **Incident Report** — ITIL post‑mortem (RCA, corrective actions)  
- **Policy** — policy/procedure with owner and dates  
- **Runbook** — what to do at 3 a.m. when things are on fire

Each template includes author, owner, review dates, tags, and version fields.

---

## 🤝 Contribution rules (short)

- All changes via pull/merge requests.  
- Minor edits → quick review; new pages → full review.  
- Keep EN/FR in sync and fill front‑matter (owner, next review date, status).  
- Store images in `media/`, use clear names, include alt text.

---

## 🖼️ Screenshots

![Site cover](docs/media/cover.png)

**ITIL tiles:**
- ![Incident Management tile](docs/media/itil-incident.png)
- ![Problem Management tile](docs/media/itil-problem.png)
- ![Change Enablement tile](docs/media/itil-change.png)

*(Keep all visual assets in `docs/media/` so they're always handy.)*

---

## ✅ Bottom line

This repo has a **solid, grown‑up structure** that saves time, tames search, and makes updates a natural part of team work. You can feel the thinking behind **roles, review cycles, and bilingual content**, while automation kills the busywork.

