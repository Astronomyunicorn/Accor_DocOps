---
title: "[Runbook] Restart API Gateway"
summary: "Safe restart procedure with health checks and rollback."
owner: "ITIL/Operations"
tags: ["ops", "apigw"]
last_review: "2025-10-28"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---

## Preconditions
- Maintenance window approved (Change Enablement)
- On-call L3 available

## Steps
1. Drain traffic from instance A
2. Restart service `apigw` (systemd)
3. Health check `/healthz`
4. Repeat for instance B

## Rollback
Revert traffic to previous stable instances.

## Verification
- 99th percentile latency < 250ms
