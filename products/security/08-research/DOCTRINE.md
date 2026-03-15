# Security Doctrine

Status: Active
Product: Security (`A-004`)
Owner: Lyra
Date: 2026-03-15

## Purpose
Capture Security's current synthesized view so the product can explain what it believes now without relying on scattered notes or chat history.

## Current doctrine

### 1. Security must be enforced in runtime reality, not only described in artifacts
Our default position is that prose-only controls are insufficient where stronger technical or procedural enforcement is feasible. A declared boundary that does not hold in practice is a real security problem, not a documentation issue.

### 2. Trust-boundary integrity is the primary current control question
The most important near-term security question is whether OS↔PXS and related runtime boundaries are genuine, narrow, and verifiable. If that is weak, many downstream security claims become less trustworthy.

### 3. Tooling surfaces are security surfaces
Shell execution paths, evidence ingestion routes, browser control, and similar operational interfaces are not merely convenience mechanisms; they are policy-enforcement points and should be designed and reviewed as such.

### 4. Agentic-security doctrine must be broader than local issue response
Security should not focus only on today's local implementation gaps. It should maintain broad awareness of agent-runtime, model-risk, tool-abuse, and deployment-surface developments so that major external shifts are not missed.

### 5. Broad radar is required; depth must stay bounded
The correct stance is broad coverage with selective deepening. Security should avoid both superficial breadth with no implications and narrow fixation that misses larger shifts.

## Known unresolved questions
- What is the smallest enforceable control set that makes the OS↔PXS boundary meaningfully trustworthy?
- Which execution surfaces should be elevated first from procedural guidance to deterministic technical controls?
- What external agentic-security practices are mature enough to adopt versus merely interesting to monitor?
- Which browser/node/device surfaces will become materially relevant first in our operating model?

## Confidence and limits
Confidence is high on the immediate importance of boundary integrity and tool-surface hardening.
Confidence is moderate on the current doctrine for broader AI-agent security because the external research layer has only just been formalized as part of the product model.
