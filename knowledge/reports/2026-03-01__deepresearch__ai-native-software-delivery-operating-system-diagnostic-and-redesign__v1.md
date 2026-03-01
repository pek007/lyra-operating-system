---
title: "AI-Native Software Delivery Operating System Diagnostic and Redesign"
date: 2026-03-01
source: deepresearch
ingest_from: "knowledge/inbox/external-analysis-dropzone/deep-research-report (18).md"
tags: [external-analysis, deepresearch]
decision_relevance: tbd
confidence: tbd
status: archived-source
---

# AI-Native Software Delivery Operating System Diagnostic and Redesign

## Evidence base, what I could verify, and what I could not

**Internal artifacts reviewed (primary evidence).** Your repos already contain a surprisingly complete “OS scaffold” for AI-heavy execution: an explicit Ways of Working, process registry with review cadence, intake/triage SOP, definition of done, model routing policy + scorecard (anti-thrash + champion/challenger), explicit multi-agent operating model (persistent Control Tower + spawned subagents + workbench lanes), and a PromptOps baseline with versioning + drift reviews. fileciteturn24file0L1-L132 fileciteturn22file0L1-L36 fileciteturn26file0L1-L64 fileciteturn28file0L1-L57 fileciteturn41file0L1-L103 fileciteturn40file0L1-L73 fileciteturn34file0L1-L61 fileciteturn36file0L1-L32 fileciteturn38file0L1-L19 fileciteturn52file0L1-L106 fileciteturn44file0L1-L104

**Direct evidence you are already running AI-native “sprints” with explicit supplier prompts.** A Control Panel commit contains a full Sprint 5 architecture brief plus an implementation prompt contract for your coding agent, with non-negotiable constraints, test requirements, documentation requirements, and acceptance criteria. This is already the shape of an AI-native delivery OS. fileciteturn67file0L1-L1

**External research used (for grounding “what top-tier looks like”).**  
- Software delivery performance measurement and its evolution (DORA now uses five delivery metrics grouped into throughput and instability). citeturn0search2  
- Organizational design for fast flow and cognitive load management (Team Topologies). citeturn0search0  
- Reliability governance via error budgets and SLOs as a mechanism to balance innovation and stability (Google SRE). citeturn1search6  
- Queueing/flow math (Little’s Law relation between WIP, throughput, and cycle time). citeturn1search49turn1search4  
- AI-agent security/operational failure modes (OWASP LLM Top 10; Claude Code security guidance; responsible-use constraints for Copilot code review/agenting). citeturn2search0turn2search10turn2search1turn2search3  
- Evidence that agentic coding benchmarks can be misleading and fragile (SWE-bench ecosystem analysis; benchmark leakage concerns). citeturn1search7turn1search1  

**Key verification limits (important).**  
- I can **see the process documentation**, templates, and sprint prompt contracts. fileciteturn22file0L1-L36 fileciteturn52file0L1-L106 fileciteturn67file0L1-L1  
- I cannot conclusively verify **day-to-day adherence** across all work because your work system is hybrid (tasks in a board tool; knowledge in Git), and the board history / actual runtime behavior is not fully observable here. fileciteturn31file0L1-L104 fileciteturn29file0L1-L41  
- Therefore: wherever I say “you are doing X,” it’s because the artifacts prove the policy exists; wherever I say “you’re likely doing Y,” it’s inference from your own stated pain points and the typical failure pattern in teams with good rituals but weak compounding.

## Executive diagnosis, strengths to preserve, critical gaps, and root causes

**Deliverable: Executive diagnosis (blunt).**  
You are not suffering from “no process.” You’re suffering from **process bifurcation**: you have a strong written OS (and even supplier-grade AI prompts), but your own stated symptoms (unstructured sprint starts, inconsistent prioritization/backlog discipline, uncertain retro-to-improvement conversion) are exactly what happens when (a) **work intake is not forced through a single gate every time**, (b) **trade-offs are not encoded as policy**, and (c) the system lacks **closed-loop verification** that the process is being followed and improving. fileciteturn26file0L1-L64 fileciteturn22file0L1-L36 fileciteturn67file0L1-L1

In an AI-agent-heavy environment, “rituals without compounding” is even more dangerous than in a human team because agents can generate high volumes of output quickly; the dominant failure mode becomes **verification debt**: lots of plausible artifacts, insufficient proof they’re correct, integrated, safe, and shipped. This risk is explicitly recognized in responsible-use guidance for AI coding/review tools (misses, hallucinations, insecure suggestions) and in LLM security taxonomies (overreliance, excessive agency, insecure output handling). citeturn2search1turn2search0turn2search3

