---
title: "Content Tagging Taxonomy"
summary: "Optimized tag namespaces and rules for consistent classification."
owner: "DocOps/Governance"
tags:
  - audience:manager
  - doc-type:reference
  - owner:platform
  - topic:taxonomy
  - lifecycle:approved
  - sensitivity:internal
last_review: "2025-10-30"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---

## Goals

- Make content easy to find by audience, type, owner, topic
- Keep tags consistent, limited, and machine-validated

## Namespaces (core, required)

- audience: who reads it (role)
  - audience:l1-support, audience:l2-support, audience:sre, audience:devops,
    audience:developer, audience:dba, audience:secops, audience:manager
- doc-type: document format
  - doc-type:runbook, doc-type:howto, doc-type:reference, doc-type:tutorial,
    doc-type:troubleshooting, doc-type:architecture, doc-type:policy
- owner: accountable team
  - owner:platform, owner:network, owner:security, owner:infra, owner:apps, owner:service-desk
- topic: what it is about (1–3 tags)
  - topic:kubernetes, topic:aws, topic:gitlab, topic:nginx, topic:api-gateway,
    topic:monitoring, topic:itil-incident, topic:itil-change, topic:cmdb
- lifecycle: document status
  - lifecycle:draft, lifecycle:review, lifecycle:approved, lifecycle:deprecated
- sensitivity: access level
  - sensitivity:public, sensitivity:internal, sensitivity:confidential, sensitivity:restricted

## Namespaces (optional)

- region: geography (only if relevant)
  - region:emea, region:amer, region:apac, region:global
- incident-priority: for runbooks and incident flows
  - incident-priority:p0, incident-priority:p1, incident-priority:p2

## Tag rules

- 3–10 tags per document
- Required: at least 1 audience, exactly 1 doc-type, exactly 1 owner, 1–3 topic,
  exactly 1 lifecycle, exactly 1 sensitivity (default internal)
- No overlapping synonyms (e.g., do not duplicate the same concept across namespaces)
- kebab-case, english only

## Front matter example

```yaml
tags:
  - audience:l1-support
  - doc-type:runbook
  - owner:network
  - topic:nginx
  - topic:api-gateway
  - topic:itil-incident
  - lifecycle:approved
  - sensitivity:internal
  - incident-priority:p1
```

## Governance

- Allowlist lives in `tools/tags-allowlist.json`
- PRs adding new tags must update allowlist with justification
- Quarterly cleanup of unused tags

