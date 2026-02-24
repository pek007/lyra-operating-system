# TASK_LINKING_STANDARD.md

## Purpose
Standardize how tasks in Trello link to OS documentation and evidence artifacts.

## ID Format
- Pattern: `OPS-YYYY-NNN`
- Example: `OPS-2026-014`
- `OPS` = Operating System lane item
- `YYYY` = year created
- `NNN` = zero-padded sequence

## Card Title Standard
`OPS-YYYY-NNN | <short action title>`

## Mandatory Card Fields
- Objective
- Priority (P1/P2/P3/P4)
- Door type (Type 1 / Type 2)
- Owner
- Linked doc(s)
- Next action

## Linking Rules
1. Every Trello task card must reference at least one canonical doc path when relevant.
2. Governance/process tasks link to `.md` docs in workspace.
3. Evidence tasks must link to log files (e.g., `RESTORE_TEST_LOG.md`, `INCIDENT_LOG.md`).
4. If a task updates a doc, include the task ID inside that doc change note where practical.

## Doc Backlink Convention
When a doc update is driven by a task, include a line:
- `Task: OPS-YYYY-NNN`

## State Mapping
- Trello `Inbox` <-> `TASKS.md` Inbox
- Trello `Triage` <-> `TASKS.md` Triage
- Trello `Active` <-> `TASKS.md` Active
- Trello `Waiting` <-> `TASKS.md` Waiting
- Trello `Done` <-> `TASKS.md` Done
- Trello `Archived` = historical/closed (usually not in TASKS.md active view)

## Version
- v1.0
- Date: 2026-02-24
