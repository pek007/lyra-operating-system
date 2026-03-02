---
title: "Memory Architecture for Lyra on OpenClaw"
date: 2026-03-02
source: deepresearch
ingest_from: "telegram attachment file_99"
tags: [external-analysis, deepresearch, memory, openclaw]
decision_relevance: "memory portability and deterministic write-back"
confidence: tbd
status: archived-source
---

# Memory Architecture for Lyra on OpenClaw

## The core problem and the relevant OpenClaw primitives

In OpenClaw, “memory” is not the same thing as “context.” Context is what is inside the model’s current context window for a given run; memory is durable state stored on disk that the agent can reload or retrieve later. OpenClaw’s own docs are explicit that memory is plain Markdown in the agent workspace and that the model only “remembers” what gets written to disk. citeturn3view0

OpenClaw’s default memory layout is intentionally minimal and tiered: an append-only daily log (`memory/YYYY-MM-DD.md`) and an optional curated long‑term file (`MEMORY.md`). The docs specify that the daily log is “today + yesterday” at session start, while `MEMORY.md` is curated, long-term, and “only load[ed] in the main, private session (never in group contexts).” citeturn3view0 This matters for your multi-channel / Telegram approach: OpenClaw already treats different session contexts (main/private vs group contexts) as different trust surfaces and encourages different memory exposure across them. citeturn3view0turn11view0

On top of the Markdown files, OpenClaw can build a semantic + lexical retrieval index and expose it via tools. The default memory plugin (`memory-core`, selected via `plugins.slots.memory`) provides `memory_search` and `memory_get`, and stores the index per agent in SQLite at `~/.openclaw/memory/<agentId>.sqlite` (configurable). citeturn15search0turn9view3 Memory search is hybrid by design: OpenClaw can combine vector similarity with BM25 keyword relevance (via SQLite FTS5) and merge candidates with configurable weighting. citeturn9view1turn9view3 When available, OpenClaw can accelerate vector search inside SQLite using the `sqlite-vec` extension (storing embeddings in a virtual table and executing vector distance queries in the database). citeturn9view0

Separately, OpenClaw has built-in mechanisms to keep context windows bounded over long sessions: compaction summarizes older conversation into a compact entry that persists in the session’s JSONL history, while keeping recent messages intact. citeturn10view0 Critically for “don’t lose important things,” OpenClaw supports a “pre-compaction memory flush” concept: a silent turn can be triggered as a session nears auto-compaction, reminding the model to store durable notes to disk. citeturn3view0turn11view0turn10view0

Finally, OpenClaw’s scaling primitives matter for your “multi-agent + jobs” evolution:

* “One agent” in OpenClaw is a fully isolated runtime with its own workspace (files), state directory (`agentDir`), and session store under `~/.openclaw/agents/<agentId>/sessions`. Credentials and auth profiles are per-agent and not automatically shared. citeturn8view1  
* Session keys are deterministic and encode isolation boundaries (DMs collapse to a main key by default; groups/channels are isolated; Telegram forum topics can be isolated via a topic ID embedded in session keys). citeturn5search1turn11view0  
* Session transcripts live on disk as JSONL per agent, and OpenClaw treats gateway-local files as the source of truth for session state. citeturn11view0  

Those primitives—workspace files as canonical memory, an optional per-agent SQLite retrieval layer, deterministic session isolation, compaction + pre-compaction memory flush—already cover a large portion of what you’re trying to engineer. The uncompromising part that remains is: **how to scope memory across agents and jobs, and how to force reliable “write-back” from ephemeral sessions into portable durable state**.

## How Lyra’s memory is currently working

The Lyra repository is already anchored on a “files are the system-of-record” philosophy.

The clearest operational contract is in `AGENTS.md`, which instructs the agent to begin every session by reading identity/persona constraints plus recent daily memory files, and to read curated long‑term memory only in the main session. It also encodes explicit “no mental notes” policy: if something must persist, it must be written to a file (daily memory, curated memory, or a relevant policy/skill doc). fileciteturn4file2L1-L1

You also already have an explicit *job* abstraction in `JOB_MARKET_MODEL_V1.md`. It defines jobs as portable responsibilities “not bound 1:1 to agents,” with assignment rules (use sessions and sub-agents first, promote to persistent agents for durable boundary differences), and it makes “memory scope” a first-class part of a job’s execution profile (alongside tools, trust boundary, latency/cost targets, escalation triggers, etc.). fileciteturn4file12L1-L1 This is the right abstraction for what you’re now facing: once “jobs” exist as objects, memory needs to be attachable to jobs, not just to a single agent identity.

