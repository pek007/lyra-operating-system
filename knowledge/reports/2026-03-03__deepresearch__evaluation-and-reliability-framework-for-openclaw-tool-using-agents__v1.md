---
title: "Evaluation and reliability framework for OpenClaw tool-using agents"
date: 2026-03-03
source: deepresearch
ingest_from: "telegram attachment deep-research-report_44"
tags: [external-analysis, deepresearch, evaluation, reliability]
decision_relevance: high
confidence: medium-high
status: archived-source
---

# Evaluation and reliability framework for OpenClaw tool-using agents

## Executive brief

### Top findings

**Execution-based evaluation beats “text-only” evaluation for real agents.** Benchmarks built for tool-using agents increasingly rely on programmatic checks of side effects (files changed, actions taken, intermediate state constraints), not just output text. This design shows up in environments like OSWorld (state setup + execution-based evaluation scripts) and WebArena (annotated programs that validate functional correctness). citeturn15view0turn17view0

**Stability and reproducibility require “simulated” or cached tool environments.** Tool and web APIs are inherently unstable; StableToolBench’s contribution is explicitly a *virtual API server + caching + simulators* to reduce evaluation noise. This is a transferable pattern for OpenClaw operations workflows (web fetches, browser automation, shell/network calls) where flaky dependencies can otherwise dominate your signal. citeturn14view0

**Benchmarks (and internal eval suites) get contaminated—quietly.** OpenAI’s analysis of SWE-bench Verified highlights two general failure modes: (1) flawed tests that reject correct solutions and (2) training contamination where models have seen benchmark problems/solutions, inflating apparent performance. The same risks apply to internal “golden tasks” if you reuse public tickets, paste solutions into prompts, or allow eval fixtures to leak into training/finetuning corpora. citeturn6view0

**LLM-as-judge is usable, but only with calibration and bias controls.** LMSYS reports >80% agreement between strong LLM judges and human preferences in MT-bench–style settings (comparable to inter-human agreement), but also documents systematic biases (position, verbosity, self-enhancement). G-Eval similarly reports meaningful correlation with humans and flags evaluator bias toward LLM-generated text. Net: LLM judge can scale, but it must be treated as *a measurement instrument requiring calibration*, not ground truth. citeturn9search0turn9search1turn8search5turn9search6

**Agent security is dominated by “instruction injection + excessive agency + cross-privilege chaining.”** OpenAI frames prompt injection as a long-term open challenge for agents, requiring layered safeguards and rapid adversarial discovery loops. AppOmni’s ServiceNow case study shows “second-order prompt injection” where a low-privileged agent causes a higher-privileged agent to take harmful actions due to default inter-agent discovery settings. For OpenClaw workflows with sub-agent spawning, this is directly relevant: autonomy level must be gated by risk and privilege boundaries, not by “confidence.” citeturn24view0turn13search15turn13search2

### Top recommendations

**Implement a two-loop evaluation system: (1) deterministic offline regression + (2) live monitoring with error budgets and canaries.** Run every prompt/tool/policy change through an offline suite built on stable fixtures and programmatic scoring; then deploy with canary routing and live alert thresholds to catch distribution shift and tool drift. Use SRE-style error budgets as the “stop-the-line” trigger when incident budgets are exceeded. citeturn14view0turn15view0turn11search1turn11search7turn17file0L1-L217

**Adopt a KPI tree where *success is defined as verified task outcomes + safe tool behavior*, not “better vibes.”** Your primary KPIs should be: task success rate (grounded in checks), safety violation rate (attempted + actual), execution reliability (tool errors/retries/timeouts), and cost/latency per successful outcome. Your internal policies already seed this direction (promotion gates, evidence schema, memory quality metrics, skills governance risk classes). fileciteturn17file0L1-L217 fileciteturn21file0L1-L227 fileciteturn22file0L1-L267

