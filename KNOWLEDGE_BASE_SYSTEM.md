# KNOWLEDGE_BASE_SYSTEM.md

## Purpose
Systematic storage and reuse of high-value inputs (e.g., Deep Research reports, daily briefs, generated analyses).

## Folder Structure
- `knowledge/inbox/` — raw incoming docs/reports (as received)
- `knowledge/reports/` — normalized markdown extracts by date/topic
- `knowledge/distilled/` — condensed reusable insights and playbooks
- `knowledge/decisions/` — decision memos and rationale snapshots
- `knowledge/indexes/` — searchable index files and topic maps

## Naming Standard
`YYYY-MM-DD__source__topic__vN.md`

Examples:
- `2026-02-24__deepresearch__multi-agent-design__v1.md`
- `2026-02-24__dailybrief__openclaw-best-practices__v1.md`

## Workflow
1. Store raw source in `knowledge/inbox/`.
2. Create normalized markdown summary in `knowledge/reports/`.
3. Extract reusable insights into `knowledge/distilled/`.
4. If decision-impacting, add memo to `knowledge/decisions/` and link in `DECISIONS.md`.
5. Update topic index in `knowledge/indexes/TOPIC_INDEX.md`.

## Reuse Rule
Before starting major work, check `knowledge/distilled/` and `knowledge/decisions/` for prior reasoning.

## Version
- v1.0
- Date: 2026-02-24
