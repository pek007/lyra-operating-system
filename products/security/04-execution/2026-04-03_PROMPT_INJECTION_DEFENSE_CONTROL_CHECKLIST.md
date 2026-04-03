# Prompt Injection Defense Control Checklist

Status: Draft
Product: Security (`A-004`)
Owner: Lyra
Date: 2026-04-03

## Purpose
Provide the first practical checklist for reviewing prompt injection exposure and control adequacy in Lyra/OpenClaw-style environments.

## Checklist

### 1. Untrusted content handling
- [ ] External content is explicitly treated as untrusted data, not trusted instructions
- [ ] Browser/web/document/retrieved content paths are identified
- [ ] Hidden/indirect instruction channels are considered in design review

### 2. Authority reduction
- [ ] Tool access is restricted to minimum necessary scope
- [ ] Broad or persistent authority is justified rather than assumed
- [ ] Sensitive data access is restricted and deliberate

### 3. High-risk action gating
- [ ] External messaging or writes require explicit approval where appropriate
- [ ] Destructive or privileged actions are behind approval/control gates
- [ ] Cross-trust-boundary actions are not silently delegated to the model

### 4. Workflow design
- [ ] Bounded workflows are preferred over broad autonomy for high-risk recurring tasks
- [ ] Open-ended agentic tasks are justified where used
- [ ] Broad "handle everything" tasking is avoided where safer task decomposition exists

### 5. Runtime safeguards
- [ ] Sandboxing/isolation is used where code execution, browser action, or sensitive file/system interaction exists
- [ ] Monitoring/logging exists for sensitive actions and suspicious behavior
- [ ] Security posture does not rely on prompt wording alone

### 6. Review and evidence
- [ ] The path has an explicit risk owner
- [ ] Control claims can be tied to evidence, not only narrative posture
- [ ] Known gaps or residual risks are explicitly documented

## First review targets
Use this checklist first on:
- browser/web-fetch + action-taking paths
- tool use + outbound messaging paths
- file/system write paths after untrusted-content ingestion
- runtimes with broad authority or shared trust boundaries
