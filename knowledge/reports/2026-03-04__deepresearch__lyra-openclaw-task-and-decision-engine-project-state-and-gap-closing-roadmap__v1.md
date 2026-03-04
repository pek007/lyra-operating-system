# Lyra OpenClaw Task & Decision Engine Project State and Gap-Closing Roadmap

## Information needs

To answer well, I must determine the project’s current state across:

- The explicit and implicit goals (system-level and TDE-level) and how they are expressed in authoritative artifacts.
- The “as-built” architecture and contracts (state model, decision/approval gating, idempotent execution, audit/evidence chain), and how these map to the stated use cases.
- The sprint/work structure (work orders, test/evidence artifacts, and operational hooks), and whether it reliably translates goals into shipped increments.
- The measurable progress signals available in the repository (verification bundles, artifacts, cadence, metrics) and what is missing/unspecified.
- The major technical, process, and organizational risks (including governance correctness and autonomy safety), and the minimum roadmap to close the highest-risk gaps.

## Executive summary

The Lyra OpenClaw Task & Decision Engine (TDE) project is unusually strong on *directional governance and “policy-as-code”-style execution guardrails* relative to its maturity: it has an explicit mission and ranked objectives at the system level, plus a TDE product goal, bounded scope, decision use cases, non-goals, success metrics, and kill criteria captured early. fileciteturn111file5L1-L1 fileciteturn111file0L1-L1 fileciteturn168file0L1-L1

Technically, the repo demonstrates a coherent “thin-slice governance kernel” approach: deterministic acceptance tests codify an end-to-end governance flow (trigger → evaluate → decision packet → approval gate → idempotent execution → audit link), plus anti-stall classification/routing and runtime-triggered cycles. fileciteturn160file3L1-L1 fileciteturn121file0L1-L1 The system then progressively hardens authority and traceability in later micro-sprints: S15 introduces runtime binding-integrity and re-authorization semantics; S16 enforces objective-to-work linkage fields in execution artifacts with fail-closed behavior. fileciteturn165file0L1-L1 fileciteturn164file0L1-L1 fileciteturn161file0L1-L1 fileciteturn163file1L1-L1

However, “big-picture readiness” to pursue complex high-level objectives remains constrained by a small number of structural gaps:

- **Operational state as Markdown (TASKS.md) is still not concurrency-safe** (explicit backlog items call out atomic/locked writeback). fileciteturn111file2L1-L1
- **Binding integrity is not fully fail-closed under all resolution paths**: if the active-binding registry cannot resolve a binding record, the current runner can fall back to a synthesized “active” binding, weakening the invariant “authority must be proven, not assumed.” This is a central risk if/when a multi-user or multi-gateway model emerges (and those trust-boundary concerns are explicitly open). fileciteturn158file0L1-L1 fileciteturn167file3L1-L1 fileciteturn111file2L1-L1
- **Delivery instrumentation is mostly “local evidence artifacts,” not continuous CI/CD** (issue tracker and PR-based review appear unused; CI is not evidenced in-repo), so DORA-style throughput/instability tracking is effectively **Unspecified** at a toolchain level. fileciteturn111file2L1-L1 citeturn1search1
- **Trello retirement is well-designed as a state-based migration**, but remains largely at the design/gate level; “Trello-free steady state” is not yet evidenced in live operations. fileciteturn129file0L1-L1 fileciteturn111file0L1-L1

The recommended near-term roadmap is to (1) harden core invariants (atomic writeback; binding resolution must fail closed; explicit trust-boundary decision), (2) formalize outcome measurement (DORA-aligned plus flow metrics using Little’s Law) and release gating, and (3) expand from “kernel correctness” into “objective pursuit” by wiring objective hierarchies and decision packets into daily execution loops and a Trello-cutover canary domain. citeturn1search1turn2search35turn0search2

## Goals, architecture, and sprint translation

### Goal clarity

At the **system level**, goals are explicit and ranked: the system exists to run and strengthen a consulting firm, and Phase 1 prioritizes (1) direction/governance, (2) reliable software delivery capability, and (3) task/decision management capability. fileciteturn111file5L1-L1 fileciteturn169file0L1-L1

At the **TDE level**, the “why” and boundaries are unusually crisp for an early system:

