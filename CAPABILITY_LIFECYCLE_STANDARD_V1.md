# Capability Lifecycle Standard v1

Status: Draft active standard
Owner: Lyra OS
Date: 2026-03-17

## Purpose
Define how a capability should move through its lifecycle inside Lyra OS.

This standard exists to ensure that capabilities are not just named, but also:
- created intentionally
- improved deliberately
- supported and monitored appropriately
- updated through controlled change
- discoverable and consumable
- tested and evidenced
- security/compliance reviewed where needed
- retired cleanly when their time is over

## Scope
This standard applies to capabilities defined under `CAPABILITY_MODEL_STANDARD_V1.md`.

It does not replace:
- Product-as-Code
- process discovery
- delivery-mode decisions
- error reporting
- closed-loop improvement

Instead, it connects them around the capability as the managed lifecycle unit.

## Core principle
A capability is only mature when its whole lifecycle is explicit.

That means a real capability should have explicit answers for:
- how it starts
- how it is approved
- how it is built and validated
- how it reaches consumers
- how it is operated and supported
- how it is improved
- how it is retired

## Lifecycle stages
Use these stages unless there is a strong reason to specialize locally.

### 1. Proposed
The capability has been identified as something the product should provide, but it is not yet approved for active build/distribution.

Questions:
- what consumer need is driving this?
- which product owns it?
- is this truly a capability or just an implementation idea?

Typical artifacts:
- product plan/roadmap entry
- decision question
- intake/idea note

### 2. Approved
The capability has passed the initial ownership/scope/governance test and is approved for design/build.

Questions:
- is ownership clear?
- is the boundary clear enough?
- does this change authority or trust posture?

Typical artifacts:
- decision record
- product-local plan entry
- approved capability record (initial)

### 3. Building
The capability is being implemented or assembled.

Questions:
- what are the implementation elements?
- what delivery mode is intended?
- what consumer-side operating package implications exist?

Typical artifacts:
- code/tools/scripts
- process docs/runbooks
- interface/schema work
- workspace package additions

### 4. Validating
The capability exists in some form and is being tested for correctness, usefulness, and governance fitness.

Questions:
- what proves it works?
- what evidence is required?
- what consumer or downstream proof is needed?

Typical artifacts:
- acceptance checks
- tests
- readiness evidence
- review findings

### 5. Active
The capability is in active use.

Questions:
- who is consuming it?
- what are the operating and support expectations?
- what changes need approval?

Typical artifacts:
- active capability record
- support/monitoring hooks
- current consumer references

### 6. Improving
The capability remains active, but meaningful changes are being made based on incidents, evidence, reviews, or strategy shifts.

Questions:
- what signals are driving improvement?
- what changes to model/process/delivery are required?
- how will improved behavior be verified?

Typical artifacts:
- error reports
- improvement tasks
- updated capability record
- revised delivery-mode decision if needed

### 7. Constrained
The capability remains active but under restrictions because of risk, breakage, readiness limits, cost issues, or boundary concerns.

Questions:
- what is constrained?
- who approved the constrained operation?
- what exits the constrained state?

Typical artifacts:
- incident/error report
- temporary operating rule
- risk note / decision record

### 8. Retiring
The capability is being phased out.

Questions:
- what replaces it, if anything?
- what consumers are affected?
- what compatibility/deprecation path is required?

Typical artifacts:
- retirement decision note
- migration plan
- deprecation warning in capability record

### 9. Retired
The capability is no longer active.

Questions:
- is the record preserved for history?
- are old references marked clearly enough?
- were consumers transitioned or consciously left without replacement?

Typical artifacts:
- retired capability record or archived record
- replacement reference if applicable

## Lifecycle dimensions that must be covered
Every serious capability should have explicit handling for the following dimensions.

### A. Creation
A capability should have:
- a clear consumer/problem statement
- product ownership
- a capability ID and initial record
- a decision that this is a real capability worth carrying

### B. Improvement
A capability should be improvable through:
- incidents
- reviews
- evidence
- direct user feedback
- product strategy changes

This must connect to `CLOSED_LOOP_IMPROVEMENT_MODEL_V1.md`.

### C. Support and operation
For active capabilities, define:
- who supports it
- what normal operating cadence/checks exist
- how failures are routed
- what counts as degradation vs outage vs misuse

### D. Update/change
Changes should be classified by impact.

