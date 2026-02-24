# TRELLO_CONNECTOR_V1.md

## Goal
Move to API-first task management (no browser relay dependency) using Trello REST API.

## Scope (v1)
- Read `TASKS.md`
- Ensure target Trello lists exist
- Upsert cards by task ID (e.g., `OPS-2026-001`)
- Move cards to matching list state (`Inbox`, `Triage`, `Active`, `Waiting`, `Done`, `Archived`)
- Optional: ensure core labels exist

## Required Credentials
Set these environment variables:

```bash
export TRELLO_KEY="<trello_api_key>"
export TRELLO_TOKEN="<trello_api_token>"
export TRELLO_BOARD_ID="<board_id>"
```

How to get them:
1. API key: Trello developer key page
2. Token: generate token for your key (read/write)
3. Board ID: open board URL and query through API/list call, or copy from board JSON endpoint

## Script
- Path: `tools/trello_sync.py`
- Default mode: dry-run (safe)
- Apply changes with: `--apply`

## Usage

### 1) Preview changes (dry-run)
```bash
python3 tools/trello_sync.py --from TASKS.md
```

### 2) Apply changes to Trello
```bash
python3 tools/trello_sync.py --from TASKS.md --apply
```

### 3) Ensure labels
```bash
python3 tools/trello_sync.py --from TASKS.md --ensure-labels --apply
```

## Mapping Rules
- Markdown headings in `TASKS.md` map to Trello list names.
- Each checkbox line is a card.
- If card title starts with ID prefix like `OPS-2026-001`, that ID is used as stable key.
- Without an ID, full card title is used as key.

## v1 Limitations
- Does not sync due dates/checklists yet.
- Does not delete/archive cards automatically.
- Minimal conflict handling (latest local state wins).

## Next Extensions (v2)
- Bi-directional sync (Trello -> TASKS)
- Due dates and owner mapping
- Label auto-mapping from priority/type keywords
- Incident/security task auto-creation from runbooks/checklists

## Version
- v1.0
- Date: 2026-02-24
