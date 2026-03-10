# TDE Owner Cutover Decision Packet

Date: 2026-03-10
Status: Draft
Owner: Lyra
Linked WO: `WO-2026-TDE-KERNEL-S26`

## Decision required
Not yet GO for live cutover.

Recommended current decision: **HOLD pending bounded-scope packet completion**.

## Why this is the right decision now
The TDE kernel appears sufficiently hardened to justify preparing for bounded live use, but the operational cutover packet is still incomplete. The limiting risk is no longer core governance semantics; it is incomplete cutover clarity for a specific live slice.

## What is already strong
- core thin-slice governance path exists
- objective, binding, and fail-closed runtime controls materially advanced
- atomic writeback path exists
- CI/runtime guardrails and activation artifacts exist
- bounded-rollout thinking already exists in prior evidence/design artifacts

## Selected canary scope
- Domain: `JOB-PROD-001` TDE-internal kernel work in `repos/lyra-operating-system/TASKS.md`
- In-scope objects: open task items with IDs beginning `TDE-2026-*`
- Authority posture: `TASKS.md` canonical for this slice; no Trello/legacy authority in scope
- Mutation limit: only the already-proven low-risk task-state movement + audit-linked runtime path

## What still blocks a bounded live GO
1. Drift and reconciliation thresholds for the live window still need to be exercised in an actual bounded run.
2. Backup/restore and reconciliation-after-rollback linkage for this exact slice is not yet attached.
3. Operator runbook now exists, but it still needs one executed canary window to validate practicality.

## Recommended next action
The packet is now specific enough to support a tightly bounded execution step.

Recommended next action:
- run one bounded live canary window for `JOB-PROD-001` handling of open `TDE-2026-*` work in `TASKS.md`
- capture cycle evidence against the S26 runbook
- then decide GO-expand / HOLD / ROLLBACK

## Suggested owner decision standard
Only approve bounded live GO if all of the following are explicit:
- bounded domain (`JOB-PROD-001` TDE-internal kernel work)
- authority posture (`TASKS.md` canonical; no legacy authority)
- in-scope inventory (open `TDE-2026-*` objects)
- drift/reconciliation thresholds
- rollback path
- operator runbook

## Suggested rollout philosophy
- start with one narrow domain only
- no uncontrolled dual-write
- no expansion without explicit post-window review
- preserve owner-visible GO/HOLD/ROLLBACK control
