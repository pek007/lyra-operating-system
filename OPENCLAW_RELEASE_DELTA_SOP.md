# SOP: OpenClaw Release Delta Tracking

## Purpose
Ensure new OpenClaw versions are consistently translated into actionable improvements in our operating system and workflows.

## Trigger
- Daily, as part of `continuous-improvement:sweep`
- Manual trigger after any explicit upgrade

## Procedure
1. Capture installed/runtime version and health:
   - `openclaw --version` (or `openclaw status` version field)
   - `openclaw status`
2. Check update/release delta signal:
   - `openclaw update status`
3. If a new version is detected since last recorded check:
   - Create/update a release delta note under `knowledge/evidence/YYYY-MM/`
   - Identify high-value capability deltas (new tools, policy changes, behavior changes, deprecations)
   - Classify impact: `none | low | medium | high`
4. Generate actions:
   - Low-risk configuration/doc updates may be auto-applied.
   - Non-trivial changes must be added to canonical TDE work intake as `IMP-AUTO-YYYYMMDD-XX` (projection: `os/runtime/TASKS_from_db.md`).
5. Close loop:
   - If actions were created, include owner, expected impact, and validation signal.

## Output Format (for sweep reports)
- OpenClaw version observed
- New release detected? (yes/no)
- High-signal deltas
- Applied now
- Backlog proposals
- Risks/assumptions

## Guardrails
- Never auto-change external messaging behavior, security boundaries, or destructive configs without explicit approval.
- Prefer docs/process updates first; runtime config changes require clear rollback path.

## Version
- v1.0
- Date: 2026-02-27
- Owner: Peter/Lyra
