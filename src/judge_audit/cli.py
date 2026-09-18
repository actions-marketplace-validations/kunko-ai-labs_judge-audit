"""CLI: run audits, write reports, gate CI on drift."""
from __future__ import annotations

import argparse
import json
import sys

from .judges.jev import JevJudge
from .report import check_drift, render_markdown
from .runner import load_jsonl, run_audit


def _judge(name: str):
    if name == "jev":
        return JevJudge()
    raise SystemExit(f"unknown judge '{name}' (available: jev)")


def main() -> None:
    ap = argparse.ArgumentParser(prog="judge-audit")
    sub = ap.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("run", help="audit a judge against a labeled JSONL file")
    r.add_argument("labels", help="JSONL: {state, questions:[...], labels:{...}}")
    r.add_argument("--judge", default="jev")
    r.add_argument("--out", default="audit-report.md")
    r.add_argument("--json", default="audit-result.json")

    c = sub.add_parser("check", help="CI gate: fail if drifted vs baseline")
    c.add_argument("labels")
    c.add_argument("--judge", default="jev")
    c.add_argument("--baseline", required=True)
    c.add_argument("--max-ece-drift", type=float, default=0.02)
    c.add_argument("--max-acc-drop", type=float, default=0.01)

    args = ap.parse_args()
    judge = _judge(args.judge)
    result = run_audit(judge, load_jsonl(args.labels))

    if args.cmd == "run":
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(render_markdown(result))
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(result.to_dict(), f, indent=2)
        print(f"judge={result.judge} n={result.n} accuracy={result.accuracy:.1%} "
              f"ece={result.ece:.4f} -> {args.out}")
    else:
        failures = check_drift(result, args.baseline,
                               args.max_ece_drift, args.max_acc_drop)
        if failures:
            print("DRIFT DETECTED:", file=sys.stderr)
            for fl in failures:
                print(f"  - {fl}", file=sys.stderr)
            sys.exit(1)
        print(f"OK: no drift (ece={result.ece:.4f}, accuracy={result.accuracy:.1%})")


if __name__ == "__main__":
    main()
