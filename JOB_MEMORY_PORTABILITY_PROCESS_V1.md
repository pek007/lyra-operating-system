# JOB_MEMORY_PORTABILITY_PROCESS_V1.md

Status: Active (v1)  
Owner: Peter (A), Lyra (R)

## Purpose
Ensure job memory is portable across agents/sessions and never trapped in transient chat context.

## Rules
1. Session memory is ephemeral; durable job memory must live in files.
2. Every active job has a job memory bundle under `jobs/<JOB-ID>/`.
3. Job reassignment requires a handover update before/at switch.
4. High-signal decisions/constraints must be reflected in job state within same work cycle.

## Required job memory bundle
- `jobs/<JOB-ID>/JOB.md` (mission, decision rights, scope)
- `jobs/<JOB-ID>/STATE.md` (current compact state)
- `jobs/<JOB-ID>/MEMORY.md` (durable lessons/facts)
- `jobs/<JOB-ID>/HANDOVER.md` (portable transfer brief)

## Minimal cadence
- Daily: update STATE for active jobs
- Weekly: prune/curate MEMORY
- On reassignment: mandatory HANDOVER update

## Quality gates
- No active job without bundle files
- No reassignment without handover note
- No major decision without link into STATE/MEMORY
