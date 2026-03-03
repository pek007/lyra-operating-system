# Making “Jobs” Operational in Lyra

## Executive synthesis

Lyra has already established most of the *governance* prerequisites for job-based operation: an internal job market model with execution profiles, a jobs process, a binding/authority transfer spec, memory-portability conventions, and explicit authority-change controls. fileciteturn23file0L1-L200 fileciteturn9file17L1-L140 fileciteturn17file0L1-L200 fileciteturn25file0L1-L200 fileciteturn16file1L1-L120

The gap is not “definition”; it is *runtime semantics*: today, jobs exist mostly as “role contracts,” while work still tends to be executed by whichever runtime happens to be active (often the main Control Tower surface), without a consistent “someone is always listening for and claiming job-scoped work.” The Task & Decision Engine (TDE) work you’ve started is the right direction because it introduces the missing control-plane primitives: deterministic task state, decision/approval gates, idempotent execution, and anti-stall loops that can be triggered by heartbeat/cron. fileciteturn61file0L1-L120 fileciteturn45file2L1-L260 fileciteturn38file0L1-L120 fileciteturn32file15L1-L120

Critically, a “job” should *not* be modeled as “a separate always-on agent” by default. Your own policy already encodes the correct stance: organize as jobs first, then choose an execution surface (session/sub-agent/persistent agent/separate gateway) based on an execution profile and lifecycle evaluation. fileciteturn22file4L60-L120 fileciteturn9file18L1-L220

In OpenClaw terms, “making jobs come alive” is less about inventing new primitives and more about consistently composing existing ones:

- **Work detection + claiming loop**: heartbeat and/or cron triggers that repeatedly evaluate “is there job-scoped work ready to run?” citeturn12view0turn0search1  
- **Execution isolation + concurrency**: job runs happen in stable session keys (for continuity) or isolated cron sessions (for hygiene), and parallelism is handled via sub-agents, constrained by gateway queue semantics. citeturn10view0turn1search8turn1search2  
- **Authority enforcement**: effective authority = (agent envelope ∩ job policy ∩ process gates), plus host-side “exec approvals” interlocks for real machine side effects. fileciteturn32file8L1-L80 citeturn3search1turn3search2  
- **Durable shared context**: a blackboard-like control plane (TDE + append-only artifacts) plus searchable memory stores to mitigate context window limits. citeturn2search2turn5search6turn6search7  

The rest of this report decomposes: (a) where you are, (b) what “target state” looks like at expert resolution, and (c) the concrete technical steps to close the gap.

## Current state in the repo

The repository already describes a coherent job system on paper:

- **Jobs are formalized as portable responsibility contracts** with an execution profile including constraints like memory scope, tool posture, latency/cost posture, and trust boundary considerations. fileciteturn23file0L1-L200  
- **Jobs are explicitly not agents**, and assignment to execution surfaces is governed by a lifecycle SOP rather than “one job = one persistent runtime.” fileciteturn22file4L60-L120 fileciteturn9file18L1-L220  
- **Binding exists as a safety protocol**: you have an explicit spec for job binding and authority transfer (including handover and enforcement expectations), plus an authority change-control policy to prevent silent privilege drift. fileciteturn17file0L1-L200 fileciteturn16file1L1-L120  
- **Memory portability exists as a process**: job memory bundles and handover artifacts are treated as first-class, enabling reassignment without relying on chat transcripts. fileciteturn25file0L1-L200  

Separately, the repo is already building the “missing runtime substrate” via TDE:

- The TDE project goal explicitly targets autonomous operation, anti-stall follow-up, and progress transparency—i.e., the control-plane behaviors you need to make job teams autonomous over long horizons. fileciteturn32file1L1-L120  
- The early TDE kernel scaffold encodes core autonomy invariants that matter operationally: idempotency keys, version guards, audit linkage, approval gating, and deterministic anti-stall classification/routing triggered by heartbeat/cron-like sources. fileciteturn45file2L1-L260  
- Canary wiring already describes a runtime-triggered status artifact written on heartbeat/cron triggers, with fail-closed guardrails when approvals are required. fileciteturn38file0L1-L120  

