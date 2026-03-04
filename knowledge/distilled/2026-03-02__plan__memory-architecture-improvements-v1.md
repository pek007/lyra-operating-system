# Memory Architecture Improvements Plan v1

Status: Active  
Owner: Peter (A), Lyra (R)

## Implemented now
1. Research report ingested and indexed.
2. Job memory portability process established.
3. Job memory bundle template created (`jobs/JOB-TEMPLATE/*`).

## Next practical steps
1. Add first real job bundle for active job(s) and start daily STATE updates.
2. Configure memory retrieval scope to include approved `jobs/` path(s).
3. Add deterministic write-back rule at job reassignment and session reset.
4. Add weekly memory quality review (signal/noise, stale facts, missing handovers).

## Success criteria
- Every active job has a memory bundle.
- Reassignment can occur without context loss.
- High-signal decisions appear in job STATE/MEMORY within one cycle.
