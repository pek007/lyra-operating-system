---
title: "Continuous-Action Orchestration for Lyra on OpenClaw"
date: 2026-03-01
source: deepresearch
ingest_from: "knowledge/inbox/external-analysis-dropzone/deep-research-report (8).md"
tags: [external-analysis, deepresearch]
decision_relevance: tbd
confidence: tbd
status: archived-source
---

# Continuous-Action Orchestration for Lyra on OpenClaw

## Why agent systems “stop” even when work exists

In practice, “the system is stopped” rarely means “no tasks exist.” It means the *active execution loop* cannot advance because it is waiting on a missing precondition (human approval, credential, external dependency), or it has no explicit instruction to continue from the current state (missing next-action encoding). In Lyra’s own operating docs, this shows up explicitly as the distinction between **Active** vs **Waiting** states and the requirement that every Active/Waiting task has an explicit next step and owner; otherwise the workflow devolves into stasis-by-ambiguity. fileciteturn29file0L1-L60

A second, subtler failure mode is *quiet-time deadlock*: even if there are periodic triggers, the agent is configured (correctly) to suppress output when nothing is urgent. OpenClaw’s heartbeat response contract (“reply `HEARTBEAT_OK` when nothing needs attention”) is designed to prevent spam, but it also means you must be deliberate about what constitutes “needs attention,” and how blocked work is represented so that it reliably surfaces when appropriate. citeturn12view0turn12view1

A third failure mode is *monolithic work units*: if “the task” is a multi-step operation that mixes computation, tool calls, and side effects, a single missing approval can freeze the whole unit. The fix is not “try harder,” it is to refactor execution into (a) deterministic multi-step workflows with explicit pause/resume points, plus (b) independent background work items that can proceed while “the main thing” is blocked. OpenClaw’s own guidance explicitly separates **heartbeat**, **cron**, and a deterministic workflow runtime (“Lobster”) as complementary mechanisms for this reason. citeturn9view0turn10view0

## What OpenClaw already provides for continuous action

OpenClaw is unusually explicit about the primitives you need to keep an agent system moving: a scheduler (**cron**), a periodic awareness loop (**heartbeat**), asynchronous parallel execution (**sub-agents**), approval gating for real side effects (**exec approvals**), and a resumable deterministic workflow runtime (**Lobster**). Lyra’s internal OS docs are already aligned with this split: they recommend batching periodic checks into heartbeat, using cron for precise or isolated runs, and using spawned subagents as the default execution form with strict handoff contracts. fileciteturn4file2L120-L220 fileciteturn7file4L1-L40

### Cron: durable schedules, isolation, delivery control, and backoff

OpenClaw cron runs inside the Gateway process, persists jobs under `~/.openclaw/cron/`, and supports two execution styles:

- **Main-session cron**: enqueue a system event and process it via the next heartbeat (optionally “wake now” rather than waiting). citeturn8view0L138-L143  
- **Isolated cron**: run a dedicated, clean agent turn in `cron:<jobId>`, with configurable delivery modes (`announce`, `webhook`, `none`) and model/thinking overrides. citeturn8view0L245-L279

Two details matter operationally for “things should happen all the time”:

1. **Deterministic staggering**: recurring top-of-hour schedules can be automatically spread via a deterministic per-job stagger window (to avoid synchronized load spikes), with explicit overrides when exact timing is required. citeturn8view0L221-L229  
2. **Failure backoff and retention**: recurring jobs apply exponential retry backoff after consecutive failures, and cron has explicit retention/pruning controls for cron sessions and run logs. This prevents “retry storms” and prevents cron history from becoming its own operational failure mode. citeturn1view0L131-L135

Lyra already has a concrete cron spec for daily hygiene checks: run `openclaw doctor --non-interactive` plus `openclaw security audit --json`, summarize compactly, deliver to Telegram, and never auto-apply fixes. fileciteturn7file3L1-L60 This “scheduled evidence + human gate” pattern is the right shape for many OS-grade routines.

### Heartbeat: the “always-on” control loop (with guardrails)

OpenClaw heartbeat is explicitly meant to be the periodic awareness loop: by default it runs every 30 minutes (with configuration for active hours, delivery targets, and optional reasoning visibility), and it can optionally consult a tiny `HEARTBEAT.md` checklist. citeturn12view0turn12view2 If `HEARTBEAT.md` is effectively empty, OpenClaw can skip the heartbeat run to save cost—meaning continuous action is achieved not by constant chatter, but by a stable “do we have something meaningful to do?” loop. citeturn12view1

