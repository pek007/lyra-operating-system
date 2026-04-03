# Synthesis — Lyra/OpenClaw Prompt Injection Gap Assessment

Date: 2026-04-03
Status: gap assessment
Confidence: medium

## Purpose
Assess how current Lyra/OpenClaw reality compares with the prompt injection defense posture defined in the prompt-injection security pilot.

## Bottom line
Current Lyra/OpenClaw posture is **partially aligned but not fully where it should be**.

Strengths already exist:
- explicit approval expectations for high-risk actions
- sandboxing/containment options in the platform
- awareness that external/untrusted content must be treated carefully
- some trust-boundary and outbound-routing controls already present

But there are meaningful gaps:
- at least one runtime still has broad exec trust (`security=full`)
- the environment is treated as potentially multi-user/shared, which raises the impact of prompt-injection-induced cross-boundary actions
- browser/web/tool use exists in a context where prompt injection should be treated as an operationally live risk
- there is not yet a formal prompt-injection-specific control checklist or runtime review loop in place

## 1. Areas of strongest current alignment

### A. High-risk actions are conceptually approval-gated
Workspace-level guidance already says to ask first for external communications, destructive changes, credential/access changes, and other high-impact actions. This is aligned with the posture recommendation to keep high-risk actions behind explicit approval.

### B. External/untrusted content is increasingly treated as untrusted
The runtime/tooling ecosystem already shows explicit external-content warnings in some fetch flows. This is aligned with the posture rule that external content should remain untrusted.

### C. Sandboxing/containment exists as a platform concept
OpenClaw supports sandbox and security modes. That means the platform is structurally capable of containment; the issue is not absence of mechanism but how consistently and narrowly it is applied.

## 2. Main current gaps

### Gap 1 — Broad exec trust remains in at least one runtime
`openclaw status --deep` reports:
- `Exec security=full is configured`
- specifically for `px-internal-dev`

This is in tension with the desired prompt-injection posture. If a runtime can access broad exec power and is also exposed to untrusted content or broad workflows, the blast radius of successful injection or adversarial steering rises materially.

### Gap 2 — Shared/multi-user trust boundary risk remains live
The security audit warns that the gateway appears to operate in a potentially multi-user/shared context. That matters because prompt injection is not only about model misbehavior; it is about what happens when a model with broad access is operating across mixed-trust human contexts.

### Gap 3 — No explicit prompt-injection operating checklist yet
We now have a research-backed posture note, but not yet a first formal control checklist or standard operating review for:
- browser/web-fetch use
- tool-ingested documents
- agent tasks that mix untrusted inputs with outbound actions
- approval boundaries specific to prompt-injection risk

### Gap 4 — Browser/tool-rich environment increases exposure
Lyra/OpenClaw can browse, fetch, execute, write files, send messages, and coordinate agents. That is useful, but it means indirect prompt injection is not abstract here. It is a real class of system-level risk because untrusted content can sit close to meaningful action channels.

### Gap 5 — Control layering is present, but not yet explicitly unified under prompt-injection posture
There are pieces of the right posture in the system (approval rules, external/untrusted warnings, sandbox concepts, channel controls), but they are not yet clearly integrated as one coherent prompt-injection defense posture with explicit review criteria.

## 3. Practical risk judgment
The highest-risk pattern is not simply "an LLM reads bad text".
It is this combination:
- untrusted content enters through browser/web/document/retrieval flows
- the model is given broad task latitude
- the runtime has meaningful tools or external action channels
- the trust boundary is shared or mixed
- containment/approval is incomplete or inconsistently applied

That is the pattern Lyra/OpenClaw should optimize hardest against.

## 4. Priority gap list

### Priority 1 — Reduce broad runtime authority where possible
Most important immediate gap: broad exec trust in runtimes that do not clearly need it all the time.

### Priority 2 — Define a formal prompt-injection control checklist
The research posture should now become a practical checklist that can be applied to current runtime/tool paths.

### Priority 3 — Review highest-blast-radius workflows
Especially:
- browser/web-fetch + action-taking flows
- tool use + outbound messaging flows
- file/system write flows after untrusted-content ingestion
- agentic multi-step tasks with broad instructions

### Priority 4 — Strengthen trust-boundary discipline in shared contexts
If the environment remains shared, boundary discipline becomes more important, not less.

## 5. Current maturity assessment
Current Lyra/OpenClaw posture is best described as:
- **aware but incomplete**
- **guardrailed in parts, but not yet coherently hardened against prompt injection as a cross-cutting system risk**

## 6. Recommended next step
Create a first practical **Lyra OS prompt injection control checklist** and use it to review current high-risk tool/runtime paths.

That is the best bridge from research posture into operational hardening.