Concretely, the repo already contains daily memory logs under `memory/` (e.g., `memory/2026-02-23.md`) storing brief bullet-point continuity (what changed, what was captured, key decisions). fileciteturn4file1L1-L1 This indicates the current durable memory write-path is primarily **manual + file-based summarization** (append to daily log; optionally distill into long-term memory when appropriate). fileciteturn4file2L1-L1

The repo also includes a formal “memory kernel” design doc (`MEMORY_KERNEL_V1.md`). While I can’t observe your running gateway configuration directly from the repo alone, the existence and prominence of that document suggests you already treat memory as a multi-tier system (ephemeral working state vs durable state vs index accelerators), rather than “one big chat transcript.” fileciteturn4file0L1-L1

Two additional repo documents reinforce the same architectural intent:

* `knowledge/indexes/structure-scope-rules.md` explicitly “freezes” a small set of bootstrapped runtime docs at root (including `AGENTS.md`, `SOUL.md`, `USER.md`, `MEMORY.md`, `TASKS.md`, etc.) while marking other areas safe to reorganize. In practice, this is managing “what is kernel (always injected/consulted)” vs “what is modular.” fileciteturn13file2L1-L1  
* `docs/architecture/openclaw-agent-deployment-report-2026-02-28.md` frames OpenClaw agents as “persistent execution profiles” (durable isolation and control boundaries) rather than anthropomorphic teammates, and recommends heavy use of sessions/sub-agents with a small number of persistent agents. This aligns strongly with your stated preference for pragmatic scaling and delaying agent proliferation until boundaries are truly durable. fileciteturn13file5L1-L1  

From your description (Telegram multi-channel sessions to keep context focused; one agent today; plans to scale to multiple agents; jobs that can move between agents), the likely critical gaps in the *current* Lyra memory behavior are:

* There is strong **write discipline** (store durable things in files), but limited **automated extraction** (end-of-session distill, job handover summaries, structured memory objects). fileciteturn4file2L1-L1  
* There is session isolation via Telegram channels, but the system does not yet appear to enforce a canonical mapping of “job ↔ session(s) ↔ durable job memory artifact,” so job migration cannot be made reliable without operator effort. citeturn5search1turn11view0  
* You may or may not be using OpenClaw’s per-agent SQLite memory index in practice. The key point: if `memory_search` is enabled + configured, you *are* using SQLite for the index (per OpenClaw docs); if not, you are relying on human-readable Markdown without the retrieval accelerator. citeturn9view3turn20view0  

Because you explicitly want a “quick wins → tailored longer-term solution” trajectory, the immediate engineering target should be less about inventing a new storage system and more about implementing **portable job-bound memory** and **deterministic write-back hooks** using OpenClaw’s existing seams.

## Best practices from OpenClaw and from the research literature

OpenClaw’s own best practices are unusually aligned with what agent-memory research has converged on: maintain durable external traces, keep the prompt window small, retrieve selectively, and write down durable state before context compression.

A few OpenClaw-specific mechanisms are “best practice” not because they are fashionable, but because they are designed to close known failure modes:

OpenClaw treats Markdown files as canonical memory and uses retrieval as an accelerator, not as the source of truth. The docs emphasize that memory files are the source of truth and that memory search tools are provided by the active memory plugin (default `memory-core`). citeturn3view0turn15search0 This architecture matches a core safety/operability principle: when retrieval breaks, you can still debug by reading files.

OpenClaw’s memory tool design is deliberately bounded and provenance-friendly: `memory_search` returns snippets (not full files), with file path and line ranges, and `memory_get` reads a file by path with optional starting line and number of lines. Additional paths are opt-in via `memorySearch.extraPaths`, which is a key scoping lever for your “job memory travels” requirement. citeturn9view3

OpenClaw explicitly separates compaction (persistent summarization into the transcript) from pruning (in-memory, per-request trimming of large tool results), and—most importantly—supports a pre-compaction “memory flush” turn so that durable memory is written to disk before compaction overwrites older context. citeturn10view0turn3view0turn11view0 This is a direct mechanism for your “extract key points and save to long-term memory” aspiration.

OpenClaw also ships a hooks system and includes a bundled `session-memory` hook that writes a dated memory snapshot when `/new` is issued. It locates the transcript, extracts the last 15 lines, generates a filename slug, and writes a dated Markdown file. citeturn17view1 Even if you don’t use this hook as-is, it demonstrates the intended extension pattern: **event-driven automation that turns session state into durable artifacts**.