**Deliverable: Current-state strengths to preserve.**  
You already have top-tier building blocks that many orgs never operationalize:

- **A real OS backbone**: canonical docs, a process registry with owners and review schedule, and explicit cadence. fileciteturn22file0L1-L36 fileciteturn24file0L1-L132  
- **Agent model clarity**: persistent Control Tower + spawned subagents + external workbench lane + explicit completion contract and escalation rules. fileciteturn34file0L1-L61 fileciteturn36file0L1-L32  
- **Governed model routing**: policy-driven routing tiers, fallback rules, and anti-thrash review cadence with a scorecard approach. fileciteturn41file0L1-L103 fileciteturn40file0L1-L73  
- **PromptOps intent**: prompts treated as interface contracts with semver and a drift review process. fileciteturn52file0L1-L106  
- **Supplier-grade sprint execution contracts** (a major maturity marker for AI-native teams): explicit tests required, constraints, acceptance criteria, and documentation requirements in the coding agent prompt. fileciteturn67file0L1-L1  

**Deliverable: Critical gaps and root causes.**  
The gaps are not “agile hygiene.” They’re **operating-system integrity gaps**—missing enforcement, missing feedback closure, and insufficient auditable linkage.

1) **Intake and prioritization are not forced through a single choke point**  
You have SOP-001 for intake/triage, but your own described reality says sprint starts can be top-of-mind driven. That mismatch usually isn’t because the SOP is wrong; it’s because the system lacks a **hard gate** (nothing starts without a work-order ID + acceptance criteria + lane + risk class). fileciteturn26file0L1-L64  

2) **Trade-offs are described, not compiled into policy**  
DORA emphasizes measuring throughput and stability; Google SRE formalizes “stop the line” behavior via error budgets. Without explicit policy, teams default to accidental trade-offs. citeturn0search2turn1search6  

3) **Audit trail exists in pieces (docs, prompts, commits) but is not end-to-end joined**  
You have a prompt changelog, definitions, and sprint briefs. What’s not yet evident is an enforced requirement that every change is traceable across: (intent → work order → prompts used → agent runs → code diff → tests → decision rationale → deployment/release → observed outcome). That “join” is the difference between “documented” and “auditable.” fileciteturn43file0L1-L25 fileciteturn67file0L1-L1  

4) **Learning loop exists but may not be closed**  
Your Ways of Working explicitly calls for measurable outcomes and cadence. fileciteturn24file0L1-L132  
Your concern is that retros are not reliably converted into measurable improvements. That is a classic missing mechanism: **retro actions must become work items with owners AND a validation metric**. Without that, retros devolve into narrative. (This is inference, but consistent with your stated concern.)

5) **AI-specific risk controls exist but are not yet fully “compiled” into delivery gates**  
You already define permission envelopes and escalation boundaries, which aligns with best practice: least privilege and controlled agency. fileciteturn38file0L1-L19  
But AI-native excellence requires additional gates around prompt injection, insecure tool use, and overreliance. These are now standard in OWASP’s LLM Top 10. citeturn2search0  

## Human best practices vs AI-agent reality, including topology and Keep/Modify/Remove/Add map

This section answers questions A1–A4 and sets up the redesign.

### What transfers directly from human teams

**Evidence-backed core:** The physics of delivery do not change because execution is AI-assisted. Flow, feedback, and reliability constraints still dominate outcomes.

- **Flow constraints & WIP discipline still rule.** If you increase WIP without increasing throughput, cycle time increases (Little’s Law). citeturn1search49turn1search4  
- **Measure delivery throughput and stability.** DORA’s metrics are explicitly built to compare performance across contexts; they remain valid even with AI execution. citeturn0search2  
- **Reliability needs explicit governance.** Error budgets are a concrete mechanism for balancing shipping speed with reliability; the concept is independent of who writes the code. citeturn1search6  
- **Organizational design must minimize cognitive load and enable fast flow.** Team Topologies’ emphasis on cognitive load and clear interaction modes remains relevant—AI doesn’t remove system complexity; it changes where it sits. citeturn0search0  

### What is overdone in human-first processes

**Expert inference:** Many “agile rituals” primarily mitigate human coordination limits (memory limits, meeting bandwidth, cross-team synchronization).

In AI-agent-heavy execution, you can safely reduce:
- **Meeting-heavy synchronization** (status meetings) if you have machine-readable work state and automatic reporting. Your OS is already aiming at “dashboard-lite metrics” and a single system of record. fileciteturn24file0L1-L132  
- **Over-specified story pointing** (especially in small teams): AI makes micro-estimation less valuable; what matters is risk class and verification requirements.

