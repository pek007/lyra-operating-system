# MEMORY_PROCESS_V1.md

## Purpose
Define how Lyra OS captures, structures, activates, retrieves, evaluates, and improves memory across agent, session, job, knowledge, and coordination scopes.

## Process Owner
- Primary owner: Lyra
- Owning product assembly: Control Panel
- Ownership type: Horizontal platform capability

## Why this process exists
Lyra OS depends on durable context, portable state, and selective retrieval. Memory is therefore not a single file or feature. It is a cross-system capability that determines continuity, coordination quality, decision quality, portability across jobs, and the compounding value of product work.

This process exists to ensure that:
- important context does not remain trapped in transient sessions,
- durable knowledge is stored in the right canonical artifacts,
- memory is retrievable at runtime with appropriate scope and provenance,
- jobs can move without losing operational continuity,
- product deliveries increase future system capability rather than only solving immediate needs.

## Core Principle
Files and structured runtime artifacts are the source of truth. Indexes and retrieval layers are accelerators. Prompt context is a bounded working cache, not the archive.

## Scope Model

### 1. Agent Memory
Purpose:
- identity, preferences, durable lessons, local operating notes, stable constraints

Canonical artifacts:
- `SOUL.md`
- `USER.md`
- `TOOLS.md`
- `MEMORY.md` (main/private-scope curated long-term memory only)
- other explicitly agent-scoped durable notes

Rules:
- keep lean and durable
- do not use as source of truth for active task or job state
- respect trust boundary and channel/session visibility rules

### 2. Session Memory
Purpose:
- transient working context, recent dialogue continuity, current tool outputs, local short-horizon reasoning support

Canonical artifacts:
- session transcripts
- compaction summaries
- daily memory notes where applicable

Rules:
- useful but non-authoritative
- must not be relied on as the sole carrier of job continuity
- should be compacted and pruned aggressively when stale

### 3. Job Memory
Purpose:
- portable execution context attached to a responsibility rather than a specific runtime or session

Canonical artifacts:
- `jobs/<JOB-ID>/JOB.md`
- `jobs/<JOB-ID>/STATE.md`
- `jobs/<JOB-ID>/MEMORY.md`
- `jobs/<JOB-ID>/HANDOVER.md`

Rules:
- every active durable job should have a portable memory bundle
- job switches, reassignment, and closeout must update job memory
- session memory must never be treated as sufficient replacement for job memory

### 4. Knowledge Memory
Purpose:
- reusable learning, grounded expertise, validated understanding, decisions, runbooks, product knowledge

Canonical artifacts:
- distilled knowledge assets
- decision memos
- approved policy/process/runbook documents
- selected research reports
- evidence artifacts where retrieval value justifies inclusion
- product management and delivery artifacts with reuse value

Rules:
- product outputs that contain durable learning should be designed to become future-retrievable memory assets
- not all documents should be retrieval-indexed; activation class must be explicit

### 5. Coordination Memory
Purpose:
- shared awareness of current activity, intent, blockers, dependencies, and requests across otherwise isolated contexts

Canonical artifacts:
- structured coordination/event state
- generated coordination views or status boards
- situational awareness summaries

Rules:
- coordination memory is not the same as long-term memory
- prefer append-only or structured event/state sources with generated views rather than shared free-form overwrite documents
- keep high-level, current, and non-sensitive by default

## Activation Model
No memory artifact is considered operationally real unless it has an activation path.

Allowed activation classes:
- `bootstrap`: always injected or always read at session start
- `retrieval-indexed`: discoverable via memory/search tooling
- `controller-generated`: projected view generated from canonical state
- `explicit-load`: loaded deterministically for a known workflow (for example, job activation)
- `archive-only`: retained for history but not expected to influence runtime behavior directly

Requirements:
- every important memory-bearing artifact should have an intended activation class
- activation class should be explicit for major process, policy, memory, and knowledge artifacts
- dead documents without an activation path should be reduced, archived, or promoted into a live form

## Write-Back Policy
Write-back is mandatory when durable context would otherwise remain trapped in a transient session or tool trace.