Research most relevant to your “multi-agent + jobs + moving memory” problem reinforces the same architectural shape, but adds deeper guidance on policies.

MemGPT formalizes an “OS-inspired” approach: treat the context window as scarce fast memory, and implement “virtual context management” with multiple memory tiers plus explicit data movement policies. citeturn22view1 The key actionable takeaway is not the branding; it is the discipline: design memory as a managed hierarchy with explicit page-in/page-out behavior instead of letting context grow until it is forcibly truncated or compacted.

Generative Agents (Park et al.) describes an agent architecture that records experiences into a memory stream, synthesizes higher-level reflections over time, and retrieves memories dynamically to plan behavior (“reflection” as explicit write-back). citeturn22view0 In your language: daily logs are memory stream; `MEMORY.md` (curated durable beliefs) is reflection; job handover briefs are “plan state.”

Recursive summarization approaches show that long-horizon dialogue consistency can be improved by continuously updating a compact “memory” summary over multiple sessions, rather than doing one-off summarization at arbitrary reset boundaries. citeturn22view3 This supports a pragmatic Lyra design choice: do not treat “summarize at end” as enough; treat memory as an always-updating compact state object that is regularly recomputed from recent increments.

LoCoMo (Maharana et al.) develops a benchmark for very long-term conversational memory, showing that even with long context windows and retrieval-augmented generation (RAG), models still struggle with long-range temporal and causal dynamics, and performance can substantially lag human performance. citeturn14search3 The practical point for Lyra is that you should expect memory failures (missed recall, wrong recall, false confidence) and therefore need both **observability** and **evaluation** for memory changes.

On evaluation, RAGAS is explicitly designed as a reference-free evaluation framework for retrieval-augmented generation pipelines, covering dimensions like the retriever’s ability to provide relevant context and the generator’s faithfulness to that context. citeturn24view0 ARES similarly frames automated RAG evaluation, reducing reliance on hand annotations by synthesizing training data for evaluators. citeturn24view1 For an expert system like yours, the best practice is to treat “memory improvements” as testable changes, not folklore.

Finally, classic IR techniques matter because your memory retrieval will increasingly look like search, not like “the model remembers.” OpenClaw already implements hybrid retrieval (BM25 + vector) and candidate merging in the memory stack. citeturn9view1turn9view3 If you extend memory to job-specific and org-wide knowledge stores, you should expect to need rank fusion and redundancy reduction. Reciprocal Rank Fusion (RRF) is an established approach for fusing rankings from multiple retrieval systems. citeturn25search2 For redundancy control and coverage, Maximal Marginal Relevance (MMR) is a well-known criterion for balancing relevance with novelty/diversity when selecting items to include. citeturn25search3

## A scoping model that solves multi-agent memory and job portability

To make “memory travels with jobs” reliable, you need a scoping model that is stricter than “some channels are for some things.” The minimal workable abstraction is this four-scope partition:

Global scope: things that must be consistent across *all* agents and *all* jobs. This includes system direction, guardrails, shared architecture constraints, shared definitions of done, and operating principles. In your repo this already lives naturally in governance/control-plane files and the “frozen” kernel documents. fileciteturn4file2L1-L1turn13file2L1-L1

Agent scope: private, durable state tied to a specific agent identity/execution profile (persona, skill preferences, agent-local tool notes, guardrail interpretations that differ by trust boundary). OpenClaw enforces this naturally: each agent has its own workspace and state directory and does not share credentials by default. citeturn8view1

Job scope: portable durable state tied to a job ID and its execution profile, designed explicitly to move between agents. In your own job model, “memory scope” is a first-class field in the job execution profile. fileciteturn4file12L1-L1 This should become the canonical place for “the memory that must go with the job.”

Session scope: ephemeral working context (conversation history, transient tool outputs, scratch planning) that should not be treated as authoritative and should be compacted/pruned aggressively. OpenClaw already persists session transcripts separately and provides compaction and pruning tools. citeturn10view0turn11view0

Once those scopes exist, the core design rule is:

**Never rely on session scope to carry job scope.**  
Job scope should be a portable artifact that can be loaded by any agent assigned to the job.

In practice, in an OpenClaw + Markdown workspace world, the most pragmatic implementation is:

*Represent each job as a directory with canonical durable artifacts,* and ensure assigned agents can retrieve those artifacts efficiently.

