---
title: "Understanding the Architecture Structure"
summary: "Why we organize architecture documentation this way"
owner: "DocOps/Platform"
tags:
  - audience:developer
  - doc-type:reference
  - owner:platform
  - topic:architecture
  - topic:onboarding
  - lifecycle:approved
  - sensitivity:internal
last_review: "2025-01-15"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---

# Understanding the Architecture Structure

Why we organize architecture documentation this way.

## Overview

Accor DocOps uses a **practical, adapted architecture documentation structure** based on industry best practices
(Arc42, ADRs, C4 diagrams) but simplified for our use case.

## Key Principles

### 1. Document Decisions, Not Just Code

**ADRs (Architecture Decision Records)** document **why** we chose certain approaches:

- Why MkDocs? → [ADR-001](../governance/architecture/decisions/0001-use-mkdocs.md)
- Why GitHub Pages? → [ADR-002](../governance/architecture/decisions/0002-github-pages.md)
- Why namespace-based tags? → [ADR-003](../governance/architecture/decisions/0003-tag-system.md)

**Benefit:** New team members understand the reasoning behind choices.

### 2. Visual Diagrams for Quick Understanding

**C4 Diagrams** show system architecture at different levels:

- **Context** — Who uses the system and why
- **Containers** — Main deployment units (MkDocs, CI/CD, etc.)

**Benefit:** Visual overview is faster than reading prose.

### 3. Practical Focus Over Theory

We document **what exists**, not hypothetical architectures.

**Structure:**

```
governance/architecture/
├── README.md              # Hub for everything
├── decisions/             # ADRs (why we chose X)
├── c4-diagrams/           # Visual overview
└── platform-features/     # How features work
```

## Structure Explained

### Architecture Decisions (ADRs)

**Location:** `docs/en/governance/architecture/decisions/`

**Purpose:** Document important decisions about:

- Technology choices (MkDocs, GitHub Pages)
- Patterns (tagging system, CI/CD workflow)
- Standards (documentation format, templates)

**Format:** Each ADR follows template:

- Context (problem we're solving)
- Decision (what we chose)
- Alternatives (what we considered)
- Consequences (pros and cons)

**Example:** See [ADR-001](../governance/architecture/decisions/0001-use-mkdocs.md)

### C4 Diagrams

**Location:** `docs/en/governance/architecture/c4-diagrams/`

**Purpose:** Visual representation of system architecture.

**Levels:**

1. **Context** — High-level: users, external systems
2. **Containers** — Deployment units: MkDocs, CI/CD, GitHub Pages

**Why not 4 levels?**

- C4 has 4 levels (Context, Containers, Components, Code)
- We only use first 2 levels (sufficient for documentation platform)
- Components/Code level would be overkill

**See:**

- [Context Diagram](../governance/architecture/c4-diagrams/context.md)
- [Container Diagram](../governance/architecture/c4-diagrams/containers.md)

### Platform Features

**Location:** `docs/en/governance/architecture/platform-features/`

**Purpose:** Detailed documentation of how platform features work.

**Topics:**

- Tagging system
- Search and facets
- CI/CD workflow
- Quality checks

**Why separate from ADRs?**

- ADRs explain **why** we chose X
- Platform Features explain **how** X works

## What We Don't Include

### Full Arc42 Structure (12 Sections)

**Why not?**

- Arc42 designed for software products documenting their own architecture
- Accor DocOps is a documentation platform, not a software product
- Full Arc42 would be overkill (too heavy)

**What we use instead:**

- Essential sections only (ADRs, diagrams, features)
- Per-system documentation as needed
- Focus on practical, operational needs

### Detailed UML Diagrams

**Why not?**

- Operational docs focus on runbooks, not class diagrams
- C4 diagrams are more accessible
- Mermaid sequence diagrams sufficient for flows

**What we use instead:**

- Mermaid diagrams in Markdown (sequence, flowcharts)
- C4 diagrams for architecture overview
- Skip detailed UML (class, state machine)

## For New Team Members

**Where to start:**

1. Read [Architecture Overview](../governance/architecture/README.md)
2. Review [ADRs](../governance/architecture/decisions/README.md) — understand key decisions
3. Check [C4 Diagrams](../governance/architecture/c4-diagrams/) — visual overview
4. Explore [Platform Features](../governance/architecture/platform-features/) — how things work

**Questions?**

- See [FAQ](./faq.md)
- Ask in #docops Slack channel
- Check GitHub Issues

## Related Documentation

- [Architecture Overview](../governance/architecture/README.md)
- [All ADRs](../governance/architecture/decisions/README.md)
- [FAQ](./faq.md)

---

**Last Updated:** 2025-01-15

