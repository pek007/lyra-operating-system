#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    ROOT / "CHIEF_ARCHITECT_AGENT_SPEC.md",
    ROOT / "SPRINT_ARCHITECTURE_BRIEF_TEMPLATE.md",
    ROOT / "ARCHITECTURE_REVIEW_REPORT_TEMPLATE.md",
    ROOT / "knowledge/registries/agents/agent-chief-architect.md",
    ROOT / "knowledge/registries/routing/route-architecture.md",
]


def fail(msg: str) -> None:
    print(f"[FAIL] {msg}")
    sys.exit(1)


def parse_frontmatter(md_path: pathlib.Path) -> dict[str, str | list[str]]:
    text = md_path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        fail(f"Missing frontmatter in {md_path.relative_to(ROOT)}")
    block = m.group(1).splitlines()
    out: dict[str, str | list[str]] = {}
    current_list_key = None
    for line in block:
        if not line.strip():
            continue
        if re.match(r"^\s*-\s+", line) and current_list_key:
            item = re.sub(r"^\s*-\s+", "", line).strip().strip('"')
            out.setdefault(current_list_key, [])
            assert isinstance(out[current_list_key], list)
            out[current_list_key].append(item)
            continue
        current_list_key = None
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip().strip('"')
            if val == "":
                out[key] = []
                current_list_key = key
            else:
                out[key] = val
    return out


def main() -> None:
    for p in REQUIRED_FILES:
        if not p.exists():
            fail(f"Required artifact missing: {p.relative_to(ROOT)}")

    spec = (ROOT / "CHIEF_ARCHITECT_AGENT_SPEC.md").read_text(encoding="utf-8")
    must_have_sections = [
        "When to Invoke the Chief Architect",
        "Evidence-first review",
        "Fitness Functions",
        "Model Policy",
        "Review SLA",
    ]
    for section in must_have_sections:
        if section not in spec:
            fail(f"Spec missing required section/text: '{section}'")

    agent = parse_frontmatter(ROOT / "knowledge/registries/agents/agent-chief-architect.md")
    routing = parse_frontmatter(ROOT / "knowledge/registries/routing/route-architecture.md")

    if agent.get("id") != "agent-chief-architect":
        fail("agent registry id must be 'agent-chief-architect'")
    if str(agent.get("status", "")).lower() != "active":
        fail("agent-chief-architect must be active")
    if routing.get("target") != "agent-chief-architect":
        fail("route-architecture target must equal agent id")
    if str(routing.get("trigger", "")).lower() != "architecture":
        fail("route-architecture trigger must be 'architecture'")

    conditions = routing.get("conditions", [])
    if not isinstance(conditions, list) or len(conditions) < 3:
        fail("route-architecture conditions must include at least 3 triggers")

    print("[PASS] Architecture fitness gate passed")


if __name__ == "__main__":
    main()
