#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
URL_RE = re.compile(r"^(https?://|mailto:|tel:)")
SKIP_PARTS = {".git", "node_modules", "repos"}


def strip_code_fences(text: str) -> str:
    out: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(line)
    return "\n".join(out)


def extract_links(text: str) -> list[str]:
    return [m.group(1).strip() for m in LINK_RE.finditer(strip_code_fences(text))]


def is_ignored(link: str) -> bool:
    if URL_RE.match(link):
        return True
    if link.startswith("#"):
        return True
    return False


def _collect_paths_from_git_output(output: str) -> set[Path]:
    paths: set[Path] = set()
    for line in output.splitlines():
        rel = line.strip()
        if not rel:
            continue
        p = ROOT / rel
        if p.suffix.lower() != ".md" or not p.exists():
            continue
        if any(part in SKIP_PARTS for part in p.parts):
            continue
        paths.add(p)
    return paths


def changed_markdown_paths() -> list[Path]:
    diff_cmd = ["git", "diff", "--name-only", "--diff-filter=ACMRTUXB", "HEAD"]
    untracked_cmd = ["git", "ls-files", "--others", "--exclude-standard"]
    try:
        changed = subprocess.check_output(diff_cmd, cwd=ROOT, text=True)
        untracked = subprocess.check_output(untracked_cmd, cwd=ROOT, text=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        # No HEAD yet, git unavailable, or git metadata inaccessible: full scan fallback.
        return all_markdown_paths()

    paths = _collect_paths_from_git_output(changed)
    paths.update(_collect_paths_from_git_output(untracked))
    return sorted(paths)


def all_markdown_paths() -> list[Path]:
    out = []
    for p in ROOT.rglob("*.md"):
        if any(part in SKIP_PARTS for part in p.parts):
            continue
        out.append(p)
    return sorted(out)


def validate_path(md_path: Path) -> list[str]:
    errs: list[str] = []
    text = md_path.read_text(encoding="utf-8", errors="replace")
    for link in extract_links(text):
        if is_ignored(link):
            continue
        target = link.split("#", 1)[0]
        if not target:
            continue
        ref = (md_path.parent / target).resolve()
        if not ref.exists():
            rel = md_path.relative_to(ROOT).as_posix()
            errs.append(f"{rel}: broken link -> {link}")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser(description="Check markdown links")
    ap.add_argument("--changed-only", action="store_true", help="Only scan markdown files changed from HEAD")
    args = ap.parse_args()

    files = changed_markdown_paths() if args.changed_only else all_markdown_paths()
    errors: list[str] = []
    for p in files:
        errors.extend(validate_path(p))

    if errors:
        print("Markdown link check failed:")
        for e in errors:
            print(f"- {e}")
        return 1

    mode = "changed-only" if args.changed_only else "full"
    print(f"Markdown link check passed ({mode}, {len(files)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