Lyra’s own `AGENTS.md` reinforces the same design: heartbeat for batching periodic checks and minimizing tool/API calls; cron for precise timing and isolation; keep the heartbeat checklist small; and track last-check timestamps to avoid redundant polling. fileciteturn4file2L120-L205

Critically, OpenClaw supports a **manual wake** that can enqueue a system event and trigger an immediate heartbeat run—this is a clean mechanism for “unsticking” without inventing a parallel signaling system. citeturn12view3

### Sub-agents: non-blocking parallelism with explicit control knobs

OpenClaw sub-agents are first-class background runs spawned from an existing run. They run in dedicated sessions and announce results back to the requester channel. citeturn11view0L112-L116 The spawn behavior is explicitly designed to avoid blocking the main run: spawning returns immediately, completion is delivered later, and delivery is “resilient” with idempotency keys, fallback routing, and backoff—i.e., the system is trying hard to make “work completes even if messaging is flaky” true. citeturn11view0L140-L147

For Lyra’s purposes, the most important sub-agent controls are:

- **Timeouts**: `runTimeoutSeconds` (default can be configured; `0` means no timeout). citeturn11view0L170-L178  
- **Concurrency caps**: global `maxConcurrent`, and `maxChildrenPerAgent` to prevent fan-out runaway. citeturn11view0L238-L246turn11view0L278-L281  
- **Nesting depth**: `maxSpawnDepth: 2` enables an orchestrator sub-agent pattern (main → orchestrator → workers) with an announce chain back up the tree. citeturn11view0L229-L267  
- **Tool policy by depth**: depth-1 orchestrators can be granted only the session-management tools needed to manage children; leaf subagents do not get session tools by default. citeturn11view0L271-L276  
- **Auto-archive**: sub-agent sessions are auto-archived after a configurable duration; this prevents background work from accumulating indefinitely as “active state.” citeturn11view0L220-L226

Lyra’s internal execution semantics already align with these primitives: a persistent Control Tower owns global context/decisions, while spawned subagents are the default for scoped tasks, with a required spawn contract and a mandatory completion handoff format. fileciteturn7file4L1-L40 fileciteturn6file0L1-L90

### Exec approvals + Lobster: making “blocked on human input” resumable (not terminal)

OpenClaw exec approvals provide a host-level safety interlock: in allowlist mode, commands run only if policy, allowlist, and (optional) user approval agree. citeturn14view0L104-L112 The approval flow is explicit: when prompting is required, the system emits an approval request and later resolves it; approvals can also be forwarded to chat channels and resolved with `/approve`. citeturn14view0L221-L264 This is a direct way to convert “blocked waiting on manual input” into “pending approval with an ID, a timeout, and an auditable decision trail.”

OpenClaw Lobster goes further: it is explicitly positioned as a deterministic, typed workflow runtime where multi-step pipelines can **pause for approval** and then **resume from a durable token** without re-running earlier steps. citeturn10view0L119-L134 This is the canonical fix for the “monolithic task stalls everything” failure mode: you factor the multi-step flow into a resumable pipeline, and your “blocked” state becomes an explicit `needs_approval` status with a `resumeToken`. citeturn10view0L316-L341

## Comparative patterns from other agent and workflow systems

The OpenClaw primitives above map cleanly onto established best practices in workflow engines and agent orchestration frameworks:

### Human-in-the-loop as a first-class pause/resume primitive

LangGraph’s `interrupt()` pattern is conceptually identical to Lobster approvals: execution pauses, state is checkpointed, and you resume by supplying a `Command(resume=...)`. Two details are particularly relevant for Lyra:

- **Durable pointer for resumption**: a `thread_id` functions as the persistent cursor to reload state; reuse it to resume, change it to start new. citeturn1view1L89-L93  
- **Idempotency requirement before pause points**: resuming restarts the node from the beginning, meaning any side effects before the interrupt must be idempotent (or explicitly guarded). citeturn1view1L140-L144

For Lyra, this implies a concrete rule: any workflow step *before a human gate* must be safe to retry; any “real-world side effect” must be behind an approval boundary or an idempotency key.

