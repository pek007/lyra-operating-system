# Workspace Operating Package Maturity and Validation v1

Status: Draft validation standard
Owner: Lyra OS
Date: 2026-03-14

## Purpose
Provide a lightweight maturity and validation layer for Workspace Operating Packages so they can be assessed consistently without turning the package model into bureaucracy.

This artifact answers two questions:
1. How mature is a given workspace operating package?
2. Is the package valid enough to rely on operationally?

## Relationship to the package model
This validation layer supports:
- `WORKSPACE_OPERATING_PACKAGE_STANDARD_V1.md`
- `WORKSPACE_BOOTSTRAP_AND_RETROFIT_PROTOCOL_V1.md`
- `WORKSPACE_OPERATING_PACKAGE_TEMPLATE_PACK_V1.md`

It is not a substitute for those artifacts.
It is a compact review and quality-control layer.

## Design principles
1. Lightweight over ceremonial
   - Validation should help strengthen real operability, not create paperwork.

2. Structural first
   - Validate whether the workspace can be operated coherently, not whether every document is perfectly polished.

3. Explicit gaps over false completeness
   - A package with clearly recorded gaps is healthier than one that pretends to be complete.

4. Front-door usability matters
   - The package should be understandable and usable by someone who did not participate in the original chat/thread.

## Maturity model
### Level 0 — Ad hoc
Characteristics:
- workspace depends primarily on thread history and implicit memory
- no explicit local SoR map
- no explicit process discovery front door
- authority is ambiguous or mostly unstated

### Level 1 — Minimal
Characteristics:
- workspace purpose and authority boundary are explicit
- local SoR map exists
- process discovery front door exists
- local task, decision, and error paths exist at least in minimal form
- major current gaps are explicitly recorded

### Level 2 — Operable
Characteristics:
- package components work together coherently
- local authority and adopted/shared authority are clearly distinguished
- major operating flows can be followed from artifacts
- package no longer depends mainly on transcript memory for routine operation
- at least some local review/maintenance discipline exists

### Level 3 — Reliable
Characteristics:
- package is deliberately maintained and periodically reviewed
- major local workflows are resilient to context transfer
- local operating artifacts are stable enough to support handoff and repeatable execution
- validation is used to catch drift and missing package elements over time

## Minimum validity criteria
A workspace operating package is minimally valid if all of the following are true:

### 1. Identity and scope are explicit
Required:
- workspace purpose is stated
- authority boundary is stated

Typical artifact:
- `WORKSPACE_PROFILE.md`

### 2. Sources of truth are explicit
Required:
- tasks, decisions, processes, and error/incident paths are mapped or explicitly marked as gaps

Typical artifact:
- `SOURCE_OF_TRUTH.md`

### 3. Official process discovery is explicit
Required:
- there is a front-door artifact for locating applicable official processes
- precedence rules are stated

Typical artifact:
- `PROCESS_DISCOVERY_INDEX.md`

### 4. Local operating guidance exists
Required:
- a top-level local operator/agent guidance artifact exists
- it points to the package front-door artifacts

Typical artifact:
- local `AGENTS.md`

### 5. Task path exists
Required:
- actionable work has an explicit local home or explicit temporary rule
- chat history is not treated as sufficient

Typical artifact:
- `TASK_SYSTEM_OF_RECORD.md`

### 6. Decision path exists
Required:
- durable local decisions have a defined home
- escalation triggers are defined at least minimally

Typical artifact:
- `DECISION_AND_ESCALATION.md`

### 7. Error path exists
Required:
- meaningful errors/incidents have a defined handling path
- stronger adopted/shared paths can be invoked when local maturity is insufficient

Typical artifact:
- `ERROR_AND_INCIDENT_HANDLING.md`

## Validation checks
Use the following checks during bootstrap review, retrofit review, or periodic package review.

### Check A — Scope clarity
Questions:
- Is it clear what this workspace is for?
- Is it clear what is local authority versus adopted/shared authority?

Pass when:
- an informed operator can answer both questions from artifacts alone

### Check B — Front-door completeness
Questions:
- Can an operator find the SoR map, process discovery index, and local operating guidance quickly?
- Do those artifacts point to each other coherently?

Pass when:
- the front-door artifacts form a usable navigation layer

### Check C — Operational route completeness
Questions:
- Can an operator determine where tasks go?
- where decisions go?
- where meaningful errors go?

Pass when:
- all three routes are explicit, even if still minimal

### Check D — Authority precedence clarity
Questions:
- Is it clear how to choose between local artifacts and adopted/shared artifacts?
- Is internal Lyra OS authority prevented from leaking in by default?

Pass when:
- precedence is stated and usable

### Check E — Gap honesty
Questions:
- Are material missing pieces listed explicitly?
- Or does the package create a false impression of completeness?

Pass when:
- significant gaps are visible and named

### Check F — Context-transfer resilience
Questions:
- Could another operator or agent take over without relying mainly on hidden thread context?

Pass when:
- the package provides enough orientation and routing for real continuation

## Validation output format
Recommended summary format:
- Workspace assessed
- Current maturity level
- Validity judgment (`invalid` | `minimally valid` | `operable` | `reliable`)
- Strengths
- Gaps
- Recommended next upgrade

## Suggested rating rules
### Invalid
Use when one or more core routes are absent:
- no usable SoR map
- no process discovery front door
- no explicit task/decision/error path

### Minimally valid
Use when:
- required front-door artifacts exist
- core routes are explicit
- meaningful gaps remain but are visible

### Operable
Use when:
- the package is coherent enough to guide routine operation without heavy transcript dependence

### Reliable
Use when:
- the package is maintained, reviewed, and resilient to transfer/drift

## Example first application: `pxs`
First-pass provisional assessment for `pxs` after retrofit:
- Likely maturity: Level 1 — Minimal
- Likely validity judgment: minimally valid

Reasoning:
- identity/scope explicit
- SoR map explicit
- process discovery explicit
- task/decision/error routes explicit in first-pass form
- still limited local maturity and deeper review discipline

## Review cadence guidance
Suggested lightweight cadence:
- during initial bootstrap
- after first retrofit
- after major workspace scope changes
- periodically for important long-lived workspaces

## Failure modes to avoid
- converting validation into heavy governance theater
- scoring polish instead of operability
- hiding gaps to achieve a higher maturity label
- treating a package as reliable before it survives real reuse or handoff

## Version
- v1.0
- Date: 2026-03-14
- Owner: Lyra OS
