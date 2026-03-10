# OPS-2026-070 — Memory Retrieval Baseline Validation

Date: 2026-03-10  
Owner: Lyra / Control Panel  
Status: Baseline established

## Objective
Validate the live memory retrieval/index behavior in the current OpenClaw runtime and determine whether the active problem is process, indexing/configuration, activation discipline, or tool failure.

## Commands run
- `openclaw status --all`
- `openclaw plugins list`
- `openclaw memory status --deep`
- `openclaw memory index --verbose`

## Findings

### 1. Memory plugin is present and loaded
- Active plugin: `memory-core`
- Plugin status: loaded
- This confirms the memory capability is present in the runtime and not disabled at the plugin layer.

### 2. Retrieval/indexing is effectively non-operational in the current runtime
For `main`:
- Provider: `none`
- Indexed: `0/9 files · 0 chunks`
- Store: `~/.openclaw/memory/main.sqlite`
- FTS: ready
- Embeddings: unavailable

For `px-internal-dev`:
- Provider: `none`
- Indexed: `0/4 files · 0 chunks`
- Store: `~/.openclaw/memory/px-internal-dev.sqlite`
- FTS: ready
- Embeddings: unavailable

### 3. Root cause is explicit in CLI output
`openclaw memory status --deep` reports:
- `No API key found for provider "openai".`
- `You are authenticated with OpenAI Codex OAuth. Use openai-codex/gpt-5.4 (OAuth) or set OPENAI_API_KEY to use openai/gpt-5.4.`

`openclaw memory index --verbose` reports:
- `[memory] Skipping memory file sync in FTS-only mode (no embedding provider)`

This means the live issue is not merely poor recall quality. The index is not being populated at all in the current mode.

### 4. Practical consequence
- `memory_search` returns no useful results because there are no indexed chunks.
- Memory files on disk exist and are correct enough to read manually.
- Retrieval-backed memory behavior is currently blocked by runtime/provider configuration rather than by the memory process design itself.

### 5. Secondary observations from runtime diagnostics
- `main` and `px-internal-dev` both show the same pattern: `0 indexed files`.
- Gateway logs confirm earlier missing-file issues from before overnight fixes (`MEMORY.md` and `memory/2026-03-10.md` were absent earlier in the day).
- Separate embedded-run `Codex error` entries exist in gateway logs; these are model/provider server errors and are not the same thing as the memory indexing issue.

## Diagnosis
Current state should be classified as:
- Plugin layer: working
- File layer: present
- Process/governance layer: improving
- Retrieval/index layer: non-functional in practice
- Root cause class: configuration/provider mismatch for memory indexing

## Implication for roadmap
This validates the prioritization in `MEMORY_IMPLEMENTATION_ROADMAP_V1.md`:
1. confirm and stabilize live memory retrieval behavior
2. only then rely on retrieval-indexed activation classes for broader memory architecture work

## Recommended next step
Resolve the memory indexing provider path for the live runtime so that file sync and chunk indexing actually occur. After that:
- re-run `openclaw memory index --verbose`
- re-run `openclaw memory status --deep`
- test `memory_search` on known phrases from `MEMORY.md` and daily memory files
- only then mark retrieval-backed memory as operational

## Conclusion
The current memory problem is not primarily that the architecture is wrong or that the memory files are absent. The immediate blocker is that `memory-core` is loaded but has no usable embedding provider in the active runtime, causing indexing to skip file sync and leaving both agents at `0 indexed files / 0 chunks`.
