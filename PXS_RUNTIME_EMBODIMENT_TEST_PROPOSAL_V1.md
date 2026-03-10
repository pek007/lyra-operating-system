# PXS_RUNTIME_EMBODIMENT_TEST_PROPOSAL_V1.md

Status: Active draft v1  
Owner: Lyra / Control Panel  
Proposed recipient: Vega / `pxs` runtime  
Date: 2026-03-10

## Purpose
Propose a bounded runtime-embodiment test in the separate `pxs` workspace to validate whether the product-embodiment approach developed in Lyra OS packages cleanly in an isolated runtime.

## Why test in `pxs`
`pxs` is a good test bed because:
- it has low current disruption risk
- it already has a stronger runtime/workspace boundary than Lyra OS
- it is a better environment for testing whether a capability can be cleanly packaged, activated, and evaluated without relying on Lyra-session context
- it is directly relevant to Company-as-Code operating foundations

## Important boundary rule
This proposal does **not** assume that Lyra OS artifacts or skills should simply be copied into `pxs`.

Any adoption in `pxs` must respect the Vega boundary model:
- separate runtime/workspace/state
- no casual cross-domain reads
- explicit handoff or dependency path where sharing is needed
- domain-local adaptation rather than naive transplant

## Recommended first test
### Candidate
A **bounded Governance/VERIFY-style capability** in `pxs`, preferably as:
- first a **Skill concept and local operating procedure**
- optionally followed by a **small cron-backed review loop** if the skill proves useful

## Why this is the best first test
This candidate is preferred because it is:
- bounded
- evidence-producing
- low-risk compared with task-engine or deeper plugin work
- compatible with Vega’s existing autonomous governance sweep posture
- easy to compare against current manual/governance behavior

It also respects the current `pxs` shape:
- Vega already has explicit governance boundary rules
- cron-driven governance sweeps already exist in the PX environment
- VERIFY-like work naturally produces evidence and clear pass/fail/issue outputs

## Proposed test objective
Demonstrate that one repeated PX governance action can be:
- packaged into a reusable local runtime capability
- executed consistently from explicit artifacts
- produce bounded evidence/output
- remain compatible with Vega’s boundary discipline

## Proposed first test shape
### Phase 1 — Skill/procedure test
Ask Vega to define and test one bounded governance-skill pattern in `pxs`:
- select one specific governance verification/review action
- define trigger, inputs, outputs, evidence, and escalation conditions
- run one live bounded trial
- record result and friction

### Phase 2 — Optional cron test
Only if Phase 1 is successful:
- wrap the same bounded pattern in a low-noise cron loop
- keep output/evidence narrow
- confirm it improves reliability without creating noise or uncontrolled automation

## What not to test first
Do **not** start with:
- plugin-building
- broad multi-product embodiment in PX
- a large shared-core refactor
- anything that weakens Vega’s boundary model
- anything that silently imports Lyra-specific coordination assumptions into PX

## Success criteria
The test is successful if:
1. the capability is packaged cleanly inside `pxs`
2. Vega can execute it from PX-local artifacts and procedures
3. output/evidence are clear and bounded
4. no boundary confusion is introduced
5. the result is useful enough to justify either standardizing the local pattern or adding a cron-backed version

## Failure signals
- the capability depends on Lyra-session context to work
- it creates ambiguity around boundary/domain ownership
- it produces noise without reliable value
- it needs plugin-level complexity immediately to be useful
- it weakens Vega’s explicit runtime separation

## Suggested communication to Vega
Recommended framing:
- this is a **bounded packaging test**, not a product redesign
- goal is to test whether one repeated PX governance action can be embodied cleanly as a reusable local capability
- Lyra OS work is reference input only, not a template to copy blindly

## Suggested ask to Vega
1. Evaluate whether a bounded Governance/VERIFY-style capability is the right first embodiment test in `pxs`.
2. If yes, propose the smallest viable local test inside PX scope.
3. State whether it should begin as:
   - a skill/procedure only,
   - or a skill plus bounded cron loop.
4. Define evidence and boundary checks for the test.

## Why not start with Task/TDE in `pxs`
Task/TDE-related embodiment is higher leverage, but also higher coupling and higher complexity.
For `pxs`, the better first test is one that proves packaging discipline without entangling the heaviest engine assumptions immediately.

## Recommended next step
Send this proposal to Vega as a structured handoff and ask for:
- accept / reject / modify
- proposed test shape
- evidence criteria
- any boundary objections

## Bottom line
Use `pxs` as a **clean proving ground** for runtime embodiment, but start with a bounded governance-style capability that fits Vega’s isolated operating model rather than trying to transplant Lyra OS coordination machinery wholesale.
