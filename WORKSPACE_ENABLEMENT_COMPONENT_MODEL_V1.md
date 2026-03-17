# Workspace Enablement Component Model v1

Status: Draft active model
Owner: Lyra OS
Date: 2026-03-17
Purpose: Define the boundary between default workspace bootstrap/retrofit outputs, capability-specific enablement components, and workspace-local adaptations.

Related:
- `WORKSPACE_ENABLEMENT_PATTERN_V1.md`
- `WORKSPACE_BOOTSTRAP_AND_RETROFIT_PROTOCOL_V1.md`
- `WORKSPACE_OPERATING_PACKAGE_STANDARD_V1.md`
- `CAPABILITY_MODEL_STANDARD_V1.md`
- `CAPABILITY_LIFECYCLE_STANDARD_V1.md`

---

## Why this exists

Once workspace enablement is treated as a real Lyra OS capability, we need a clear answer to:

1. what every supported workspace should receive by default
2. what should be added only when a specific consumed capability requires it
3. what should remain local to one workspace as a true local adaptation

Without this split, bootstrap/retrofit risks becoming either:
- too generic to enable real downstream consumption, or
- too bloated because every capability-specific need gets forced into the default package

---

## Three component classes

## Class A — Core workspace enablement components
These are the components every serious supported workspace should receive by default through bootstrap/retrofit.

They are not tied to one specific product capability.
They create the minimum local operating environment in which any downstream capability can later be consumed coherently.

### Required default set
- `WORKSPACE_PROFILE.md`
- `SOURCE_OF_TRUTH.md`
- `PROCESS_DISCOVERY_INDEX.md`
- local `AGENTS.md` or equivalent top-level operating guidance
- explicit local decision/escalation path
- explicit local error/incident path

### What these do
They answer:
- what this workspace is
- what is authoritative locally
- where official processes are found
- how decisions/errors are routed

### Rule
If a workspace lacks these, it is not yet even minimally enabled.

---

## Class B — Capability-specific enablement components
These are installed only when the workspace consumes a specific product capability that requires more than the default core package.

They are the consumer-side enablement layer for one capability family.

### Examples
- local routing note for when to use Task Management intake
- local reference to a provider consumption interface
- local intake helper/template
- local capability access matrix
- local proof/validation scaffold for one consumed capability
- local runbook for a consumed security/review loop

### What these do
They answer:
- how this specific capability is discovered locally
- when it should be invoked
- what provider contract applies
- how local context links to provider-side behavior
- how the workspace proves it can actually use the capability

### Rule
If a capability cannot be consumed correctly without a local component, that component should normally be treated as a capability-specific enablement component — and therefore something Lyra OS should be able to package and provide repeatedly.

---

## Class C — Workspace-local adaptations
These are truly local to one workspace’s own context, domain, or operating preferences.

They should not automatically be promoted into shared enablement patterns unless the same need repeats across multiple workspaces.

### Examples
- local roadmap files unique to one workspace
- local stakeholder-specific conventions
- workspace-specific naming/domain rules
- a local planning structure that reflects the workspace’s own product domain

### What these do
They answer:
- what is special about this one workspace
- what local domain choices exist beyond shared enablement needs

### Rule
A local adaptation should remain local unless it shows repeated cross-workspace demand.
When the same local adaptation keeps recurring, reconsider whether it is actually a missing shared enablement capability.

---

## Decision rule for classification

When deciding where a component belongs, ask these questions in order.

### 1. Would every serious supported workspace need this, regardless of which capability it consumes?
- If yes → **Class A: core workspace enablement**

### 2. Is this needed only because the workspace is consuming a specific product capability?
- If yes → **Class B: capability-specific enablement**

### 3. Is this mostly unique to the local workspace’s own domain/context/preferences?
- If yes → **Class C: workspace-local adaptation**

If the answer is unclear, start with B or C and promote upward only after repeated evidence.

---

## The `pxs` proof-case interpretation

The first `pxs` Task Management proof case clarifies the split.

### Core workspace enablement (Class A)
Already present in `pxs`:
- `WORKSPACE_PROFILE.md`
- `SOURCE_OF_TRUTH.md`
- `PROCESS_DISCOVERY_INDEX.md`
- local authority routes

These belong in default bootstrap/retrofit for serious workspaces.

### Capability-specific enablement (Class B)
Created/discovered through the Task Management proof case:
- local Task Management routing pattern
- explicit intake artifact path
- proof-item/result linkage
- capability access matrix
- package pattern / proof-case plan

These should not stay `pxs`-specific forever if future workspaces will also consume Task Management.
They are evidence for a reusable capability-specific enablement package.

### Workspace-local adaptations (Class C)
Remain local to `pxs`:
- `docs/now-next-later.md`
- `docs/milestones.md`
- domain-specific roadmap and architecture choices

These are not default outputs for every workspace.

---

## Bootstrap/retrofit implication

### Bootstrap default should install Class A by default
That is the minimum package baseline.

### Bootstrap/retrofit should then assess which Class B components are needed
Based on:
- consumed products/capabilities
- chosen delivery modes
- interface shape
- governance/risk posture

### Class C should be left to local workspace ownership
Unless repeated cross-workspace evidence shows it should be promoted.

---

## Initial recommended defaults

### Default bootstrap/retrofit outputs (Class A)
- workspace profile
- source-of-truth map
- process discovery index
- local top-level agent guidance
- local decision/escalation route
- local error/incident route

### Default capability-specific package triggers (Class B)
A capability-specific enablement component should be added when a consumed capability requires any of the following:
- local invocation/routing guidance
- provider-side contract reference
- local helper/template for repeated use
- proof/validation scaffold
- local capability status/access mapping

---

## Anti-patterns

Avoid:
- dumping capability-specific behavior into the default bootstrap package
- treating repeated cross-workspace enablement needs as one-off local tweaks
- promoting obviously local domain conventions into shared defaults too early
- assuming Class A alone is enough for real capability consumption

---

## Practical operating rule

Bootstrap/retrofit should answer three separate questions:
1. what core enablement does every serious workspace need?
2. what extra enablement is required because this workspace consumes specific capabilities?
3. what remains genuinely local and should stay owned by the workspace?

If those are not separated, enablement architecture will drift.

---

## Initial conclusion

The right split is:
- **Class A:** core workspace enablement components
- **Class B:** capability-specific enablement components
- **Class C:** workspace-local adaptations

This gives Lyra OS a cleaner way to scale downstream support without turning bootstrap into either a bare skeleton or a bloated universal package.
