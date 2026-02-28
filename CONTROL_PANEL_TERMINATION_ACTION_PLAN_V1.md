# Control Panel Termination — Action Plan v1

Date: 2026-02-28  
Owner: Peter/Lyra  
Status: Active

## Objective
Turn post-mortem findings into enforced process improvements that increase convergence speed, reduce waste, and prioritize decision-value over feature throughput.

## What changes now (non-negotiable)
1. No new project starts without a Start Packet.
2. Every MVP starts as a decision-first artifact (report/job output) before UI expansion.
3. Systems-of-record ownership must be explicit before implementation.
4. Data contract inventory is mandatory for any dashboard/reporting product.
5. External supplier flow uses context-pack + autonomy + verification evidence, with strict WIP limits.

## Process changes

### A) Start Packet Tollgate (required before Sprint 1)
Required sections:
- Product Goal (why)
- Top 3 decisions the product must improve
- Explicit non-goals
- Success metrics
- Kill criteria

Gate policy:
- No backlog item may enter Active for a new project without Start Packet approval.

### B) Decision-First MVP Default
Before building UI-heavy scope, first deliver a recurring artifact that answers the core decision questions with evidence links and freshness metadata.

Examples:
- daily executive status summary
- risk posture summary
- weekly build reliability summary

### C) System Ownership Contract
For each surface, mark:
- System of record owner
- Derived view owner
- Freshness contract
- Deep-link to source of truth

### D) Data Contract Inventory
For each decision question, define:
- required data
- current source
- schema/contract
- freshness target
- owner
- known gaps

### E) Supplier Operating Model
Use one context pack per deliverable:
- goal + decision questions
- constraints and boundaries
- data contracts
- acceptance tests

Execution rules:
- max 1-2 in-flight supplier deliverables
- evidence required before accepting next item
- review outputs/evidence, not micromanaged implementation steps

## What to eliminate (low-value overhead)
- Roleplay-heavy agent/persona design for work that does not require durable runtime boundaries.
- Premature UI elaboration before decision-value proof.
- Large speculative scope batches without acceptance evidence.
- Duplicate ownership surfaces (e.g., overlapping authoritative screens).

## What to preserve (high-value assets)
- Verified audit/idempotency primitives
- Reliable local runtime diagnostics and health checks
- Materialization jobs and freshness-aware artifact pipeline
- Existing reusable UI component primitives where decision-value fit exists

## 14-day execution plan

### Days 1-3
- Create and adopt Start Packet template
- Add gate in intake process
- Classify Control Panel as terminated project with salvage inventory

### Days 4-7
- Create data contract inventory template
- Create systems-of-record vs derived-view contract template
- Add WIP cap policy for external supplier deliverables

### Days 8-10
- Publish supplier context-pack standard
- Add acceptance evidence checklist (tests/screenshots/sample outputs)
- Apply to next active implementation item

### Days 11-14
- Run first weekly compliance review against new gates
- Measure violations and process friction
- Tune templates to reduce overhead while preserving control

## Success metrics (30-day)
- 100% of new initiatives have approved Start Packet
- 100% of dashboard/report work has explicit data contract inventory
- <=2 concurrent external supplier deliverables
- 100% accepted supplier deliverables include evidence pack
- Reduction in rework caused by scope/ownership ambiguity

## Version
- v1.0
- Date: 2026-02-28
