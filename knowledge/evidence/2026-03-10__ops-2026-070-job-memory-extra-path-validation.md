# OPS-2026-070 — Job Memory Extra-Path Validation

Date: 2026-03-10  
Owner: Lyra / Control Panel  
Status: Controlled scope expansion validated

## Objective
Execute the first controlled retrieval-scope expansion by adding job memory bundles to `memorySearch.extraPaths`, then verify indexing and recall before touching broader knowledge sources.

## Change applied
Updated live OpenClaw config to add:
- `agents.defaults.memorySearch.extraPaths = ["jobs"]`

This triggered the normal config reload path.

## Validation steps
1. Inspected current `jobs/` tree in workspace.
2. Confirmed current config hash.
3. Applied the `extraPaths` patch for `jobs` only.
4. Re-ran `openclaw memory index --verbose`.
5. Tested `memory_search` against known job-memory phrases.

## Current workspace reality
The current workspace `jobs/` tree contains only the template bundle:
- `jobs/JOB-TEMPLATE/JOB.md`
- `jobs/JOB-TEMPLATE/STATE.md`
- `jobs/JOB-TEMPLATE/MEMORY.md`
- `jobs/JOB-TEMPLATE/HANDOVER.md`

This means the validation proves the retrieval path is working for job-memory artifacts, but it does **not** yet prove recall over populated live job bundles.

## Results

### 1. Indexing behavior
`openclaw memory index --verbose` now reports:
- `Extra paths: ~/.openclaw/workspace/jobs`
- successful sync/index completion for `main`

This confirms the `jobs` path is being included in the memory index.

### 2. Retrieval behavior
`memory_search` now returns job-bundle artifacts from `jobs/JOB-TEMPLATE/`.

Validated examples:
- Query around handover/update language returned:
  - `jobs/JOB-TEMPLATE/HANDOVER.md`
  - `jobs/JOB-TEMPLATE/JOB.md`
- Query around active job bundle structure returned:
  - `jobs/JOB-TEMPLATE/JOB.md`
  - `jobs/JOB-TEMPLATE/MEMORY.md`

### 3. Interpretation
The technical retrieval pathway for job memory is now working.

What is validated:
- `jobs/` can be added safely via `memorySearch.extraPaths`
- indexing completes successfully
- job-memory markdown becomes retrievable through `memory_search`

What is not yet validated:
- recall quality on active populated job bundles
- interaction between multiple live job bundles and ranking/noise
- handover/state retrieval usefulness in real task execution

## Decision / implication
This controlled expansion is a success and supports the roadmap recommendation to expand retrieval scope incrementally.

The next best step inside the job-memory lane is not broader config work. It is to create/populate real active job bundles so retrieval can be tested against meaningful live state rather than templates.

## Recommended next step
1. Stand up at least one real active job bundle under `jobs/<JOB-ID>/`
2. Populate `STATE.md`, `MEMORY.md`, and `HANDOVER.md` with real content
3. Re-index and test task-relevant recall against that live job bundle
4. Only then consider the next retrieval expansion (`knowledge/distilled/`)

## Conclusion
The first `extraPaths` rollout succeeded technically. Job-memory artifacts under `jobs/` are now indexed and retrievable. However, the current workspace only contains the job template bundle, so the result should be treated as infrastructure validation rather than full operational proof of job-memory recall.
