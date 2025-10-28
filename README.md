
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

---

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

