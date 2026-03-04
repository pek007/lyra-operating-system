# Process-as-Code Implementation Plan v1

Status: Active  
Owner: Peter (A), Lyra (R)

## Executive intent
Convert process governance from mostly document conventions into machine-checkable, low-friction controls.

## Implemented immediately
1. Canonical process metadata schema file created:
   - `processes/standards/PROCESS_METADATA_SCHEMA_V1.yaml`
2. New deep research report ingested into knowledge library and indexed.

## Next implementation steps (high leverage)
1. Add `tools/validate_process_metadata.py` to verify required metadata fields for process docs.
2. Add CI/cron check for:
   - missing owner/review dates
   - overdue nextReview
   - missing links in process registry
3. Normalize evidence frontmatter format to one convention (YAML).
4. Add process lifecycle status transitions to enforcement checks (draft->review->approved->published...)
5. Publish weekly process compliance summary artifact.

## Guardrails
- Keep runtime bootstrap docs at root unchanged.
- No hard file moves for core docs without compatibility stubs.
- Prefer incremental enforcement over big-bang cleanup.

## Success criteria
- >=90% active process docs metadata-complete
- 0 process docs without owner
- 0 unknown statuses in process registry
- Weekly compliance summary generated automatically
