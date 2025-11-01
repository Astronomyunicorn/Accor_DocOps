---
title: "ITIL in Accor DocOps"
summary: "How ITIL framework is integrated into the documentation platform"
owner: "ITIL/Governance"
tags:
  - audience:manager
  - audience:developer
  - doc-type:reference
  - owner:platform
  - topic:itil
  - topic:governance
  - lifecycle:approved
  - sensitivity:internal
last_review: "2025-01-15"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---

# ITIL in Accor DocOps

How the ITIL framework is integrated into the Accor DocOps documentation platform.

## Overview

**Accor DocOps** is built around **ITIL-aligned structure** that organizes documentation by ITIL processes.
This ensures that IT operations documentation follows industry best practices and is easy to find for different roles.

> **ITIL (Information Technology Infrastructure Library)** is a framework of best practices for delivering IT services.
Accor DocOps organizes documentation following ITIL 4 practices.

## ITIL Processes in Accor DocOps

The platform includes five core ITIL practices:

| ITIL Practice | Location | Purpose | Audience |
|---------------|----------|---------|----------|
| **Incident Management** | `/itil/incident/` | Handle service interruptions | L1 Support, Service Desk |
| **Problem Management** | `/itil/problem/` | Identify root causes | L2 Support, Problem Managers |
| **Change Enablement** | `/itil/change/` | Manage changes safely | Change Managers, Developers |
| **Configuration Management (CMDB)** | `/itil/cmdb/` | Track IT assets | Infrastructure, Managers |
| **Service Catalog Management** | `/itil/service-catalog/` | Define and manage services | Service Owners, Managers |

## How ITIL Works in This Project

### 1. Process Documentation Structure

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

### 2. Cross-Referenced Content

ITIL processes reference operational documentation:

- **Incident Management** → Links to runbooks in `/ops/`
- **Problem Management** → Links to troubleshooting guides in `/kb/`
- **Change Enablement** → Links to deployment guides in `/devops/`
- **All processes** → Link to policies in `/governance/`

### 3. Integrated Workflows

Documentation flows follow ITIL workflows:

**Incident Flow:**

1. **Incident detected** → Check `/itil/incident/` for process
2. **Use runbook** → Follow procedure from `/ops/`
3. **Escalate if needed** → Reference `/itil/problem/` for problem management
4. **Document incident** → Use `incident-report.md` template
5. **Create change if needed** → Reference `/itil/change/` for change process

**Problem Flow:**

1. **Problem identified** → Check `/itil/problem/` for process
2. **Root cause analysis** → Use troubleshooting guides from `/kb/`
3. **Create change** → Follow `/itil/change/` process
4. **Update CMDB** → Update configuration in `/itil/cmdb/`

### 4. Role-Based Access

ITIL processes are tagged for specific audiences:

| Process | Primary Audience | Tags |
|---------|------------------|------|
| Incident Management | L1 Support | `audience:l1-support`, `owner:service-desk` |
| Problem Management | L2 Support | `audience:l2-support`, `owner:service-desk` |
| Change Enablement | Managers | `audience:manager`, `owner:platform` |
| CMDB | Managers, Infrastructure | `audience:manager`, `owner:infra` |
| Service Catalog | Managers | `audience:manager`, `owner:apps` |

### 5. Documentation Templates

Templates support ITIL processes:

- **Incident Report** (`templates/incident-report.md`) — Post-incident analysis
- **Runbook** (`templates/runbook.md`) — Operational procedures
- **Policy** (`templates/policy.md`) — ITIL policies with RACI

## ITIL Process Details

### Incident Management

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

### Problem Management

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

### Change Enablement

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

### Configuration Management (CMDB)

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

### Service Catalog Management

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

## Integration with Other Sections

### ITIL → Operations

ITIL processes reference operational documentation:

```
/itil/incident/  →  /ops/runbook-restart-apigw.md
/itil/problem/   →  /kb/troubleshooting-guide.md
/itil/change/    →  /devops/deployment-guide.md
```

### ITIL → Governance

ITIL processes follow governance policies:

```
/itil/incident/     →  /governance/escalation-policy.md
/itil/change/       →  /governance/change-policy.md
/itil/service-catalog/  →  /governance/service-ownership.md
```

### ITIL → Knowledge Base

Knowledge base supports ITIL processes:

```
/kb/how-to-reset-vpn.md  →  Used in /itil/incident/ workflows
/kb/troubleshooting.md    →  Used in /itil/problem/ workflows
```

## Finding ITIL Documentation

### By Navigation

1. Open main site
2. Click **ITIL** in navigation
3. Select process (Incident, Problem, Change, etc.)

### By Tags

Search/filter by ITIL tags:

- `topic:itil-incident`
- `topic:itil-problem`
- `topic:itil-change`
- `topic:cmdb`
- `topic:service-catalog`

### By Audience

- **L1 Support** → Incident Management, Runbooks
- **L2 Support** → Problem Management, Troubleshooting
- **Managers** → Change Enablement, CMDB, Service Catalog

## Creating ITIL Documentation

### Step 1: Choose the Right Location

- **Process overview** → `/itil/<process>/`
- **Incident report** → Use `templates/incident-report.md`
- **Operational procedure** → `/ops/` (linked from ITIL)
- **Policy** → `/governance/` (linked from ITIL)

### Step 2: Tag Correctly

Always include ITIL topic tag:

```yaml
tags:
  - topic:itil-incident    # For incident-related docs
  - topic:itil-problem     # For problem-related docs
  - topic:itil-change      # For change-related docs
```

### Step 3: Cross-Reference

Link between ITIL processes and related documentation:

```markdown
See [Related Runbook](../../ops/runbook-example.md)
See [Change Process](../change/index.md)
See [Problem Management](../problem/index.md)
```

## ITIL Workflow Example

### Complete Incident-to-Change Workflow

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

## Benefits of ITIL-Aligned Structure

1. **Industry Standard** — Follows ITIL 4 best practices
2. **Role Clarity** — Each process has clear audience
3. **Easy Navigation** — Processes organized logically
4. **Cross-References** — Documentation linked across processes
5. **Consistency** — Standardized structure and templates

## Related Documentation

- [Governance Overview](../governance/index.md) — Policies and RACI
- [Architecture](../governance/architecture/README.md) — Platform architecture
- [FAQ](../../onboarding/faq.md) — Common questions
- [Taxonomy](../governance/taxonomy.md) — Tag definitions

---

**Last Updated:** 2025-01-15