So why does it still feel like “we have jobs, but we don’t work by jobs”?

Because the repo also documents (implicitly and explicitly) the failure mode: without a hard *claiming loop* and a hard *system-of-record*, job definitions are inert. Work still defaults to (a) whoever is currently “chatting,” and (b) whatever is currently in the transient context window.

Concretely, the current operational work substrate is still transitional:

- TASKS is explicitly a temporary kanban and you’re still in a migration world (Trello sync, interim markdown). fileciteturn23file3L1-L120  
- Multi-agent execution exists, but the default model is “spawn subagents for scoped tasks,” not “jobs as continuously-operating actors that pull from job queues.” fileciteturn62file0L1-L120  

This is not a critique—this is a normal maturity stage: governance artifacts exist, and kernelization is underway, but the “always-on coordination fabric” isn’t yet generalized from canary slices to “the whole job market.”

## How OpenClaw primitives should shape job semantics

To answer your core technical questions (“is a job a session?”, “do we need heartbeats?”), it helps to pin down the primitives OpenClaw already gives you.

### Sessions are execution context, not responsibility

OpenClaw’s session model is explicit: the gateway is the source of truth for session state, with stable session keys mapped from transports (DM vs group vs topic/thread), and stored transcripts/metadata under the agent’s sessions directory. citeturn10view0L126-L140 citeturn10view0L256-L271

Key operational implications:

- You can isolate conversations by DM, channel, account, peer, group, and Telegram topic/thread identifiers. citeturn10view0L84-L110 citeturn10view0L264-L270  
- Cron jobs and hooks also have their own session key shapes (e.g., `cron:<job.id>`). citeturn10view0L269-L272  
- OpenClaw’s internal command queue serializes runs by session key lane to prevent collisions (only one active run per session key), while still allowing global concurrency caps and subagent lanes. citeturn1search2  

**Answer to “Do we need a separate session for each job?”**  
Not inherently. A job is a *responsibility contract*; a session is a *context container*. For jobs to work well, you typically want either:

- a **job home session key** (stable context surface for job oversight and continuity), *and/or*  
- **isolated execution sessions** (cron isolated runs, subagent sessions) for hygiene, determinism, and to avoid contaminating the main/control context.

OpenClaw directly supports both patterns. citeturn0search1turn1search8turn10view0

### Heartbeat is “periodic scheduling + batching,” not “job runtime”

Heartbeat is a first-class gateway mechanism that runs periodic agent turns with a strict prompt contract, optionally reading `HEARTBEAT.md`, and suppressing outbound delivery when the agent returns `HEARTBEAT_OK` within a char budget. citeturn12view0L129-L151

Operationally important details for your design:

- Heartbeat can be configured per-agent, targeted to a delivery channel (or `none`), and even run in an explicit session key. citeturn12view0L156-L170 citeturn12view0L279-L283  
- The docs frame heartbeat as best for batching “background checks” where timing can drift, and cron as best for exact timing, isolation, model overrides, and preventing main-session spam. citeturn11search3  

**Answer to “Do we need to connect jobs to HEARTBEATS?”**  
You need jobs connected to *some* periodic trigger; heartbeat is one option, but not the only one, and often not the best per-job trigger.

A robust pattern is:

- **Heartbeat = control-plane batching** (triage, surfacing urgent decisions, checking for stalled work across jobs, escalating to the human).  
- **Cron (isolated) = job-plane execution** (repeatable “job tick” loops, per-job queue polling, noisy background chores, periodic audits). citeturn11search3turn0search1

This aligns directly with your existing anti-stall work order and canary wiring, which already treat heartbeat/cron as trigger sources for a governance loop. fileciteturn32file15L1-L120 fileciteturn38file0L1-L120

### Cron is your “job-tick substrate” (with isolation semantics)

OpenClaw cron is a gateway scheduler that persists jobs and supports two execution styles:

- **Main session**: enqueue a system event and run it on the next heartbeat.  
- **Isolated**: run a dedicated agent turn in session `cron:<jobId>`, minting a fresh session ID each run, with optional delivery modes. citeturn0search1turn0search2

This is extremely close to what job execution wants:

- A job “tick” is naturally an isolated cron run (fresh context + deterministic prompt scaffold), which then *pulls* work from the job queue and spawns subagents as needed. citeturn0search1turn1search8  
- Delivery can be suppressed (`delivery.mode = "none"`) so job ticks don’t spam the human; only escalations or end-of-cycle summaries should surface. citeturn0search1turn0search0  

### Tool policy, approvals, and resumability are already there

OpenClaw provides multiple layers of enforcement you can compose with job authority:

- Tool profiles and groups let you shape the base capability envelope (files, sessions, memory, messaging, exec/process, automation). citeturn3search3  
- Exec approvals add a host-side interlock: policy + allowlist + optional prompt/approval decide whether a command can run on gateway/node hosts; unresolved approvals default to deny via fallback. citeturn3search1turn3search2  
- Lobster provides a typed workflow runtime for deterministic multi-step tool sequences with explicit approval checkpoints and resumable tokens—exactly the class of mechanism you want for high-level autonomous tasks that must pause safely for human gates. citeturn3search0  

This is not just “nice to have”: it’s the mechanism that allows you to scale autonomy without scaling risk.

### Memory and context-window pressure: rely on durable stores + retrieval, not “bigger prompts”

OpenClaw’s memory is explicitly “Markdown as source of truth,” with an indexing/search layer backed by a per-agent SQLite store, and guardrails on what paths are retrievable unless explicitly included (extraPaths). citeturn2search2turn2search3

Two OpenClaw features are particularly relevant to your “hivemind vs context window” concern:

- **Semantic retrieval tools (`memory_search`, `memory_get`)** allow job-relevant memory to be fetched on demand, rather than stuffed into every prompt. citeturn2search2turn2search3  
- **Pre-compaction “memory flush”** runs a silent turn (`NO_REPLY`) before compaction to write durable state to disk so compaction doesn’t erase critical context. citeturn2search0  

On the research side, MemGPT formalizes the same stance: treat the context window as fast memory and build an OS-like hierarchy that pages state between fast and slow tiers. citeturn5search6 That idea is also consistent with “memory stream + reflection + planning” architectures used in long-horizon agent simulations. citeturn5search0

## Target state architecture for autonomous job teams

The target state that closes your “jobs exist / jobs operate” gap is best described as a two-plane system: **control plane (governance + coordination)** and **execution plane (work)**.

### Control plane: TDE as the shared blackboard for jobs

Your own contract already draws the right system-of-record boundaries: operational task state belongs in the task engine, decisions belong in decision artifacts, durable identity/context belongs in memory files, and runtime behavior rules belong in policies/agent configs. fileciteturn61file0L1-L120

Technically, the TDE should become a “job blackboard”:

- **Jobs** are durable role contracts (already modeled). fileciteturn23file0L1-L200  
- **Bindings** map “job authority → execution principal” with explicit time bounds and handover artifacts (already spec’d). fileciteturn17file0L1-L200  
- **Work items** are tasks/decisions/evidence transitions that are atomically claimed, executed, and audited. fileciteturn61file0L1-L120  
- **Event log** is append-only audit history (task transitions, approvals, retries, escalations). Your existing kernel slice already demonstrates the core invariants: idempotency keys, expected-version guards, replay-safe execution, and explicit “blocked_pending_approval” states. fileciteturn45file2L1-L120  

This control-plane stance mirrors classic blackboard control architectures: agents (knowledge sources) act asynchronously but coordinate through a shared, mutable problem-solving state rather than direct peer-to-peer invocation. citeturn6search7

### Execution plane: jobs as actors; agents/sessions as runtime surfaces

A job should behave like an “actor” in the Actor Model sense: it has a private state (job memory + job queue view), it processes messages/tasks, it emits messages/outcomes, and it can spawn other actors/workers to accomplish subtasks. citeturn9view0L24-L34

In Lyra terms, that means:

- A **job is an addressable work sink** (“send work here”) and an accountable authority surface.  
- A **job runner** is a routine that repeatedly:
  - queries TDE for work routed to that job,
  - claims work (respecting WIP limits),
  - executes via the appropriate runtime surface (subagent / isolated cron session / main),
  - writes back decisions, evidence links, and state transitions,
  - escalates when approvals are required or blockers persist.