### Callback tokens + heartbeats to prevent “stuck forever”

AWS Step Functions’ callback-token pattern is the enterprise workflow analog of “waiting on human approval”: a task emits a token, the workflow pauses until `SendTaskSuccess/Failure` arrives, and you can configure heartbeats/timeouts so the workflow does not hang indefinitely. citeturn3search0 The key operational point is that a waiting task must have *a heartbeat/timeout contract*; otherwise you do not know if you are “waiting” or “dead.” citeturn3search0

OpenClaw already embeds the same logic at multiple layers (cron retry backoff; heartbeat loop; approval IDs; sub-agent announce retries). The missing piece for Lyra is mostly *standardization*: encode “waiting on X” in a structured way so the system can timebox, retry, and escalate consistently.

### Scheduling is not “cron vs not-cron”; it’s about catchup, overlap, and manageability

Temporal’s Schedules are explicitly positioned as “more flexible than cron” because they add lifecycle management concepts: list/describe/pause/backfill/update, and overlap/catchup policies. citeturn6search4 Even if Lyra never adopts Temporal, the lesson applies: scheduled work must include explicit policies for missed runs, overlap, and backoff—otherwise scheduling becomes a reliability liability.

Kubernetes CronJobs demonstrate the same point in a lower-level environment: `startingDeadlineSeconds` defines whether missed runs should be skipped, and `concurrencyPolicy` defines overlap behavior (`Allow`, `Forbid`, `Replace`); importantly, the docs explicitly warn that missed jobs may execute immediately upon unsuspending and therefore **Jobs should be idempotent**. citeturn7search1 This is exactly the agent-automation equivalent of “don’t send the same email twice because the scheduler retried.”

Apache Airflow’s “catchup” and “backfill” concepts similarly formalize “what happens when time passes but work didn’t run,” and how historical intervals can be re-run. citeturn7search13 Lyra’s control tower should treat “missed schedule windows” as a first-class operational state, not an edge case.

### Multi-agent orchestration: conversation frameworks vs control-plane governance

AutoGen frames multi-agent systems as conversable agents coordinating via structured chat, integrating tools and humans, with a focus on orchestration of complex workflows. citeturn3search1 The key lesson for Lyra is that “multi-agent” does not automatically mean “continuous action.” Without a control-plane that enforces budgets, handoffs, and resumption semantics, multi-agent systems tend to thrash (fan-out without convergence) or stall (waiting on the same missing input).

Lyra’s internal multi-agent model (Control Tower + specialist roles + mandatory handoffs + least-privilege envelopes) is the right governance layer to prevent that outcome, but it must be connected to OpenClaw’s concrete spawn-depth limits, concurrency caps, and tool policies to be enforceable. fileciteturn6file0L1-L120 citeturn11view0L229-L281

## A vision for Lyra: a control-plane that guarantees “always something useful is happening”

Lyra’s Control Panel repo is already headed in the right direction: a local-first, read-only ops dashboard that parses workspace artifacts and renders four operator views (Now/Next/Watch/Changes). fileciteturn53file0L1-L80 Lyra’s OS docs similarly specify the Control Tower views as: live state (Now), prioritized next work (Next), risk watchlist (Watch), and audit-style change feed (Change Feed). fileciteturn4file8L1-L45

The missing “vision layer” is to make this control plane *action-complete*:

- It should not just **show** that work is blocked; it should encode *what wakes it*, *when it retries*, and *what alternative work is eligible now*.
- It should not just **allow** sub-agents; it should treat them as a managed resource pool with explicit objectives, timeboxes, and acceptance criteria.
- It should treat “waiting for human input” as a resumable state machine (approval IDs, resume tokens, timeouts), not a conversational dead end.

Concretely, think of Lyra as running three interlocking loops:

1. **Heartbeat loop (context-aware batching)**: periodic triage, inbox/calendar checks, “do we have blocked items that need a nudge?”, and opportunistic low-risk background work. citeturn9view0turn12view1  
2. **Cron loop (precise + isolated execution)**: hygiene checks, weekly reviews, model-heavy analysis, integration sync, and time-critical reminders. citeturn8view0turn9view0  
3. **Workflow loop (deterministic pipelines with approvals)**: multi-step automations where approvals create explicit pause states and resumable tokens, rather than yielding conversational limbo. citeturn10view0

