---
title: "Incident Report: <INC-YYYY-NNN>"
summary: "Post-incident review and actions."
owner: "Your Team/Your Name"
tags:
  - audience:manager  # Options: manager, developer, l2-support, etc.
  - doc-type:reference
  - owner:service-desk  # Options: service-desk, platform, security, etc.
  - topic:itil-incident  # Replace with actual topic (1-3 topics required)
  - lifecycle:approved  # Options: draft, review, approved, deprecated
  - sensitivity:internal  # Options: public, internal, confidential, restricted
  - incident-priority:p1  # Optional: p0, p1, p2 (for incident classification)
last_review: "YYYY-MM-DD"  # Format: YYYY-MM-DD
locale: "en"  # Options: en, fr
service: "docops"  # Replace with actual service name
version: "v1.0"
outdated: false  # Set to true if translation lags behind English
---

## Summary

**Incident ID:** INC-YYYY-NNN

**Date:** YYYY-MM-DD

**Duration:** Start time - End time (Total duration: X hours Y minutes)

**Severity:** P0 / P1 / P2 / P3

**Status:** Resolved / Closed

**Impact:**
- Affected services: Service 1, Service 2
- Users affected: Number or percentage
- Business impact: Description

## Timeline

| Time | Event | Action Taken | Owner |
|------|-------|--------------|-------|
| T0: HH:MM | Detection | Initial detection | Team/Person |
| T+5m: HH:MM | Triage | Incident classified, team notified | Team/Person |
| T+15m: HH:MM | Investigation | Root cause investigation started | Team/Person |
| T+30m: HH:MM | Mitigation | Workaround applied | Team/Person |
| T+1h: HH:MM | Resolution | Root cause fixed | Team/Person |
| T+2h: HH:MM | Verification | Service restored, monitoring confirmed | Team/Person |

## Root Cause Analysis

### What Failed

Describe what component/system/process failed.

### Why It Failed

**Root cause:** Primary reason for failure

**Contributing factors:**
- Factor 1
- Factor 2

**Timeline of failure:**
1. Event 1 led to...
2. Event 2 caused...
3. Event 3 resulted in incident

## Impact Assessment

**Services affected:**
- Service 1: Description of impact
- Service 2: Description of impact

**Data impact:**
- Data loss: Yes/No, details if yes
- Data corruption: Yes/No, details if yes

**Financial impact:**
- Estimated cost (if applicable)

## Actions Taken

### Immediate Actions (During Incident)

1. **Action 1:** What was done
   - Result: Outcome
   - Time: HH:MM

2. **Action 2:** What was done
   - Result: Outcome
   - Time: HH:MM

### Corrective Actions (After Resolution)

1. **Action 1:** What will be done
   - Owner: Team/Person
   - Due date: YYYY-MM-DD
   - Status: Open / In Progress / Completed

2. **Action 2:** What will be done
   - Owner: Team/Person
   - Due date: YYYY-MM-DD
   - Status: Open / In Progress / Completed

### Preventive Actions

1. **Action 1:** What will prevent recurrence
   - Owner: Team/Person
   - Due date: YYYY-MM-DD
   - Status: Open / In Progress / Completed

2. **Action 2:** What will prevent recurrence
   - Owner: Team/Person
   - Due date: YYYY-MM-DD
   - Status: Open / In Progress / Completed

## Lessons Learned

### What Went Well

- Positive aspect 1
- Positive aspect 2

### What Could Be Improved

- Area 1: Improvement needed
- Area 2: Improvement needed

### Recommendations

1. **Recommendation 1:** Description
   - Priority: High / Medium / Low
   - Owner: Team/Person

2. **Recommendation 2:** Description
   - Priority: High / Medium / Low
   - Owner: Team/Person

## Related Documentation

- [Runbook](./../ops/) — Related operational procedure
- [Architecture](./../governance/architecture/) — System architecture
- [Monitoring](./../devops/) — Monitoring setup

## Follow-up

**Post-mortem meeting:** Date (if applicable)

**Action items tracking:** [Link to issue tracker or board]

**Next review:** YYYY-MM-DD