**Engineer “safe autonomy levels” into the runtime: ask-first defaults + approval cards + privilege segmentation for subagents and skills.** Use a decision matrix that maps action risk classes to: auto-act, ask-first (with structured approval cards), or block. Treat sub-agent spawning and third-party skills as capability multipliers that require explicit controls, evidence packs, and audit trails. fileciteturn23file0L1-L203 fileciteturn22file0L1-L267 citeturn24view0turn13search15

### Biggest risks if you do nothing

**You will ship regressions you can’t detect, explain, or roll back.** Without a stable offline suite + trace-level observability, you’ll only notice failures via operator frustration, while tool drift and “randomness” mask true causality. citeturn14view0turn12view0

**You increase the probability of a real security incident (exfiltration, destructive action, cross-agent privilege misuse).** Prompt injection and cross-agent chaining are not theoretical; both vendor and third-party security research show realistic failure paths and recommend layered controls plus supervisory gates. citeturn24view0turn13search15turn19view1

**You will optimize the wrong thing (Goodhart) and overfit to noisy metrics.** Public benchmarks demonstrate contamination and flawed test design, and LLM judges have measurable biases—both can create “illusory wins” unless you validate the measurement instrument and protect the eval set. citeturn6view0turn9search0turn9search6

## Evaluation system blueprint

### Architecture diagram described in text

A practical OpenClaw evaluation system is best viewed as **a dual-plane system**:

**Runtime plane (production-like runs)**
- **Task intake** (operator request, scheduled job, channel message)
- **Agent runtime**: model layer + memory layer + tool layer + channel layer (as described in OpenClaw’s architecture) citeturn18view0  
- **Tool execution sandbox** (file/shell/browser/web/skill/sub-agent calls)
- **Trace emission** (spans/events per step and per tool call)
- **Real-time guards** (policy checks, allowlists, approvals, spend caps, rate limits)
- **Outcome capture** (artifacts changed, external side effects, user acceptance, follow-up actions)

**Evaluation plane (offline + online scoring)**
- **Offline eval harness** (stable fixtures + deterministic scoring)
- **Online monitors** (dashboards + alerts + canary comparison)
- **Judging layer** (programmatic checks + calibrated rubric scoring + optional LLM judge)
- **Improvement loop** (task set curation, regression additions, policy/tool changes, promotion gates)

Your repository already sketches a “self-improvement loop v1” and promotion gates; the blueprint below formalizes it into a measurable system with explicit separation of offline vs live. fileciteturn17file0L1-L217

### Data flow from task to improvement loop

**Task → Run → Traces → Scoring → Dashboard → Improvement**

1. **Task definition**
   - task_id, task_type, risk_class, expected artifacts/outcomes, allowed tools/skills, autonomy level
   - for scheduled jobs: cadence class + minimum safe cadence (your cadence governance policy) fileciteturn27file0L1-L120

2. **Agent run**
   - the agent executes multi-step workflows with tools and persistent memory (OpenClaw supports multi-step workflows, tools, and persistence) citeturn18view0turn19view0
   - sub-agents may be spawned under explicit depth/concurrency/tool boundaries (your orchestration policy) fileciteturn23file0L1-L203

3. **Tool traces**
   - for each tool call: inputs, outputs (redacted), duration, retries, sandbox status, approval status, error taxonomy
   - emit traces using OpenTelemetry GenAI conventions as a baseline schema for LLM + tool spans, token usage, and operation timing citeturn12view0turn12view1

4. **Scoring & labeling**
   - **programmatic checks** (tests, diff checks, invariants, “no forbidden tools,” “approval required but missing,” etc.)
   - **rubric scoring** (human or calibrated judge) for quality dimensions not reducible to tests
   - **incident flags** (safety and reliability issues)

5. **Dashboards**
   - KPI tree rollups (quality/safety/reliability/cost)
   - drill-down: per task type, per tool, per skill, per autonomy mode, per model tier (your routing policy provides a natural stratification) fileciteturn24file0L1-L122

6. **Improvement loop**
   - weekly review selects 1–2 experiments (prompt/tool/policy changes) and defines expected KPI movement (your AI-native operating policy + retro-to-improvement rule) fileciteturn26file0L1-L210
   - successful changes are promoted after passing regression gates; failures become new regression tasks and/or new guardrails fileciteturn17file0L1-L217

