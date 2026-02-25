#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import pathlib
import subprocess

WS = pathlib.Path('/Users/lyra/.openclaw/workspace')


def run(cmd):
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return p.returncode, p.stdout.strip(), p.stderr.strip()


def now_local():
    return dt.datetime.now().astimezone()


def write_evidence(kind: str, status: str, summary: dict, artifacts: list, linked_tasks=None):
    ts = now_local()
    ym = ts.strftime('%Y-%m')
    out_dir = WS / 'knowledge' / 'evidence' / ym
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = ts.strftime('%Y%m%d-%H%M%S')
    path = out_dir / f"{slug}__{kind}.md"
    linked_tasks = linked_tasks or []

    front = {
        'id': f"EVID-{slug}-{kind}",
        'source': kind,
        'timestamp': ts.isoformat(),
        'status': status,
        'severitySummary': summary,
        'artifacts': [{'path': a} for a in artifacts],
        'linkedTasks': linked_tasks,
        'owner': 'Lyra'
    }

    lines = ['---']
    lines.append(json.dumps(front, indent=2))
    lines.append('---\n')
    lines.append(f"# Evidence: {kind}\n")
    lines.append(f"- Recorded: {ts.isoformat()}\n")
    lines.append(f"- Status: {status}\n")
    lines.append(f"- Summary: critical={summary.get('critical',0)}, warn={summary.get('warn',0)}, info={summary.get('info',0)}\n")

    path.write_text('\n'.join(lines), encoding='utf-8')
    return path


def main():
    ap = argparse.ArgumentParser(description='Ingest OpenClaw hygiene evidence into knowledge/evidence')
    ap.add_argument('--doctor', action='store_true', help='Run doctor and store evidence')
    ap.add_argument('--security', action='store_true', help='Run security audit and store evidence')
    ap.add_argument('--all', action='store_true', help='Run both doctor and security audit')
    args = ap.parse_args()

    do_doctor = args.all or args.doctor
    do_security = args.all or args.security
    if not do_doctor and not do_security:
        do_security = True

    created = []

    if do_security:
        code, out, err = run('openclaw security audit --json')
        status = 'pass' if code == 0 else 'fail'
        summary = {'critical': 0, 'warn': 0, 'info': 0}
        artifacts = []
        if out:
            try:
                j = json.loads(out)
                summary = j.get('summary', summary)
                findings_path = WS / 'knowledge' / 'evidence' / 'latest-security-audit.json'
                findings_path.parent.mkdir(parents=True, exist_ok=True)
                findings_path.write_text(json.dumps(j, indent=2), encoding='utf-8')
                artifacts.append(str(findings_path))
                if summary.get('critical', 0) > 0 or code != 0:
                    status = 'fail'
                elif summary.get('warn', 0) > 0:
                    status = 'warn'
            except Exception:
                pass
        p = write_evidence('security_audit', status, summary, artifacts)
        created.append(p)

    if do_doctor:
        code, out, err = run('openclaw doctor --non-interactive')
        status = 'pass' if code == 0 else 'fail'
        summary = {'critical': 0, 'warn': 0, 'info': 0}
        raw_path = WS / 'knowledge' / 'evidence' / 'latest-doctor.txt'
        raw_path.write_text(out + ('\n' + err if err else ''), encoding='utf-8')
        p = write_evidence('doctor', status, summary, [str(raw_path)])
        created.append(p)

    print('Created evidence records:')
    for p in created:
        print('-', p)


if __name__ == '__main__':
    main()
