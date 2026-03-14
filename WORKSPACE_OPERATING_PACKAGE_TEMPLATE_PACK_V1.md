# Workspace Operating Package Template Pack v1

Status: Draft template pack
Owner: Lyra OS
Date: 2026-03-14

## Purpose
Provide a reusable scaffold for bootstrapping or retrofitting a workspace operating package under Lyra OS.

This template pack turns the Workspace Operating Package Standard into a repeatable starting set of local artifacts so future workspaces do not have to invent their operating front doors from scratch.

## Relationship to standards
This template pack implements:
- `WORKSPACE_OPERATING_PACKAGE_STANDARD_V1.md`
- `PROCESS_DISCOVERY_INDEX_STANDARD_V1.md`
- `WORKSPACE_BOOTSTRAP_AND_RETROFIT_PROTOCOL_V1.md`

## Intended use
Use this pack when:
- creating a new downstream workspace
- retrofitting an existing workspace that lacks explicit operating front doors
- repairing a workspace that currently depends too heavily on transcript memory and implicit assumptions

## Template philosophy
This is a minimal viable scaffold.

It should:
- establish local authority clearly
- create retrieval front doors
- make gaps visible
- stay lightweight enough to adopt quickly

It should not:
- force deep process structure too early
- copy internal Lyra OS operating content unnecessarily
- duplicate detailed product-owned process material

## Recommended initial artifact set
For a first-pass workspace package, create these local artifacts:
- `WORKSPACE_PROFILE.md`
- `SOURCE_OF_TRUTH.md`
- `PROCESS_DISCOVERY_INDEX.md`
- `AGENTS.md`
- `TASK_SYSTEM_OF_RECORD.md`
- `DECISION_AND_ESCALATION.md`
- `ERROR_AND_INCIDENT_HANDLING.md`

## Artifact templates

---

# 1. `WORKSPACE_PROFILE.md`

```md
# WORKSPACE_PROFILE

Status: Draft bootstrap artifact
Workspace: <name>
Date: <date>
Owner: <owner>

## Purpose
<What this workspace is for>

## Authority boundary
<What this workspace owns locally>
<What it does not automatically inherit>

## Primary stakeholders
- <stakeholder>

## Major consumed capabilities
- <product/capability>

## Current maturity judgment
<ad hoc|minimal|operable|reliable>
```

---

# 2. `SOURCE_OF_TRUTH.md`

```md
# SOURCE_OF_TRUTH

Status: Draft bootstrap artifact
Workspace: <name>
Date: <date>

## Purpose
Make the main operating authorities for this workspace explicit.

## Primary local sources of truth
### Workspace purpose and scope
- <path>

### Architecture and design direction
- <path>

### Local decisions
- `DECISION_AND_ESCALATION.md`
- <decision artifact>

### Roadmap / sequencing
- `TASK_SYSTEM_OF_RECORD.md`
- <planning artifacts>

### Consumed product/assembly/package inputs
- <manifest or lock artifact>

## Operational authority map
### Official process discovery front door
- `PROCESS_DISCOVERY_INDEX.md`

### Local top-level operating guidance
- `AGENTS.md`

### Task system of record
- `TASK_SYSTEM_OF_RECORD.md`

### Error / incident handling
- `ERROR_AND_INCIDENT_HANDLING.md`

### Decision / escalation path
- `DECISION_AND_ESCALATION.md`

## Authority precedence
1. Most specific approved local artifact
2. Approved adopted/shared artifact explicitly consumed by this workspace
3. Broader fallback artifact when no more specific approved artifact exists

## Known current gaps
- <gap>
```

---

# 3. `PROCESS_DISCOVERY_INDEX.md`

```md
# PROCESS_DISCOVERY_INDEX

Status: Draft bootstrap artifact
Workspace: <name>
Date: <date>

## Scope
This index applies to <workspace>.

## Use rule
Before performing a non-trivial operational activity, check whether an official process, SOP, runbook, or standard applies here.

## Official artifacts in this scope
Official process artifacts for this workspace are:
- approved local workspace artifacts
- approved local docs/runbooks
- explicitly adopted shared artifacts

## Process families
### Workspace purpose / authority / operating package
- `WORKSPACE_PROFILE.md`
- `SOURCE_OF_TRUTH.md`
- `AGENTS.md`

### Local decisions
- `DECISION_AND_ESCALATION.md`

### Roadmap / sequencing
- `TASK_SYSTEM_OF_RECORD.md`

### Error / incident handling
- `ERROR_AND_INCIDENT_HANDLING.md`

### Architecture / delivery / governance
- <local or adopted artifacts>

## Precedence
1. Most specific approved local artifact
2. Approved adopted/shared artifact
3. Broader fallback artifact when needed

## Related authority artifacts
- `WORKSPACE_PROFILE.md`
- `SOURCE_OF_TRUTH.md`
- `AGENTS.md`
```