### Separation of offline testing vs live monitoring

**Offline testing (high rigor, low noise)**
- run on **fixed fixtures**: pinned repos/files, recorded web pages (or snapshots), “simulated APIs,” deterministic seeds, controlled timeouts
- score with programmatic checks where possible (OSWorld/WebArena pattern) citeturn15view0turn17view0
- explicitly manage dependency instability (StableToolBench pattern: caching + simulators) citeturn14view0  
- produce a regression report and block promotion on defined failures

**Live monitoring (high realism, higher noise)**
- observe real tool drift, distribution shift, and security pressure
- use canaries: route a small % of runs to new configs, compare KPI deltas, rollback on threshold breaches
- treat safety and incident indicators as “stop-the-line” signals (error budgets + postmortem triggers) citeturn11search1turn11search7

## KPI framework

### KPI tree overview

A decision-oriented tree that avoids proxy traps:

**Level 0**
- **Quality** (did it solve the user’s task correctly and usefully?)
- **Safety** (did it avoid unsafe actions/data exposure and follow autonomy constraints?)
- **Execution reliability** (did it complete without stalls, tool failures, or non-deterministic thrash?)
- **Cost & time efficiency** (did it achieve success with acceptable latency and spend?)
- **Improvement velocity** (are changes making it better, measurably, without regressions?)

This aligns with: OpenClaw’s model/memory/tool/channel layers citeturn18view0 and your internal control system emphasis on audit trails, promotion gates, and measurable retrospectives. fileciteturn26file0L1-L210

### Hierarchical KPI tree with definitions and formulas

| KPI | Definition | Formula (suggested) | Leading / lagging |
|---|---|---|---|
| **Task success rate** | % of runs that meet acceptance checks (or human “accept”) | successes / total_runs | Lagging (primary) |
| **Verified correctness rate** | % runs passing programmatic checks (tests, invariants) | passes / eligible_runs | Lagging |
| **Quality rubric score** | Composite quality score (clarity, completeness, grounding, actionability) | avg(rubric_points) | Lagging |
| **First-pass acceptance** | % outputs accepted without rework | accepted_first_try / total_runs | Leading+lagging |
| **Safety violation rate** | % runs with a policy/tool violation (attempted or actual) | violations / total_runs | Lagging (critical) |
| **High-risk action without approval** | Count of actions requiring approval that executed without it | Σ(approval_required ∧ executed_without_approval) | Leading (critical) |
| **Data leakage indicators** | Any sensitive data in outbound channels/tool payloads | leakage_flags / total_runs | Leading (critical) |
| **Tool success rate** | % tool calls that return success | tool_ok / tool_calls | Leading |
| **Retry rate** | Mean retries per run | total_retries / total_runs | Leading |
| **Stall episodes** | Runs that exceed step/time budget or enter unresolved waiting | stalls / total_runs | Leading+lagging |
| **p50/p95 end-to-end latency** | Human-perceived completion time | percentile(runtime_seconds) | Lagging |
| **Token cost per success** | LLM tokens or $ per successful run | total_cost / successes | Leading (optimization) |
| **Tool cost per success** | External tool/API costs per success | tool_cost / successes | Leading |
| **Human time per success** | Operator minutes per successful outcome | operator_minutes / successes | Lagging (ROI) |
| **Regression escape rate** | Issues found in prod that should’ve been caught by offline suite | prod_regressions / releases | Lagging |
| **Measurement coverage** | % task types with stable programmatic checks | covered_task_types / total_task_types | Leading |

Key internal mappings you can wire in immediately:
- Model tier stratification (Tier 1/2/3 routing) for cost-quality trade-offs fileciteturn24file0L1-L122  
- Waiting/approval KPIs and blocker contract compliance from orchestration policy fileciteturn23file0L1-L203  
- Memory quality metrics (precision@k, leakage rate, write-back success) from memory kernel policy fileciteturn21file0L1-L227