A concrete (but still minimal) job bundle could be:

* `jobs/<jobId>/JOB.md` — mission, outcomes, decision rights, execution profile (the schema you already outlined). fileciteturn4file12L1-L1  
* `jobs/<jobId>/STATE.md` — the current compact state: decisions made, open loops, constraints, current plan, interfaces/contracts.  
* `jobs/<jobId>/MEMORY.md` — durable facts and lessons learned *specific to the job* (not to the agent).  
* `jobs/<jobId>/HANDOVER.md` — a “handover brief” template for job reassignment events, designed to be read in <2 minutes.

Then make those job directories retrievable in two ways:

First, add `jobs/` (or a filtered subpath) to OpenClaw’s indexing via `memorySearch.extraPaths`, so `memory_search` can surface job memory snippets without loading entire files. This is exactly what `extraPaths` is for: enabling retrieval for Markdown outside the default `MEMORY.md` + `memory/` layout. citeturn9view3

Second, make job activation a deterministic context assembly step: on “job start” (however you signal it), load `jobs/<jobId>/STATE.md` into the working context and optionally retrieve additional snippets. This is consistent with OpenClaw’s explicit separation: the kernel (`AGENTS.md`, `SOUL.md`, etc.) is always injected/consulted, everything else should have an activation path (retrieval or explicit load). fileciteturn4file2L1-L1turn9view3

Where your Telegram session/channel strategy fits:

Use Telegram to isolate **session scope**, not to store **job scope**. The cleanest approach is to map “job-specific sessions” to Telegram isolation primitives that already exist (groups, channels, and for Telegram specifically: forum topics). OpenClaw’s session key examples show Telegram topics embedded in session keys (e.g., `agent:main:telegram:group:<id>:topic:<topicId>`), which is a ready-made way to keep separate job threads without exploding the number of channels humans have to manage. citeturn5search1turn11view0

## Recommendations for improving Lyra memory

### Quick wins that reduce failure probability before you add more agents

Treat this as “make the existing system reliable before making it bigger.”

Start with observability: confirm the real memory surfaces you are currently using. The fastest way to resolve your “are we even using SQLite?” uncertainty is to use the OpenClaw CLI memory inspection commands (`openclaw memory status --deep`, `openclaw memory index --verbose`, and memory search). These commands are designed to probe embedding availability, index dirtiness, and indexing activity, and they operate per agent if needed (`--agent <id>`). citeturn20view0 In parallel, verify which memory plugin is active via `openclaw plugins list` and `plugins.slots.memory` configuration semantics. citeturn15search0turn20view0

Make write-back deterministic at the boundaries that already exist. You already have three natural boundaries: `/new` (session reset), compaction, and “job reassignment.” OpenClaw already offers two mechanisms you should exploit immediately:

* Enable and/or customize the bundled `session-memory` hook so session resets automatically create a durable snapshot artifact. citeturn17view1  
* Ensure pre-compaction memory flush stays enabled and tuned so “durable things” are written to disk before compaction compresses older context. citeturn3view0turn10view0turn11view0  

Then add one Lyra-specific write-back rule: **every job switch or job completion must produce an update to `jobs/<jobId>/STATE.md` and optionally `jobs/<jobId>/HANDOVER.md`.** This can initially be manual (“when we reassign, run the handover template”), but it should be automated via hooks as soon as you have a stable signal for “job switch.”

Reduce channel sprawl by re-framing Telegram as a session-scope isolator. Rather than “more channels,” prefer “one job = one isolated session key.” OpenClaw gives you deterministic session isolation in channel routing (groups, channels) and in Telegram specifically via topic IDs; you can get your focused context windows without increasing human routing overhead. citeturn5search1turn11view0

### A medium-term design that makes job memory portable across agents

Once you have more than one agent, you need a normal form for what is shared and what is private.

Make job memory physically portable. In OpenClaw, multiple agents typically means multiple workspaces. citeturn8view1 Therefore, if job artifacts live only in a single agent’s workspace, job migration will require copying or syncing. The most pragmatic solution is to introduce a shared job-artifact store that is mounted or mirrored into each agent workspace. The repo already treats root-level docs as “frozen” kernel and allows other areas to be reorganized safely; job bundles fit naturally into the “safe-to-organize” category. fileciteturn13file2L1-L1

