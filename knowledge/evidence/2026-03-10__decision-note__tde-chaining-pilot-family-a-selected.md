# Decision Note — TDE Chaining Pilot Family A Selected

Date: 2026-03-10
Owner: Lyra
Linked WO: `WO-2026-TDE-CHAINING-PILOT-V1`

## Decision
Select **Pilot family A — implementation -> verification -> deployment-readiness review** as the first bounded real chaining pilot.

## Why
This family offers the best balance of:
- deterministic stage semantics
- boundedness
- clear predecessor/successor relationships
- strong evidence value for proving objective-linked continuation
- low risk of uncontrolled fan-out

## Implication for execution
The next implementation work should target:
1. canonical DB metadata support for this three-stage chain
2. deterministic successor promotion in job ticks
3. verification evidence for both promotion and fail-closed behavior