OpenClaw gives you three composable ways to implement a job runner without inventing new infrastructure:

1. **Isolated cron job as job runner** (recommended default): hygienic, repeatable, can be frequent without polluting the main session, and naturally maps to `cron:<jobId>` runs. citeturn0search1turn10view0L269-L272  
2. **Heartbeat-based batching** (best for cross-job “control tower” oversight): summarize, detect anti-stall signals, surface urgent decisions. citeturn12view0L136-L151  
3. **Subagent fan-out** (best for parallelizable work decomposition): depth-limited session key shapes, explicit concurrency caps, and automatic announce chaining back to the parent. citeturn1search8  

### Authority, safety, and resumability as first-class invariants

Your internal authority model is already converging on the right technical rule:

> effective_authority = base_agent_envelope ∩ active_job_policy ∩ process_gate_conditions fileciteturn32file8L1-L80

To make that real in the target state:

- Every side-effecting operation must carry `(actor_id, job_id, policy_decision_id, idempotency_key, expected_version)`—which your TDE kernel slice already encodes at the test harness level. fileciteturn45file2L1-L120  
- Host-side side effects must be interlocked with exec approvals where applicable (gateway/node), so job authority alone cannot bypass machine safety. citeturn3search1turn3search2  
- Multi-step workflows that may pause for human approval should be executed in resumable runtimes (Lobster in OpenClaw, or a similar checkpointing mechanism), so you avoid brittle “LLM keeps the whole plan in its head” orchestration. citeturn3search0 citeturn6search1  

### “Hivemind” without shared-context chaos

The “hivemind” you want is not “all agents share one giant prompt.” It is:

- **Shared durable state** (TDE + append-only evidence + stable design constraints), and  
- **Shared retrievable memory** (indexed job bundles, curated long-term memory, domain artifacts), and  
- **Shared invariants** (policies, gates, authority model), enforced by code.

This is the same direction supported by OS-inspired memory hierarchies (MemGPT) and long-horizon agent architectures that maintain a memory stream and synthesize reflections rather than relying on the immediate context window. citeturn5search6turn5search0

In OpenClaw specifically, the “hivemind substrate” should use:

- `memory_search` / `memory_get` over curated + daily markdown, expanded via `memorySearch.extraPaths` to include job memory bundles and TDE-derived summaries. citeturn2search2turn2search3  
- Pre-compaction memory flush to prevent silent loss of cross-job state. citeturn2search0  

## Gap analysis

The delta between current state and target state clusters into four gaps.

### No generalized “job runner” loop

You have canary anti-stall loops and kernel tests, but not yet a generalized mechanism that ensures *each active job has an execution surface that repeatedly pulls and progresses job work*. fileciteturn38file0L1-L120 fileciteturn45file2L1-L260

Without this, jobs remain declarative and execution remains opportunistic.

### Weak coupling between task routing and job binding

You have a binding spec and an authority model, but in practice most work systems (TASKS/Trello) don’t enforce “no execution without an active binding,” nor do they guarantee that task mutations carry job-bound audit metadata.

The TDE kernel slice already shows what correctness should look like (idempotency + approval gating + version guards), but it’s not yet the controlling substrate for all work. fileciteturn45file2L1-L120 fileciteturn61file0L1-L120

### Session strategy is not yet job-native

OpenClaw gives you precise session-key isolation and cron/heartbeat targeting, but Lyra does not yet appear to have a formal, enforced mapping like:

- job home session keys,
- job execution sessions (cron/subagent),
- delivery suppression rules (internal vs human-visible),
- and “one active run per job key” concurrency guarantees.

These are prerequisites if you want job teams to run continuously without stepping on each other. citeturn10view0turn1search2turn0search1

### “Hivemind” is still mostly conceptual

You have job memory portability as a process, and you’re using OpenClaw memory indexing, but the missing element is a canonical shared working set that every job runner reliably reads/writes (beyond ad hoc markdown). fileciteturn25file0L1-L200 citeturn2search2

## Recommendations to close the gap

