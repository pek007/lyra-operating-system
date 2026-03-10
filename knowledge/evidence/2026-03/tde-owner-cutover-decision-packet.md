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

## What still blocks a bounded live GO
1. Exact canary domain not yet declared in the packet.
2. Object inventory / mapping proof for the bounded slice not yet consolidated.
3. Drift and reconciliation thresholds for the live window not yet declared.
4. Operator runbook was missing before S26 packetization.
5. Rollback triggers and reconciliation-after-rollback steps were not yet consolidated into one decision path.

## Recommended next action
Complete S26 artifacts and then make an explicit owner decision on one bounded live rollout slice:
- GO for bounded slice
- HOLD for further hardening
- ROLLBACK / remain on current posture

## Suggested owner decision standard
Only approve bounded live GO if all of the following are explicit:
- bounded domain
- authority posture
- in-scope inventory
- drift/reconciliation thresholds
- rollback path
- operator runbook

## Suggested rollout philosophy
- start with one narrow domain only
- no uncontrolled dual-write
- no expansion without explicit post-window review
- preserve owner-visible GO/HOLD/ROLLBACK control
