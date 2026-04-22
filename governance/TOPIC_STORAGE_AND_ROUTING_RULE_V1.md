# Topic Storage and Routing Rule v1

Status: Draft active rule
Owner: Governance
Date: 2026-04-22

## Purpose
Define the default rule for where discussed topics should be stored in Lyra OS.

This rule exists to prevent three common failures:
- relying on chat or memory alone for operational continuity
- turning every topic into a wiki page
- scattering the same topic across the wrong artifact types without a clear primary home

## Core principle
Do not start with the storage medium.
Start with the **nature of the topic**.

A topic should be stored primarily according to what kind of thing it is:
- active work
- failure / incident
- durable operating rule
- reusable knowledge
- continuity memory

## Default routing order
Use the following order of preference.

### 1. Active work -> execution system / product execution artifacts
If the topic needs to be done, tracked, delegated, decided, or followed up, its primary home is:
- TDE / canonical execution state
- related product execution artifacts such as `PLAN.md`, `TOP_PRIORITIES.md`, current execution notes, or linked decision packets

Use for:
- active investigations
- implementation work
- open follow-through
- unresolved questions requiring explicit next steps
- items that need ownership and progression

Rule:
Chat may discuss the work, but chat is not the primary home.

### 2. Incident / near miss / control failure -> incident or error artifact + execution routing
If the topic is mainly about something that failed, almost failed, or exposed a control/process weakness, its primary home is:
- incident / error artifact
- `INCIDENT_LOG.md` where applicable
- then corrective/preventive follow-through in TDE or canonical execution state

Use for:
- outages
- security/control failures
- silent degraded mode
- misrouting or failed recovery
- meaningful operational misses with recurrence risk

Rule:
Incident prose is not enough by itself. Material follow-through should be routed into canonical execution state.

### 3. Durable operating rule / standard / architecture -> product or governance artifact
If the topic becomes a durable way of working, design rule, recovery rule, or architecture rule, its primary home is:
- SOP
- runbook
- standard
- architecture/design artifact
- relevant product operating-model or governance artifact

Use for:
- recovery playbooks
- resilience workflow
- health model
- architecture constraints
- routing rules
- decision-rights logic

Rule:
If the system should behave differently next time because of the topic, a durable operating artifact is usually the right home.

### 4. Reusable compact knowledge -> wiki
If the topic is primarily reusable knowledge rather than live operational truth, its primary home may be:
- wiki

Use for:
- compact syntheses
- stable operating patterns
- reusable conceptual explanations
- distilled knowledge worth browsing later

Do **not** use wiki as the primary home for:
- active work state
- live incident management
- current control posture
- execution routing
- unresolved operational questions

Rule:
Wiki is for compact reusable knowledge, not active operational truth.

### 5. Continuity only -> memory
If the topic mainly needs continuity support rather than formal operational handling, its home is:
- `memory/YYYY-MM-DD.md`
- selectively `MEMORY.md` when truly durable and appropriate

Use for:
- session continuity
- recent decisions already stored canonically elsewhere
- lightweight reminders of what happened

Rule:
Memory supports continuity; it is not the system of record for active operations.

## Practical decision rule
When a topic comes up, ask in this order:

### Q1. Does something need to be done, tracked, or decided?
If yes -> route to TDE / execution artifacts.

### Q2. Did something fail or nearly fail?
If yes -> create or update an incident/error artifact, then route follow-through into execution state.

### Q3. Should the system behave differently next time because of this?
If yes -> create or update a durable operating artifact (runbook, SOP, standard, architecture note).

### Q4. Is this mainly reusable, compact knowledge?
If yes -> wiki may be appropriate.

### Q5. Is this mainly continuity context?
If yes -> memory is enough.

## Anti-patterns
Avoid these default mistakes.

### 1. Chat-only operational state
Do not leave active work or important follow-through only in transcript history.

### 2. Wiki-first operational handling
Do not create wiki pages for active incidents, open work, or live control posture.

### 3. Memory as substitute for execution routing
Do not use memory files as the primary home for work that needs ownership, progression, and verification.

### 4. Architecture artifact for every small issue
Do not over-promote short-lived or unresolved issues into standards too early.

### 5. Incident note without corrective routing
Do not stop at documenting the incident if follow-through is required.

## Examples

### Example A. OpenClaw auth outage with silent fallback spend
Primary homes:
- incident artifact
- TDE follow-through
- later runbook update
- maybe later wiki only if a stable reusable pattern is worth distilling

### Example B. New resilience playbook
Primary home:
- product operating-model artifact

### Example C. Bootstrapping detector annoyance caused by historical BOOTSTRAP.md
Primary home:
- improvement or product/runtime work item if action is needed
- maybe later small operating note if it becomes a recurring known pattern

### Example D. Compact explanation of line/staff structure in code
Primary home:
- PXS model / architecture artifact
- optionally later wiki if the concept becomes stable reusable explanatory knowledge

## Short conclusion
The primary home for a topic depends on the kind of thing it is.

Default order:
1. active work -> execution system
2. failure -> incident/error artifact + execution routing
3. durable operating rule -> SOP/runbook/standard/architecture
4. reusable compact knowledge -> wiki
5. continuity only -> memory

## Short rule
**Operations first, incident/error second when relevant, durable rule third, wiki fourth, memory last.**
