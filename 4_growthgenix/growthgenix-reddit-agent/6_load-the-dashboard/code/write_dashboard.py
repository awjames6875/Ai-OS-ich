"""
write_dashboard.py - Room 6: Load The Dashboard
60% DETERMINISTIC. No AI. Builds ONE self-contained dashboard.html and cleans up old files.

Reads  ../5_make-it-sound-like-me/output/final-drafts.json  (from Room 5)
Reads  template/dashboard-template.html                     (UI shell; data injected inline)
Writes output/dashboard.html                               (OVERWRITTEN every run)

FRESH-EVERY-RUN GUARANTEE:
- dashboard.html is overwritten each run, so yesterday's posts are physically replaced.
- Any leftover/stale files in output/ (old data.js, dated dashboards) are deleted, so the
  folder always holds exactly ONE current dashboard.html. Nothing piles up.
"""

import json
import re
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
FINAL = BASE.parent / "5_make-it-sound-like-me" / "output" / "final-drafts.json"
TEMPLATE = BASE / "template" / "dashboard-template.html"
OUTDIR = BASE / "output"
OUTPUT = OUTDIR / "dashboard.html"

PLACEHOLDER = "/*__REDDIT_DATA__*/"


def clean_url(url):
    if not url:
        return ""
    if url.startswith("/"):
        url = "https://www.reddit.com" + url
    m = re.match(r"(https?://(?:www\.)?reddit\.com/r/[^/]+/comments/[^/?]+)/?", url)
    if m:
        return m.group(1) + "/"
    return url.split("?")[0]


def to_card(post):
    value_only = post.get("value_only", False)
    if value_only:
        tag = "Just help - do not mention Safe Harbor"
        rule = "Just be helpful. Do NOT mention Safe Harbor here."
    else:
        tag = "OK to mention Safe Harbor"
        rule = "You may gently mention Safe Harbor if it fits naturally."
    return {
        "priority": post.get("priority", False),
        "funnel": post.get("funnel"),
        "format": post.get("format"),
        "who": post.get("who", post.get("audience", "Someone who needs help")),
        "summary": post.get("summary", post.get("title", "")),
        "tag": tag,
        "rule": rule,
        "ruleType": "tooyoung" if post.get("too_young") else ("help" if value_only else "brand"),
        "fact": post.get("fact"),
        "redditUrl": clean_url(post.get("permalink", "")),
        "draft": post.get("draft", ""),
    }


def clean_old_files():
    """Delete stale artifacts so output/ holds only the fresh dashboard.html."""
    removed = []
    if OUTDIR.exists():
        for f in OUTDIR.iterdir():
            if f.name == "dashboard.html":
                continue  # this is the one we are about to refresh
            if f.suffix in (".js", ".json") or f.name.startswith("dashboard-"):
                try:
                    f.unlink()
                    removed.append(f.name)
                except Exception as e:
                    print("Could not delete " + f.name + " (" + str(e) + ") - skipping.")
    return removed


def main():
    if not FINAL.exists():
        print("No final drafts found. Run Room 5 first.")
        return
    if not TEMPLATE.exists():
        print("No template found at template/dashboard-template.html.")
        return

    drafts = json.loads(FINAL.read_text())
    cards = [to_card(d) for d in drafts]
    cards.sort(key=lambda c: not c["priority"])

    payload = {"date": date.today().strftime("%A, %B %d, %Y"), "posts": cards}
    data_js = "window.REDDIT_DATA = " + json.dumps(payload, indent=2) + ";"

    html = TEMPLATE.read_text().replace(PLACEHOLDER, data_js)

    OUTDIR.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(html)
    (OUTDIR / "index.html").write_text(html)  # served at the Netlify root URL
    removed = clean_old_files()

    print("Wrote " + str(len(cards)) + " posts into self-contained dashboard.html (overwrote previous run).")
    if removed:
        print("Cleaned up old files: " + ", ".join(removed))
    print("output/ now holds only the fresh dashboard.html. Open it directly.")

    # Auto-publish to GitHub -> Netlify auto-deploys the live link.
    try:
        import subprocess
        pub = BASE / "code" / "publish_to_github.sh"
        if pub.exists():
            r = subprocess.run(["bash", str(pub)], capture_output=True, text=True)
            print((r.stdout or "").strip() or (r.stderr or "").strip())
    except Exception as e:
        print("Publish step skipped:", e)


if __name__ == "__main__":
    main()