- Product goal: establish a definition baseline enabling continuous, policy-governed operation without human micro-management, integrate natively with OpenClaw, and enable Trello retirement; vision addendum explicitly targets autonomy toward high-level goals. fileciteturn111file0L1-L1
- Decision use cases: (1) allow/deny transitions with gates, (2) escalation vs autonomy, (3) anti-stall and drift detection, (4) progress transparency (active vs stuck). fileciteturn111file0L1-L1
- Non-goals clearly exclude UI-first rebuilds and ML-first prioritization as prerequisites. fileciteturn111file0L1-L1
- Success metrics and kill criteria exist and are time-windowed (but sprint length is **Unspecified**; these windows appear calendar-based in early artifacts). fileciteturn111file0L1-L1

This is high goal clarity by typical standards: mission → ranked objectives → operating principles → bounded TDE use cases and acceptance tests. fileciteturn111file5L1-L1 fileciteturn121file0L1-L1

### Architecture and contracts mapped to goals

The as-built TDE is best described as a *local-first, deterministic governance substrate* over a Markdown-based system of record, with explicit “guardrails first” semantics:

- A thin governance kernel encodes deterministic decisioning patterns: idempotency, approval gating, version conflict handling, partial failure reconciliation, and progress-state classification. fileciteturn160file3L1-L1
- A canary runtime cycle formalizes heartbeat/cron triggers and stable “canary status” artifacts with guardrail thresholds and “clean-cycle” gating. fileciteturn160file0L1-L1 fileciteturn156file0L1-L1
- A job-tick runner evolves the kernel into “operational jobs”: claim rules, mutation envelopes, writeback, and strict validation of objective linkage and binding integrity—codified as an explicit runtime contract. fileciteturn158file0L1-L1 fileciteturn155file0L1-L1
- Governance boundaries clarify what belongs in task/decision systems vs memory and prose runtime rules (AGENTS/policies). fileciteturn171file0L1-L1 fileciteturn103file5L1-L1

Conceptually (and consistent with the direction package), governance documents are the human source-of-truth while runtime scripts and hooks enforce what must not be “prose-only.” fileciteturn169file0L1-L1

## Progress and gaps

### Progress toward the assumed objective

Given the assumed overarching objective (“enable pursuit of complex high-level objectives”), the repository indicates progress on the *prerequisites* to safe autonomy:

- **Direction and governance layer:** system charter + direction package are present and detailed, addressing the prior failure mode of “high-quality work without outcome accumulation.” fileciteturn111file5L1-L1 fileciteturn169file0L1-L1
- **Deterministic governance mechanics:** the governance kernel codifies idempotency, approval requirements, conflict handling, reconciliation, and progress classification. fileciteturn160file3L1-L1
- **Operationalization into runnable loops:** canary cycles and job ticks exist as runnable scripts with explicitly documented trigger contracts and stable output schemas, producing evidence artifacts. fileciteturn156file0L1-L1 fileciteturn155file0L1-L1
- **Authority hardening and traceability:** S15 and S16 produce verification bundles and machine-readable evidence showing (a) re-auth required on binding change and (b) fail-closed objective-linkage enforcement. fileciteturn164file0L1-L1 fileciteturn163file1L1-L1

### Major gaps (technical, process, organizational)

1) **Concurrency and atomicity of TASKS.md are not solved** (pending backlog).
2) **Binding resolution still has a synthesized fallback path** that should become strict fail-closed.
3) **Objective linkage exists, but not yet a full objective model/graph.**
4) **CI/CD and DORA instrumentation remain partial/unspecified at system level.**
5) **Trust boundary for multi-user/group usage remains unresolved.**

## Roadmap and KPIs (summary)

### Wave 1 (0–2 weeks)
- Remove binding fallback for side-effecting mutation paths (fail closed on unresolved binding).
- Implement atomic/locked TASKS writeback.
- Resolve and enforce trust boundary model.
- Publish canonical TDE entrypoint index.

### Wave 2 (2–6 weeks)
- Objective model v1 (registry + owners + checkpoints + measurable criteria).
- Daily decision packet MVP linked to fresh evidence.
- Flow instrumentation + DORA baseline boundary definition.

### Wave 3 (6–12 weeks)
- Trello canary live in TDE with strict clean-cycle gates.
- CI/CD + release gating hardening.
- Security uplift aligned with SSDF + LLM risk model.

## Key references

- Internal: TDE start packet, WOs S15/S16, contracts, runner/tests, TASKS backlog.
- External: DORA metrics model, NIST SSDF, Little’s Law, Trunk-based development, OWASP LLM Top 10.
