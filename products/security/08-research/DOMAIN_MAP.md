# Security Research Domain Map

Status: Active
Product: Security (`A-004`)
Owner: Lyra
Date: 2026-03-15

## Purpose
Define the full domain surface Security should monitor so the product stays broad enough to avoid blind spots while concentrating depth only where decision value is highest.

## Scope rule
Default posture:
- broad watch across the full relevant security surface
- deeper work in a few currently critical themes
- explicit acknowledgment of out-of-focus areas rather than silent omission

## Domain map

### Core domains
These are central to the Security product's current mission and should be monitored continuously.

1. **OpenClaw security architecture and controls**
   - gateway, sessions, tools, permissions, browser control, nodes, cron, config, update paths
   - local docs, source behavior, release deltas, config/control changes

2. **Agent runtime isolation and trust boundaries**
   - OS↔PXS boundary integrity
   - sandboxing, workspace boundaries, runtime embodiment, cross-context read/write risk
   - permission-envelope and least-privilege control design

3. **Identity, auth, and secret handling**
   - tokens, credentials, privilege escalation, session boundaries, auth flows, secret leakage prevention

4. **Tool permission and execution safety**
   - shell execution risk, browser risk, file mutation risk, external side effects, approval boundaries, auditability

5. **Model risk and prompt-injection defenses**
   - prompt injection, tool hijacking, indirect prompt attacks, unsafe output handling, jailbreak/reasoning abuse patterns where product-relevant

6. **Monitoring, logging, auditability, and incident response**
   - traceability, decision/evidence linkage, anomaly visibility, residual-risk handling, incident readiness

### Adjacent domains
These are important because they can materially affect our operating environment or become core later.

7. **Browser, node, and device attack surfaces**
   - browser relay/user browser exposure
   - paired-node/mobile companion risks
   - camera, screen, location, notification, device permission surfaces

8. **Dependency and supply-chain security**
   - npm/tooling dependencies
   - update channels
   - third-party integrations
   - trust in external packages, plugins, and runtimes

9. **Deployment posture for local, VPS, and tailnet setups**
   - exposure management
   - firewall/SSH/Tailscale posture
   - remote access assumptions
   - environment-specific risk trade-offs

10. **External cyber developments material to AI-agent environments**
    - major new attack patterns
    - defensive techniques
    - changes in best practice relevant to agentic systems

### Peripheral-but-relevant domains
These should be watched lightly unless they become materially relevant.

11. **Regulatory and standards developments**
    - AI Act, GDPR-adjacent operational implications, secure development standards, audit/control frameworks

12. **Customer-facing security expectations**
    - what future externalization or packaging would require in assurance, documentation, and isolation

13. **Human factors and operational misuse risk**
    - approval fatigue, unsafe defaults, misunderstanding of boundaries, social-engineering-adjacent operating risks

## Current priority themes for depth
1. **OS↔PXS boundary enforcement**
   - highest current risk because declared boundary and runtime reality are not yet fully aligned

2. **Tool and evidence execution surface hardening**
   - critical because policy currently depends too much on procedural sharpness rather than deterministic control

3. **AI-agent runtime and tool-abuse controls**
   - strategic because this is where broader security developments are most likely to affect our architecture

## Out-of-focus but watched
These are not current deep-dive priorities, but should still remain on radar:
- broad enterprise cybersecurity topics with little relevance to agentic environments
- mass-market security news without architectural implications
- compliance detail not yet connected to our operating model

## Review rule
Reassess this domain map monthly or whenever a major product, runtime, or deployment change suggests the current scope is too narrow or misweighted.
