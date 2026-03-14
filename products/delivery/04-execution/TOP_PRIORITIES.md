# TOP_PRIORITIES

Product: Delivery
Last updated: 2026-03-14
Owner: Product Owner / Control Tower

## Priority 1
**Title:** Pilot one real TDE slice end to end as a Delivery Unit
**Why this matters now:** Delivery needs a real proving path, not just framework definition, to show that capabilities can move safely from concept into use.
**Current status:** Schema, state-transition policy, and rendered packet templates are complete; the end-to-end pilot is the next active step.
**Next concrete step:** Select and execute the smallest viable real TDE slice as a Delivery Unit with explicit evidence and gates.
**Links:** `products/delivery/04-execution/PLAN.md`, `products/delivery/06-architecture/DELIVERY_UNIT_SCHEMA_V1.yaml`, `products/delivery/03-operating-model/DELIVERY_STATE_TRANSITION_POLICY_V1.md`

## Priority 2
**Title:** Wire deterministic gate checks into the TDE flow
**Why this matters now:** Delivery reliability depends on verification becoming part of the flow rather than a separate memory-based habit.
**Current status:** Identified as the next execution-order item after the first real pilot.
**Next concrete step:** Define and connect the smallest useful deterministic gate checks into the current TDE delivery path.
**Links:** `products/delivery/04-execution/PLAN.md`, `products/delivery/04-execution/RISKS.md`, `products/delivery/05-performance/METRICS.md`

## Priority 3
**Title:** Shift coordination to TDE-native assigned work with wake/notification
**Why this matters now:** Delivery coordination should move away from interim inbox-style patterns toward execution-native assignment and wake behavior.
**Current status:** Interim inbox experiment is explicitly superseded; direction is clear but not fully embodied.
**Next concrete step:** Align Delivery’s execution and pilot contract with the TDE-native assigned-work / wakeup model.
**Links:** `products/delivery/04-execution/PLAN.md`, `products/delivery/04-execution/TDE_UI_PILOT_DELIVERY_CONTRACT_V1.md`, `TDE_ASSIGNED_WORK_WAKEUP_MODEL_V1.md`
