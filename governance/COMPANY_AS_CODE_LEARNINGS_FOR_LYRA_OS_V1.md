# Company-as-Code Learnings for Lyra OS v1

Status: Active
Owner: Lyra
Date: 2026-03-09
Source input: PXS deep research report `Turning PXS into Company-as-Code for Lyra OpenClaw`

## Purpose
Distill which Company-as-Code (CaC) learnings from the PXS report should be applied to Lyra OS itself, and in what order.

This is not a claim that Lyra OS and PXS should be modeled the same way. It is a translation note: what is transferable, what is later-stage, and what is mostly PXS-specific.

## Bottom line
The strongest transferable insight is this:

**Lyra OS should make more of its operating model machine-checkable, explicitly distinguish desired state from runtime state, and tighten change-safety around policy/runtime updates.**

That is more relevant than “Company-as-Code” as a label.

## Adopt now

### 1) Strengthen structured-source-over-markdown where operational truth matters
Lyra OS already has strong markdown governance, but several important areas still rely too much on human-readable artifacts as the effective source of truth.

Adopt now for:
- registries
- decision metadata
- policy packs
- product records
- interface contracts
- assembly metadata

Operating rule:
- where an artifact must be validated, compared, indexed, promoted, or enforced, prefer structured source with generated human-readable views when useful.

Why now:
- reduces ambiguity
- improves validation
- lowers drift risk
- makes agent-safe automation more reliable

### 2) Make desired state vs runtime state more explicit
This is already a real Lyra OS pain point.

We should model more clearly:
- repo-declared desired state
- runtime-applied state
- generated/derived state
- evidence of actual execution

Adopt now for:
- TDE runtime vs repo artifacts
- gateway/runtime config state
- generated indexes/inventories
- policy/effective-direction snapshots

Why now:
- drift and “what is actually active?” ambiguity are already recurring problems
- this improves auditability and safer operations

### 3) Add stronger policy-as-code gates around ownership, boundaries, and risk
Lyra OS has substantial governance intent, but some controls are still convention-heavy.

Adopt now for checks such as:
- every governed artifact has an owner
- boundary-sensitive changes require explicit approval path
- interface changes require the right dominant/co-approver logic
- high-risk operational changes must show evidence and validation
- runtime-impacting changes should not bypass preflight checks

Why now:
- this directly supports TDE, product governance, and security posture

### 4) Treat risky runtime changes with explicit preflight/postflight controls
Today’s OpenClaw update incident makes this urgent.

Adopt now for:
- gateway updates
- runtime package changes
- config changes affecting service continuity
- policy/runtime pack promotions

Minimum control pattern:
- identify active runtime path
- identify install mode
- verify target version/path before restart
- restart only through an explicit controlled procedure
- verify running version after restart
- document rollback path first

Why now:
- immediate reliability/safety gain

### 5) Improve observability for policy/runtime changes
Lyra OS should be better at answering:
- what changed?
- who/what changed it?
- why was it allowed?
- what policy/contract governed it?
- what runtime/evidence shows the outcome?

Adopt now by improving:
- evidence linkage
- change receipts
- drift reports
- runtime verification notes

Why now:
- needed for reliable autonomous operations
- supports continuous improvement and auditability

## Adopt later

### 6) Signed/promotable bundles for policy packs and assemblies
This is strategically strong, but not the first bottleneck.

Potential Lyra OS future applications:
- policy bundles
- prompt/interface packs
- product assemblies
- runtime governance packs

Why later:
- valuable once structured-source and promotion mechanics are cleaner
- premature if underlying contracts are still settling

### 7) More formal GitOps-style reconciliation for runtime state
This is likely part of the right long-term architecture.

Potential later-state pattern:
- repo declares desired state
- runtime exposes actual state
- reconciler identifies drift
- allowed classes self-heal or fail closed
- risky drift requires explicit human decision

Why later:
- strong fit conceptually
- but only after desired-state modeling and contract boundaries are firmer

### 8) Progressive rollout/canary handling for critical runtime changes
Likely valuable for:
- policy changes
- tool permission changes
- runtime behavior thresholds
- high-impact TDE automation changes

Why later:
- useful, but depends on stronger observability and clearer deployable units first

## Mostly PXS-specific / not a near-term Lyra OS priority
The following ideas are valid in the PXS context but should not be imported blindly into Lyra OS right now:
- company-model node-card migration as a primary OS priority
- full business-operating-model resource hierarchy inside Lyra OS
- PXS environment-promotion mechanics as-is
- broad Company-as-Code packaging before Lyra OS operational contracts are stabilized

These may inform interface design between PXS and Lyra OS, but they are not core Lyra OS bottlenecks today.

## Recommended Lyra OS interpretation
Do not copy the PXS Company-as-Code program wholesale.

Instead, apply the report as a pressure test on Lyra OS in five questions:
1. Where are we still using markdown where structured source is needed?
2. Where is desired state not clearly separated from runtime/applied state?
3. Which governance rules are still advisory when they should be machine-checked?
4. Which risky operational changes still lack explicit preflight/postflight controls?
5. Where do we lack visibility into what changed, why, and with what effect?

## Practical next actions
1. Use `OPS-2026-069` to harden runtime update/change procedure immediately.
2. Continue TDE/product-governance work that increases explicit desired-state vs runtime-state separation.
3. Prioritize policy/validator work that makes ownership/boundary rules more enforceable.
4. Identify one or two high-value areas where structured source should replace markdown-led operational truth.
5. Delay signing/bundle/progressive-delivery sophistication until the underlying contracts are cleaner.

## Decision
**Adopt the CaC report as a Lyra OS architectural learning input, not as a direct implementation blueprint.**

Immediate value comes from:
- stronger structured contracts,
- better desired-state/runtime-state separation,
- tighter policy gates,
- safer runtime change procedures,
- and stronger observability.
