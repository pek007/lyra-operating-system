# CROSS_RUNTIME_HANDOFF_LOOP_STANDARD_V0_1.md

Status: Active draft v0.1  
Owner: Lyra via Control Panel  
Scope: Lyra OS <-> PX / Vega initial standard  
Date: 2026-03-10

## Purpose
Define a simple, stable communication pattern for cross-runtime handoffs between isolated runtimes such as:
- Lyra OS
- PX / Vega

This standard exists because same-runtime coordination patterns do not transfer reliably across runtime/workspace boundaries.

## Core principle
Use **explicit inbox/outbox artifact exchange** for cross-runtime coordination.

Do not rely on:
- manual copy-paste as the normal method
- implicit session visibility
- same-runtime handoff assumptions
- hidden shared context

## Minimal structure per runtime
Each runtime should have:
- `handoffs/incoming/`
- `handoffs/outgoing/`
- a handoff register

Optional later additions:
- archive folder
- consumed/rejected subfolders
- lightweight state marker on each handoff

## Artifact types
### 1. Handoff envelope
YAML artifact containing at least:
- `handoff_id`
- `from_domain`
- `to_domain`
- `owner`
- `purpose`
- `classification`
- `created_at`
- `expires_at` (when applicable)
- `source_refs`
- `checksum`
- `approved_by`

### 2. Payload
Referenced document(s) required to understand or process the handoff.

### 3. Response artifact
Destination runtime writes a response artifact to its `handoffs/outgoing/` path, referencing the incoming handoff ID.

## Validation rules
A handoff is invalid if any of the following are missing:
- owner
- purpose
- checksum
- approval reference
- visible payload when payload is required

If invalid:
- do not process silently
- respond with rejection or correction-needed artifact

## Default loop model
### Transport/storage layer
- artifacts are placed in the target runtime’s `handoffs/incoming/`
- response artifacts are placed in the responding runtime’s `handoffs/outgoing/`

### Pickup layer
Preferred mechanism:
- **cron-backed inbox check**

Secondary/support mechanism:
- **heartbeat awareness only**

Why:
- heartbeat is useful for awareness and batching
- cron is better for deterministic pickup and repeatable behavior

## Recommended v0.1 cadence
For active paired runtimes:
- check `handoffs/incoming/` every 15–30 minutes

Start at the slower end unless traffic proves the need for tighter cadence.

## What the pickup loop should do
1. scan `handoffs/incoming/`
2. identify new/unhandled valid handoffs
3. validate required fields and payload visibility
4. either:
   - accept/process, or
   - reject/escalate
5. write a response artifact to `handoffs/outgoing/`
6. update the handoff register/status

## Status model
Suggested minimal statuses:
- `Open`
- `Consumed`
- `Rejected`
- `Expired`
- `Archived`

## Output/noise rules
1. No chatter-only responses.
2. Every meaningful response should create a durable response artifact.
3. No repeated reprocessing of already handled handoffs.
4. If nothing is new, the pickup loop should stay quiet.
5. If the handoff is invalid, say exactly what is missing.

## Boundary rules
Cross-runtime handoffs must:
- assume no hidden shared context
- avoid same-runtime shortcut assumptions
- avoid implicit authority transfer
- respect each runtime’s local boundary model
- keep payloads local to the target runtime if processing there is required

## Human role
The human should not need to act as the routine courier once the loop exists.

The human should still be involved when:
- approval is required
- boundary exceptions are needed
- a handoff is disputed or repeatedly rejected
- the runtimes disagree about ownership or interpretation

## v0.1 implementation recommendation
For Lyra OS <-> PX:
1. keep the current explicit handoff artifact format
2. add a simple cron-backed incoming-handoff review loop on each side later
3. do not automate execution of the payload itself until pickup/response reliability is proven
4. start with review/respond discipline before attempting full autonomous relay

## Non-goals
- replacing same-runtime `sessions_send` for intra-Lyra work
- building a full message bus
- introducing plugin complexity at v0.1
- hiding approval/boundary decisions behind automation

## Bottom line
Cross-runtime coordination should use:
- explicit inbox/outbox artifacts
- deterministic pickup via cron
- durable response artifacts
- explicit status/register updates

Heartbeat may help with awareness, but **cron should be the primary pickup mechanism**.

## Version
- v0.1
- Date: 2026-03-10
