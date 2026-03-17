# Workspace Enablement Pattern v1

Status: Draft active pattern
Owner: Lyra OS
Date: 2026-03-17
Purpose: Define the canonical first pattern for enabling a downstream workspace to consume a Lyra OS capability correctly.

Related:
- `CAPABILITY_MODEL_STANDARD_V1.md`
- `CAPABILITY_LIFECYCLE_STANDARD_V1.md`
- `WORKSPACE_BOOTSTRAP_AND_RETROFIT_PROTOCOL_V1.md`
- `WORKSPACE_OPERATING_PACKAGE_STANDARD_V1.md`
- `DELIVERY_MODES_DECISION_FRAMEWORK_V1.md`
- `governance/CAPABILITY_DISTRIBUTION_INVENTORY_V1.md`

---

## Why this exists

The first `pxs` proof case showed that downstream capability use depends not only on the provider-side capability itself, but also on consumer-side enablement.

That consumer-side enablement should not be treated as bespoke workspace glue.
It is a **workspace enablement capability** that Lyra OS should be able to provide systematically.

This pattern captures the first canonical answer to:
**What must Lyra OS provide so a downstream workspace can actually consume a product capability?**

---

## Core principle

A downstream workspace should not need hidden thread memory, tribal knowledge, or bespoke rescue work in order to consume a supported capability.

The enablement pattern should provide the minimum consumer-side structure needed for:
- discovery
- invocation
- governance clarity
- validation
- upgradeability

---

## Pattern structure

A valid workspace enablement pattern for one consumed capability should include all of the following.

### 1. Provider-side capability definition
The provider product must expose:
- a capability record
- a consumer-facing interface artifact when relevant
- current readiness and scope limits

This defines what is being consumed.

### 2. Local workspace front-door integration
The downstream workspace must be able to find the capability through its own local package.

Minimum local routes:
- `SOURCE_OF_TRUTH.md`
- `PROCESS_DISCOVERY_INDEX.md`
- relevant local route artifact(s)

This defines where the consumer starts.

### 3. Local usage pattern
There must be a compact local rule for:
- when the capability should be used
- when it should not be used
- what route the operator/agent follows
- what local artifact is authoritative first

This defines how the consumer behaves.

### 4. Machine contract where automation matters
If the capability depends on intake, validation, request/response semantics, or persistence, the consumer path should rely on an explicit provider-owned contract/schema rather than ad hoc local interpretation.

This defines how machine-usable behavior works.

### 5. Proof/validation scaffold
There must be one concrete proof path showing that the capability can be consumed from the downstream workspace.

This should include:
- one bounded real work item or use case
- one explicit consumption artifact
- acceptance/failure output
- local linkage back to workspace context

This defines how the pattern becomes evidence-backed instead of theoretical.

---

## Minimal enablement bundle

For a first real downstream capability, the minimum enablement bundle is:
- provider capability record
- provider consumption/interface artifact
- local SoR/discovery integration
- local usage note/pattern
- machine contract if needed
- one proof item
- one proof artifact/result

If one of these is missing, the workspace is not yet robustly enabled for that capability.

---

## What the first `pxs` proof case taught us

The first bounded Task Management proof case in `pxs` demonstrated several important rules.

### A. Validation must be fail-closed
The intake path rejected invalid packets until corrected.
That is good and should be preserved.

### B. Consumer-side friction becomes visible only in real proof
Two schema/contract mistakes became visible only when a real local item was routed:
- missing `requested_action`
- invalid `source_type`

This shows why proof cases matter.

### C. Provider capability can be real before consumer path is friction-light
The provider-side intake capability was already real.
The consumer-side path was still awkward.

That means readiness must be judged separately for:
- provider capability
- workspace enablement capability

### D. Local linkage back to workspace context matters
A downstream proof is incomplete unless the workspace can point back to:
- what local item was selected
- what was submitted
- what happened
- where canonical follow-through now lives

---

## Lifecycle rule for workspace enablement

A workspace enablement capability should move through the same broad lifecycle as other capabilities:
- proposed
- approved
- building
- validating
- active
- improving
- retiring/retired

But its proof point is different.

A workspace enablement capability is not proven when the provider-side capability merely exists.
It is proven when a downstream workspace can actually use it through a repeatable path.

---

## Bootstrap/retrofit implication

Bootstrap and retrofit should treat missing downstream-consumption components as missing enablement capability instances.

Use `WORKSPACE_ENABLEMENT_COMPONENT_MODEL_V1.md` to decide whether a needed component belongs in:
- core workspace enablement
- capability-specific enablement
- workspace-local adaptation

That means the protocol should ask not only:
- what product capabilities are consumed here?

but also:
- what enablement capability instances must be present locally for those consumed capabilities to be usable?

Examples:
- local discovery integration
- local intake helper pattern
- local validation scaffold
- local capability access matrix

---

## Default delivery mix for workspace enablement

For current Lyra OS maturity, the default first delivery mix for workspace enablement should usually be:
- workspace artifact
- ops-pack style operating guidance
- schema-backed provider contract where required
- optional skill when guidance-heavy behavior is central

Do not default to service/plugin/daemon for workspace enablement unless the consumer interaction truly requires it.

---

## Validation checklist

A workspace enablement pattern passes v1 when:
- [ ] provider capability is explicit
- [ ] local front-door integration exists
- [ ] local usage rule exists
- [ ] machine contract is explicit where required
- [ ] one real downstream proof item has been run
- [ ] fail-closed behavior is visible where relevant
- [ ] local linkage back to workspace context is explicit
- [ ] known friction and limits are recorded

---

## Anti-patterns

Avoid:
- treating downstream local scaffolding as unowned workspace clutter
- assuming provider capability readiness automatically means consumer readiness
- copying detailed provider contracts into local front-door artifacts
- trying to package everything as a service before local patterns are proven
- declaring a workspace “enabled” without one real proof case

---

## Initial conclusion

Workspace enablement is now a first-class Lyra OS capability family.

The first canonical enablement pattern is:
- provider capability record
- provider consumption interface
- local workspace routing integration
- local usage pattern
- machine contract where needed
- proof item + proof result

That is the first robust answer to downstream capability enablement.
