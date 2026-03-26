# TDE Self-UI Proving Experiment Brief

Status: Draft active
Date: 2026-03-26
Owner: Task Management Product / Lyra
Product: A-007 Task Management
Classification: `processes/classifications/CLASSIFICATION_TDE_SELF_UI_PROVING_EXPERIMENT_2026-03-26.yaml`

## Hypothesis
TDE is now mature enough to take a bounded product vision for a UI about TDE itself, convert that into canonical work, drive implementation through the real task/runtime path, and produce inspectable operating evidence with limited manual rescue.

## Purpose
This is not a "build a nice UI" exercise.

The purpose is to test whether TDE can:
- accept a bounded product vision
- form and govern the required work
- move that work through canonical runtime/task state
- result in an implemented and operated slice
- leave behind evidence that is inspectable without tribal knowledge

## Scope
### In scope
One bounded operator-facing TDE UI slice that exposes real execution state.

Recommended slice:
- **TDE Operator Readiness View**

Minimum contents:
- experiment objective / slice identity
- canonical tasks generated for the slice
- current state and recent transitions
- assignment / acceptance status
- runtime events or execution markers
- readiness / cutover evidence links
- links to canonical source artifacts

### Out of scope
- full TDE product UI
- polished design system work
- generalized workflow builder
- all-role task management UI
- broad automation claims beyond the experiment slice

## Entry artifact
The experiment enters through one explicit anchor only:
- `control/tde-intake/tde-self-ui-proving-experiment-2026-03-26.json`

That artifact should remain the canonical entry point for the experiment vision, scope, success rubric, and linkage into execution.

## Success criteria
The experiment counts as a pass only if all of the following are true.

### A. Formation success
A bounded UI vision becomes explicit canonical work:
- objective exists
- tasks/work items are formed
- ownership/pathing is visible
- state is canonical, not inferred from chat

### B. Runtime-path success
The work moves through the actual producer/adapter/runtime path:
- intake -> task formation -> runtime state changes are visible
- no hidden side-channel is required to understand progress
- state updates are reflected in the canonical surface

### C. Implementation success
A working UI slice exists:
- operator can open the slice
- data shown is tied to canonical underlying state
- at least one real update/state change is reflected in the UI

### D. Operation success
The slice is not just built; it is operated:
- at least one real run/update/event occurs after implementation
- the slice reflects that event
- evidence shows the slice is alive, not merely rendered once

### E. Inspection success
A reviewer can understand what happened without tribal memory:
- source objective visible
- current status visible
- evidence links visible
- readiness judgment visible
- limitations/manual interventions explicitly declared

## Failure criteria
The experiment should be marked failed or partial if any of the following occurs:
- canonical state is ambiguous
- progress depends on undocumented manual stitching
- the UI is manually populated rather than driven from real state
- implementation succeeds but operation is not evidenced
- evidence exists only as narrative explanation after the fact
- the slice is so broad that the result cannot be interpreted cleanly

## Preconditions before start
These should be true before launch:
- one explicit entry artifact
- canonical runtime/task truth identified
- producer/adapter/runtime path made explicit
- experiment operating mode declared
- bounded GO/NO-GO posture for DB/readiness stated
- one thin slice selected

## Operating mode
Recommended declared mode:
- **bounded pilot-operational experiment**

Meaning:
- real enough to test the true path
- narrow enough to avoid false generalization
- manual steps allowed only if explicitly declared
- any manual rescue must be logged as experiment evidence

## Evidence package required
At minimum, the experiment should leave behind:
- experiment brief / intake artifact
- canonical task/runtime references
- implementation artifact(s)
- UI access or screenshot proof
- at least one post-build runtime/event proof
- readiness/cutover judgment
- short retrospective:
  - what worked
  - what required rescue
  - what this does and does not prove

## Pass / partial / fail rubric
### PASS
- bounded vision entered cleanly
- canonical work formed
- runtime path genuinely used
- working UI slice implemented
- operated proof exists
- inspection is easy and honest

### PARTIAL PASS
- working slice exists
- but runtime closure still required meaningful manual rescue
- or operation proof is weak
- or inspectability still depends on explanation

### FAIL
- mostly narrative/manual orchestration
- UI disconnected from canonical state
- no credible operation evidence
- result cannot distinguish system capability from operator intervention

## Recommended next step
Before launching the experiment:
- do one explicit runtime-closure hardening step
- then instantiate this brief as a live experiment artifact and initial task set

That is the cleanest path to a serious thin-slice test rather than a visually persuasive but strategically weak demo.