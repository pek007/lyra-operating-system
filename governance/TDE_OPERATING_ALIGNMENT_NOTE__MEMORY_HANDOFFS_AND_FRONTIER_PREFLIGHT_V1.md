# TDE Operating Alignment Note — Memory, Handoffs, and Frontier Preflight v1

Status: Active
Owner: JOB-PROD-001
Date: 2026-03-10
Related:
- `knowledge/evidence/2026-03-10__tde-operating-impact-note__memory-runtime-topology-and-handoffs.md`
- `knowledge/evidence/2026-03-10__tde-s26-supersession-and-sequence-failure-review.md`
- `knowledge/evidence/2026-03-10__error-report__tde-sequence-failure-and-context-loss.md`

## Purpose
Translate the new Lyra OS memory/handoff operating model into explicit TDE-facing operating assumptions without changing the TDE kernel contract.

## Policy statement
The improved memory and handoff substrate strengthens TDE operations, but does **not** replace canonical TDE state, authority rules, or readiness gates.

TDE should use the new operating substrate to improve continuity and coordination while keeping canonical execution state and mutation authority strict.

## Operating rules

### 1. Job-shaped TDE work must prefer job-bundle continuity
If work is durable, multi-step, transferable, or likely to survive a session boundary, TDE-facing execution should prefer a job bundle over transcript continuity.

Minimum expectation for durable job-shaped work:
- durable job state written to files
- linked artifact refs for decisions/evidence
- explicit handoff/update trail when work changes lane or owner

### 2. Same-runtime handoffs must reference durable artifacts
Intra-Lyra handoffs may use the standardized same-runtime handoff protocol, but they must not rely on chat summary alone.

Minimum handoff shape:
- bounded request
- artifact refs
- expected write-back target
- concise result / status / blocker response

### 3. Handoff state is not canonical execution state
Structured handoffs improve coordination, but they do **not** replace canonical TDE task/job state.

Use the distinction strictly:
- canonical task/job execution state -> canonical TDE runtime surfaces
- coordination/handoff state -> supporting operating artifacts and messages

### 4. Same-cycle write-back is expected for active durable work
When active TDE-related work changes durable state, the responsible lane should write back the change in the same work cycle when feasible.

This reduces hidden state and makes handoffs/recovery safer.

### 5. Post-cutover frontier inspection must prefer canonical runtime surfaces
For post-cutover TDE work, inspect the canonical runtime/projection surfaces before relying on legacy markdown boards.

Preferred inspection order:
1. current `origin/main`
2. `os/tde/INDEX.md`
3. canonical runtime evidence / SOPs
4. `os/runtime/TASKS_from_db.md`
5. legacy/reference boards only as supporting context

### 6. Frontier preflight is mandatory before resuming TDE work
No TDE implementation/resumption should proceed until the session can answer all of the following:
- What is the current canonical TDE store?
- What is the latest TDE frontier or active phase?
- Is the intended slice already superseded?
- What artifacts define the current authority model?

If those answers are not clear, TDE work should fail closed into **frontier reconstruction**, not implementation.

## What this note does not do
This note does not:
- change TDE kernel mutation rules
- bypass approval or authority gates
- make chat/handoff artifacts authoritative over TDE state
- replace DB-canonical state with lighter operating-layer continuity

## Immediate implementation guidance
- Update TDE-facing operating docs to expect job-bundle continuity for durable work.
- Update TDE-facing operating docs to require artifact-backed handoffs.
- Keep explicit anti-confusion language between canonical state and coordination state.
- Use the frontier-preflight rule before future TDE work resumes.