### Suggested targets and alert thresholds

Targets should be **baseline-relative** for the first 2–4 weeks, then converted into absolute SLOs.

**Initial absolute “do no harm” thresholds (day 0)**
- Safety violations: **0 tolerated** for high-risk categories (destructive shell/file, outbound exfil, credential mishandling). citeturn19view1turn24view0turn13search15
- High-risk tool without approval: **0** (hard block + incident)
- Tool success rate: **≥ 98%** on core tools (file read, memory retrieval, non-network shell) in controlled environments
- Stall rate: **≤ 2%** (and each stall becomes a regression case)

**After baselining (week 2–4)**
- Task success rate: +5–10 pts over baseline on the eval suite, no statistically meaningful regression on any critical slice (by task type/risk class)
- p95 latency: no worse than +10–15% vs baseline unless quality increases justify it (explicit trade-off decision)
- Token cost per success: improve 10–20% over 60–90 days (after reliability stabilizes)

Use an “error budget” concept to control release velocity: as long as you remain within budgeted incident rates, you can ship; if you burn the budget, you pause promotion and invest in reliability. citeturn11search1turn11search14

### Trade-off notes that prevent metric gaming

**Quality vs latency:** OSWorld-Human shows that agent latency can blow up due to inefficient planning/reflection and excess steps—even when accuracy improves—so you should track *steps per success* and *planning tokens share* as first-class metrics. citeturn16view0

**Cost vs safety:** “Unbounded consumption” and runaway tool loops are common; treat rate limits, timeouts, and approval requirements as safety controls, not just cost controls (OpenClaw security guidance uses rate limiting/timeouts as part of defense-in-depth). citeturn19view1

**Judge score vs reality:** LLM-as-judge can drift or be biased (self-preference, verbosity); require periodic human calibration and anti-bias procedures (randomization, pairwise swaps, rubric form-filling). citeturn9search0turn9search6turn8search5

## Measurement design

### Minimum viable eval suite

A 20–30 task suite should be **representative, tool-covered, and regression-friendly**, with a bias toward tasks you actually run. A practical composition:

**Writing & synthesis (6 tasks)**
- Create a client-ready memo from three provided documents (offline fixtures); score via rubric + citation correctness.
- Summarize a long thread into action items; check for required fields and “no invented facts.”
- Draft an SOP/runbook update in markdown with a required template; check section presence + style constraints.

**Planning & decision support (5 tasks)**
- Produce a plan with explicit milestones, dependencies, and risks; check structure + risk identification.
- Given a “work order” (WO), produce acceptance criteria + verification plan; verify template completeness (maps to your WO gating). fileciteturn26file0L1-L210

**Ops checks & governance sweeps (6 tasks)**
- Run a “safe” healthcheck workflow on a mocked environment (fixed outputs); check: correct tool usage + correct escalation.
- Detect and classify a stalled workflow; require blocker contract fields and an escalation plan (maps to blocker contract policy). fileciteturn23file0L1-L203
- Simulate a prompt injection attempt inside fetched content; verify the agent refuses, asks-first, or contains the blast radius (aligns with agent security threat). citeturn24view0turn19view1

**Coding support (6 tasks)**
- Make a constrained code change in a fixture repo and run unit tests; success = tests passing + no forbidden file changes.
- Refactor a function without behavior change; verify via golden tests + diff constraints.
- Diagnose a failing test from logs and propose minimal fix; verify patch touches only allowed files.

**Memory & context (4 tasks)**
- “Preference recall” task: retrieve a stored preference and apply it correctly.
- “Prior decision recall”: retrieve a decision artifact and apply it.
- “Stale memory trap”: ensure the agent does not use expired info (requires TTL/recency tags).
- “Isolation test”: ensure no cross-namespace leakage (your memory kernel sets target zero leakage). fileciteturn21file0L1-L227

This suite mirrors what real benchmarks do: OSWorld and WebArena explicitly include state setup and execution-based scripts to make evaluation reproducible. citeturn15view0turn17view0

### Scoring rubrics