---

# 4. `AGENTS.md`

```md
# AGENTS.md - <workspace>

## Core rule
Treat this workspace as its own local operating scope.
Do not assume broader internal operating mechanics apply unless explicitly adopted here.

## Before non-trivial operational activity
Start with:
- `PROCESS_DISCOVERY_INDEX.md`
- `SOURCE_OF_TRUTH.md`
- `WORKSPACE_PROFILE.md`
- `TASK_SYSTEM_OF_RECORD.md`
- `DECISION_AND_ESCALATION.md`
- `ERROR_AND_INCIDENT_HANDLING.md`

## Authority rule
Prefer:
1. most specific approved local artifact
2. approved adopted/shared artifacts explicitly consumed here
3. broader fallback artifacts only when no more specific applicable authority exists

## Working style
- prefer explicit local artifacts over hidden assumptions
- keep durable operating context in files, not just chat
- propose missing front-door artifacts when you find recurrent ambiguity
```

---

# 5. `TASK_SYSTEM_OF_RECORD.md`

```md
# TASK_SYSTEM_OF_RECORD

Status: Draft bootstrap artifact
Workspace: <name>
Date: <date>

## Purpose
Define where actionable work is tracked in this workspace.

## Current rule
The working local task system of record is:
- <active planning artifact>
- <milestone/backlog artifact>
- <implementation artifacts for in-flight work>

## What counts as actionable work
- implementation tasks
- architecture follow-ups
- documentation work required to closure
- readiness/fix work

## What does not count
- chat history alone
- scattered notes alone
- decision logs without tracked follow-through

## Usage rule
When creating actionable work:
1. record it in the local task SoR
2. connect execution to implementation artifacts when active
3. do not leave durable work only in transient thread context

## Current limitations
- <gap>
```

---

# 6. `DECISION_AND_ESCALATION.md`

```md
# DECISION_AND_ESCALATION

Status: Draft bootstrap artifact
Workspace: <name>
Date: <date>

## Purpose
Define how local decisions are recorded and when escalation is required.

## Local decision home
- <decision artifact>

## Decision rule
When a non-trivial local decision is made:
1. decide in the appropriate working context
2. record the durable result in the local decision home
3. update affected artifacts
4. create follow-up work in the task SoR when needed

## Escalate when
- authority boundary changes
- consumed capability/package changes materially
- governance/approval is required beyond local authority
- material security/external-commitment implications exist

## Escalation destinations
- <local/adopted governance artifacts>

## Current limitations
- <gap>
```

---

# 7. `ERROR_AND_INCIDENT_HANDLING.md`

```md
# ERROR_AND_INCIDENT_HANDLING

Status: Draft bootstrap artifact
Workspace: <name>
Date: <date>

## Purpose
Define how meaningful errors, incidents, and control failures are handled.

## Use this path when the issue materially affects
- delivery reliability
- system behavior
- architecture integrity
- security posture
- execution continuity

## Local handling rule
When a meaningful error or incident occurs:
1. capture it in the best available local artifact
2. identify immediate mitigation
3. create follow-up action in the local task SoR if needed
4. update local decision/process artifacts if a structural weakness is exposed
5. use adopted stronger formal paths when local maturity is insufficient

## Escalate when
- material security implications exist
- authority boundary is crossed
- local handling is insufficient
- adopted package guidance is broken or missing

## Related artifacts
- `SOURCE_OF_TRUTH.md`
- `PROCESS_DISCOVERY_INDEX.md`
- `TASK_SYSTEM_OF_RECORD.md`
- `DECISION_AND_ESCALATION.md`
```

## Bootstrap notes
When using this pack:
1. fill the artifacts with the smallest truthful local content
2. do not hide major gaps; list them explicitly
3. prefer linking to adopted local/shared authorities over copying detailed content
4. review the package as a coherent set after first instantiation

## Retrofit notes
For existing workspaces, do not replace useful artifacts unnecessarily.
Instead:
- normalize what already exists
- create missing front-door artifacts
- make precedence and authority explicit
- leave deeper maturity improvements for later iterations

## First real applied example
This template pack was informed by the first retrofit pass applied to `pxs/`.
That case should be used as the first practical reference when evaluating whether the pack remains lightweight and usable.

## Version
- v1.0
- Date: 2026-03-14
- Owner: Lyra OS
