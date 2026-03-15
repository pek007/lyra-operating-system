# Security Deep-Dive Index

Status: Active
Product: Security (`A-004`)
Owner: Lyra
Date: 2026-03-15

## Purpose
Track bounded deep analysis topics so Security stays broad in awareness but focused in detailed research.

## Active deep dives

### 1. OS↔PXS boundary enforcement
- **Why this matters now:** It is the clearest gap between declared security posture and runtime reality.
- **Status:** active
- **Expected product impact:** architecture boundary tightening, verification evidence, possible control/policy updates
- **Linked artifacts:**
  - `products/security/04-execution/TOP_PRIORITIES.md`
  - `products/security/06-architecture/BOUNDARY.md`
  - `governance/VEGA_ACCEPTANCE_TEST_RUN_SHEET_V1.md`

### 2. Tool and evidence execution surface hardening
- **Why this matters now:** Tooling and evidence paths are functioning as de facto control surfaces and therefore require harder guarantees.
- **Status:** active
- **Expected product impact:** tighter execution controls, hardened evidence paths, clearer enforcement requirements
- **Linked artifacts:**
  - `products/security/04-execution/TOP_PRIORITIES.md`
  - `SECURITY_ADOPTION_PLAN.md`
  - `products/security/07-decisions/DECISIONS.md`

### 3. AI-agent runtime and tool-abuse controls
- **Why this matters now:** This is the most likely area where external developments in agentic security will alter our architecture and governance posture.
- **Status:** active
- **Expected product impact:** doctrine updates, architecture/control implications, future roadmap changes
- **Linked artifacts:**
  - `products/security/08-research/DOMAIN_MAP.md`
  - `products/security/08-research/DOCTRINE.md`

## Capacity rule
Do not keep more than three active deep dives at once unless an explicit decision says otherwise.
