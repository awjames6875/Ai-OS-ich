"""
write_tracker.py — Room 6: Mission Control (the scoreboard; dashboard.html is the to-do list).
60% DETERMINISTIC. No AI. Reads every pipeline output, snapshots today's numbers, renders
ONE self-contained tracker.html next to dashboard.html.

Run after the daily pipeline:  python write_tracker.py

Sections: AI citation rate vs 2.5% baseline · Reddit activity trend · 9-to-1 ratio check ·
funnel mix · competitor mentions · question bank · blogs · original posts.
"""

import json
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
PROJECT = BASE.parent
OUTDIR = BASE / "output"
HISTORY = OUTDIR / "stats-history.jsonl"
TRACKER = OUTDIR / "tracker.html"
BASELINE_PCT = 2.5  # Red Rover report, 2 of 80, 2026-07-06


def load_json(path, default):
    p = Path(path)
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return default


def snapshot(stats: dict):
    """Append today's numbers (idempotent — rerunning replaces today's line)."""
    entries = []
    if HISTORY.exists():
        entries = [json.loads(l) for l in HISTORY.read_text(encoding="utf-8").splitlines() if l.strip()]
    today = date.today().isoformat()
    entries = [e for e in entries if e.get("date") != today]
    entries.append({"date": today, **stats})
    HISTORY.write_text("\n".join(json.dumps(e) for e in entries) + "\n", encoding="utf-8")
    return entries


def tile(label, value, note=""):
    return (f'<div class="tile"><div class="tile-num">{value}</div>'
            f'<div class="tile-label">{label}</div>'
            f'<div class="tile-note">{note}</div></div>')


def main():
    raw = load_json(PROJECT / "1_find-the-posts/output/raw-posts.json", [])
    keepers = load_json(PROJECT / "2_sort-the-keepers/output/keepers.json", [])
    drafts = load_json(PROJECT / "5_make-it-sound-like-me/output/final-drafts.json", [])
    citations = load_json(PROJECT / "9_check-the-citations/output/citation-log.json", [])
    bank = load_json(PROJECT / "content/question-bank.json", [])

    blog_dir = PROJECT / "content/blog"
    published = len(list(blog_dir.glob("*.md"))) if blog_dir.exists() else 0
    pending_dir = blog_dir / "pending"
    pending = len(list(pending_dir.glob("*.md"))) if pending_dir.exists() else 0
    orig_dir = PROJECT / "10_write-original-posts/output"
    month = date.today().strftime("%Y-%m")
    originals = len(list(orig_dir.glob(f"original-posts-{month}*.md"))) if orig_dir.exists() else 0

    value_only = sum(1 for k in keepers if k.get("value_only"))
    brand_ok = len(keepers) - value_only
    priority = sum(1 for k in keepers if k.get("priority"))
    competitor = sum(1 for k in keepers if "competitor-mention" in (k.get("tags") or []))
    funnel_mix = {s: sum(1 for k in keepers if k.get("funnel") == s)
                  for s in ("TOFU", "MOFU", "BOFU")}

    history = snapshot({"scraped": len(raw), "kept": len(keepers), "drafted": len(drafts),
                        "priority": priority, "competitor": competitor})

    latest = citations[-1] if citations else None
    cit_pct = latest["pct"] if latest else BASELINE_PCT
    cit_note = f'{latest["cited"]} of {latest["total"]} · {latest["source"]}' if latest else "no checks yet"
    ratio_warn = brand_ok > max(1, len(keepers)) / 10
    ratio_note = "over 10% brand-eligible — lean value-only" if ratio_warn else "healthy (9-to-1 respected)"

    trend_rows = "".join(
        f'<tr><td>{e["date"]}</td><td>{e["scraped"]}</td><td>{e["kept"]}</td>'
        f'<td>{e["drafted"]}</td><td>{e["priority"]}</td><td>{e["competitor"]}</td></tr>'
        for e in history[-14:]
    )
    cit_rows = "".join(
        f'<tr><td>{e["date"]}</td><td>{e["cited"]} / {e["total"]}</td>'
        f'<td><b>{e["pct"]}%</b></td><td>{e.get("source","")}</td></tr>'
        for e in citations
    )
    top_q = "".join(
        f'<li>"{q["question"]}" <span class="dim">(r/{q["subreddit"]}, seen {q["times_seen"]}x)</span></li>'
        for q in sorted(bank, key=lambda q: -q.get("times_seen", 1))[:5]
    ) or "<li class='dim'>question bank is empty — run build_question_bank.py</li>"

    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mission Control · Safe Harbor</title>