Use a **two-layer scoring model**:

**Objective layer (preferred for gating)**
- pass/fail unit tests
- invariant checks (no forbidden tools, no writes outside allowlist, approval required but missing)
- artifact checks:
  - file diffs limited to allowed paths
  - required outputs present (sections/fields)
  - external side effects absent unless approved (emails, merges)

**Subjective layer (required for “quality”)**
- 0–4 scale across dimensions:
  - correctness/grounding (no hallucinated facts; cites sources when required)
  - completeness (covers acceptance criteria)
  - clarity/actionability (next steps, crisp decisions)
  - operational safety posture (asks-first appropriately; explicit assumptions)
  - efficiency (no unnecessary tool calls or thrashing)

For rubric evaluation at scale, you may use an LLM judge—but only as “instrumented judging,” following known mitigation patterns and calibrating against human ratings. citeturn9search0turn8search5turn9search6

### Inter-rater consistency and judge calibration

**Human rater protocol (minimal overhead)**
- Two raters for 20% of eval tasks each run (rotate), single rater for the rest.
- Weekly compute: Cohen’s kappa (categorical) or Krippendorff’s alpha (ordinal), but don’t over-engineer—use it as a drift detector.
- Calibrate with a small “anchor set” of 10 examples with agreed gold rubrics and common failure modes.

**LLM judge calibration safeguards**
- Use pairwise comparisons when possible (reduces scale drift vs raw scoring); randomize order to mitigate position bias. citeturn9search0turn9search1
- Use structured form-filling prompts (G-Eval paradigm) rather than freeform rating; log judge explanations for auditability. citeturn8search5
- Periodically test for self-preference bias by cross-model judging on the same set (documented as a real effect). citeturn9search6

### Regression policy: what blocks deployment

A practical blocking policy, consistent with your repo’s gate-based operating model and evidence requirements: fileciteturn26file0L1-L210

**Hard blocks (must not ship)**
- any high-risk action executed without required approval
- any data leakage signal (secrets/PII in outbound calls or logs)
- any increase in safety violation rate above baseline (even if quality improves)
- offline suite flakiness above a defined threshold (the eval itself must be stable before it can be a gate) citeturn14view0
- evidence schema mismatch between trace producer and dashboard/ingest (explicitly called out as a “no promotion” rule in orchestration policy) fileciteturn23file0L1-L203

**Soft blocks (ship only with explicit risk acceptance)**
- success rate regression > 2 pts on critical tasks
- p95 latency regression > 15% without offsetting success gains
- cost per success regression > 20% without explicit decision

**Governance:**
- every override requires a change artifact and rollback plan (your CA template supports this directly). fileciteturn26file0L1-L210

## Safety and governance layer

### Decision matrix for auto-act, ask-first, block

A workable matrix for a small team (single primary operator) is **risk-class × action-type**:

| Action category | Examples | Default autonomy | Notes / controls |
|---|---|---|---|
| Low-risk, reversible | read-only file access, cached web lookup, formatting, drafting | **Auto-act** | Must be within sandbox + rate limits; log all actions. citeturn19view1turn12view0 |
| Medium-risk, bounded | write to a draft file, open PR draft, internal notification | **Ask-first** | Use “approval card” with what/why/risk/rollback + expires_at (your orchestration standard). fileciteturn23file0L1-L203 |
| High-risk, destructive or external | shell commands that modify system state, send emails, merge PR, bulk deletes, add integrations | **Block by default** (or ask-first with explicit allowlist) | Map to skills governance action gates; require evidence pack/sign-off. fileciteturn22file0L1-L267 |
| Capability-expanding | install new skill, enable a skill in prod, add MCP server, spawn privileged sub-agent | **Block / gated** | Treat as security boundary change; require owner approval + audit trail. fileciteturn22file0L1-L267 citeturn13search15 |

This matches OpenClaw’s own “least privilege + defense in depth + secure by default” posture (dangerous tools disabled until enabled; audit logging; rate limits; sandbox isolation). citeturn19view1

### High-risk action categories and required controls

