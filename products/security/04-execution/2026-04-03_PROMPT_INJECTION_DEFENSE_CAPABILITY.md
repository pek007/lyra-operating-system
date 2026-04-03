# Prompt Injection Defense Capability

Status: Draft capability artifact
Product: Security (`A-004`)
Owner: Lyra
Date: 2026-04-03

## Purpose
Define Prompt Injection Defense as a concrete Security capability within the Security product, turning the current research-to-capability test into a real as-Code artifact that can drive controls, plans, and review.

## Why this capability exists
Lyra/OpenClaw-style environments combine:
- untrusted external content
- tool use
- browser/web flows
- external messaging paths
- file/system actions
- multi-step agent workflows

That creates a real prompt injection risk surface, especially for indirect prompt injection and consequence amplification through tools and broad authority.

This capability exists to reduce that risk through explicit posture, control objectives, and implementation/review discipline.

## Scope
In scope:
- direct and indirect prompt injection risk
- browser/web/document/retrieval content as untrusted instruction channels
- agent/tool/runtime blast-radius reduction
- instruction/data boundary controls
- least privilege, approval gating, sandboxing, monitoring, and review patterns
- practical control assessment for Lyra/OpenClaw-style environments

Out of scope:
- claiming prompt injection is fully solved
- replacing broader security governance or all application security work
- silently redefining canonical product/runtime controls outside owned security surfaces

## Capability outcome
The capability succeeds when prompt injection risk is:
- explicitly understood
- translated into concrete control expectations
- reviewed against live runtime/tool paths
- improved through evidence-backed hardening steps

## Current posture
Current posture should be treated as:
- cautious
- layered
- bounded-by-default
- consequence-limiting, not detection-only

## Core control objectives
1. Keep untrusted content untrusted
2. Reduce authority/blast radius by default
3. Require approval for high-risk actions
4. Prefer bounded workflows over broad autonomy where practical
5. Use layered safeguards rather than single-point defenses
6. Keep review and evidence explicit for high-risk paths

## Current evidence base
Grounded by:
- `knowledge/pilots/prompt-injection-security/compiled/syntheses/2026-04-03__lyra-os-prompt-injection-defense-posture.md`
- `knowledge/pilots/prompt-injection-security/compiled/syntheses/2026-04-03__lyra-openclaw-prompt-injection-gap-assessment.md`
- current Security product governance and risk surfaces