### What is missing because AI agents introduce new constraints/opportunities

**Evidence-backed risk categories and controls exist externally.** OWASP explicitly highlights prompt injection, insecure output handling, supply chain vulnerabilities, excessive agency, and overreliance. citeturn2search0  
Your own OS already anticipates some of these (permission envelopes; escalation; prompt governance), but top-tier requires hard gating and telemetry. fileciteturn38file0L1-L19 fileciteturn52file0L1-L106

Missing “AI-native” practices you should treat as first-class:
- **Prompt-to-change traceability** (prompt version + work-order ID embedded into PR/commit metadata).  
- **Determinism variance management** (repeatability budgets—when you require reproducible outputs vs acceptable variance).  
- **Agent tool orchestration contracts** (what tools are allowed, and how tool outputs are validated). fileciteturn36file0L1-L32  
- **Verification-as-a-product** (tests, checks, and independent review agents) to stop verification debt. Responsible-use docs explicitly warn AI may miss problems and produce insecure or incorrect code; the process must assume this. citeturn2search1turn2search3  

### Team topology when some “teammates” are specialized agents/models

**Deliverable: Topology, AI-native.**  
Use Team Topologies as the conceptual model, but implement it as **human+agent “team APIs”**.

- **Stream-aligned “delivery pod” = Human intent owner + Control Tower agent + Build agent(s)**  
  - Human owns priorities and trade-offs (decision rights).  
  - Control Tower owns coordination, context, audit trail. fileciteturn34file0L1-L61  
  - Build agents implement bounded changes under work-order contracts. fileciteturn56file0L1-L40  

- **Platform team (mostly agentic) = Tooling + CI/CD + golden paths**  
  - Purpose: reduce cognitive load by making the “right way” automatic (templates, scripts, checks). This matches Team Topologies’ platform function. citeturn0search0  

- **Enabling team = Review/QA/Security agents + periodic human architecture review**  
  - Purpose: help the stream pod go faster safely, via facilitation and guardrails, not by taking ownership of delivery.

- **Complicated-subsystem = only when necessary**  
  - In a small org, treat this as a temporary “expert lane” (deep-research or specialized coding model) rather than a permanent team.

## Target AI-native operating model, governance, documentation/audit architecture, PromptOps, agent utilization, metrics, dependency resilience, sprint/flow options, and implementation plan

This section contains the required deliverables and answers B–H.

### Deliverable: Human-best-practice vs AI-native adaptation map

Below is the blunt “Keep / Modify / Remove / Add” mapping. Each item includes **Impact / Effort / Confidence / Evidence level**.

**Keep**
- **Single system of record** for work + knowledge (you already chose Hybrid with explicit linking rules).  
  - Impact: H | Effort: M | Confidence: H | Evidence: Strong (your ADR + OS docs). fileciteturn31file0L1-L104 fileciteturn24file0L1-L132  
- **Definition of Done** as a gate, not a suggestion.  
  - Impact: H | Effort: L | Confidence: H | Evidence: Moderate→Strong (DORA + flow logic supports gating; you have DoD). fileciteturn28file0L1-L57 citeturn0search2  
- **Error-handling and graceful degradation** in runtime systems (especially for agent-built systems).  
  - Impact: H | Effort: M | Confidence: H | Evidence: Strong (SRE + your own sprint constraints explicitly require graceful failure). citeturn1search6 fileciteturn67file0L1-L1  

**Modify**
- **Sprint planning**: move from “calendar sprint rituals” to **work-order gating + flow control**, with timeboxed “replan windows.”  
  - Impact: H | Effort: M | Confidence: M | Evidence: Moderate (flow theory; Little’s Law). citeturn1search49turn1search4  
- **Code review**: shift from human-only review to **multi-layer verification**: static checks + tests + AI review agent + selected human review for risk class.  
  - Impact: H | Effort: M | Confidence: H | Evidence: Strong (Copilot responsible-use warns of missed issues/hallucinations; therefore review must be layered). citeturn2search1turn2search3  
- **Retros**: convert from discussion to **measured experiments** (retro items must include a metric + expiry date).  
  - Impact: H | Effort: M | Confidence: M | Evidence: Moderate (Lean/flow logic; inference given your symptom).

**Remove**
- **Ritualized estimation** that doesn’t change decisions (detailed story points). Replace with **risk class + verification class**.  
  - Impact: M | Effort: L | Confidence: M | Evidence: Weak→Moderate (mostly experiential; not heavily evidenced in primary research).  
- **Manual status reporting** if your work system and evidence pipeline can generate it automatically.  
  - Impact: M | Effort: L | Confidence: M | Evidence: Moderate (fits your OS direction). fileciteturn24file0L1-L132  

