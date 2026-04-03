# Prompt Injection Defense

Status: draft wiki page
Date: 2026-04-03
Domain: Controls & Security

## Summary
Prompt Injection Defense is a Security capability focused on reducing the risk that malicious or misleading content can steer model behavior in ways that conflict with intended instructions, user intent, or control boundaries.

In Lyra/OpenClaw-style environments, this is especially important because untrusted content may be combined with browser use, tool use, external messaging, file writing, and multi-step agent behavior.

## Current posture
Recommended posture is:
- cautious
- layered
- bounded by default
- consequence-limiting, not detection-only

## Core defense principles
- keep untrusted content untrusted
- reduce authority/blast radius by default
- require approval for high-risk actions
- prefer bounded workflows over broad autonomy where practical
- use layered safeguards rather than single-point defenses
- keep review and evidence explicit

## Why it matters
Prompt injection is not just a model-quality problem. It becomes a system-risk problem when untrusted content is combined with broad authority and meaningful action channels.

## Current Lyra/OpenClaw assessment
Current posture is partially aligned but not yet fully hardened. The highest-priority gap identified so far is the existence of at least one runtime with broad exec trust and no ask-gating or sandboxing.

## Current implementation status
- security research pilot created and populated
- posture synthesis created
- gap assessment created
- Security product capability artifact created
- first applied checklist assessment performed against `px-internal-dev`

## Related pages
- [Knowledge Compilation](../capabilities/knowledge-compilation.md)
- [Operational Truth vs Compiled Knowledge Boundary](../governance-authority/operational-truth-vs-compiled-knowledge-boundary.md)
