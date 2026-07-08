"""
check_citations.py — Room 9: Check The Citations
60% DETERMINISTIC. No AI. Builds the monthly checklist; parses results into the log.

Monthly flow (run once a month):
1. python check_citations.py         -> writes output/citation-checklist-YYYY-MM.md
                                        (top-20 target queries x 3 engines)
2. ADAM (by hand): run each query through ChatGPT, Perplexity, and Claude.
   Mark [x] where Safe Harbor was cited. Save the file.
3. python check_citations.py --log   -> parses the filled checklist, appends the
                                        month's numbers to output/citation-log.json.

Baseline: 2.5% (2 of 80) from the Red Rover report, 2026-07-06 (seeded in the log).
NEVER let AI guess whether an engine cited Safe Harbor — only hand-checked boxes count.
"""

import json
import re
import sys
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
OUTDIR = BASE / "output"
LOG = OUTDIR / "citation-log.json"
TARGET_QUERIES_FILE = Path(
    r"C:\Users\1alph\.claude\skills\safeharbor-reddit-triage\references\target-queries.md"
)
ENGINES = ["ChatGPT", "Perplexity", "Claude"]
TOP_N = 20  # target-queries.md is sorted UNTAPPED-first, then by volume — top 20 = the right 20


def load_target_queries():
    """Parse the target-queries.md table -> list of query strings. Empty if file missing."""
    if not TARGET_QUERIES_FILE.exists():
        return []
    queries = []
    for line in TARGET_QUERIES_FILE.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or set(line.strip()) <= {"|", "-", " ", ":"}:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 2 and cells[0].lower() != "query":
            queries.append(cells[0])
    return queries


def checklist_path():
    return OUTDIR / f"citation-checklist-{date.today().strftime('%Y-%m')}.md"


def build_checklist():
    queries = load_target_queries()[:TOP_N]
    if not queries:
        print(f"No target queries found at {TARGET_QUERIES_FILE}.")
        print("Create that file from the Red Rover report first, then rerun.")
        return
    month = date.today().strftime("%B %Y")
    lines = [
        f"# Citation Check — {month}",
        "",
        "Run each query below through each engine BY HAND. If Safe Harbor",
        "(safeharborbehavioralhealth.com) is named or cited in the answer, mark [x].",
        "When done, run:  python check_citations.py --log",
        "",
    ]
    for i, q in enumerate(queries, 1):
        lines.append(f"## {i}. {q}")
        for engine in ENGINES:
            lines.append(f"- [ ] {engine} cites Safe Harbor")
        lines.append("")
    OUTDIR.mkdir(parents=True, exist_ok=True)
    checklist_path().write_text("\n".join(lines), encoding="utf-8")
    print(f"Checklist written: {checklist_path()}")
    print(f"{len(queries)} queries x {len(ENGINES)} engines = {len(queries) * len(ENGINES)} checks.")


def log_results():
    path = checklist_path()
    if not path.exists():
        print(f"No checklist for this month at {path}. Run without --log first.")
        return
    text = path.read_text(encoding="utf-8")
    cited = len(re.findall(r"- \[x\]", text, re.IGNORECASE))
    unchecked = len(re.findall(r"- \[ \]", text))
    total = cited + unchecked
    if total == 0:
        print("Checklist has no checkboxes — nothing to log.")
        return
    entries = json.loads(LOG.read_text(encoding="utf-8")) if LOG.exists() else []
    month = date.today().strftime("%Y-%m")
    entries = [e for e in entries if e.get("month") != month]  # rerunning replaces the month
    pct = round(100 * cited / total, 1)
    entries.append({
        "date": date.today().isoformat(),
        "month": month,
        "source": "monthly hand-check (Room 9)",
        "cited": cited,
        "total": total,
        "pct": pct,
    })
    LOG.write_text(json.dumps(entries, indent=2), encoding="utf-8")
    print(f"Logged {month}: {cited} of {total} cited ({pct}%). Baseline was 2.5%.")


if __name__ == "__main__":
    if "--log" in sys.argv:
        log_results()
    else:
        build_checklist()
