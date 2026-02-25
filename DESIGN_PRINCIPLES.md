# DESIGN_PRINCIPLES.md

## Purpose
Set default design philosophy for all systems, workflows, automations, and deliverables.

## Core Principles
1. **Scalable by default**
   - Design for growth in volume, complexity, and collaborators.
   - Avoid choices that only work for a single-user edge case.

2. **Modular architecture**
   - Keep components loosely coupled and replaceable.
   - Separate policies, processes, templates, and execution tooling.

3. **Reusable assets**
   - Prefer templates, checklists, and standards over one-off solutions.
   - Any repeated work should become a reusable artifact.

4. **Transparent operations**
   - Decisions, assumptions, and changes must be documented.
   - Use versioned files as source of truth where possible.

5. **Continuous improvement**
   - Treat operations as a product: measure, review, improve.
   - Maintain an improvement backlog and close loops weekly.

6. **Professional quality bar**
   - Outputs should be clear, reliable, and decision-ready.
   - Risk, privacy, and governance are first-class constraints.

7. **UI and ease-of-use first**
   - Favor low-friction workflows with clear user experience.
   - If a process is hard to use, it will not be used.

8. **Shared modules, isolated instances**
   - Reuse service architecture across domains (OS, PX, future domains).
   - Enforce strict data/config/runtime separation between domain instances.

9. **State-of-the-art ambition, pragmatic delivery**
   - Aim for best-in-class architecture and quality over time.
   - Deliver in increments that are usable and safe now.
   - Separate must-have quality from aspirational polish.
   - Upgrade quality in planned iterations, not by delaying all value.

## Design Check (apply before adoption)
For any new tool/process, answer:
- Does this scale?
- Is it modular and replaceable?
- Is it reusable beyond this one case?
- Is it transparent/auditable?
- Does it improve over time with metrics?
- Is the UX simple for daily operation?
- Is the scope balanced between a shippable **Now bar** and an ambitious **Next bar**?

If two or more answers are “no”, redesign or defer.

## Version
- v1.1
- Date: 2026-02-25
- Owner: Peter + Lyra