<style>
  :root {{ --navy:#1E3A5F; --teal:#2A7A6E; --cream:#F5F1E8; --border:#ddd6c8; --warn:#9A3412; }}
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  body {{ font-family:'Segoe UI',system-ui,sans-serif; background:var(--cream); color:#1a1a1a; padding-bottom:60px; }}
  .topbar {{ background:var(--navy); color:#fff; padding:20px 24px; text-align:center; }}
  .topbar h1 {{ font-size:24px; }} .topbar .date {{ opacity:.7; font-size:14px; }}
  .wrap {{ max-width:860px; margin:24px auto 0; padding:0 20px; }}
  .tiles {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:12px; }}
  .tile {{ background:#fff; border:1px solid var(--border); border-radius:14px; padding:16px; text-align:center; }}
  .tile-num {{ font-size:30px; font-weight:800; color:var(--teal); }}
  .tile-label {{ font-size:13px; font-weight:700; color:var(--navy); margin-top:2px; }}
  .tile-note {{ font-size:12px; color:#6b7280; margin-top:4px; }}
  .warn .tile-num {{ color:var(--warn); }}
  h2 {{ font-size:15px; text-transform:uppercase; letter-spacing:1px; color:#6b7280; margin:28px 4px 10px; }}
  table {{ width:100%; background:#fff; border:1px solid var(--border); border-radius:12px; border-collapse:separate; border-spacing:0; overflow:hidden; font-size:14px; }}
  th,td {{ padding:8px 12px; text-align:left; border-bottom:1px solid var(--border); }}
  th {{ background:var(--navy); color:#fff; font-size:12px; }} tr:last-child td {{ border-bottom:none; }}
  ul {{ background:#fff; border:1px solid var(--border); border-radius:12px; padding:14px 14px 14px 32px; font-size:15px; line-height:1.9; }}
  .dim {{ color:#6b7280; font-size:13px; }}
</style></head><body>
<div class="topbar"><h1>Mission Control</h1><div class="date">{date.today().strftime("%A, %B %d, %Y")}</div></div>
<div class="wrap">
  <h2>The number that matters</h2>
  <div class="tiles">
    {tile("AI citation rate", f"{cit_pct}%", cit_note + f" · baseline {BASELINE_PCT}%")}
    {tile("Blogs live / pending", f"{published} / {pending}", "published on site / awaiting approval")}
    {tile("Original posts this month", originals, "target: 2–4, always disclosed")}
  </div>
  <h2>Today's pipeline</h2>
  <div class="tiles">
    {tile("Scraped", len(raw))}
    {tile("Kept", len(keepers))}
    {tile("Priority (target-query)", priority)}
    {tile("Competitor mentions", competitor)}
    {tile("Funnel T/M/B", f'{funnel_mix["TOFU"]}/{funnel_mix["MOFU"]}/{funnel_mix["BOFU"]}')}
  </div>
  <h2>9-to-1 ratio check</h2>
  <div class="tiles">
    {tile("Value-only keepers", value_only)}
    <div class="tile{' warn' if ratio_warn else ''}"><div class="tile-num">{brand_ok}</div>
      <div class="tile-label">Brand-eligible</div><div class="tile-note">{ratio_note}</div></div>
  </div>
  <h2>Citation history (Room 9)</h2>
  <table><tr><th>Date</th><th>Cited</th><th>Rate</th><th>Source</th></tr>{cit_rows}</table>
  <h2>Top questions people keep asking (next blog topics)</h2>
  <ul>{top_q}</ul>
  <h2>Last 14 runs</h2>
  <table><tr><th>Date</th><th>Scraped</th><th>Kept</th><th>Drafted</th><th>Priority</th><th>Competitor</th></tr>{trend_rows}</table>
</div></body></html>"""

    OUTDIR.mkdir(parents=True, exist_ok=True)
    TRACKER.write_text(html, encoding="utf-8")
    print(f"Wrote {TRACKER} — open it, or it publishes with the dashboard (/tracker.html).")


if __name__ == "__main__":
    main()