**Add**
- **Work Orders (WO) as the universal execution contract** (human intent → agent execution). You already have WO templates; make them mandatory and attach them to every meaningful change. fileciteturn48file0L1-L34 fileciteturn50file0L1-L34  
  - Impact: H | Effort: M | Confidence: H | Evidence: Strong (your repo proves the structure exists; AI tool guidance implies need). fileciteturn56file0L1-L40 citeturn2search1turn2search0  
- **Prompt-to-change provenance**: prompt semver + hash + model/lane stored in PR metadata and in a machine-readable change log.  
  - Impact: H | Effort: M | Confidence: M | Evidence: Moderate (needed for auditability; thin formal research, but consistent with your PromptOps intent). fileciteturn52file0L1-L106  
- **AI security gates** aligned to OWASP LLM Top 10 (prompt injection, excessive agency, insecure output handling, supply chain risk).  
  - Impact: H | Effort: M | Confidence: H | Evidence: Strong. citeturn2search0turn2search10  
- **Verification debt metric** (defined below) and an explicit policy: “No new scope while verification debt is above threshold.”  
  - Impact: H | Effort: M | Confidence: M | Evidence: Moderate (SRE-style stop-the-line logic; inferred application). citeturn1search6  

### Deliverable: Target AI-native operating model (end-to-end workflow)

This is the practical OS that your current artifacts are *almost* implementing. The redesign is: **compile the OS into hard gates and telemetry**.

**Strategy alignment**
- **Quarterly intent**: define 3–5 outcomes (not features) with explicit “kill criteria.”  
- **Monthly focus**: choose “Now / Next / Watch” as *portfolio states* (not UI tabs), tied to outcomes and error budget status. (This mirrors your Control Panel IA consolidation intent.) fileciteturn67file0L1-L1  

**Work intake and prioritization**
- All incoming work enters **Inbox** and is triaged daily (keep SOP-001). fileciteturn26file0L1-L64  
- **Hard gate:** nothing becomes “Active” without:
  1) Work Order ID  
  2) Lane (Build / Research / Ops / Security)  
  3) Risk class (Type 1 / Type 2 decision; or P1–P4)  
  4) Acceptance criteria  
  5) Verification plan (tests/checks required)  
  6) Dependency declaration (tools/models/3PPs touched)

**Planning quality**
- Replace “Sprint starts are unstructured” with:  
  - Weekly: select a bounded batch of WOs with explicit WIP limits per lane (Build lane WIP ≤ 1–2 concurrent WOs per agent). This is queueing/flow discipline. citeturn1search49turn1search4  
  - Any item not ready as a WO remains in Triage.

**Execution flow efficiency**
- Use your agent execution semantics: spawned subagents by default; persistent only where global context is required. fileciteturn36file0L1-L32  
- Every agent run must output the completion contract (outcome, artifacts changed, risks, next actions). fileciteturn36file0L1-L32  
- For coding: require Plan → Execute → Verify phases (your Prompting OS already states this). fileciteturn52file0L1-L106  

**Technical quality assurance**
- Treat AI code as “unsafe until proven.” This follows directly from responsible-use guidance (AI may miss issues, hallucinate, suggest insecure code). citeturn2search1turn2search3  
- Minimum QA stack per change:
  - Automated tests (unit/integration)  
  - Static analysis / lint  
  - Dependency/supply-chain scan (where relevant)  
  - AI review agent pass  
  - Human review required only for high-risk classes (security-sensitive, architecture changes)

**Release**
- DORA metrics remain your outcome verification layer for delivery health; your process should make them easy to collect (see Metrics system). citeturn0search2  
- Add an SRE-style rule: if stability is degrading (failed deployment recovery time rising, change fail rate rising), shipping throughput must slow until stability recovers. citeturn1search6turn0search2  

**Learning**
- Retros become a pipeline: Observation → Hypothesis → Experiment → Metric → Decision.  
- A retro item is not “done” until the validation metric moved (or you explicitly falsified the hypothesis).

### Deliverable: Governance model (decision rights, escalation, exceptions)

You already use the language of decision owner and escalation. fileciteturn24file0L1-L132 fileciteturn26file0L1-L64 fileciteturn67file0L1-L1  
Make governance explicit per work type:

**Decision rights**
- **Peter (human)**: priority, scope trade-offs, model/provider spend, any external commitments, any Type 1 decision. (Type 1 = high irreversibility / high downside.)  
- **Control Tower (Lyra)**: orchestration, enforcing gates, maintaining audit trail artifacts, routing tasks to lanes, approving MINOR/PATCH prompt changes (per your PromptOps policy). fileciteturn52file0L1-L106  
- **Build Agent(s)**: execution within approved plan; stop and escalate on blocker/deviation. fileciteturn50file0L1-L34  

