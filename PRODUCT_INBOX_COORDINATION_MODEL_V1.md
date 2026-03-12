# Product Inbox Coordination Model v1

Status: Superseded / archived for reference
Owner: Peter / Lyra
Date: 2026-03-12
Superseded by: `TDE_ASSIGNED_WORK_WAKEUP_MODEL_V1.md`

## Archive note
This artifact captured a temporary interim idea: using product inboxes as a bridge for cross-product coordination.

That experiment was useful because it showed:
- request storage can work,
- visibility can work,
- auditability can work,
- but storage + visibility alone do not create real delegated response.

## Why it is superseded
The key missing primitive was not mailbox-style intake.
It was TDE-native:
- assignment,
- assignee wake/notification,
- explicit acknowledgment,
- canonical collaboration state.

That is now the preferred direction.

## Historical summary of the inbox approach
The inbox concept used:
- product-local request folders,
- explicit request artifacts,
- heartbeat/checker visibility,
- write-back response discipline.

This remains useful as historical reference for what was tried and why it was insufficient.

## Current recommendation
Do not extend the inbox model further as the primary coordination mechanism.

Prefer:
- canonical assigned work in TDE,
- assignee wake/notification,
- explicit response semantics,
- collaboration state tracked in TDE.