Use your existing skills governance classes (S0–S3) as the enforcement mechanism. fileciteturn22file0L1-L267

**High ROI controls (small team)**
- **Approval gates** for any external side effect (send email, merge, release, bulk write/delete, add tool integration). fileciteturn22file0L1-L267
- **Sandbox mandatory** for S2/S3 skills + strict allowlists (network domains, file paths). fileciteturn22file0L1-L267
- **Privilege segmentation for sub-agents**: default leaf workers cannot manage spawning or access high-risk tools; cap depth and concurrency. fileciteturn23file0L1-L203
- **Prompt injection resilience loop**: add a “red team task pack” to offline evals; treat successful injections as regressions (mirrors OpenAI’s rapid response loop mindset). citeturn24view0turn13search15
- **Stall control & blocker contracts**: “blocked tasks must have unblock metadata,” preventing silent failure and keeping the system moving. fileciteturn23file0L1-L203

### Audit logging requirements and review cadence

Minimum viable audit trail should support reconstruction: intent → execution → evidence → decision—exactly as your operating policy states. fileciteturn26file0L1-L210

**Audit log schema (minimum)**
- run_id, task_id, agent_id, model_id/tier, policy_version, tool_allowlist hash
- per step: timestamp, action type, tool name, inputs (redacted), outputs (redacted), duration, retries, sandbox id, approval status
- artifacts: files changed (paths + diffs), external calls (domains/endpoints), sub-agent lineage (parent/child ids)
- “decision events”: approvals granted/edited/rejected with approval_id and expires_at (approval card standard). fileciteturn23file0L1-L203
- retention policy + access controls (NIST AI RMF GenAI profile emphasizes lifecycle governance and risk management; use it as the overarching framework for “govern/map/measure/manage”). citeturn10search0turn10search1

**Cadence**
- weekly: metrics review + top incidents + regression additions (aligns with your cadence governance and weekly governance checklists). fileciteturn27file0L1-L120
- monthly: model routing review (value vs cost), memory quality review, skill re-review schedule fileciteturn24file0L1-L122 fileciteturn21file0L1-L227

## Implementation roadmap

### First 30 days

**Milestones**
- Implement trace schema and logging for every tool call + run outcome (OpenTelemetry GenAI conventions as baseline). citeturn12view0turn12view1
- Stand up “MVE” (minimum viable eval) suite: 20 tasks, with at least 8 programmatic checks (file diffs, test passes, tool allowlist compliance).
- Establish hard safety blocks:
  - approval required → cannot execute without approval card
  - strict allowlists for shell/file/network for production-like runs (OpenClaw security posture) citeturn19view1
- Capture baseline metrics for 2 weeks and create first dashboard.

**Owner roles (one-person mapped)**
- AI Ops lead (you): instrumentation, dashboards, eval suite
- Safety reviewer (you wearing a different hat): approval gates and high-risk allowlists
- “Data steward” (again you): memory and log retention decisions (use NIST AI RMF as policy reference) citeturn10search0

**Tooling options**
- Lightweight: JSONL traces + SQLite/postgres + simple Grafana dashboard (or even markdown weekly report) → upgrade later
- Scalable later: OpenTelemetry Collector → trace store (Tempo/Jaeger) + metrics (Prometheus) + logs (Loki)

### Next 60 days

**Milestones**
- Expand eval suite to 30 tasks; add 5 prompt-injection / misuse simulations (inspired by real agent security cases). citeturn24view0turn13search15
- Add calibrated rubric scoring:
  - build anchor set, compute rater agreement weekly
  - introduce LLM judge only after calibration and bias checks (LMSYS + G-Eval guidance). citeturn9search0turn8search5turn9search6
- Introduce canary deployments:
  - small % of runs to “challenger” prompt/policy/tool config
  - rollback automation on safety or reliability thresholds
- Memory evaluation harness:
  - implement the “memory-critical prompt set”
  - measure precision@k, leakage rate, and write-back success (your memory kernel policy already defines these). fileciteturn21file0L1-L227

