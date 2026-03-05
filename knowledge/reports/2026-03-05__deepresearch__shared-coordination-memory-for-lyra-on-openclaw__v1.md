# Shared Coordination Memory for Lyra on OpenClaw

## Current memory and context architecture

Your repository already encodes a fairly crisp separation between **context** (what fits in a model window) and **durable state** (what survives across runs). The declared design goal is explicit: treat prompt context as a **managed cache**, keep durable memory/knowledge as **auditable markdown**, and treat indexes as **derivative accelerators** rather than canonical state. fileciteturn49file0L6-L12

In Lyra’s documented tiering, the important operational boundary is that L1 (“working context window”) is intentionally bounded and policy-driven, while L2/L3 provide durability. L3 is explicitly defined to include daily memory files, curated long-term memory, distilled knowledge, decisions, and “approved policy/runbook documents.” fileciteturn49file0L16-L55 This matches OpenClaw’s primary memory model: memory is plain Markdown in an agent workspace, with a daily layer (`memory/YYYY-MM-DD.md`, today+yesterday loaded at session start) and an optional curated layer (`MEMORY.md`, intended only for the main/private session). citeturn2search0

Two repo documents make the “who reads what, when” rule operational:

* `AGENTS.md` enforces that every session reads identity/user constraints plus the daily memory files, but only the *main* (direct/private) session reads `MEMORY.md`, explicitly for security/non-leakage reasons. fileciteturn55file0L55-L83  
* `AGENT_EXECUTION_SEMANTICS.md` declares the multi-agent run model: a persistent Control Tower plus spawned subagents as default, with explicit spawn/completion contracts and an anti-drift rule that prevents specialist agents from redefining policies/principles without approval. fileciteturn56file0L6-L32

On the “jobs” axis, you already have a portability contract: “session memory is ephemeral; durable job memory must live in files,” and every active job must have a bundle of `JOB.md`, `STATE.md`, `MEMORY.md`, and `HANDOVER.md` under `jobs/<JOB-ID>/`. fileciteturn50file0L6-L19 The presence of a `jobs/JOB-TEMPLATE/MEMORY.md` suggests a canonical structure for job-scoped durable facts, lessons, constraints, and references. fileciteturn54file0L1-L13

Beyond “memory files,” you also have two additional durable knowledge planes:

* A **process/policy/runbook plane**: `PROCESS_REGISTRY.md` enumerates review-cadenced operating documents across governance, security, delivery, model routing, etc., indicating that “what the system knows” is meant to live not just in memory files but in versioned, reviewed artifacts. fileciteturn50file1L1-L15  
* A **machine-checkable artifact plane**: `tools/gen_knowledge_indexes.py` generates indexes over decisions, inbox, and—critically—an observations index with a content-derived root hash (indicating an intent to treat “observations” as a verifiable evidence substrate). fileciteturn61file0L65-L114 The repo validator enforces cross-artifact linking rules (e.g., evidence JSON can reference observations by `observation_id` + `recordHash`, and mismatches fail validation). fileciteturn61file3L167-L213

Finally, on the “stateful coordination” plane, you already have the beginnings of an **event log + idempotency ledger** in SQLite via `tools/tde_state_store.py`: WAL mode, full synchronous, event chaining via `prev_hash/hash`, and an action ledger keyed by idempotency key. fileciteturn60file5L20-L65 This is highly relevant to your message-board hypothesis because it’s the difference between “a shared text file people overwrite” and “a shared append-only log you can project into views.”

OpenClaw’s platform primitives explain *why* your contexts are separated and what coordination options exist. OpenClaw defines **AgentId** as an isolated workspace + session store and **SessionKey** as the bucket used both for context storage and concurrency control, with deterministic routing and explicit key shapes for DMs, groups, and threads/topics. citeturn0search1 This is the mechanical source of your “different entities on different levels do not share a context window” observation: isolation is a feature, but it creates coordination blind spots unless you add a shared state substrate.

## Why disconnected contexts create coordination blind spots

It helps to separate two problems that are often conflated:

1) **Memory continuity** (“what did we learn/decide?”)  
2) **Work coordination** (“what’s happening right now, and what depends on what?”)