Lyra’s own execution semantics already define the organizational structure to power this: persistent Control Tower for decision rights; spawned subagents by default; permission envelopes and escalation boundaries; and explicit completion contracts. fileciteturn7file4L1-L40 fileciteturn20file0L1-L60

## What should be scheduled, and how

The “what to schedule” question becomes tractable if you treat scheduling as an OS capability with explicit policies (overlap, catchup, backoff, and delivery), not as a bag of cron strings.

### A practical scheduling taxonomy for Lyra

Lyra already has an explicit daily hygiene cron spec (08:30 Europe/Stockholm, isolated, announce to Telegram, no auto-fix). fileciteturn7file3L1-L60 That should be the template for OS-grade scheduled tasks:

**Health + security evidence (daily / high criticality).**  
Run OpenClaw doctor and security audit, ingest evidence artifacts, and post only a compact delta (“what changed since last run”). This aligns with Lyra’s evidence-ingestion tooling, which writes structured evidence records and stores raw artifacts for drill-down. fileciteturn7file3L1-L60 fileciteturn3file13L1-L120

**Cadence integrity tasks (weekly/monthly).**  
Lyra’s OS docs call out weekly metrics cadence and monthly reviews; these should be isolated cron jobs because they are standalone, can use different models, and shouldn’t pollute the main conversational session. fileciteturn7file5L1-L80 citeturn9view0L190-L206

**Sync + instrumentation tasks (frequent / noisy).**  
Examples already appear in Lyra’s task log (e.g., Trello sync “every 30 min”). These should be isolated cron jobs with `delivery.mode = none` (or webhook delivery into the Control Panel backend) so they don’t spam the human, but still update state. fileciteturn4file1L10-L40 citeturn8view0L251-L279

**Triage nudges (daily / main-session).**  
Lyra’s intake SOP specifies a daily short triage pass; in OpenClaw, the cleanest implementation is main-session cron that enqueues a system event and wakes the heartbeat runner immediately. This preserves main-context awareness while still being time-driven. fileciteturn34file0L1-L55 citeturn8view0L235-L242

### Scheduling mechanics Lyra should standardize on

OpenClaw already encodes the right knobs; Lyra should require them explicitly in every scheduled job spec:

- **Execution style**: main vs isolated (system event vs dedicated agent turn). citeturn8view0L138-L141  
- **Delivery policy**: announce/webhook/none, plus “best effort” semantics (don’t fail the job just because delivery failed). citeturn8view0L274-L289  
- **Backoff + retry semantics**: accept OpenClaw’s built-in backoff for cron failures and add Lyra-level escalation thresholds (e.g., “after N consecutive failures, open an incident task and page the Control Tower”). citeturn1view0L131-L135  
- **Staggering policy**: accept deterministic stagger defaults for top-of-hour load spreading unless the job is explicitly marked “exact.” citeturn8view0L221-L229

If you want a crisp rule: any scheduled job without **(a) an explicit delivery mode, (b) an explicit isolation choice, and (c) an explicit failure policy** is incomplete.

## How Lyra should keep working when blockers exist

The core design goal is: *a blocker blocks a task, not the system.*

### Encode blockers as structured state, not conversational context

Lyra’s work tracking already includes a **Waiting** state. fileciteturn29file0L15-L40 The upgrade is to make “Waiting” machine-actionable by adding a minimal, standardized blocking contract inside the task representation (whether in `TASKS.md`, Trello, or a registry). The Control Panel task parser already supports parenthetical metadata; Lyra should exploit this by standardizing fields like:

- `blocked_on`: human approval | external reply | credential | upstream task ID  
- `unblock_action`: what will be done immediately once unblocked  
- `next_check_at`: timestamp for an automatic follow-up ping/poll  
- `escalate_at`: timestamp for escalation (create incident / notify human)  

The Control Panel’s parsing/tests show that section headings and parenthetical metadata are supported formats, so this is a low-friction evolution. fileciteturn43file4L1-L120

### Convert “waiting for human input” into resumable approvals

For host-side effects, use OpenClaw exec approvals so blocked execution yields an approval ID with an explicit resolution path (macOS UI or `/approve` in chat), and so you can forward approval prompts into whichever channel is your operational cockpit. citeturn14view0L221-L264