**Escalation paths (hard triggers)**
- Any security/compliance uncertainty (per SOP-001). fileciteturn26file0L1-L64  
- Any prompt/tool behavior that suggests prompt injection or unsafe agency. citeturn2search0turn2search10  
- Any attempt to expand scope beyond WO constraints. fileciteturn50file0L1-L34  

**Exception handling**
- Exceptions are allowed, but must produce an **Exception Record**: why, what was bypassed, what compensating control was used, and what follow-up task closes the gap. (Without this, exceptions become the real process.)

### Deliverable: Documentation + audit trail architecture

You already have the “docs as code” substrate and a process registry listing core artifacts. fileciteturn22file0L1-L36 fileciteturn24file0L1-L132

**What must be documented (minimum viable, enforceable):**
- **Work Orders**: intent, scope/non-goals, acceptance criteria, risk class, dependencies, verification plan.  
- **Decision records (ADRs/DDAs)** for Type 1 decisions and architecture changes. fileciteturn58file0L1-L19  
- **Change Artifacts (CA)** for any code/config change: plan vs actual, tests run, rollback, follow-ups. fileciteturn60file0L1-L29  
- **Prompt versioning evidence**: prompt template version, lane, and changelog entry when templates move. fileciteturn43file0L1-L25 fileciteturn52file0L1-L106  
- **Run evidence** for jobs/automation (durations, success/failure). Your Sprint 5 prompt is already demanding this shape for materialized summaries. fileciteturn67file0L1-L1  

**Where and at what fidelity**
- Canonical store: Git repo knowledge base (high fidelity; version controlled). fileciteturn31file0L1-L104  
- Work board: lightweight, but must contain IDs and links (low fidelity + pointers). fileciteturn31file0L1-L104  

**Audit trail joins (the missing piece)**
- Every WO must carry:  
  - `WO-ID`  
  - `PromptTemplate@semver`  
  - `ModelLane` (ops/research/build/premium)  
  - `AgentRole`  
  - `EvidenceRefs` (CA/DDA links)  
- Every commit/PR must include the WO-ID.  
This is the difference between “we have docs” and “we can reconstruct why this exists.”

### Deliverable: PromptOps standard (templates, QC, experiment logging, versioning)

You already implemented most of this in PROMPTING_OS_V1 plus templates for Plan/Execute and research/public and handoff artifacts. fileciteturn52file0L1-L106 fileciteturn48file0L1-L34 fileciteturn50file0L1-L34 fileciteturn54file0L1-L32 fileciteturn56file0L1-L34 fileciteturn58file0L1-L19 fileciteturn60file0L1-L29

What makes it “top-tier” is enforcement + validation sets:

**Mandatory prompt QC (gate)**
- Your checklist is correct; make it a preflight gate (no run without passing). fileciteturn52file0L1-L106  

**Prompt experiment logging**
- Add a single machine-readable log line per run:  
  - prompt template + version  
  - model + provider  
  - cost estimate  
  - time to first usable output  
  - rework required (Y/N)  
  - constraint violations (Y/N)  
  This allows a champion/challenger loop for prompts, not only models.

**Security alignment**
- Add explicit defenses for OWASP risks (prompt injection, insecure output handling, excessive agency) into each lane template. citeturn2search0  
- Take advantage of vendor security boundaries where available (Claude Code’s permission model and safeguards) but do not rely on them alone. citeturn2search10  

### Deliverable: Agent utilization model (autonomy vs constraint, anti-micromanagement)

You already have permission envelopes by role (least privilege boundaries). fileciteturn38file0L1-L19  
Top-tier usage is about **where to be strict** and **where to get out of the agent’s way**.

**Grant autonomy when**
- The task is **bounded**, has **clear acceptance criteria**, and verification is cheap (e.g., refactors with tests; codegen with strong lint/test harness).  
- The agent is operating within a “golden path” (scaffolded project structure, known scripts, known tools).

**Constrain when**
- High downside risk, ambiguous requirements, or weak tests (this matches your Type 1 / premium lane thinking). fileciteturn34file0L1-L61 fileciteturn41file0L1-L103  
- Any action that touches credentials, deployments, billing, or external messaging. (Aligns with OWASP “excessive agency” risk.) citeturn2search0  

**Anti-micromanagement rules (practical)**
- Humans should not tell the agent *how to type*; humans must specify:
  - objective  
  - constraints  
  - acceptance criteria  
  - verification evidence required  
  That is exactly what your WO templates enforce. fileciteturn48file0L1-L34 fileciteturn50file0L1-L34  

