# MULTI_AGENT_OPERATING_MODEL_V1_1.md

## Purpose
Execution-grade refinement of v1 based on second-opinion review.

## Key Clarification
- **GPT-5.3-Codex remains an approved default where available in OpenClaw and/or Codex workbench flows.**
- Model routing is policy-driven and cost-aware; no single premium model is default across all agents.

## Structural Refinements

### 1) Execution Modes (explicit)
1. **Persistent agent**: Control Tower (Lyra main), owns global context and decision rights.
2. **Spawned subagents (default)**: stateless, task-scoped workers with strict handoff format.
3. **External workbench lane**: Codex/Deep Research/manual specialist runs treated as formal execution lane with mandatory handoff back into OS artifacts.

### 2) Permission Envelopes (per agent)
Each specialist agent must define:
- allowed inputs (files/tools/channels)
- allowed outputs (which docs/registries it may modify)
- escalation boundaries (what requires Control Tower/Peter approval)

### 3) Tool/Data Boundaries (minimum)
- Security & Audit: no outbound messaging by default; can open incidents and write controls docs.
- Build: shell/git/tooling allowed; external publish/send requires approval.
- Research: web tools allowed; cannot change governance docs without handoff approval.
- Content Delivery: drafting and formatting only unless explicitly delegated.

### 4) Model Routing as Policy (not fixed assignment)
Routing follows trigger-based policy:
- **Default lane (cost-efficient):** mid-tier high-value model
- **Premium lane:** Type 1, high-risk, must-be-right outputs only
- **Coding lane:** Codex-capable model/workbench for build tasks
- **Fallback lane:** secondary provider/model if primary unavailable or quality regression detected

### 5) Anti-thrash Rule
- Default model/routing changes only on **monthly review**, unless there is a clear regression/outage.
- Emergency override allowed with documented reason + rollback plan.

### 6) Champion-Challenger Loop
- Keep one champion model per lane.
- Run challenger on sampled tasks weekly.
- Track quality/time/cost.
- Promote challenger only with evidence.

## Measurable Success Metrics (additions)
- Handoff acceptance rate (first-pass usable)
- Rework rate per agent
- Cost per completed task by lane
- Incident rate linked to tool/model misuse
- Routing stability (number of model-switch events/month)

## Immediate Adoption Plan
1. Keep current Control Tower + role structure.
2. Implement spawned-subagent default and explicit handoff schema.
3. Add per-agent permission envelope docs.
4. Add model routing scorecard + monthly anti-thrash review.

## Version
- v1.1
- Date: 2026-02-24
- Owner: Peter + Lyra
