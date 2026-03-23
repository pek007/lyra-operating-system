# CONTINUOUS_IMPROVEMENT_PROCESS_V1.md

Status: Active (v1.1)
Owner: Lyra (R), Peter (A)

## Flow
Observe friction -> Capture improvement item -> Prioritize -> Pilot small change -> Measure impact -> Keep/adjust/revert

## Discovery Layers
- Layer A (daily, internal): hygiene/drift/friction capture from docs, tools, tasks, and evidence.
- Layer B (weekly, internal): pattern detection and root-cause synthesis from recurring signals.
- Layer C (weekly, external analysis): larger non-obvious leverage opportunities, generated via Deep Research using a CI handoff prompt packet prepared by Lyra and executed by Peter.

## Rules
- Small reversible changes by default
- One-way-door changes require explicit decision packet
- Every improvement has owner + success signal + review date
- Material incidents, repeated errors, and meaningful near-misses must follow the A-005 incident-to-improvement loop: written record -> preventive action -> execution routing -> verification
- Process misses are first-class improvement triggers. A process miss includes: no process consulted before non-trivial work, wrong process selected, discovery failure, ownership ambiguity, routing ambiguity, or a required process artifact being missing/stale/hard to find.
- Every material process miss should be classified as one or more of: `discovery_failure`, `ownership_failure`, `routing_failure`, `missing_process`, or `enforcement_failure`.
- Closure for a material process miss requires updating the relevant layer (for example discovery index, routing artifact, owning process, ownership rule, or execution rule) and verifying that the same miss is less likely next time.
- Cron-discovered non-trivial items go to `TASKS.md` Inbox with ID format `IMP-AUTO-YYYYMMDD-XX` and one-line impact statement
- Keep continuous-improvement edits low-risk by default (no automatic changes to security boundaries, credentials, external integrations, or runtime permissions)
- Weekly Layer C must produce a Deep Research prompt packet with:
  - current system context (recent decisions/releases)
  - top recurring friction patterns (from Layer B)
  - explicit request for non-obvious, high-leverage interventions
  - required output format: opportunity thesis, mechanism, expected impact, pilot design, risk/assumption, evidence signals
- Deep Research output is converted into executable backlog items (`IMP-DR-YYYYMMDD-XX`) or explicit reject-with-rationale notes.

## Process-miss handling
When a material process miss is detected:
1. record the miss in the appropriate error/improvement artifact
2. classify the miss type
3. route corrective work into canonical execution state
4. update the specific discovery/routing/process/control layer that failed
5. verify that retrieval or execution behavior improved

Preferred fix layers:
- `PROCESS_DISCOVERY_INDEX.md` or a workspace-local discovery index when the miss is findability-related
- `PROJECT_PROCESS_ROUTING_V1.md` when the miss is bundle-selection or project-type ambiguity
- the owning product or platform process artifact when the miss is substantive process content
- ownership/coordination artifacts when the miss is boundary ambiguity

## Cadence
- Daily: Layer A hygiene + low-risk implementation sweep
- Weekly: Layer B pattern synthesis + Layer C Deep Research handoff and conversion to execution backlog
- Weekly: improvement portfolio cleanup (replaces monthly cadence due to rapid operating tempo)