### Deliverable: Metrics system (leading/lagging, formulas, collection, targets)

This must combine DORA + flow + AI-native leading indicators.

**Lagging indicators (outcome health)**
1) **Software delivery throughput and instability (DORA 5-metric model)**  
   DORA now groups into throughput (lead time, deploy frequency, failed deployment recovery time) and instability (change fail rate, deployment rework rate). citeturn0search2  
   - Collection: CI/CD + deployment logs + incident tags + hotfix labels.  
   - Target bands (contextual): aim for trend improvement; absolute “elite” thresholds are informative but not the point—your process must move them.

2) **Reliability governance: Error budget burn**  
   - Error Budget = 1 − SLO (over window); release velocity depends on remaining budget. citeturn1search6  
   - Alert threshold: budget burn > planned trajectory → suspend feature WOs and shift to reliability WOs.

**Leading indicators (process integrity and compounding)**
1) **WIP and cycle time (flow control)**  
   - Little’s Law: WIP = Throughput × Cycle Time. citeturn1search49turn1search4  
   - Targets: keep Build lane WIP low (≤ 1–2 per executor) to minimize cycle time variance.

2) **First-pass acceptance rate (by lane and agent)**  
   - Definition: % of WO outputs accepted without major rework.  
   - Targets:  
     - Research lane ≥ 70% first-pass usable  
     - Build lane ≥ 60% with strong tests (raise over time)

3) **Verification debt (AI-native critical)**  
   - Definition: count of “merged/shipped changes lacking required evidence” (missing tests, missing CA artifact, missing WO link, missing security scan).  
   - Policy: if verification debt > threshold (e.g., > 2), freeze new feature WOs until cleared.

4) **Constraint violation rate**  
   - Definition: agent attempted forbidden tool/action or violated prompt contract.  
   - Target: trending down; any spike triggers prompt drift review. fileciteturn52file0L1-L106  

5) **Model routing stability**  
   - Your scorecard already defines anti-thrash and promotion rule. fileciteturn40file0L1-L73  
   - Metric: # of routing changes/month; threshold: >1 triggers governance review.

### Deliverable: 3PP dependency analysis (map, risk scoring, fallback, continuity)

You already acknowledge multi-provider reality and fallback lanes in your model routing policy. fileciteturn41file0L1-L103  
Top-tier means: explicitly classifying dependencies and designing an “internal minimum viable mode.”

**Dependency categories**
- **Model providers** (e.g., entity["company","OpenAI","ai model provider"], entity["company","Anthropic","ai model provider"]) as execution substrate. fileciteturn41file0L1-L103  
- **Tooling** (e.g., entity["company","GitHub","code hosting platform"]) for code, issues, CI.  
- **External data/search** sources (e.g., your mention of Brave usage baselines in tasks). fileciteturn29file0L1-L41  

**Single points of failure**
- Any lane whose execution relies on a single provider/model/tool with no fallback, especially for the Build lane.

**Minimum viable internal operating mode**
- “Continue degraded” mode should include:
  - local knowledge access (repo)  
  - local task management (exported board snapshot)  
  - at least one fallback model lane (cloud secondary or local utility model) for triage, summarization, and low-risk work. Your policy explicitly anticipates a local fallback lane. fileciteturn41file0L1-L103  

### Deliverable: Sprint/flow optimization recommendation + three alternative models with decision matrix

You asked explicitly: fixed sprints, flow-based, or hybrid.

**Reality check grounded in AI-agent constraints (evidence + inference).** Agentic benchmarks show performance can be overstated and fragile; capabilities vary by task distribution and evaluation setup. Do not design your OS around “agents can do everything”; design around “agents are fast but not reliably correct.” citeturn1search7turn1search1  
Therefore, your cadence should optimize for **verification throughput** and **fast feedback**, not for maximum parallel coding.

**Operating model options**

**Option 1: Sprint-centric (fixed cadence, scope freeze)**
- Best when: product roadmap needs synchronized demos, external stakeholders, batch releases.  
- Risk in AI-heavy execution: encourages batching → higher verification debt and larger diffs.

**Option 2: Flow-centric (continuous delivery with WIP limits)**
- Best when: you can ship in small increments and measure quickly; strong automated verification exists.  
- Risk: without governance, “continuous” becomes “random.”

**Option 3: Hybrid (flow execution + cadence for governance) — recommended for your maturity stage**
- Execution is flow-based with WIP limits; governance runs on a weekly/monthly cadence:
  - Weekly: portfolio rebalancing + WIP setting + metrics review  
  - Monthly: retro + prompt drift review + model routing review  
