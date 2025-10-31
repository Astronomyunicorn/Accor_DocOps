---
title: "[How\u2011to] Reset VPN on macOS"
summary: "Troubleshooting steps to restore VPN connectivity."
owner: "ITIL/Service Desk"
tags:
  - audience:l1-support
  - doc-type:howto
  - owner:service-desk
  - topic:vpn
  - lifecycle:approved
  - sensitivity:internal
last_review: "2025-10-28"
locale: "en"
service: "docops"
version: "v1.0"
outdated: false
---

## Purpose
Restore VPN connection for remote users.

## Steps
1. Open **Keychain Access** → remove saved VPN certificates (if corrupted).
2. Delete `/Library/Preferences/com.vpn.client.plist`.
3. Reboot and re-import the profile from **Service Catalog**.

## Validation
- VPN connects within 10 seconds; no auth loops.
