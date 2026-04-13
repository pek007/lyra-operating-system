# Delivery / TDE / PXS Tools CRM Integration Pilot Note

Date: 2026-04-13
Owner: Lyra
Status: Proposed bounded pilot

## Purpose
Define the next concrete bounded integration pilot across Delivery, TDE, and PXS Tools using CRM as the real proving case.

## Pilot choice
Use **CRM Core Slice 1** as the real project context, but do **not** use TDE as the primary implementation plane for CRM feature development.

Instead, pilot the **change-to-evidence execution loop** around CRM Core Slice 1.

## Why this pilot
This is the cleanest first integration slice because:
- CRM is real and already has a bounded restart package
- the CRM artifacts explicitly state that TDE should not yet own primary implementation work for this slice
- Delivery needs a real professional-delivery proof case, not more abstract framing
- TDE needs a real machine-execution support slice with visible state, retries, continuity, and evidence handling
- the repeated workflow around implementation, verification, evidence assembly, and status reporting is a better first machine-execution target than feature-building itself

## In scope
The pilot covers the bounded execution-support workflow for CRM Core Slice 1:
1. accepted CRM slice brief exists
2. implementation kickoff packet is explicit
3. verification/test run is triggered and captured
4. evidence pack assembly is tracked explicitly
5. unresolved items / retries / follow-up state are visible
6. compact status output is available for review

## Out of scope
- using TDE as the primary feature-implementation plane for CRM Core Slice 1
- broad CRM product rollout
- generalized workflow-engine behavior beyond this bounded pilot
- broad Delivery commercialization packaging
- forcing all CRM decisions into TDE when they still require architecture/product judgment

## Role split
### PXS Tools / CRM
Owns:
- CRM product/tool embodiment
- slice scope and architecture choices
- implementation decisions within the accepted slice

### Delivery
Owns:
- professional delivery envelope for the pilot
- at least one enforceable gate in the slice
- evidence expectations and completion review discipline
- delivery-status framing for the pilot

### TDE / Task Management
Owns:
- machine-execution state for the support workflow
- dependency/retry/follow-up handling for the pilot loop
- explicit state transitions for execution-support steps
- visibility into active machine work for this slice

## Recommended first workflow family
**CRM Core Slice 1 change-to-evidence loop**

Canonical flow:
1. slice accepted
2. implementation work packet prepared
3. implementation/test step executed outside TDE primary ownership
4. verification result captured
5. evidence pack assembled
6. gaps route into explicit follow-up / retry / escalation state
7. compact pilot status becomes reviewable

## Minimum success criteria
The pilot is successful only if:
- one real CRM Slice 1 delivery cycle is run through the bounded support loop
- Delivery contributes at least one real enforceable gate or fail-closed validation step
- TDE holds explicit state for the support workflow rather than relying on chat memory
- evidence output is explicit and reviewable
- unresolved issues are visible as state rather than buried in prose
- the pilot produces a clear judgment on whether this execution-support pattern should be expanded

## Immediate next artifact needed
Create a short pilot contract that states:
- exact trigger for pilot start
- pilot states owned by TDE
- Delivery gate(s) used in the pilot
- evidence packet contents
- completion/abort criteria

## Bottom line
The next integration step is **not** “TDE builds CRM.”
It is: **use CRM Core Slice 1 as the real proving case for a Delivery-governed, TDE-supported change-to-evidence execution loop.**
