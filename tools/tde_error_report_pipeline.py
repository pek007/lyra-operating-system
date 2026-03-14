#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from tde_error_report_adapter import adapt_error_report
from tde_error_report_markdown import parse_error_report_markdown
from tde_intake_ingest import ingest_packet


def run_pipeline(*, report: dict[str, Any], report_out: Path | None, packet_out: Path | None, workspace_scope: str, db_path: Path | None) -> dict[str, Any]:
    if report_out is not None:
        report_out.parent.mkdir(parents=True, exist_ok=True)
        report_out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    packet = adapt_error_report(report=report, workspace_scope=workspace_scope)
    if packet_out is not None:
        packet_out.parent.mkdir(parents=True, exist_ok=True)
        packet_out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")

    result = {
        "report_path": str(report_out) if report_out else None,
        "packet_path": str(packet_out) if packet_out else None,
        "intake_id": packet["intake_id"],
        "intake_class": packet["intake_class"],
    }
    if db_path is not None:
        result["ingest"] = ingest_packet(packet=packet, db_path=db_path)
    return result


def run_markdown_pipeline(*, md_path: Path, report_out: Path | None, packet_out: Path | None, workspace_scope: str, db_path: Path | None, priority_hint: str | None = None) -> dict[str, Any]:
    report = parse_error_report_markdown(
        md_path.read_text(encoding="utf-8"),
        source_reference=str(md_path),
        priority_hint=priority_hint,
    )
    return run_pipeline(
        report=report,
        report_out=report_out,
        packet_out=packet_out,
        workspace_scope=workspace_scope,
        db_path=db_path,
    )


def main() -> None:
    ap = argparse.ArgumentParser(description="Run markdown/structured error-report -> TDE intake -> ingest pipeline")
    ap.add_argument("--report-path", default=None)
    ap.add_argument("--markdown-path", default=None)
    ap.add_argument("--workspace-scope", required=True)
    ap.add_argument("--structured-out", default=None)
    ap.add_argument("--packet-out", default=None)
    ap.add_argument("--db-path", default=None)
    ap.add_argument("--priority-hint", default=None)
    args = ap.parse_args()

    if bool(args.report_path) == bool(args.markdown_path):
        raise SystemExit("provide exactly one of --report-path or --markdown-path")

    if args.report_path:
        report = json.loads(Path(args.report_path).read_text(encoding="utf-8"))
        result = run_pipeline(
            report=report,
            report_out=Path(args.structured_out) if args.structured_out else Path(args.report_path),
            packet_out=Path(args.packet_out) if args.packet_out else None,
            workspace_scope=args.workspace_scope,
            db_path=Path(args.db_path) if args.db_path else None,
        )
    else:
        result = run_markdown_pipeline(
            md_path=Path(args.markdown_path),
            report_out=Path(args.structured_out) if args.structured_out else None,
            packet_out=Path(args.packet_out) if args.packet_out else None,
            workspace_scope=args.workspace_scope,
            db_path=Path(args.db_path) if args.db_path else None,
            priority_hint=args.priority_hint,
        )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