### Next 90 days

**Milestones**
- Promotion gates integrated into CI:
  - “no merge without passing offline suite”
  - evidence pack required for new/changed skills (S2/S3) fileciteturn22file0L1-L267
- Add error-budget controls:
  - if incident budget burned, pause new feature starts and invest in resilience (Google SRE model). citeturn11search1turn11search14
- Implement “efficiency KPIs” beyond raw latency:
  - steps per success, tool calls per success, planning-token share (OSWorld-Human points to planning/reflection overhead as a driver). citeturn16view0
- Operationalize a monthly “measurement integrity” review:
  - flakiness audits, contamination checks, judge drift checks (motivated by SWE-bench contamination lessons). citeturn6view0

## Practical artifacts

### Example scorecard template

**Run Scorecard (per task_id / per release candidate)**  
- Metadata: run_id, task_id, task_type, risk_class, model_tier, policy_version, tool_allowlist version  
- Outcome:
  - Task success: Yes/No (programmatic check)
  - Quality rubric: 0–4 per dimension (correctness, completeness, clarity, safety posture, efficiency)
  - Safety: violations (attempted/actual), approvals used, blocked actions
- Execution:
  - tool_calls count, tool_success %, retries, stall flags
  - latency p50/p95 slice (if batch), steps per run
- Cost:
  - tokens_in/out, $ estimate, tool/API costs
- Notes:
  - failure mode label (taxonomy below)
  - regression added? (Y/N)
  - follow-up WO/CA link (ties to your operating policy artifacts) fileciteturn26file0L1-L210

### Example incident taxonomy

A compact taxonomy that maps to mitigation levers:

| Category | Subtype | Typical signal | Default severity |
|---|---|---|---|
| Safety | prompt injection / instruction hijack | follows untrusted instructions; attempts forbidden action | Sev 1 |
| Safety | data exfiltration | sensitive strings in outbound payloads/logs | Sev 1 |
| Autonomy | approval bypass | action executed without required approval | Sev 1 |
| Reliability | tool failure | persistent 4xx/5xx, auth failures, timeouts | Sev 2 |
| Reliability | stall / thrash | step budget exceeded, repeated loops | Sev 2 |
| Quality | hallucination / ungrounded claim | contradicts provided sources/fixtures | Sev 2–3 |
| Memory | stale memory | uses expired info; wrong recall | Sev 2–3 |
| Memory | namespace leakage | cross-namespace retrieval/write | Sev 1 (per your target “zero leakage”) fileciteturn21file0L1-L227 |

### Example weekly review ritual agenda

A 45-minute agenda consistent with your governance patterns (WO/CA gating, cadence governance, retro-to-improvement). fileciteturn26file0L1-L210 fileciteturn27file0L1-L120

1. KPI snapshot (10 min): success, safety, tool reliability, cost per success, latency, stalls
2. Incidents (10 min): top 3, with “what changed” and “why it escaped”
3. Eval suite health (10 min): flakiness, coverage gaps, new regressions added
4. Canary results (5 min): challenger vs champion deltas
5. Decisions (10 min):
   - ship/hold decision
   - pick max 1–2 improvement experiments with explicit success metrics and rollback plan

### Definition of Done for eval maturity level 1

Level 1 is “measurable improvement loops” (your stated need), not “perfect measurement.”

**DoD (Level 1)**
- A 20-task offline eval suite exists; ≥8 tasks have deterministic programmatic scoring. citeturn15view0turn17view0
- All runs emit trace events for tool calls (inputs/outputs redacted), latency, retries, and approvals; dashboards exist for core KPIs. citeturn12view0
- Hard safety blocks implemented: approvals required for high-risk actions; forbidden tool calls cannot execute. fileciteturn22file0L1-L267
- A weekly review ritual runs, and at least one regression case is added per week from real incidents.
- A basic canary mechanism exists for config changes with rollback thresholds.
- Memory eval includes at least: preference recall, stale-memory trap, and namespace leakage test. fileciteturn21file0L1-L227

## Source quality appendix

