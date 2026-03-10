# TASK_MANAGEMENT_PROOF_CASE_V1.md

Status: Active draft v1  
Owner: Lyra via Control Panel + Task Management lane  
Date: 2026-03-10

## Purpose
Define the first proof case for the new hybrid runtime / cross-session coordination model using Task Management as the test lane.

## Why Task Management
Task Management is the best first proof case because:
- it is execution-heavy
- it naturally benefits from deterministic wake-up logic
- it is closely linked to TDE and job portability concerns
- it can prove whether stronger artifacts + direct session coordination reduce dependence on thread context

## Objective
Run one real task-management coordination flow using:
- a real job bundle
- direct `sessions_send`-style handoff semantics
- durable state updates
- no copy-paste as the operating mechanism

## Scope of the proof case
In scope:
- one bounded task or coordination request
- one real job bundle created/populated enough to carry the flow
- one explicit handoff from Control Panel to Task Management lane
- one durable artifact update during the same work cycle
- one response back to Control Panel with clear outcome state

Out of scope:
- creating a new persistent runtime
- redesigning TDE itself
- broad multi-product orchestration

## Proposed minimum flow
1. Control Panel identifies a real Task Management action/request.
2. Control Panel sends a lightweight intra-Lyra handoff packet.
3. Task Management lane receives and acts.
4. Task Management updates the job bundle (`STATE.md` minimum; `HANDOVER.md` if ownership shifts).
5. Task Management replies with one of:
   - status
   - result
   - decision-needed
   - blocked
6. Control Panel updates oversight state only with the high-signal result.

## Required artifacts
- `INTRA_LYRA_HANDOFF_PROTOCOL_V1.md`
- one real `jobs/<JOB-ID>/` bundle for the test flow
- evidence or note linking the request and the outcome

## Success criteria
The proof case is successful if:
1. no human copy-paste relay is needed
2. the request is understandable without relying on thread history alone
3. the durable state after execution is visible in a job artifact
4. Control Panel can track the outcome without storing the full execution context itself
5. the flow feels lighter and clearer than the current manual pattern

## Failure signals
- request still depends mainly on prior thread context
- no durable artifact gets updated
- the receiver cannot tell what action is being requested
- Control Panel becomes the de facto storage location of the whole workflow
- the flow creates more friction than manual copy-paste

## Recommended first candidate action
Use a Task Management item tied to:
- TDE operating cadence,
- job-memory portability,
- or a concrete task-claiming / state-update question

This keeps the proof case close to the current operating bottleneck.

## Follow-up after proof case
After the first run:
- capture what worked / failed
- refine the handoff protocol if needed
- decide whether the pattern is good enough to standardize across other Lyra product lanes

## Version
- v1.0
- Date: 2026-03-10
