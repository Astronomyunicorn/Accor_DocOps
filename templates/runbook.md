---
title: "Runbook: <Service/Procedure>"
summary: "Operational procedure for routine or emergency tasks."
owner: "Your Team/Your Name"
tags:
  - audience:l1-support  # Options: l1-support, l2-support, sre, devops, etc.
  - doc-type:runbook
  - owner:platform  # Options: platform, security, network, apps, etc.
  - topic:api-gateway  # Replace with actual topic (1-3 topics required)
  - lifecycle:approved  # Options: draft, review, approved, deprecated
  - sensitivity:internal  # Options: public, internal, confidential, restricted
  - incident-priority:p1  # Optional: p0, p1, p2 (for incident-related runbooks)
last_review: "YYYY-MM-DD"  # Format: YYYY-MM-DD
locale: "en"  # Options: en, fr
service: "docops"  # Replace with actual service name
version: "v1.0"
outdated: false  # Set to true if translation lags behind English
---

## Context

**Service/System:** What service this runbook applies to

**Environment:** Production, staging, etc.

**On-call Contact:**
- Primary: @team-channel or email
- Escalation: @escalation-channel

**Maintenance Window:** Required (yes/no), duration if applicable

**Impact:** What happens if this procedure fails

## Preconditions

Before starting, verify:

- ✅ Prerequisite 1 is met
- ✅ Prerequisite 2 is met
- ✅ Access to required systems

**If prerequisites not met:** Contact on-call or escalate

## Procedure

### Step 1: <Action>

1. **Action:** What to do
   ```bash
   # Command or script
   kubectl get pods -n namespace
   ```

2. **Expected output:** What you should see

3. **Verification:** How to confirm success

### Step 2: <Action>

1. **Action:** What to do
   ```bash
   # Next command
   ```

2. **Expected output:** What you should see

3. **Verification:** How to confirm success

### Step 3: <Action>

Continue with remaining steps...

## Rollback

**When to rollback:** If X happens

**Rollback procedure:**

1. **Stop current operation:**
   ```bash
   # Command to stop
   ```

2. **Revert changes:**
   ```bash
   # Command to revert
   ```

3. **Verify rollback:**
   - Check 1
   - Check 2

**Expected state after rollback:** Describe restored state

## Verification

**Success criteria:**
- ✅ Check 1: Expected value/state
- ✅ Check 2: Expected value/state
- ✅ Check 3: Expected value/state

**KPIs to monitor:**
- Metric 1: < threshold
- Metric 2: < threshold

**Monitoring dashboard:** [Link to dashboard]

## Troubleshooting

### Issue: <Problem Description>

**Symptoms:**
- Error message or unexpected behavior

**Resolution:**
1. Check this
2. Do that
3. If persists, escalate

### Issue: <Another Problem>

**Symptoms:**
- Error message or unexpected behavior

**Resolution:**
1. Check this
2. Do that

## Escalation

**When to escalate:**
- Condition 1
- Condition 2

**Escalation path:**
1. Contact: @primary-oncall
2. If no response (15 min): @escalation
3. If critical (P0): @manager-channel

## Related Documentation

- [Architecture Overview](./../governance/architecture/)
- [Related How-to](./../kb/)
- [Monitoring Guide](./../devops/)