Your repo is already opinionated about (1): durable continuity must be written to files (daily memory, job bundles, decisions, processes). fileciteturn49file0L16-L55 fileciteturn50file0L6-L19 OpenClaw reinforces this: “the model only ‘remembers’ what gets written to disk,” and memory search tools operate over Markdown chunks, returning snippet+path+line ranges rather than full payloads. citeturn2search0

Your hypothesis is about (2): a “common message board” is not primarily a memory tier; it is a **coordination substrate**. In distributed AI and distributed systems terms, what you are proposing is a lightweight **blackboard system**: multiple specialized workers post partial state to a shared workspace, and other workers opportunistically act based on that shared state. Classic blackboard architectures were designed specifically to coordinate multiple independent “knowledge sources” in ill-defined problem spaces, with the blackboard acting as the shared problem-solving state. citeturn4search3turn3search2

Two adjacent models are worth naming because they sharpen design choices:

* **Actor model**: each job/agent behaves as an actor that processes messages, maintains private state, and interacts only via message passing; shared mutable state is avoided, and ordering/concurrency are handled via messaging semantics. citeturn5search2turn5search6  
* **Tuple-space coordination (Linda)**: a shared associative memory (“tuple space”) decouples producers and consumers in time and space; processes coordinate by asserting/removing tuples rather than direct calls. This is basically “a structured message board” with pattern matching and blocking/non-blocking reads. citeturn4search0

Your current Lyra/OpenClaw setup sits in between: you already have actor-like composition (Control Tower + spawned subagents with completion contracts) fileciteturn56file0L6-L32 and durable shared state in files (job bundles, tasks, policies). fileciteturn50file0L6-L19 The missing piece is an explicit, low-friction **“WIP awareness channel”** that is:

* visible across sessions/agents without collapsing them into one shared context, and  
* machine-usable (so it can be selectively retrieved and projected), not just human-readable.

## Assessment of the common message-board hypothesis

Your proposed solution—“an md file to which an agent in a job role in a session notifies what it is doing, on a high level; every other instance can read the file”—is directionally sound **if** you treat it as a coordination artifact, not long-term memory.

### What this would improve

A shared board directly addresses three coordination failure modes that emerge under context isolation:

* **Duplicate work**: two contexts independently decide to do the same thing because neither can see the other’s in-progress intent.
* **Cross-domain side effects**: a job makes a local optimization that creates a hidden constraint in another domain (e.g., security policy changes affecting developer workflow).
* **Lost implicit requests**: a subagent generates a need (“someone must update X”) that is not elevated to a durable, discoverable artifact quickly enough.

Your repo’s memory kernel already anticipates the need for cross-namespace sharing but insists on explicitness: retrieval is namespace-local by default; cross-namespace retrieval requires a bridge policy; shared artifacts must be explicitly designated and non-sensitive/redacted. fileciteturn49file0L67-L85 A message board fits naturally as one of the few explicitly allowed `shared` artifacts—*if you hold it to those rules*.

### Where an md board will break, unless designed carefully

The largest risk is that a message board becomes a “Schrödinger artifact”: people assume it’s live and authoritative, but it drifts, becomes stale, or is not consistently consulted. Your own artifact governance model is explicit that an artifact is “real” only if it has an activation path, and artifacts must be classified as injected kernel, retrieval module, controller input, or archive. fileciteturn57file0L6-L34 If you create `MESSAGE_BOARD.md` without:

* a mandatory “read rule” (when do agents consult it?), and  
* a write contract (what must be posted, how often?), and  
* an expiry/compaction rule (how does it stay small?),  

then it becomes an additional state surface that creates *more* confusion.

There are also hard engineering constraints:

* **Concurrency**: multiple sessions writing to one markdown file is merge-conflict prone unless you enforce append-only writes with locking. OpenClaw’s SessionKey serialization limits concurrency *within* one session key, but does not imply global single-writer semantics across all sessions. citeturn0search1  
* **Information overload**: a free-form board quickly becomes unscannable, and if agents start retrieving it into context, you reintroduce the “context pollution” problem in a new form.
* **Security/trust**: `AGENTS.md` is explicit that curated long-term memory must not load in shared contexts for security. fileciteturn55file0L75-L83 A global board must follow the same discipline: high-level, non-sensitive, minimal.

