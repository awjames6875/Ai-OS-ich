"""
log_episode.py — Room 11: Make The Episode (episode tracking).
60% DETERMINISTIC. No AI. Appends a finished episode to output/episodes-log.json
so pick_episode_topic.py never repeats a topic.

    python log_episode.py <slug>

Reads the lane from output/episode-queue.json if the slug matches, else asks nothing
and logs the lane as "unknown".
"""

import json
import sys
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
LOG_FILE = BASE / "output" / "episodes-log.json"
QUEUE = BASE / "output" / "episode-queue.json"


def main():
    if len(sys.argv) != 2:
        print("Usage: python log_episode.py <slug>")
        return
    slug = sys.argv[1]

    log = json.loads(LOG_FILE.read_text(encoding="utf-8")) if LOG_FILE.exists() else []
    if any(e["slug"] == slug for e in log):
        print(f"Already logged: {slug}")
        return

    lane = "unknown"
    if QUEUE.exists():
        queue = json.loads(QUEUE.read_text(encoding="utf-8"))
        if queue.get("slug") == slug:
            lane = queue.get("lane", "unknown")

    log.append({"slug": slug, "lane": lane, "date": date.today().isoformat()})
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    LOG_FILE.write_text(json.dumps(log, indent=2), encoding="utf-8")
    print(f"Logged episode #{len(log)}: {slug} (lane: {lane})")
    print("Next by hand: embed on the blog post + upload to YouTube, then Room 12 for shorts.")


if __name__ == "__main__":
    main()
