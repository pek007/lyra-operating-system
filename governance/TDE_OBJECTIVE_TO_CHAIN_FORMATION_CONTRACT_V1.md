# TDE Objective-to-Chain Formation Contract v1

Status: Active
Owner: JOB-PROD-001
Date: 2026-03-10
Related WO: `WO-2026-TDE-OBJECTIVE-TO-CHAIN-FORMATION-V1`
Related runtime contract: `os/sops/TDE_CHAINING_CONTRACT_V1.md`

## Purpose
Define the first bounded contract for turning approved high-level objectives into executable chain structures in TDE.

This contract governs **formation**, not broad autonomous generation.
Its job is to ensure that objective-level intent becomes bounded, explicit, auditable chain structure before runtime chaining executes it.

## Core principle
TDE may execute bounded chains only after the chain structure has been made explicit.

High-level objectives do not become executable through conversational implication or free-form interpretation alone.
They must first be converted into a bounded approved chain model.

## Scope
### In scope
- approved workflow-family templates
- required fields for objective-to-chain formation
- bounded stage semantics
- dependency structure rules
- approval-boundary declaration
- evidence/decision packet for formation readiness

### Out of scope
- free-form autonomous decomposition
- generic open-ended task generation
- recursive or branching chain synthesis without explicit approval
- replacement of product-owner judgment with implicit agent inference

## Required preconditions for objective-to-chain formation
An objective may be converted into an executable chain only if all of the following are explicit:
1. **Objective identity**
   - objective ID exists and is valid
2. **Approved workflow family**
   - the objective maps to an approved bounded workflow family
3. **Outcome definition**
   - the intended outcome is explicit enough to bound stage semantics
4. **Stage model**
   - required stages are explicitly named
5. **Dependency structure**
   - predecessor/successor rules are explicit
6. **Approval boundary**
   - any stage requiring approval is identified up front
7. **Boundedness rule**
   - no uncontrolled branching/fan-out is implied
8. **Evidence expectation**
   - expected evidence or verification outputs per stage are clear enough for governed progression

If any of these are unclear, formation must fail closed into clarification rather than inventing chain structure implicitly.

## Formation output requirements
A valid objective-to-chain formation output must produce:
- objective ID
- approved workflow-family ID
- ordered stage list
- task/stage mapping
- dependency edges
- approval-gated stage markers where applicable
- chain-policy object
- expected evidence/verification note per stage where relevant

## Approved workflow family rule
In v1, formation is allowed only for explicitly approved workflow families.

Initial approved family:
- `pilot_family_a`
  - `implementation -> verification -> deployment_readiness_review`

Additional workflow families require explicit approval before being used for formation.

## Stage semantics rule
Each stage must have:
- a clear name
- a clear role in progression
- a bounded completion meaning
- a defined predecessor set (if any)

Stages must not be vague placeholders such as:
- "do more work"
- "continue exploring"
- "figure out next step later"

## Approval rule
If a stage may require approval, that must be declared at formation time.

Formation must not hide approval dependency inside later runtime behavior.

The runtime may still promote the stage to eligible/ready per chaining rules, but execution must remain blocked pending approval where required.

## Boundedness rule
Formation v1 must remain narrow.

Not allowed in v1:
- recursive decomposition
- automatic branching trees
- open-ended improvement fan-out
- cross-domain chain synthesis from a single vague objective

## Product-owner rule
Formation is a structured translation of explicit product-owner intent.
It is not permission for the system to infer broad strategic decomposition from underspecified goals.

Product Owners must still provide enough clarity for the chain to be bounded and governed.

## Evidence contract
A formation packet should include:
- objective ID and description
- approved family used
- proposed stage/task structure
- dependency map
- approval-gated stages
- evidence expectations
- explicit statement of why the chain is bounded

## Fail-closed conditions
Formation must not proceed when:
- objective ID is missing/invalid
- approved family is missing
- stage boundaries are ambiguous
- approval requirements are unclear
- dependency structure cannot be made explicit
- the proposed chain would imply uncontrolled branching or open-ended generation

## Change rule
Any expansion beyond approved bounded family templates requires a new contract version or explicit amendment evidence.
