# P1 Canonical TDE Substrate — Session Prep

Date: 2026-03-18
Prepared by: Overnight execution loop
Source priority: `control/CT-OVERNIGHT-SYNTHESIS-2026-03-17.md` selected priority 3

## Why this exists
Control Tower explicitly chose **"record improvement canonical substrate as a next-session preparation item"** as the remaining highest-leverage follow-through after the overnight closure of IMP-ERR-20260315 and the Interfaces assembly link fix.

This note does **not** attempt to finish P1 overnight. It creates the smallest useful preparation artifact so the next focused session can define the substrate deliberately instead of restarting discovery.

## Selected priority → current work → evidence chain
- **Selected priority:** Define the canonical improvement execution substrate in TDE terms (`products/improvement/04-execution/TOP_PRIORITIES.md`, Priority 1).
- **Current TDE-selected validation surface:** `OPS-2026-066` through `OPS-2026-069` are already present in canonical TDE Inbox (`os/runtime/TASKS_from_db.md`).
- **Reference proof case already closed:** `IMP-ERR-20260315-ARCHIVED-REPO-MISUSE-01` closure artifact at `products/improvement/04-execution/tde-improvement-imp-err-20260315-archived-repo-misuse-01-close-imp-err-20260315-archived-repo-misuse-01-20260317-003605-532136.md`.
- **Control Tower rationale:** portfolio bottleneck is fragmented improvement execution across non-canonical surfaces (`control/CT-OVERNIGHT-SYNTHESIS-2026-03-17.md`).

## What the next focused session must define
### 1. Queue / task-class rule
Decide whether improvement work should use:
- a dedicated improvement-prefixed task class in canonical TDE, or
- existing task classes plus mandatory improvement metadata.

Minimum outcome required: a single unambiguous routing rule for improvement items so they do not float between memory notes, product docs, and ad hoc task creation.

### 2. Mandatory linkage rules
For every material improvement item, define required links to at least:
- triggering source (`error report`, `review finding`, `nightly report`, `decision follow-up`, etc.)
- owning product
- canonical TDE task ID
- closure evidence artifact

Minimum outcome required: no improvement item can be considered closed without source-link and evidence-link integrity.

### 3. Intake contract
Define the minimum intake fields required when converting a signal into canonical TDE work.

Suggested minimum fields:
- `source_type`
- `source_ref`
- `product`
- `improvement_intent`
- `risk_if_ignored`
- `proposed_validation_path`

### 4. Validation set
Use the already-ingested Jobs Review items as the first stress-test set after the substrate is defined:
- `OPS-2026-066`
- `OPS-2026-067`
- `OPS-2026-068`
- `OPS-2026-069`

These are bounded, live, and already canonical enough to test routing discipline without inventing synthetic cases.

## Explicit non-goals for the next session
- Do not redesign Task Management ownership boundaries.
- Do not start pinned-lane/A-005 distribution work as part of P1.
- Do not broaden into portfolio-wide process rewrite beyond the minimum substrate needed to make improvement execution canonical and repeatable.

## Recommended next-session output
A good next-session completion should publish one concise artifact that states:
1. the canonical routing rule,
2. the required metadata/linkage rule set,
3. the approved intake format,
4. the first validation cases, and
5. the runbook/doc updates required to enforce it.

## Immediate overnight outcome
One concrete overnight step is now complete: the previously implicit P1 preparation item is recorded as an explicit execution artifact with named validation cases and completion criteria.
