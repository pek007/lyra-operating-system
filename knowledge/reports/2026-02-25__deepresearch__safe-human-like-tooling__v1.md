# Deep Research Report — Safe Human-Like Tooling for Lyra

- Date: 2026-02-25
- Source: Deep Research markdown shared by Peter
- Topic: Safe architecture for granting human-like tools (email/calendar/SMS/docs/payments)

## Core Thesis
Treat tool access as risk transfer. Design for **capability without custody**:
- Lyra can draft/propose/execute within strict boundaries
- Peter retains control over irreversible actions

## High-Value Recommendations
1. Put a Policy Enforcement Point (Tool Proxy) between agent and external systems.
2. Use least privilege + short-lived credentials + revocation workflows.
3. Require approvals for irreversible/external actions.
4. Treat evidence/audit artifacts as first-class outputs.
5. Add spend/rate/anomaly guardrails for action tools.

## Relevance to Current OS
Very high. Aligns with our current:
- approval mindset
- security/audit runbooks
- model routing governance
- control panel strategy

## Practical “Adopt-Now” Items
- Define data classification policy + outbound redaction gate.
- Add tool capability contracts before enabling new action tools.
- Add approval-card template in control panel backlog.
- Keep payments/crypto out of scope for current stage.