At minimum distinguish:
- descriptive changes (wording, docs, clarity)
- behavioral changes (what the capability does)
- boundary/authority changes (security/trust/risk implications)
- distribution changes (same capability, new delivery mode)
- retirement changes

Behavioral or boundary-impacting changes should trigger stronger review.

### E. Discovery and findability
A capability should be discoverable through:
- product-local records
- portfolio inventory where useful
- process discovery routing where relevant
- workspace operating package front doors for consumer-side use

If consumers cannot find a capability without tribal knowledge, the lifecycle is incomplete.

### F. Testing and evidence
A capability must specify:
- what good operation looks like
- how correctness is tested
- what readiness proof is required
- what evidence artifacts should exist

### G. Security / compliance / governance approval
Capabilities with meaningful risk must specify:
- approval owner/path
- security/compliance review path where relevant
- rollback/disable path
- boundary assumptions and allowed operating posture

### H. Retirement
A capability should define:
- what triggers retirement
- how consumers are informed or migrated
- where history is retained
- how stale references are prevented from appearing live

## Relationship to existing Lyra OS models
This lifecycle standard should not create a parallel management system.
It should connect to existing layers.

### Product model
Use product artifacts for strategic ownership and product-local plans.

### Process discovery
Use discovery/front-door artifacts to route consumers to the right processes and local operating paths.

### Delivery-mode decisions
Use `DELIVERY_MODES_DECISION_FRAMEWORK_V1.md` to decide how a capability reaches a consumer.

### Error reporting
Use `ERROR_REPORTING_STANDARD_V1.md` when failures, control misses, or incidents affect the capability lifecycle.

### Closed-loop improvement
Use `CLOSED_LOOP_IMPROVEMENT_MODEL_V1.md` to convert meaningful signals into durable capability improvements.

### Workspace operating package
Use `WORKSPACE_OPERATING_PACKAGE_STANDARD_V1.md` and bootstrap/retrofit protocols when a downstream workspace must consume the capability.

## Ownership model
### Products own:
- capability definition
- lifecycle state of their capabilities
- product-local improvement and retirement logic

### Shared governance owns:
- cross-product lifecycle standards
- shared approval rules where boundaries are affected
- shared/system-level lifecycle exceptions

### Workspaces own:
- local package implications for consuming capabilities
- local adaptations required for safe/useful use in that workspace

## Required lifecycle checks
A capability should not be treated as mature unless these questions can be answered:

1. **Creation** — Why does this capability exist, and who owns it?
2. **Delivery** — How does it reach the consumer?
3. **Discovery** — How would a consumer/operator find and understand it?
4. **Validation** — What proves it works?
5. **Governance** — What approvals/controls apply?
6. **Support** — Who notices and handles failure?
7. **Improvement** — How do meaningful signals change it?
8. **Retirement** — How would it be removed cleanly?

## Change classes
Use this lightweight change classification for capability changes.

### Class 1 — Descriptive
- wording, examples, metadata clarity
- no behavior or boundary change

### Class 2 — Behavioral
- capability behavior or consumer outcome changes
- new evidence/validation may be required

### Class 3 — Delivery/distribution
- delivery mode changes, packaging changes, consumer activation changes
- workspace implications may change

### Class 4 — Boundary/authority
- security, trust, approval, scope, side-effect, or compliance posture changes
- stronger governance review required

### Class 5 — Retirement
- capability being deprecated or removed
- migration and compatibility implications required

## Anti-patterns
Avoid:
- creating capability records with no lifecycle path
- allowing active capabilities to have no support/monitoring owner
- treating discovery as optional after build
- shipping capabilities to consumers without defining local workspace implications
- improving a capability in code without updating the governing capability record
- retiring a capability informally while leaving live-looking references behind

## Minimal lifecycle checklist
For any significant capability, ensure:
- [ ] capability record exists
- [ ] owner and consumers are explicit
- [ ] delivery mode is explicit
- [ ] evidence/validation path is explicit
- [ ] governance/security path is explicit if needed
- [ ] support/failure path is explicit
- [ ] improvement path is explicit
- [ ] retirement trigger/path is explicit

## Initial conclusion
Capability lifecycle management in Lyra OS is broader than classic product lifecycle management because capabilities may be delivered through multiple vehicles (docs, skills, tools, services, cron loops, workspace packages) and consumed in multiple scopes.

So the managed unit here is not just the product.
It is the **capability plus its delivery and consumption path**.

## Version
- v1.0
- Date: 2026-03-17
- Owner: Lyra OS