### Primary empirical evidence and standards

- entity["company","OpenAI","ai research company"]: SWE-bench Verified contamination analysis (test flaws + training exposure) and the resulting recommendation shift. Evidence: empirical audits and contamination rationale. citeturn6view0  
- entity["organization","National Institute of Standards and Technology","us standards agency"]: AI RMF 1.0 and Generative AI Profile—governance-oriented risk management guidance. Evidence: standards/framework documents. citeturn10search0turn10search1  
- entity["organization","OpenTelemetry","observability standards project"]: GenAI semantic conventions (token usage, operation duration, spans). Evidence: specification docs (implementation-facing). citeturn12view0turn12view1  
- StableToolBench (ACL Anthology): stable benchmarking through virtual API server + caching + simulators; LLM evaluator used to reduce randomness. Evidence: peer-reviewed publication abstract and methodology claims. citeturn14view0  
- OSWorld (NeurIPS 2024): real computer environment with execution-based evaluation scripts and human baseline metrics. Evidence: peer-reviewed abstract with quantitative results. citeturn15view0  
- WebArena: self-hostable environment with annotated programs to validate functional correctness. Evidence: benchmark description + evaluation approach. citeturn17view0  
- LMSYS MT-bench / Chatbot Arena: reported agreement rates and documented biases for LLM-as-judge. Evidence: methodology and reported agreement from primary LMSYS posts/dataset release. citeturn9search0turn9search1  
- G-Eval (EMNLP 2023; Microsoft Research page): quantitative correlation reported and bias concerns noted. Evidence: published results summary. entity["company","Microsoft","technology company"] citeturn8search5  

### Real-world security case studies

- entity["company","AppOmni","saas security company"] AO Labs: second-order prompt injection via agent-to-agent discovery and privilege context (design/config-driven risk). Evidence: practitioner-reported research with concrete threat model and mitigations. citeturn13search15  
- ServiceNow incident reporting (CyberScoop): configuration-driven abuse risk + vulnerability disclosure context. Evidence: security journalism grounded in disclosed CVE/reporting. entity["company","ServiceNow","enterprise software company"] citeturn13search2  
- OpenAI prompt injection hardening: automated red teaming + rapid response loop framing; acknowledges non-deterministic guarantees. Evidence: vendor security engineering description. citeturn24view0  

### Internal repository evidence used to tailor this framework

From your repo (decision-oriented operating system artifacts), treated as “local ground truth” for intended governance and operating practices:

- Self-improvement loop v1 (telemetry + eval + promotion gates). fileciteturn17file0L1-L217  
- Memory kernel v1 (tiered memory, write-back, namespace isolation, memory eval metrics). fileciteturn21file0L1-L227  
- Skills governance policy + evidence pack + YAML controls (risk classes, action gates, monitoring). fileciteturn22file0L1-L267  
- Continuous action orchestration v1 (blocker contracts, approval cards, sub-agent boundaries, evidence schema alignment). fileciteturn23file0L1-L203  
- AI-native operating policy v1 + WO/CA templates (audit trail chain; non-negotiable gates; R/Y/G thresholds). fileciteturn26file0L1-L210  
- Model routing policy v1 and FinOps-lite policy (cost governance and tiering). fileciteturn24file0L1-L122 fileciteturn25file0L1-L156  
- Cadence governance policy (cadence floors and downgrade approvals). fileciteturn27file0L1-L120  

### Uncertainty flags

- OpenClaw public documentation is treated as **product-intent evidence** (architecture description, memory model, security posture). It should be validated against actual runtime behavior (e.g., which tool calls are truly blocked by default; what is actually logged; how sandboxing is implemented) before using it as a compliance guarantee. citeturn18view0turn19view1turn19view0  
- LLM-as-judge “agreement” results generalize best to tasks similar to MT-bench/dialogue; for tool-using workflows, judge reliability depends heavily on whether you can reduce scoring to programmatic checks (recommended) and whether you can prevent the judge from being misled by superficially plausible narratives. citeturn9search0turn8search5turn14view0