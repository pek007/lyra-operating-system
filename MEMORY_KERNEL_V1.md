# MEMORY_KERNEL_V1.md

Status: Active draft v1  
Owner: Peter (governance), Lyra (memory operations), Engineering role (implementation)

## Objective
Implement a memory architecture where **context is a managed cache** and **durable knowledge remains auditable markdown**.

## Design principle
- Prompt context (L1) is for current work only.
- Durable memory/knowledge (L3) is the source of truth.
- Indexes (L4) are derivative accelerators, never canonical truth.

---

## 1) Memory tier architecture

### L0 — Execution scratchpad (ephemeral)
- Temporary reasoning/planning state.
- Not persisted as memory.
- No direct user-facing durability guarantees.

### L1 — Working context window (fast, expensive, bounded)
Contains only what is required for current step:
- minimal recent conversation
- active task state / open loops
- selected retrieved snippets (memory + knowledge)
- compacted session summary where needed

Policy:
- strict token budgets per component
- admission based on relevance + recency + importance
- drop low-value blocks before compressing high-value blocks

### L2 — Session store (durable operational trace)
- session JSONL history
- compaction summaries
- tool/run traces

Purpose:
- reproducibility
- incident/debug timeline
- source for later distillation

### L3 — Durable curated memory and knowledge (canonical)
- `memory/YYYY-MM-DD.md` (daily operational memory)
- `MEMORY.md` (curated long-term memory, private/main scope)
- `knowledge/distilled/`
- `knowledge/decisions/`
- approved policy/runbook documents

Properties:
- auditable
- versioned
- human-readable/editable

### L4 — Retrieval/index accelerators (derivative)
- vector and lexical indexes over selected L3/L2 paths
- per-namespace index partitions
- rebuildable from source files

Rule:
- index loss must not equal memory loss

---

## 2) Namespace and isolation policy

## Namespaces
Minimum namespaces:
- `os`
- `px`
- optional `shared`

## Isolation rules
1. Retrieval is namespace-local by default.
2. Cross-namespace retrieval requires explicit bridge policy.
3. Indexes must be partitioned per namespace.
4. Memory writes must include namespace metadata.
5. Session keys/routes must resolve deterministically to a namespace.

## Shared memory rules
- Only explicitly designated artifacts may enter `shared`.
- Shared artifacts must be non-sensitive or redacted.

---

## 3) Context budget policy (L1)

## Budget buckets (example defaults)
- System + policy invariants: 20%
- Active task state/open loops: 25%
- Recent conversation: 25%
- Retrieved memory/knowledge snippets: 25%
- Reserve buffer: 5%

## Admission order
1. Must-have invariants
2. Active task requirements
3. Recent interaction needed for coherence
4. Retrieved supporting context
5. Optional enrichment

## Eviction order
1. Optional enrichment
2. Lowest-confidence retrieval snippets
3. Older recent conversation
4. Redundant task context

Never evict core policy invariants for convenience context.

---

## 4) Compaction write-back protocol

Before compaction (manual or automatic), execute write-back:

1. Extract durable items from current context:
   - key decisions made
   - stable preferences/constraints learned
   - open loops/commitments
   - critical references/sources
2. Persist to L3 targets:
   - daily memory file
   - decision/knowledge files as relevant
3. Validate write success
4. Only then run compaction

## Guardrails
- No compaction if write-back fails
- Redact secrets before persistence
- Keep source links where possible for auditability

---

## 5) Knowledge indexing policy

## Index priority
1. `knowledge/distilled/` (high priority)
2. `knowledge/decisions/` (high priority)
3. `memory/` and `MEMORY.md` (high priority, session rules apply)
4. `knowledge/reports/` (lower priority)
5. `knowledge/inbox/` (excluded from auto-recall by default)

## Rationale
- Distilled/decisions are highest signal and most reusable.
- Reports are higher entropy and should be selective.
- Inbox is noisy/untrusted until processed.

## Retrieval policy
- Start with small top-k
- Increase only when confidence is low or question requires breadth
- Prefer snippet retrieval with citations over full-file injection

---

## 6) Memory quality evaluation

## Evaluation suite
Maintain a “memory-critical prompts” test set covering:
- preference recall
- prior decision recall
- policy/rule recall
- factual grounding against knowledge artifacts
- namespace isolation behavior

## Metrics
- Retrieval precision@k (practical relevance)
- Grounding/faithfulness rate
- Cross-namespace leakage rate (target: zero)
- Token cost per successful answer
- Latency impact of retrieval
- Write-back success rate before compaction

## Regression policy
Any change to retrieval/index/compaction policies must run eval suite before promotion.

---

## 7) Operational cadence

### Weekly
- Review retrieval quality metrics
- Review compaction/write-back outcomes
- Review top missed-memory incidents

### Monthly
- Rebalance context budget if needed
- Review namespace bridge rules
- Prune stale low-value memory/index sources
- Update policy/version changelog

---

## 8) Implementation plan (first 4 weeks)

Week 1:
- Define namespace metadata + routing map
- Finalize L1 budget buckets and eviction order
- Add write-back checklist template

Week 2:
- Partition indexes by namespace
- Implement index priority policy for knowledge paths
- Add retrieval debug logging (query, sources, confidence)

Week 3:
- Implement compaction pre-write-back guard
- Add failure handling and alerting
- Build initial memory-critical evaluation set

Week 4:
- Run baseline evals
- Tune top-k and budgets
- Publish first monthly memory quality report

---

## 9) Done definition (v1)

v1 complete when:
1. Memory tiers and namespace rules are documented and enforced.
2. Compaction cannot run without successful write-back.
3. Knowledge indexing priorities are active and testable.
4. Memory eval suite exists and runs on policy changes.
5. Leakage rate across namespaces is zero in tests.
6. Operators can inspect why a memory snippet was injected.
