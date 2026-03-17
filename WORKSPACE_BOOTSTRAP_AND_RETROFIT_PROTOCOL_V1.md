# Workspace Bootstrap and Retrofit Protocol v1

Status: Draft protocol
Owner: Lyra OS
Date: 2026-03-14

## Purpose
Define how Lyra OS:
- bootstraps a new workspace as a usable operating package
- assesses an existing workspace against the Workspace Operating Package Standard
- closes the most important structural gaps without relying on hidden thread memory

## Scope
This protocol applies to downstream workspaces that consume Lyra OS product capabilities.

It is the lifecycle/control companion to:
- `WORKSPACE_OPERATING_PACKAGE_STANDARD_V1.md`
- `PROCESS_DISCOVERY_INDEX_STANDARD_V1.md`

## Core principle
A workspace package should not be expected to appear fully formed by accident.
Lyra OS must be able to:
- provision a minimum viable package for a new workspace
- assess and strengthen an existing workspace
- make structural gaps explicit when they cannot yet be resolved

## Modes
### Mode A — Bootstrap
Use when creating a new workspace package from scratch.

### Mode B — Retrofit
Use when a workspace already exists and needs structure, repair, or completion.

## Protocol outputs
A valid run of this protocol should produce some or all of the following:
- workspace package assessment
- list of existing artifacts mapped to the standard
- identified package gaps
- proposed or installed minimum artifacts
- unresolved decisions or authority questions
- readiness judgment

## Bootstrap protocol
### Step 1. Define workspace scope
Capture:
- workspace name
- purpose
- owner/stakeholder boundary
- authority boundary
- primary users/consumers

Primary output:
- initial `WORKSPACE_PROFILE.md`

### Step 2. Identify consumed products and capabilities
Determine:
- which Lyra OS products this workspace consumes
- which delivery modes are active for those products in this workspace
- what local operating implications follow from that consumption
- which **workspace enablement capabilities** must be instantiated locally in order for those consumed capabilities to be usable

Primary output:
- consumed-capability inventory or equivalent bootstrap notes
- first-pass workspace enablement inventory (or equivalent notes)

### Step 3. Instantiate minimum package artifacts
Create, at minimum:
- `WORKSPACE_PROFILE.md`
- `SOURCE_OF_TRUTH.md`
- `PROCESS_DISCOVERY_INDEX.md`
- local `AGENTS.md` or equivalent top-level operating guidance

### Step 4. Define local authority paths
Make explicit:
- task home
- decision home
- error/incident home
- official process locations
- escalation path

Primary output:
- first-pass `SOURCE_OF_TRUTH.md`

### Step 5. Define process discovery front door
Create a local Process Discovery Index using the standard.

It should route to:
- local process families
- adopted shared standards when applicable
- relevant workspace-local runbooks if they already exist

### Step 6. Record open structural gaps
If the workspace lacks important local artifacts, do not hide the gap.
Record what is still missing and whether the workspace is only minimally operable or fully operable.

Interpretation rule:
- if a missing local component is required for repeated downstream capability consumption, treat it as a missing **workspace enablement capability instance**, not just a random documentation gap

### Step 7. Validate package minimum viability
Check whether the workspace can be operated without relying mainly on transcript memory.

Minimum viability questions:
- is purpose explicit?
- is authority explicit?
- are main SoRs explicit?
- can official processes be discovered?
- can major local work routes be followed?

## Retrofit protocol
### Step 1. Inventory existing artifacts
Collect the current top-level and domain-local operating artifacts that appear to govern the workspace.

Typical inventory targets:
- profile/identity docs
- AGENTS-style guidance
- process/runbook docs
- SoR/registry docs
- task/decision/error homes
- local product/workspace operating artifacts

### Step 2. Map inventory to package components
Map existing artifacts against the Workspace Operating Package Standard.

Key question:
- which mandatory package components already exist, partially exist, or do not exist?

### Step 3. Assess authority clarity
For each key operating area, determine whether authority is:
- explicit and local
- explicit but external/shared
- ambiguous
- absent

Focus especially on:
- tasks
- decisions
- errors/incidents
- official processes
- escalation

### Step 4. Identify package gaps and overlaps
Classify findings such as:
- missing mandatory artifact
- duplicated authority
- stale front-door artifact
- process not discoverable
- local artifact wrongly depending on internal-only knowledge

### Step 5. Propose minimum viable retrofit
Prefer the smallest set of artifacts/changes that makes the workspace materially more operable.

Typical first retrofit package:
- `WORKSPACE_PROFILE.md`
- `SOURCE_OF_TRUTH.md`
- `PROCESS_DISCOVERY_INDEX.md`
- light update to local `AGENTS.md`

### Step 6. Install or update artifacts
Create or update local artifacts.
Where existing useful material already exists, normalize or point to it rather than rewriting everything from scratch.

### Step 7. Record residual gaps
If the workspace still lacks deeper runbooks or authority decisions, record those gaps explicitly instead of pretending the retrofit is complete.

### Step 8. Judge readiness
Classify the workspace package state, for example:
- ad hoc
- minimal
- operable
- reliable

## Decision rules
When applying this protocol:
- prefer local authority over hidden thread context
- prefer the smallest viable package that improves operability
- prefer linking to owning artifacts over duplicating detailed process content
- do not leak internal Lyra OS operating mechanics into downstream workspaces unless required

## Relationship to product delivery
Bootstrap and retrofit must be informed by product consumption.
A workspace package should reflect the product capabilities actually delivered into that workspace, not a generic checklist detached from real consumption.

This means the protocol should ask:
- which products are consumed here?
- what delivery modes were chosen?
- what local operating artifacts are required to consume them well?

## Recommended evidence/output format
A bootstrap or retrofit review should produce:
- workspace assessed
- products/capabilities consumed
- existing package artifacts
- missing package artifacts
- changes applied now
- remaining gaps
- readiness status
- next recommended actions

## Suggested first use case
Use `pxs` as the first retrofit case.
Goals:
- test whether the package model is concrete enough to apply
- avoid importing internal-only Lyra OS mechanics unnecessarily
- determine the minimum viable operating package for a real downstream workspace

## Failure modes to avoid
- creating too much structure before clarifying authority
- copying internal Lyra OS artifacts into downstream scopes without need
- writing a discovery/index layer that points nowhere concrete
- confusing workspace package assembly with product ownership
- declaring a workspace “set up” when it still depends mainly on thread history

## Version
- v1.0
- Date: 2026-03-14
- Owner: Lyra OS