### Treat “job” as an addressable actor with a pull queue; stop treating it as a persona

Make the target technical definition explicit:

- **Job = role contract + queue + memory bundle + authority policy**. fileciteturn23file0L1-L200  
- **Binding = active authority lease** that can be held by any execution principal. fileciteturn17file0L1-L200  
- **Agent/session = execution container**, not ownership. citeturn10view0L84-L90  

This aligns with your stated doctrine (“jobs are not agents”) and prevents premature proliferation of persistent agents. fileciteturn22file4L60-L120

### Implement a “job tick” loop per active job using isolated cron by default

Concretely:

- Create one isolated cron job per “job runner” (or per small cluster of jobs with compatible risk/tool/memory profiles), using `delivery.mode = "none"` so ticks are silent unless escalation is needed. citeturn0search1turn0search0  
- Each tick performs:
  1) pull ready tasks for its job from TDE,  
  2) claim up to WIP limit,  
  3) spawn subagents for decomposable work,  
  4) write back outcomes and evidence links,  
  5) emit escalations as TDE decisions when approvals/ambiguity appear,  
  6) update job state summary artifacts.

This is the crucial “someone is on the other side picking this up” mechanism you called out. It is also directly compatible with OpenClaw’s isolated cron semantics (fresh session id per run, `cron:<jobId>` session key shape). citeturn0search1turn10view0L283-L284

### Use heartbeat for cross-job governance, not as the primary job executor

Configure heartbeat as a Control Tower batcher:

- It should read a compact `HEARTBEAT.md` checklist, query TDE for “decision-required” items, stalled items, and active job runner health, then surface only high-signal statuses. citeturn12view0L136-L151  
- Rely on the `HEARTBEAT_OK` suppression contract to avoid noisy “nothing happened” spam. citeturn12view0L145-L151  

This matches OpenClaw’s own heartbeat vs cron guidance. citeturn11search3

### Standardize a session strategy: job home keys + execution keys + delivery policy

A job-native session strategy typically uses three layers:

- **Job home session key**: persistent “job cockpit” context (lightweight), where its current objectives, constraints, and active blockers are maintained.  
- **Execution sessions**: isolated cron sessions and subagent sessions for real work. citeturn0search1turn1search8  
- **Delivery suppression rules**: internal job ticks do not deliver; only escalations do.

OpenClaw already makes this safe:

- One active run per session key prevents job ticks from colliding if schedules overlap. citeturn1search2  
- You can route heartbeats to a specific session key if you truly need job-specific heartbeat behavior, but cron remains the better primitive for per-job loops. citeturn12view0L279-L283  

### Make binding/authority “real” by enforcing it at mutation boundaries

You already have the conceptual model; now make it executable:

- Require that *any* workflow that mutates task/decision state (including “mark done,” “escalate,” “publish,” “merge,” “send”) must include the job id and binding id, and must be denied/blocked when binding is missing/expired. fileciteturn17file0L1-L200  
- Keep using the effective authority intersection rule (agent envelope ∩ job policy ∩ gates); treat it as a runtime check, not a guideline. fileciteturn32file8L1-L80 fileciteturn63file0L1-L120  
- For machine side effects, compose that with exec approvals (host allowlist and approval flow). citeturn3search1turn3search2  

### Build the “hivemind” as a blackboard + retrieval fabric, not shared chat context

Recommended minimal architecture:

- **TDE = blackboard**: canonical task/decision state + event log + approvals. fileciteturn61file0L1-L120 citeturn6search7  
- **Job memory bundles**: per-job handover + durable work context. fileciteturn25file0L1-L200  
- **Retrieval**: expand OpenClaw memory indexing to include job bundles and key distilled artifacts (via configured extra paths) so every job runner can pull necessary context on demand. citeturn2search2turn2search3  
- **Memory flush before compaction**: ensure job runners write durable state before context compression erodes working memory. citeturn2search0  

If you want a theoretical “why this works” anchor for experts: this is essentially OS-style memory tiering for agents (fast context window + slow durable memory + retrieval paging), as described in MemGPT. citeturn5search6

### Use resumable typed workflows for high-risk multi-step autonomy