Minimum required write-back triggers:
- after material decisions
- after incidents and non-trivial mistakes
- before or during major session compaction boundaries where durable state could be lost
- after job switches or reassignment
- at job completion or pause
- after substantial research synthesis
- after meaningful product deliveries that produce reusable learning, policy, patterns, or operational constraints

Write-back targets should be chosen by memory type:
- agent lesson -> agent memory
- transient continuity note -> daily memory
- portable responsibility state -> job memory
- reusable insight -> knowledge memory
- active cross-context status -> coordination memory
- decision rationale -> decision artifact

## Promotion Rules
Raw observations should not all become long-term memory.

Promotion guidance:
- keep raw chronology in daily notes, evidence, and logs
- promote durable lessons and stable preferences into curated agent memory only when repeatedly useful or identity-level
- promote execution continuity into job state/handover when another runtime/session might need it
- promote reusable reasoning into decisions, distilled knowledge, runbooks, or product artifacts
- avoid copying the same fact into multiple stores unless each copy has a different operational purpose

## Retrieval Policy
Retrieval should be selective, scoped, and provenance-friendly.

Rules:
- use retrieval for recallable modules, not as a blanket load-everything behavior
- prefer curated/distilled artifacts over raw/noisy sources when both exist
- preserve path/line/source awareness wherever possible
- keep retrieval namespace-local by default; use explicit bridge rules for shared/cross-namespace access
- prioritize low-noise, high-reuse sources first

Target indexing priority:
1. job memory bundles
2. curated memory files
3. distilled knowledge and decision artifacts
4. approved runbooks/processes/policies with runtime relevance
5. selected research corpora where retrieval value is proven

Default caution:
- exclude noisy inboxes, draft dumps, and high-churn scratch spaces from automatic retrieval unless explicitly justified

## Product Delivery Rule
A high-quality delivery should improve both immediate outcomes and future memory quality.

For major deliveries, ask:
- what should be durable after this work is done?
- what should become reusable by another job, session, or agent?
- should this become a decision, runbook, standard, product artifact, job note, or knowledge asset?

## Evaluation and Quality Control
Memory changes must be treated as evaluable engineering changes.

Quality dimensions:
- retrieval relevance
- grounding/faithfulness to sources
- scope isolation / no leakage across boundaries
- staleness and drift resistance
- activation coverage
- write-back reliability
- portability across sessions/jobs/agents
- cost and context-window efficiency

Minimum review questions:
- was the right memory captured?
- was it stored in the right scope?
- is it retrievable when needed?
- is it being activated in real workflows?
- did the change reduce or increase noise?

## Ownership Model
Central ownership:
- Lyra, via the Control Panel product assembly, owns the memory capability as a horizontal operating process

Central owner responsibilities:
- architecture
- policy
- scope definitions
- activation rules
- indexing/retrieval policy
- evaluation
- hygiene/pruning standards
- observability and improvement backlog

Distributed responsibilities:
- jobs, products, sessions, and specialist runtimes produce memory content near the work
- reusable outputs should be promoted into the correct durable memory plane
- contributors should not rely on the center to reconstruct everything from transcripts afterward

## Governance Cadence
- Daily: capture meaningful continuity and triggered write-back items
- Weekly: review high-value promotions, retrieval issues, stale artifacts, and coordination visibility gaps
- Monthly: review scope boundaries, activation coverage, and memory-quality metrics
- Trigger-based: update immediately after major incidents, architecture shifts, product-boundary changes, or job-model changes

## Initial Implementation Priorities
1. Confirm and stabilize live memory retrieval behavior in runtime
2. Make job memory bundles first-class and consistently updated
3. Extend retrieval scope to selected knowledge assets and decision artifacts
4. Define a lightweight coordination-memory substrate and generated view
5. Add memory quality checks and recurring review cadence

## Non-Goals
- Turning memory into one giant always-injected prompt
- Treating session transcripts as the primary durable system of record
- Indexing everything by default
- Replacing task/decision systems with memory files
- Storing sensitive context broadly in shared retrieval spaces

## Version
- v1.0
- Date: 2026-03-10