This matches your existing cadence intent and anti-thrash review logic. fileciteturn24file0L1-L132 fileciteturn40file0L1-L73 fileciteturn52file0L1-L106

**Decision matrix (blunt)**

| Criterion | Sprint-centric | Flow-centric | Hybrid (recommended now) |
|---|---:|---:|---:|
| Controls WIP and cycle time variance (Little’s Law) citeturn1search49turn1search4 | M | H | H |
| Minimizes verification debt risk | M | H (if strong gates) | H |
| Works with variable model reliability | M | H | H |
| Easy to enforce with limited management bandwidth | M | M | H |
| Supports clear auditability | M | H | H |
| Supports regular strategic rebalancing | H | M | H |

**Recommendation: Hybrid for the next 90 days.**  
You already act like a hybrid system: you run “sprints” with supplier briefs, but you also maintain a Kanban-style task system and daily/weekly cadence. fileciteturn29file0L1-L41 fileciteturn67file0L1-L1

**“What would need to be true” to switch later**
- Switch to **Flow-centric** when:
  - automated test + verification coverage is strong enough that most changes can be shipped continuously with low human review load  
  - verification debt stays near zero for multiple weeks  
  - deployment/release is cheap and frequent (DORA metrics improving). citeturn0search2  
- Switch to **Sprint-centric** when:
  - you have larger cross-functional stakeholder synchronization needs and can tolerate batching with strong release gates (error budget + strict verification). citeturn1search6turn0search2  

### Deliverable: 30/60/90-day implementation roadmap

**30 days (stabilize execution integrity)**
- Implement the hard gate: no “Active” work without WO fields + verification plan (compile SOP-001 into enforcement). fileciteturn26file0L1-L64  
- Add mandatory CA artifact for every code change (even tiny changes). fileciteturn60file0L1-L29  
- Add WO-ID stitching into commits/PRs and prompt logs (minimum viable provenance).

Impact: H | Effort: M | Confidence: H | Evidence: Moderate–Strong (flow + audit principles; your own artifacts already exist). citeturn1search49turn1search4

**60 days (close the learning loop)**
- Convert retros into experiment backlog with “metric + owner + expiry.”  
- Implement verification debt metric and policy freeze thresholds.  
- Start champion/challenger not only for models (already defined) but for prompts (prompt drift review becomes measurable). fileciteturn40file0L1-L73 fileciteturn52file0L1-L106

Impact: H | Effort: M | Confidence: M | Evidence: Moderate.

**90 days (resilience + top-tier measurement)**
- Implement an SRE-style error budget gate over your core surfaces (especially if Control Panel is an operational tool). citeturn1search6  
- Expand 3PP continuity mode: documented fallback provider/model and periodic failover drills (tabletop).  
- Baseline DORA metrics collection and begin trend tracking. citeturn0search2  

Impact: H | Effort: H | Confidence: M | Evidence: Strong for error budgets + DORA; moderate for AI-specific failover design.

### Deliverable: Top 10 failure modes + preventive controls

1) **Verification debt explosion** (fast output, slow proof)  
   - Control: verification evidence gates + verification debt metric + freeze policy. citeturn2search1turn2search3  

2) **Prompt injection / poisoned context**  
   - Control: input sanitization, least privilege, don’t allow agents to execute untrusted instructions; align to OWASP LLM01. citeturn2search0turn2search10  

3) **Excessive agency (agent takes irreversible actions)**  
   - Control: permission envelopes + approval gates + “no external send” default. fileciteturn38file0L1-L19 citeturn2search0  

4) **Model thrash (constant switching, unstable baseline)**  
   - Control: monthly anti-thrash rule; champion/challenger. fileciteturn40file0L1-L73  

5) **Silent stale data after adding materialization jobs**  
   - Control: freshness metadata, last-run status, stale warnings (you already require this in Sprint 5). fileciteturn67file0L1-L1  

6) **Large batch merges because AI makes it easy**  
   - Control: WIP limits + small-diff policy; flow metrics. citeturn1search49turn1search4  

7) **Security regression via plausible AI code**  
   - Control: layered review + automated security checks; OWASP insecure output handling guidance. citeturn2search0turn2search1  

8) **Auditability gaps (can’t reconstruct why/what)**  
   - Control: WO/CA/DDA linking discipline with mandatory IDs. fileciteturn58file0L1-L19 fileciteturn60file0L1-L29  

9) **Unstructured sprint starts (priority drift)**  
   - Control: hard intake gate + weekly WIP setting + explicit “stop starting, start finishing.” citeturn1search49turn1search4  