For multi-step workflows, prefer Lobster-style pause/resume tokens so you don’t re-run earlier steps or re-fetch state (which is where duplicate side effects and drift creep in). citeturn10view0L131-L134turn10view0L316-L341 This is directly aligned with LangGraph’s best practice that any pre-interrupt side effects must be idempotent because restart-on-resume replays node code. citeturn1view1L140-L144

### “Work stealing” policy: always maintain a ready queue

To avoid stalling on blocked items, Lyra should maintain (conceptually, at least) three queues:

- **Ready-now**: tasks with no unmet dependencies and no human gates.  
- **Waiting-with-timer**: blocked tasks that have a next-check timestamp (cron-driven follow-up).  
- **Waiting-with-signal**: blocked tasks that will resume only when an approval/event arrives (exec approval resolve, Lobster resume token, message-based reply).

Heartbeat should preferentially pull from “Ready-now,” and when that queue is empty it should either (a) perform OS maintenance tasks that are safe and non-invasive, or (b) explicitly surface the *smallest* number of unblock requests that would restore throughput. This matches OpenClaw heartbeat’s intended use (“periodic awareness” + “surface what matters”) and Lyra’s own heartbeat guidance about being proactive without being noisy. citeturn9view0turn12view1 fileciteturn4file2L120-L205

### Timeouts and escalation are not optional

Any “wait indefinitely” mechanic must still have an operational timeout/escalation policy. Step Functions makes this explicit via heartbeat timeouts on waiting tasks. citeturn3search0 OpenClaw’s ecosystem already has similar hooks (approval timeouts resolve as denial; cron retries back off; sub-agent announces retry and expire). citeturn14view0L223-L235turn2view0L120-L122

Lyra should encode this as: *every waiting task must declare an escalate-at timestamp or a max-wait duration*. Otherwise “waiting” becomes silent backlog rot.

## Sub-agents for maximum impact and control

Lyra’s internal operating model correctly assumes “spawned subagents are the default.” fileciteturn7file4L1-L20 OpenClaw provides the concrete mechanics to make that safe and controllable.

### Recommended sub-agent topology for Lyra

Use a two-tier topology (enabled via `maxSpawnDepth: 2`) for the specific case the user described: a continuously-spawned set of workers receiving tasks from a Control Tower that may itself be busy.

- **Depth 0 (Control Tower)**: owns decision rights, prioritization, and final synthesis. fileciteturn8file0L1-L20  
- **Depth 1 (Orchestrator sub-agent, optional)**: manages a bounded set of depth-2 workers for a specific campaign (e.g., “clear inbox backlog,” “evaluate scheduling policy,” “refactor evidence schemas”). citeturn11view0L229-L267  
- **Depth 2 (Leaf workers)**: execute scoped work items, return structured handoffs, cannot spawn further. citeturn11view0L254-L276

This structure lets you keep the Control Tower responsive while letting an orchestrator manage parallel work—without letting the overall system go “distributed uncontrolled.”

### Governance: enforce contracts, budgets, and tool boundaries

Lyra already has the right governance artifacts:

- Spawn contract + completion contract (objective, scope boundary, allowed tools, output format, timebox; then outcome, artifacts, risks, next actions). fileciteturn7file4L10-L30  
- Least-privilege permission envelopes per role. fileciteturn20file0L1-L40

OpenClaw adds the enforceable runtime knobs:

- `maxConcurrent` + `maxChildrenPerAgent` to cap resource use. citeturn11view0L238-L246turn11view0L278-L281  
- `runTimeoutSeconds` (default timeboxes) to prevent zombie runs. citeturn11view0L170-L178  
- Tool policies by depth so orchestrators can manage sessions but leaf workers cannot escalate privileges by spawning. citeturn11view0L271-L276  
- Auto-archive for sub-agent sessions so the sub-agent registry stays clean. citeturn11view0L220-L226

The “continuous action” insight here is counterintuitive but critical: **unbounded subagent spawning reduces action** over time (thrash, contention, unreadable outputs). The maximum-impact system is the one that keeps subagent parallelism *within a budget*, and always converges via structured handoff back to the Control Tower.

## Implementation recommendations for Lyra

### Make “blocked” and “resume” first-class in the workspace data model

