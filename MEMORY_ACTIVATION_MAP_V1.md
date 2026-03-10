# MEMORY_ACTIVATION_MAP_V1.md

Status: Initial working map  
Owner: Lyra via Control Panel  
Date: 2026-03-10

## Purpose
Provide the first explicit activation-class map for major memory-bearing artifacts in Lyra OS.

## Activation classes
- `bootstrap` — always injected or always read at startup/session entry
- `retrieval-indexed` — discoverable through search/retrieval tooling
- `controller-generated` — generated view from canonical source state
- `explicit-load` — loaded deliberately for a known workflow
- `archive-only` — retained for history/reference, not expected to shape runtime directly

## Activation map (initial)

| Artifact / Class | Memory scope | Canonical role | Activation class | Notes |
|---|---|---|---|---|
| `AGENTS.md` | agent | runtime operating instructions | bootstrap | core runtime kernel |
| `SOUL.md` | agent | identity/behavior posture | bootstrap | core runtime kernel |
| `USER.md` | agent | human-specific collaboration preferences | bootstrap | core runtime kernel |
| `TOOLS.md` | agent | local operational notes | bootstrap | keep lean |
| `IDENTITY.md` | agent | compact identity reference | bootstrap | keep lean |
| `HEARTBEAT.md` | coordination / agent | periodic check directives | bootstrap | conditional utility |
| `MEMORY.md` | agent | curated long-term main/private memory | bootstrap | main/private scope only |
| `memory/YYYY-MM-DD.md` | session | daily continuity notes | retrieval-indexed | not always-injected; retrieve/selective use |
| session JSONL transcripts | session | detailed operational trace | archive-only | canonical trace, not prompt-default |
| session compaction summaries | session | compressed carry-forward trace | explicit-load | used when session continuity requires it |
| `jobs/<JOB-ID>/JOB.md` | job | durable job contract | explicit-load | should load on job start/activation |
| `jobs/<JOB-ID>/STATE.md` | job | current compact job state | explicit-load | mandatory primary job activation artifact |
| `jobs/<JOB-ID>/MEMORY.md` | job | durable job-specific lessons/facts | retrieval-indexed | candidate for selective job recall |
| `jobs/<JOB-ID>/HANDOVER.md` | job | portable handover summary | explicit-load | required on reassignment/handover |
| `knowledge/distilled/` | knowledge | high-signal reusable learning | retrieval-indexed | priority knowledge corpus |
| `knowledge/decisions/` | knowledge | durable decision rationale | retrieval-indexed | priority knowledge corpus |
| approved runbooks/processes/policies | knowledge | operational rules and methods | retrieval-indexed | only where runtime relevance justifies it |
| `knowledge/reports/` | knowledge | raw/long-form research library | archive-only | candidate selective retrieval later, not blanket activation |
| `knowledge/inbox/` | knowledge | unprocessed inputs | archive-only | excluded from default retrieval |
| evidence logs / raw snapshots | knowledge / trace | proof and audit substrate | archive-only | retrieve only where justified |
| `SITUATIONAL_AWARENESS.md` | coordination | current-state synthesized awareness | controller-generated | should remain high-signal and compact |
| generated coordination board/view (future) | coordination | cross-context current activity view | controller-generated | should be derived, not primary source |
| structured coordination event log (future) | coordination | canonical shared awareness substrate | explicit-load / retrieval-indexed | source should be structured and append-oriented |

## Priority gaps identified
1. Job bundle activation exists conceptually but is not yet clearly operationalized for all active jobs.
2. Daily memory files exist, but retrieval behavior currently appears unreliable in practice.
3. Knowledge assets are rich, but most are not yet clearly activated for runtime use.
4. Coordination memory lacks a canonical structured substrate.
5. Some active files remain present on disk without a confirmed live activation path.

## Initial decisions implied by this map
- Keep bootstrap/kernel files small and high-leverage.
- Treat daily memory as retrievable session memory, not auto-injected bulk context.
- Make `jobs/<JOB-ID>/STATE.md` the key explicit-load artifact for job activation.
- Prioritize `knowledge/distilled/` and `knowledge/decisions/` before broad report indexing.
- Prefer generated coordination views over free-form shared mutable docs.

## Immediate follow-up
- Validate the retrieval-indexed paths that are expected to be live today.
- Confirm whether activation classes need to be recorded more systematically in a registry.
- Use this map as the baseline for `OPS-2026-070` implementation work.

## Version
- v1.0
- Date: 2026-03-10
