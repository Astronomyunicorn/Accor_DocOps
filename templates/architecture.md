---
title: "Architecture: <System/Service>"
summary: "High-level architecture with diagrams."
owner: "Your Team/Your Name"
tags:
  - audience:developer
  - doc-type:architecture
  - owner:platform
  - topic:kubernetes  # Replace with actual topic (1-3 topics allowed)
  - topic:api-gateway  # Optional: additional topics
  - lifecycle:review  # Options: draft, review, approved, deprecated
  - sensitivity:internal  # Options: public, internal, confidential, restricted
last_review: "YYYY-MM-DD"  # Format: YYYY-MM-DD
locale: "en"  # Options: en, fr
service: "docops"  # Replace with actual service name
version: "v1.0"
outdated: false  # Set to true if translation lags behind English
---

## Overview

Describe the system/service, its purpose, and key components.

## Architecture Diagram

```mermaid
graph TB
    User[User]
    System[System]
    User --> System
```

Or reference an image:
![Architecture Diagram](../../docs/media/architecture-diagram.png)

## Components

### Component 1
- Purpose
- Responsibilities
- Interfaces

### Component 2
- Purpose
- Responsibilities
- Interfaces

## Data Flow

Describe how data flows through the system.

## Interfaces

### APIs
- REST API endpoints
- gRPC services
- Message queues

### External Integrations
- Third-party services
- Dependencies

## Deployment

- Where it runs (Kubernetes, bare metal, etc.)
- Scaling strategy
- Environment specifics

## Related Documentation

- [ADR-XXX: Decision](./../governance/architecture/decisions/)
- [Runbook](./../ops/)
- [Deployment Guide](./../devops/)
