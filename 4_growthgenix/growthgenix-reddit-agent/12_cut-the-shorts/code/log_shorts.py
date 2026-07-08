"""
log_shorts.py — Room 12: Cut The Shorts (batch tracking).
60% DETERMINISTIC. No AI. Marks an episode's shorts batch done in
output/shorts-log.json so nothing gets clipped twice.

    python log_shorts.py <slug>

Run AFTER Adam has posted the shorts by hand.
"""

import json
import sys
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
LOG_FILE = BASE / "output" / "shorts-log.json"
SHORTS_DIR = BASE / "output" / "shorts"


def main():
    if len(sys.argv) != 2:
        print("Usage: python log_shorts.py <slug>")
        return
    slug = sys.argv[1]

    manifest_file = SHORTS_DIR / slug / "manifest.json"
    if not manifest_file.exists():
        sys.exit(f"No manifest for '{slug}' — run cut_shorts.py {slug} first.")

    log = json.loads(LOG_FILE.read_text(encoding="utf-8")) if LOG_FILE.exists() else []
    if any(e["slug"] == slug for e in log):
        print(f"Already logged: {slug}")
        return

    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    log.append({"slug": slug, "shorts": len(manifest),
                "date": date.today().isoformat()})
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    LOG_FILE.write_text(json.dumps(log, indent=2), encoding="utf-8")
    print(f"Logged: {slug} ({len(manifest)} shorts). Episode is done end to end.")


if __name__ == "__main__":
    main()