Scope retrieval to avoid cross-contamination. Once `jobs/` is indexed, you must avoid “everything everywhere all at once.” OpenClaw already isolates memory indexes per agent and allows session transcript indexing only as an opt-in experimental feature; it also notes that the trust boundary is filesystem access. citeturn9view3 Use that as your constraint: job memory that is “shared” should be explicitly whitelisted into retrieval (`extraPaths`), and agent-private memory should remain in agent-private spaces (`MEMORY.md` in main session only, and/or agent workspace-private files). citeturn3view0turn8view1

Adopt a job handover contract. Your job market model already includes “Job Change Process.” Extend it with a memory contract: whenever a job is reassigned, write a handover brief that contains (a) compact job state, (b) open decisions, (c) key constraints, (d) links/citations to canonical decision artifacts, and (e) what not to forget. This aligns with the broader agent-memory research trend: consistent long-horizon performance requires explicit write-back/reflection artifacts, not just longer contexts. citeturn22view0turn22view3turn22view1

### A longer-term tailored solution that stays “local-first” but becomes more powerful

If you want to go beyond “Markdown + retrieval” without adopting third-party memory products, you can evolve toward a typed memory layer while keeping Markdown as the canonical record.

A robust target architecture is:

* Markdown remains the system-of-record (auditable, versionable, human-readable). citeturn3view0  
* A derived index layer expands from “memory files” to “job bundles + governance + distilled knowledge,” using hybrid retrieval and structured selection policies. citeturn9view3turn9view1  
* Context assembly becomes a budgeted subsystem (“working set manager”): it decides what enters the prompt each turn, with hard budgets and explicit provenance. This is the OS-inspired “virtual context management” that MemGPT argues for, and it is consistent with OpenClaw’s own separation of kernel-injected files vs retrieved memory. citeturn22view1turn9view3  

At this stage, two things become non-negotiable for expert-grade systems:

First, memory evaluation. Use RAG evaluation frameworks to measure whether retrieval is returning the right evidence and whether generations remain faithful to retrieved context. RAGAS is a reference-free evaluation framework intended to measure retrieval and faithfulness dimensions without requiring human-labeled ground truth. citeturn24view0 ARES similarly evaluates RAG components using synthetic training data for judges and limited human annotations. citeturn24view1 This is how you avoid shipping “memory improvements” that feel good but degrade correctness.

Second, safety against memory being treated as instructions. As you expand what is indexed and retrieved, you increase the risk that retrieved text is interpreted as authoritative instructions (prompt injection via memory/notes). OpenClaw’s architecture pushes you toward provenance-aware snippet retrieval (paths + line ranges) rather than opaque “recall blocks,” which is a good baseline. citeturn9view3 Preserve that discipline as you expand memory.

## Risks and operational constraints to design around

The hardest problems you’re describing are not “storage problems”; they are **policy** and **boundary** problems.

Cross-agent leakage is the default failure mode if you index too widely. OpenClaw is very explicit that session logs live on disk and that filesystem access is the trust boundary; for stricter isolation you must use separate OS users or hosts, not just separate agents. citeturn9view3turn8view1 This intersects directly with your “jobs” abstraction: if jobs have materially different trust boundaries, the job market model’s recommendation to use separate gateway/host for real trust boundary differences is correct. fileciteturn4file12L1-L1

Memory noise is the default failure mode if auto-capture is naive. Even with manual capture, daily logs can become junk drawers unless there is a compaction/curation loop. OpenClaw’s pre-compaction memory flush is a mechanical reminder to write durable notes before compression, but it does not solve “what is worth writing.” citeturn3view0turn10view0 The research literature reinforces that scoring and selection policies (recency/importance/relevance; reflection summaries) are central to avoiding memory bloat and degraded performance. citeturn22view0turn22view3turn22view1

Finally, “more agents” does not mean “more effective context.” OpenClaw’s own multi-agent docs define agents as isolated workspaces and session stores, which is powerful for isolation but does not magically expand a single run’s context window. Better context discipline comes from **segmentation and explicit retrieval**, not from proliferating personas. citeturn8view1turn9view3 This aligns with the design principle in your internal deployment report: add persistent agents for durable boundary differences, and use sessions/sub-agents for topical separation and throughput. fileciteturn13file5L1-L1

In short: you are already on the right path (file-based durability + jobs as portable responsibilities). The key upgrade is to make **job memory a first-class portable artifact**, use OpenClaw’s existing indexing and hook seams to make write-back deterministic, and treat memory changes as evaluable engineering changes rather than discretionary “good practice.” citeturn9view3turn17view1turn24view0