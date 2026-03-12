# Intent-to-Task Maturity Assessment — 2026-03-12

Status: Draft active
Owner: Peter / Lyra
Reference model: `INTENT_TO_TASK_MATURITY_MODEL_V1.md`
Related artifacts:
- `OBJECTIVE_START_GATE_V1.md`
- `INTENT_TDE_DELIVERY_OPERATIONS_MODEL_V1.md`
- `TDE_ASSIGNED_WORK_WAKEUP_MODEL_V1.md`
- `knowledge/reports/2026-03-12__deepresearch__best-practices-for-an-intent-to-execution-service-feeding-lyra-openclaw-tde__v1.md`

## Purpose
Assess current Lyra OS work against the Intent-to-Task maturity model.

This assessment is not a claim that the capability is already operational.
It is a judgment about what has been designed, what has been partially shaped, and what is still missing.

## Overall summary
Current overall maturity: **between Level 1 and early Level 2 in design, with isolated forward-looking concepts reaching toward Levels 3-4.**

That means:
- the structural shape is becoming clear,
- some important primitives are now defined,
- but the capability is not yet assembled into a reliable operational flow.

## Level-by-level assessment

## Level 1 — Structurally correct linear baseline
### Assessment
**Partially achieved in design. Not yet fully operational.**

### What exists
- We have a growing distinction between upstream shaping and downstream execution/governance.
- `OBJECTIVE_START_GATE_V1.md` defines a disciplined objective packet with strong required fields.
- The broader chain from intent/shaping to execution/release/operations is explicitly described in `INTENT_TDE_DELIVERY_OPERATIONS_MODEL_V1.md`.
- We now explicitly reject the naive model of jumping straight from loose idea to execution.

### What is still missing
- A concrete canonical artifact set for all Level 1 objects is not yet fully defined and in use.
- In particular, we do not yet have a fully specified and active set of separate canonical artifacts for:
  - Vision
  - Goal
  - Design
  - Plan
  - Task Bundle
- The Objective Packet is strong, but it is not yet the same as a full Intent-to-Task artifact family.
- We have not yet defined the exact minimum Design standard in an executable/canonical way.

### Judgment
Level 1 is **conceptually close**, but not yet complete enough to call operational.

## Level 2 — Disciplined decomposition
### Assessment
**Early partial progress.**

### What exists
- The current work strongly emphasizes first-slice thinking and bounded scope.
- The TDE UI pilot work has forced explicit attention to smallest acceptable slice, non-goals, and design constraint surfaces.
- The research and recent architecture discussion now explicitly support richer decomposition methods rather than arbitrary breakdown.
- We have started to recognize the importance of use cases, architecture substance, and decomposition discipline.

### What is still missing
- No formal decomposition method has yet been selected and standardized.
- No explicit goal tree / story map / use-case decomposition template is yet in use.
- No rules yet exist for split/merge when a plan becomes too large or unclear.
- No canonical requirement yet ensures that verification tasks are derived directly from goal/design claims.

### Judgment
We are **entering Level 2**, but only in scattered design ideas. The decomposition discipline is not yet systematized.

## Level 3 — Iterative convergence loops
### Assessment
**Recognized conceptually, not yet operationalized.**

### What exists
- We explicitly agreed that intent shaping is iterative and not waterfall.
- The broader architecture now distinguishes iterative shaping from downstream execution.
- The deep research report provides a clear loop structure: clarify, decompose, validate, execute/observe.
- We now have the language of convergence, reframing, and “current best converged packet.”

### What is still missing
- No explicit convergence-loop artifact or protocol yet exists.
- No formal triggers for reframe / return to vision / return to goal / return to design are defined.
- No stopping criteria are yet defined in Lyra-native artifacts beyond broad boundedness thinking.
- No canonical handling yet exists for uncertainty-driven discovery/prototype work inside shaping.

### Judgment
Level 3 is **understood**, but still mostly conceptual. It is not yet designed tightly enough to guide execution behavior.

## Level 4 — Bounded compile / submit / observe integration
### Assessment
**Target state recognized; implementation missing.**

### What exists
- The report’s compile / submit / observe interface is now clearly visible as the likely architectural seam.
- The system already values bounded execution, fail-closed runtime behavior, and canonical state on the TDE side.
- The need to separate upstream iterative planning from bounded runtime execution is clearly understood.

### What is still missing
- No actual Intent-to-Task service exists yet.
- No compile contract is defined.
- No formal TDE intake bundle schema exists for this upstream capability.
- No observe/writeback interface has been defined from TDE into the shaping side.
- No canonical provenance contract yet connects intent/goals/design/plan to execution bundle structure.

### Judgment
Level 4 is **an architectural direction, not a built capability**.

## Level 5 — Advanced planning intelligence and governance
### Assessment
**Research-informed only.**

### What exists
- We now know relevant best-practice families: HTN, goal graphs, story mapping, design thinking loops, guarded agentic planning, stronger provenance, bounded validators.
- We have a more mature understanding of the risks of open-ended planning and excessive agency.

### What is still missing
- No advanced planning engine exists.
- No deterministic validator stack exists for the shaping side.
- No advanced planning-quality metric model exists.
- No richer provenance/canonicalization implementation exists.

### Judgment
Level 5 is currently **knowledge only**, not capability.

## Cross-cutting observations

## Strongest current assets
1. **Architecture awareness has improved sharply**
   - We now have a more coherent picture of the system boundary and capability split.

2. **Boundedness thinking is strong**
   - We are increasingly clear that runtime execution must remain bounded and controlled.

3. **Objective shaping discipline is improving**
   - The Objective Start Gate is a meaningful asset and likely one of the strongest current artifacts in this space.

4. **Collaboration and assignment gaps are visible**
   - The inbox experiment failed in a useful way and led to the stronger assigned-work wakeup model.

## Weakest current areas
1. **Canonical artifact family is incomplete**
   - especially Vision / Goal / Design / Plan as distinct operational objects.

2. **Design standard is underdefined**
   - we still need a stronger practical standard for what a “good enough design” must contain.

3. **Convergence logic is not yet encoded**
   - we agree on iterative loops, but the system does not yet know how to run them.

4. **Compile/submit/observe seam is not yet designed concretely**
   - this may be the most important architectural gap after basic artifact hygiene.

## Current maturity judgment by dimension
- **Artifact structure:** 2/5
- **Decomposition discipline:** 2/5
- **Iterative convergence support:** 1.5/5
- **Bounded runtime handoff architecture:** 2/5
- **Advanced planning intelligence:** 1/5
- **Overall operational maturity:** 2/5

These are directional judgments, not formal scores.

## Recommended next priorities
### Priority 1
Define the **Level 1 canonical artifact pack** clearly:
- Vision
- Goal
- Design
- Plan
- Task Bundle

### Priority 2
Define a **minimum Design standard** that includes at least:
- problem statement
- scope/non-goals
- functional design
- data/information architecture
- use cases / flows
- risks/constraints
- verification approach

### Priority 3
Define the first **convergence-loop protocol** for iterative intent shaping.

### Priority 4
Define the first **compile / submit / observe interface contract** between Intent-to-Task and TDE.

## Bottom line
The work is on the right track, but the system is still much earlier than it may sometimes feel from the number of artifacts.

The strongest honest statement is:

**We now have a promising architecture frame and some good control artifacts, but the actual Intent-to-Task capability is still at an early maturity stage.**

That is not failure.
It is useful clarity.
