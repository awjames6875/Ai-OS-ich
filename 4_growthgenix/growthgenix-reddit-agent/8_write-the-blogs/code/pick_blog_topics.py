"""
pick_blog_topics.py — Room 8: Write The Blogs (topic selection).
60% DETERMINISTIC. No AI. Picks the month's 2-4 blog topics.

Priority order:
1. UNTAPPED target queries (nobody is cited for these yet — clearest AEO win)
2. Question-bank questions by times_seen (highest real demand)
Skips topics already covered in content/blog/ (word-overlap on slugs).

    python pick_blog_topics.py

Writes output/blog-queue.json. Then the adam-story-blog-engine skill drafts each
topic to content/blog/pending/, Adam approves, publish_blog.py pushes them live.
"""

import json
import re
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
PROJECT = BASE.parent
OUTPUT = BASE / "output" / "blog-queue.json"
BANK_JSON = PROJECT / "content" / "question-bank.json"
BLOG_DIR = PROJECT / "content" / "blog"
TARGET_QUERIES_FILE = Path(
    r"C:\Users\1alph\.claude\skills\safeharbor-reddit-triage\references\target-queries.md"
)
MAX_TOPICS = 4

STOPWORDS = {"what", "when", "does", "your", "with", "that", "this", "have", "from", "will"}


def significant_words(text: str) -> set:
    return {w for w in re.findall(r"[a-z]+", text.lower()) if len(w) >= 4 and w not in STOPWORDS}


def load_untapped_queries() -> list:
    """Rows from target-queries.md whose cited column says UNTAPPED."""
    if not TARGET_QUERIES_FILE.exists():
        return []
    rows = []
    for line in TARGET_QUERIES_FILE.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or set(line.strip()) <= {"|", "-", " ", ":"}:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 4 and cells[0].lower() != "query" and cells[3].upper() == "UNTAPPED":
            rows.append({"topic": cells[0], "funnel": cells[2].upper(),
                         "source": "target-query UNTAPPED"})
    return rows


def load_bank_questions() -> list:
    if not BANK_JSON.exists():
        return []
    bank = json.loads(BANK_JSON.read_text(encoding="utf-8"))
    return [{"topic": e["question"], "funnel": e.get("funnel"),
             "source": f"question-bank (seen {e['times_seen']}x)"}
            for e in sorted(bank, key=lambda e: -e.get("times_seen", 1))]


def existing_topic_words() -> list:
    """Word-sets of every published + pending blog slug."""
    slugs = []
    for folder in (BLOG_DIR, BLOG_DIR / "pending"):
        if folder.exists():
            slugs += [f.stem for f in folder.glob("*.md")]
    return [significant_words(s.replace("-", " ")) for s in slugs]


def main():
    covered = existing_topic_words()
    picked, skipped = [], []

    for cand in load_untapped_queries() + load_bank_questions():
        if len(picked) >= MAX_TOPICS:
            break
        words = significant_words(cand["topic"])
        if any(len(words & c) >= 2 for c in covered):
            skipped.append(cand["topic"])
            continue
        picked.append(cand)
        covered.append(words)  # don't pick two near-identical topics in one batch

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(picked, indent=2), encoding="utf-8")

    if not picked:
        print("No topics picked. Is target-queries.md created and the question bank built?")
    for i, t in enumerate(picked, 1):
        print(f"{i}. [{t.get('funnel') or '-'}] {t['topic']}  <- {t['source']}")
    if skipped:
        print(f"Skipped {len(skipped)} already-covered topics: " + "; ".join(skipped[:5]))
    print(f"Queue written: {OUTPUT}")
    print('Next: say "write the blogs" — the blog engine drafts each queued topic.')


if __name__ == "__main__":
    main()