10) **Benchmarks mislead capability assumptions**  
   - Control: your own evaluation set for prompts/models, because public benchmarks can be leaky or not representative. citeturn1search7turn1search1  

### Deliverable: First 14 days exact action plan (owners, artifacts, measurable outcomes)

Day-by-day, minimal management bandwidth, maximum enforcement.

**Day 1–2 (Owner: Peter + Control Tower)**
- Ratify a single “WO required fields” schema and make it the only route into Active.  
  - Artifact: `WO_SCHEMA_V1.md` (or embed into existing SOP).  
  - Outcome metric: 100% of Active items have WO fields.

**Day 3–4 (Owner: Control Tower)**
- Implement commit/PR convention: every change references `WO-ID`.  
  - Artifact: `CONTRIBUTING_AI_NATIVE.md` (or equivalent) plus lint/check that fails if missing.  
  - Outcome metric: 0 merges without WO-ID.

**Day 5–6 (Owner: Build lane)**
- Make Change Artifact mandatory for any merge.  
  - Artifact: CA template already exists; enforce it. fileciteturn60file0L1-L29  
  - Outcome metric: 100% merges have CA link + tests-run evidence.

**Day 7 (Owner: Peter)**
- Define “work type policy” for trade-offs: exploration vs feature dev vs refactor vs bugfix vs incident.  
  - Artifact: `TRADEOFF_POLICY_V1.md`  
  - Outcome: each WO specifies work type and default trade-off profile.

**Day 8–10 (Owner: Control Tower + Security/Audit lane)**
- Add OWASP-aligned security checklists into prompt templates as a required section for high-risk WOs. citeturn2search0  
  - Outcome metric: 0 high-risk WOs executed without security checklist completion.

**Day 11–12 (Owner: Control Tower)**
- Start metrics capture: WIP, cycle time, first-pass acceptance, verification debt, DORA placeholders. citeturn1search49turn1search4turn0search2  
  - Outcome: first weekly metrics report produced.

**Day 13–14 (Owner: Peter + Control Tower)**
- Run the first “retro as experiment” and select exactly 1–2 improvement experiments with validation metrics and expiry dates.  
  - Outcome: 100% retro actions have an owner + metric + due date.

### Deliverable: Open questions and data gaps (what to measure next)

These are the missing inputs that would let the OS be calibrated precisely (rather than “best practice”).

1) **Actual delivery telemetry today**: deploy frequency, lead time, failed deployment recovery time, change fail rate, rework rate (DORA). citeturn0search2  
2) **Verification coverage**: what % of changes have strong tests? What % rely on manual verification?  
3) **Agent performance stats**: first-pass acceptance and rework by lane/model.  
4) **Prompt drift frequency**: how often do you change templates because of regressions? (You have governance for it; need data.) fileciteturn52file0L1-L106  
5) **3PP outage/degradation history**: what has failed over the last 90 days? (Needed to design continuity mode.)  
6) **Time allocation**: how much time is spent on (a) creating artifacts, (b) verifying artifacts, (c) rework? This is the backbone for economic efficiency.

## Research thin areas, contradictions, and explicit trade-offs

**Where research is thin (and I’m making assumptions).**
- There is strong research on flow, delivery performance measurement, and reliability governance (DORA, SRE, queueing theory). citeturn0search2turn1search6turn1search49  
- There is **less rigorous longitudinal research** on “AI-agent team process design” as a mature discipline; much of it is emerging practice plus vendor guidance and security taxonomies. citeturn2search10turn2search0  
- Public agent benchmarks (SWE-bench variants) can be contaminated or misleading; relying on them as a predictor of your environment is risky. citeturn1search7turn1search1  

**Key contradictions/trade-offs you must choose, not “balance.”**
- **Speed vs auditability**: every audit artifact costs time; therefore enforce a *minimal* mandatory set (WO + CA + test evidence) and keep everything else optional unless risk class requires it.  
- **Agent autonomy vs security**: OWASP explicitly calls out excessive agency; autonomy must be risk-tiered. citeturn2search0  
- **Small batches vs coordination overhead**: smaller diffs reduce risk but can increase overhead; solve with automation (templates, checks), not meetings.  
- **Sprints vs flow**: sprints provide synchronization; flow provides speed and predictability. Hybrid gives you both, but only if WIP limits are real and gates are enforced. citeturn1search49turn1search4  

**Bottom line.** You already have the blueprint. The redesign is not “write more process.” It is: **turn your existing process into hard gates + end-to-end provenance + closed-loop metrics**—because in an AI-agent-heavy shop, output is abundant and cheap; *trustworthy progress* is scarce and expensive.