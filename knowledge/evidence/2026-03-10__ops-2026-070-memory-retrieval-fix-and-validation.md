# OPS-2026-070 — Memory Retrieval Fix and Validation

Date: 2026-03-10  
Owner: Lyra / Control Panel  
Status: Fix applied and baseline retrieval validated

## Context
Baseline validation established that `memory-core` was loaded but memory indexing was non-operational because no embedding provider was configured. The result was `0 indexed files / 0 chunks` and `memory_search` returned no useful recall.

Baseline evidence:
- `knowledge/evidence/2026-03-10__ops-2026-070-memory-retrieval-baseline-validation.md`

## Change applied
Updated live OpenClaw config to set:
- `agents.defaults.memorySearch.enabled = true`
- `agents.defaults.memorySearch.sources = ["memory"]`
- `agents.defaults.memorySearch.provider = "local"`
- `agents.defaults.memorySearch.fallback = "none"`

This triggered a normal OpenClaw config reload/restart via the gateway config patch path.

## Validation steps
1. Confirmed gateway health after config reload.
2. Confirmed local embedding model download/init path.
3. Re-ran `openclaw memory status --deep`.
4. Re-ran `openclaw memory index --verbose`.
5. Re-tested `memory_search` against known phrases from `MEMORY.md` and daily memory files.

## Results

### 1. Memory provider status
After the fix:
- Provider: `local`
- Embeddings: `ready`
- Vector: `ready`
- FTS: `ready`

### 2. Indexing behavior
`openclaw memory index --verbose` now shows:
- `[memory] sync: indexing memory files`
- repeated embedding batch activity
- successful completion for both `main` and `px-internal-dev`

This confirms memory file sync is no longer skipped.

### 3. Retrieval behavior
`memory_search` now returns useful results.

Validated examples:
- Query: Peter preference / writing block / high-signal outputs
  - returned `MEMORY.md`
- Query: update lesson / runtime path / install mode before OpenClaw updates
  - returned `memory/2026-03-09.md`
  - also returned `MEMORY.md`

### 4. Runtime interpretation
Memory retrieval has moved from:
- non-operational in practice

to:
- operational baseline using local embeddings on-host

## Remaining limitations
- Retrieval quality/ranking is still baseline-level, not yet tuned.
- Current retrieval corpus is still narrow (`memory` source only).
- Additional paths (for example job bundles, distilled knowledge, decisions) should be added only in a controlled next phase.

## Decision / implication
The immediate blocker for memory retrieval on this host is resolved. This unblocks the next layer of memory work:
- controlled expansion of retrieval scope
- activation-class execution
- job-memory portability improvements
- memory-quality tuning/evaluation

## Recommended next step
Use the now-working retrieval baseline to extend memory carefully via `agents.defaults.memorySearch.extraPaths`, prioritizing:
1. job memory bundles
2. `knowledge/distilled/`
3. `knowledge/decisions/`

Do this incrementally with validation after each scope expansion.

## Conclusion
The memory retrieval issue was caused by a missing embedding provider path. Switching memory search to the local provider resolved the blocker on this host. Memory indexing and retrieval are now functioning at a baseline operational level.
