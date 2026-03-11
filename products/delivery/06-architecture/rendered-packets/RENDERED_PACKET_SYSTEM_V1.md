# Rendered Packet System v1

Status: Draft
Owner: Lyra
Date: 2026-03-11

## Purpose
Define the first standard rendered outputs for Delivery-as-Code.

Rendered packets are professional human-readable documents generated from canonical Delivery Unit state, evidence, decisions, and exceptions.
They are not the primary source of truth.

## Design rule
Canonical source of truth:
- Delivery Unit object
- evidence records
- decision records
- exception records
- transition state

Rendered outputs:
- summarize
- present
- request decision
- support audit
- support handoff

## Packet set in v1
1. `DELIVERY_BRIEF_TEMPLATE_V1.md`
2. `VERIFICATION_PACKET_TEMPLATE_V1.md`
3. `RELEASE_HANDOFF_PACKET_TEMPLATE_V1.md`
4. `APPROVAL_MEMO_TEMPLATE_V1.md`
5. `POST_DELIVERY_REVIEW_TEMPLATE_V1.md`

## Packet intent by lifecycle stage
### Delivery Brief
Used from `qualified` onward.
Purpose: concise operational and executive framing.

### Verification Packet
Used during `in_verification` and for transition into `release_recommended`.
Purpose: show whether the DU actually satisfies verification expectations.

### Release / Handoff Packet
Used in `release_recommended`, `awaiting_approval`, and `approved`.
Purpose: assemble a decision-quality recommendation and route package.

### Approval Memo
Used whenever human or dual-control approval is required.
Purpose: capture approval or rejection in auditable concise form.

### Post-Delivery Review
Used from `verified_in_use` into `closed`.
Purpose: close the loop with operational proof and learning capture.

## Rendering rules
- packets should be generated from canonical state whenever possible
- manual edits, if allowed, should be visibly marked as curated additions
- missing canonical fields should surface as gaps, not be silently invented
- packet generation failure for a mandatory stage should block progression when policy requires the packet

## Relationship to policy
Rendered packets support but do not replace policy validation.
A polished packet must never override failed evidence or failed gate conditions.

## Recommended next step
Map one real TDE Delivery Unit candidate into these rendered packets and test whether the packet set is sufficient or whether one additional packet type is needed.