Lyra’s Control Tower MVP spec already wants the Next view to show “blocked items requiring human decision.” fileciteturn4file8L10-L25 Convert that from a UI concept into a schema requirement:

- Extend task representation to include structured blocker fields (blocked_on, next_check_at, escalate_at, unblock_action).  
- Add a Control Panel rendering rule: blocked tasks must always show (a) what is missing, (b) who can provide it, and (c) when Lyra will next attempt to unblock.

This directly addresses the “no instruction to continue” failure mode by making continuation instructions durable artifacts, not chat memory.

### Standardize on “heartbeat for awareness, cron for precision, Lobster for multi-step” as an operating doctrine

OpenClaw’s own Cron vs Heartbeat guide is already a concise decision procedure; codify it inside Lyra as policy, not preference, and mirror it in the Control Panel UX (e.g., when defining a new automation, force the user/agent to pick the execution class and delivery mode). citeturn9view0turn8view0

Lyra’s `AGENTS.md` likewise recommends batching periodic checks into heartbeat and using cron for exact timing, isolation, model overrides, and one-shot reminders; treat this as the default “action engine” configuration for Lyra. fileciteturn4file2L120-L205

### Fix the evidence schema mismatch between ingestion and the Control Panel

Lyra’s evidence ingestion script writes evidence records with a JSON-frontmatter payload containing fields like `timestamp`, `status: warn|pass|fail`, and `severitySummary`. fileciteturn3file13L1-L110 Meanwhile, the Control Panel’s evidence schema expects fields like `title`, `date`, `type`, and status values like `complete|warning|incomplete|pending`. fileciteturn48file0L1-L25 This disconnect will manifest as “evidence appears missing,” which is a direct hit to continuous action because the system can’t see its own health signals.

Recommendation: define a single canonical evidence schema (even if it’s a minimal common subset) and enforce it at write time in the ingestion job.

### Introduce an “approval card” pattern as the universal human-gate interface

Lyra’s tasks already include “approval-card pattern before enabling human-like tools” as active work. fileciteturn4file1L12-L18 Make this universal:

- For exec-side effects: rely on OpenClaw exec approvals and forward prompts to the operational chat channel; approval IDs become task-linked artifacts. citeturn14view0L237-L264  
- For multi-step workflows: Lobster `needs_approval` status + resume token is the card. citeturn10view0L316-L341  
- For “soft approvals” (content publishing, client sends): use a LangGraph-style approve/edit/reject decision model (approve as-is, edit, reject with feedback) to reduce friction while keeping governance. citeturn1view2

The goal is that every blocked-on-human state yields the same interface primitives: an ID, a preview, allowed decisions, a timeout/escalation policy, and a resume action.

### Configure sub-agent pooling explicitly and expose it in the Control Panel

Implement sub-agent “pool policy” as config + UI:

- Default `maxSpawnDepth: 2` **only** for orchestrator patterns that are explicitly enabled. citeturn11view0L229-L246  
- Set `runTimeoutSeconds` defaults per agent type (research/build/ops), and enforce a max child count per orchestrator. citeturn11view0L238-L246turn11view0L278-L281  
- Require Lyra’s completion handoff schema for every subagent completion announcement (the OS already defines this). fileciteturn7file4L10-L30  

Then in the Control Panel “Now” view, add: active sub-agents, their timeouts, and whether they are stalled on approvals or tool errors (mirroring OpenClaw’s sub-agent control surfaces). citeturn11view0L117-L135

### Add “anti-stall” automation: detect and react when throughput collapses

Lyra already defines weekly metrics for throughput, cycle time, WIP, incidents, and bottlenecks. fileciteturn29file0L1-L30 Use this to create an automated anti-stall response:

- If WIP is low but Waiting is high → trigger an unblock review heartbeat (“what are we waiting on, what’s the next smallest unblock needed?”). citeturn12view1L370-L380  
- If cron failures exceed a threshold → open an incident task and post a compact alert (cron already backoffs retries; Lyra should decide escalation). citeturn1view0L131-L135  
- If sub-agent announce retries are accumulating → treat as a control-plane health issue (OpenClaw has explicit failure modes for announce retry expiration). citeturn2search6turn8view0

This closes the loop: you are no longer “hoping” the system stays action-oriented; you are measuring and enforcing it.