For “high-level complex tasks autonomously,” your biggest technical risk is multi-step tool orchestration with failure/approval boundaries. OpenClaw’s Lobster is directly designed to solve this class: deterministic pipelines, explicit approvals, and resumable state tokens. citeturn3search0

In target state terms:

- Job runners should prefer “workflow calls” (Lobster) over long chains of ad-hoc tool calls when executing multi-step operations that touch external systems or require approvals.  
- TDE should treat these as “activities” with explicit checkpoints, and store their tokens/receipts as evidence.

This parallels the broader durable-execution pattern in workflow engines (deterministic orchestration + side effects guarded as activities), but you already have an OpenClaw-native primitive, so you can stay inside the ecosystem. citeturn3search0turn6search2

## Implementation roadmap and acceptance criteria

### Immediate milestone: define “job tick” as a first-class operational contract

Deliverables:

- A single spec describing the job tick loop contract (inputs/outputs): trigger source, job id, binding id, claimed task ids, idempotency keys, decision ids created, evidence artifacts written. This is consistent with your existing TDE trigger contract work (heartbeat/cron sources, session keys, actor/job fields). fileciteturn45file2L1-L220 fileciteturn43file3L1-L220  
- At least one job runner cron configured as isolated, internal delivery, running frequently enough to prove “someone is always listening.” citeturn0search1  

Acceptance criteria:

- A job with ready work progresses without human prompting within one tick interval.  
- No job tick produces external delivery unless escalation criteria are met. citeturn0search1turn12view0L145-L151  

### Near-term milestone: generalize the canary anti-stall loop into a multi-job scheduler

You already have the anti-stall shape: classify progress state, produce follow-ups, and fail closed when approvals are required. fileciteturn45file2L120-L220 fileciteturn38file0L1-L120

Generalization steps:

- Expand from `tde_canary=true` to “all active tasks with explicit owner/job bindings,” and let the classifier emit job-scoped follow-ups (resume/escalate/redefine/retire). fileciteturn45file2L120-L220  
- Route “requiresApproval=true” follow-ups into explicit decision queue objects, not ad hoc notifications. fileciteturn61file0L1-L120  
- Surface only the decision queue summary via heartbeat (Control Tower visibility), letting cron runners do the actual follow-up work. citeturn11search3turn12view0L136-L151  

Acceptance criteria:

- Stalled items become decision records (not silent stagnation) within a bounded time window.  
- Policy-gated tasks remain blocked until approval; no bypass is possible because approvals are enforced at the tool/host layer (exec approvals) and at the job policy layer. citeturn3search1turn3search2 fileciteturn32file8L1-L80  

### Medium-term milestone: enforce binding/authority at all mutation boundaries

Deliverables:

- A single “mutation gateway” wrapper in TDE: no mutation without `(job_id, binding_id, policy_decision_id, idempotency_key, expected_version)`. fileciteturn45file2L1-L120  
- Automated evidence artifacts for each run cycle (similar to your canary status JSON), but now stratified by job/team view. fileciteturn38file0L1-L120  

Acceptance criteria:

- Attempted jobless mutations are denied and logged (must be visible in audit).  
- “Authority change” operations cannot be self-approved and require explicit evidence/rollback plans, per your policy. fileciteturn16file1L1-L120  

### Long-horizon milestone: autonomous multi-job initiatives with shared working set

This is the “high-level complex tasks autonomously” end state. The needed additional control-plane feature is a canonical *initiative/campaign object* that binds:

- target outcomes and constraints,  
- job responsibilities,  
- task decomposition,  
- decision queue,  
- and a rolling “initiative state summary” that all job runners treat as the shared working set.

This is the “hivemind” layer: not shared chat context, but shared durable + retrievable state, synchronized by job runners and protected by your governance gates. citeturn2search2turn5search6turn6search7

Acceptance criteria:

- Multiple jobs coordinate without requiring the main session to retain full context.  
- The system survives context compaction because state is flushed to disk and retrievable. citeturn2search0turn2search2  
- High-risk steps pause cleanly and resume deterministically after approval (via a resumable workflow token). citeturn3search0turn4search3