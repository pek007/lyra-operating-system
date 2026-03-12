# Operating Model

Delivery runs as a repeatable flow from intake through implementation, verification, release/handoff, and post-delivery learning, while continuously improving the delivery system itself.

## Current design direction
Delivery is evolving toward **Delivery-as-Code**:
- delivery units become explicit governed objects
- state transitions become policy-controlled
- evidence is first-class
- approvals are explicit decision records
- professional documentation is rendered from canonical delivery state

Primary design reference:
- `06-architecture/DELIVERY_AS_CODE_DESIGN_V1.md`

## Coordination note
The interim inbox approach has been superseded.

Current direction:
- cross-product collaboration should move toward TDE-native assigned work,
- assignees should be notified/woken when new assigned work enters canonical state,
- collaboration state should be tracked canonically in TDE rather than through mailbox-style polling.

Reference:
- `TDE_ASSIGNED_WORK_WAKEUP_MODEL_V1.md`