Net: the hypothesis is good, but “an md file everyone edits” is the weakest implementation of the idea.

## Stronger alternatives for shared coordination

The design space here is best understood as: **canonical event stream** vs **editable shared document**.

A mature coordination substrate is almost always *append-only events* plus *projected views*—the same pattern used in event sourcing. Event sourcing stores state changes as a sequence of events and uses those events to reconstruct current or historical state. citeturn6search1 Your repo is already adopting this for TDE state (events table + action/idempotency ledger), and it is materially safer under concurrency than “everyone edits one markdown file.” fileciteturn60file5L20-L65

Three options, ordered by increasing correctness under concurrency:

### A shared board as a projection of canonical job state

You already have job `STATE.md` as part of the required job memory bundle. fileciteturn50file0L15-L19 If every job runner reliably updates its `STATE.md` (“current focus / blockers / requests”), then a global board can be *generated* as an aggregated view.

This aligns with your artifact activation doctrine: the generated board is a **controller output/projection**, not a second source of truth. fileciteturn57file0L48-L76

### A structured “coordination log” (JSONL) plus a markdown view

This is the tuple-space/blackboard idea implemented pragmatically: agents append structured records (timestamp, job, session, intent, request) to an append-only log; a periodic compiler generates a human-friendly markdown board.

This is also compatible with OpenClaw memory retrieval: indexing is explicitly extensible via `memorySearch.extraPaths`, allowing you to make the board retrievable without injecting it into every run. citeturn2search0

### A SQLite coordination event store with projections and idempotent writers

This is the “TDE direction” and the most robust option given you already have the scaffolding:

* SQLite WAL mode is explicitly designed for concurrent access, and WAL activation is a one-line pragma. citeturn5search7  
* SQLite’s synchronous settings in WAL mode define the durability/consistency tradeoffs; FULL in WAL mode is described as ACID. citeturn5search1  
* Your `tde_state_store.py` already uses WAL + FULL synchronous and implements events + actions/idempotency. fileciteturn60file5L20-L65

If you later need cross-process delivery guarantees (e.g., “post coordination event only if task mutation committed”), you can lift standard “transactional outbox” mechanisms: write state + outgoing event in one DB transaction, then relay. citeturn6search0turn6search2

## Recommended architecture and implementation details

Given what already exists in your repo, the most leverage-maximizing path is:

**Do not implement the board as a manually edited shared md file.**  
Implement the **board as a projection** from an append-only coordination event stream, with an optional markdown “reading surface.”

This is consistent with (a) your Memory Kernel posture (“indexes are derivative accelerators”) fileciteturn49file0L6-L12, (b) your Artifact Activation model (“artifact is real only with activation path”), fileciteturn57file0L6-L34 and (c) your live TDE direction (SQLite event log and projections). fileciteturn60file5L20-L65

### Minimal viable design

**Canonical store:** extend the existing SQLite event log (or create a sibling DB) with a new event type, e.g. `coord_status`.

Event payload schema (conceptual, not a full JSON Schema):

* `event_id` (unique, deterministic if possible)  
* `at` (RFC 3339)  
* `job_id` (or `job_scope = os|px|shared`)  
* `session_key` (OpenClaw session key) citeturn0search1  
* `actor` (`agent_id`, optional `subagent_id`)  
* `kind` (`status`, `request`, `blocker`, `handoff`, `impact_notice`)  
* `summary` (bounded length, e.g. 240–400 chars)  
* `refs` (task IDs, decision IDs, file paths)  
* `ttl_days` (default, e.g. 7)  
* `safety` (`non_sensitive=true`, optional redaction marker)

**Write rules:**

* Append-only; no edits in place (new event supersedes old).  
* Idempotency required for periodic writers (e.g., session heartbeats) to avoid log spam—your current action ledger pattern is already keyed by idempotency key. fileciteturn60file5L41-L49  
* Post on state transitions, not on every thought: start work, blocked, request another job, completion/handoff. This matches your spawned-agent completion contract expectations. fileciteturn56file0L22-L29  

**Projection:** generate `governance/WORKBOARD.md` (or `shared/WORKBOARD.md`) as a deterministic summary:

* Per job: “current active intent,” “latest blocker,” “open requests to other jobs,” “last update time.”  
* Global: last N notable events (e.g., blockers/requests only).  

This is exactly the “event log → materialized view” pattern from event sourcing, but kept local-first and auditable. citeturn6search1

**Activation path and retrieval:**

Classify `WORKBOARD.md` as a Retrieval Module (not kernel injection) to avoid polluting every run. Your activation model requires retrieval modules be indexed and queryable on demand, with provenance. fileciteturn57file0L79-L92 OpenClaw supports indexing additional paths via `memorySearch.extraPaths`, enabling you to make the board discoverable without hard-injecting it. citeturn2search0

### Why this beats “one shared md file”

* **Concurrency-safe by construction** (DB transactions vs merge conflicts). citeturn5search7turn5search1  
* **Machine-usable semantics** (typed fields, filters, TTL).  
* **Human-readable where it matters** (markdown projection).  
* **Auditable** (append-only log, optional hash chaining—your current event table already supports prev-hash chaining semantics). fileciteturn60file5L29-L40  
* **Aligned with your repo’s governance posture**: “projection is not truth.” fileciteturn49file0L6-L12

## Evaluation, governance, and failure-mode controls

The success criterion for a hivemind-like step is not “more shared text”; it’s **less duplicated effort and fewer cross-job surprises** without sacrificing isolation guarantees.

### Controls to prevent turning the board into a new failure mode

**Namespace and sensitivity gates:** Your memory kernel requires explicit bridge policy for cross-namespace retrieval and requires shared artifacts to be non-sensitive or redacted. fileciteturn49file0L67-L85 Enforce the same on coordination events:

* `shared` events must be non-sensitive by default.  
* escalation path for “sensitive cross-job dependency” should be: store details in job bundle / decision artifact; emit only a redacted coordination stub that points to the authoritative location.

**Size and TTL:** enforce TTL-based compaction (e.g., retain 7–14 days of events) and keep projections bounded. This mirrors your L1 budget discipline: drop low-value blocks before compressing high-value blocks. fileciteturn49file0L23-L33

**Activation discipline:** if no tool/cron/heartbeat reads the board, it will rot. Your artifact activation model mandates that artifacts must have explicit consumers and enforcement modes. fileciteturn57file0L35-L76 Make the board’s activation path explicit:

* Control Tower heartbeat: consult projection for “open blockers/requests” only. OpenClaw heartbeat is specifically designed to batch periodic checks and suppress delivery when nothing matters. citeturn1search1turn1search4  
* Job ticks via isolated cron: write coordination events after completing a job tick, with delivery suppressed by default when appropriate. OpenClaw cron supports isolated sessions (`cron:<jobId>`) and delivery modes that can keep output internal. citeturn1search0turn1search5  

### Measurement

Your memory kernel already defines memory-quality metrics like cross-namespace leakage rate, write-back success, and token cost. fileciteturn49file0L160-L175 For a coordination board, add a small set of “coordination quality” metrics:

* **Duplicate-work rate** (count of tasks closed as duplicates / repeated analyses).  
* **Cross-job blocker latency** (time from blocker emitted → acknowledged by relevant job).  
* **Staleness** (percentage of jobs whose “current intent” timestamp exceeds threshold).  
* **Noise ratio** (events per completed work unit; should trend down as you refine triggers).  

### A key design constraint: don’t rebuild “shared context”

The system-level win here is a **shared, retrievable working set** without collapsing all sessions into one window. That is consistent with OpenClaw’s deterministic session isolation model (SessionKey as the context bucket) citeturn0search1 and with your repo’s stance that durable state belongs in files (job bundles, decisions, processes), not in mental notes. fileciteturn55file0L55-L83

In other words: the “hivemind” step is a **blackboard/event-log substrate + projections**, not a giant shared prompt. citeturn4search3turn6search1