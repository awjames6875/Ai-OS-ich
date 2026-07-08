"""
cut_shorts.py — Room 12: Cut The Shorts (the in-house clipper).
60% DETERMINISTIC. No AI, no paid APIs. Cuts a Room 11 episode into vertical shorts.

The Room 11 script marks [CLIP] paragraphs — those decide WHERE to cut. Local Whisper
timestamps decide WHEN. ffmpeg cuts + center-crops 16:9 -> 9:16 (1080x1920).

    python cut_shorts.py <slug>

Inputs (from Room 11):
    ../11_make-the-episode/output/episodes/<slug>.mp4
    ../11_make-the-episode/output/scripts/<slug>.md
Outputs:
    output/shorts/<slug>/short-N.mp4 + manifest.json (title/caption left empty
    for the AI step — say "title the shorts")
"""

import json
import re
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
PROJECT = BASE.parent
ROOM11_OUT = PROJECT / "11_make-the-episode" / "output"
SHORTS_DIR = BASE / "output" / "shorts"

PAD_SECONDS = 0.3
MIN_LEN, MAX_LEN = 15, 45  # shorts-format.md band — warn outside, still cut


def words_of(text: str) -> list:
    return re.findall(r"[a-z0-9']+", text.lower())


def load_clip_texts(script_path: Path) -> list:
    """Paragraphs starting with [CLIP] in the Room 11 episode script."""
    body = re.sub(r"^---.*?---", "", script_path.read_text(encoding="utf-8"),
                  flags=re.DOTALL)  # strip frontmatter
    clips = []
    for para in re.split(r"\n\s*\n", body):
        para = para.strip()
        if para.startswith("[CLIP]"):
            text = para[len("[CLIP]"):].strip()
            # drop ON SCREEN cue lines — they are not spoken
            text = "\n".join(l for l in text.splitlines()
                             if not l.strip().upper().startswith("ON SCREEN:"))
            clips.append(text.strip())
    return clips


def load_transcript_units(episode: Path) -> list:
    """Normalized [{text, start, end}] from the transcript, transcribing if needed.
    Accepts word-level or segment-level Whisper JSON shapes."""
    sidecar = episode.with_suffix(".transcript.json")
    if not sidecar.exists():
        print("Transcribing locally (Whisper via hyperframes — free, no API)...")
        result = subprocess.run(
            ["npx", "hyperframes", "transcribe", str(episode), "--json",
             "--dir", str(episode.parent)],
            capture_output=True, text=True, shell=True)
        if result.returncode != 0:
            sys.exit(f"Transcription failed:\n{result.stderr[-2000:]}")
        sidecar.write_text(result.stdout, encoding="utf-8")

    data = json.loads(sidecar.read_text(encoding="utf-8"))
    for key in ("words", "segments", "transcript", "entries"):
        if isinstance(data, dict) and isinstance(data.get(key), list):
            data = data[key]
            break
    if not isinstance(data, list):
        sys.exit(f"Unrecognized transcript shape in {sidecar} — expected a list "
                 "of words/segments. Open the file and check.")
    units = []
    for u in data:
        text = u.get("word") or u.get("text") or ""
        if text.strip() and u.get("start") is not None and u.get("end") is not None:
            units.append({"text": text, "start": float(u["start"]),
                          "end": float(u["end"])})
    if not units:
        sys.exit(f"No timed units found in {sidecar}.")
    return units


def match_clip(clip_words: list, units: list):
    """Best contiguous unit window covering the clip's words. Returns
    (start, end, score) or None. Pure set-overlap — good enough for narration."""
    target = set(clip_words)
    best = None
    for i in range(len(units)):
        seen, count = set(), 0
        for j in range(i, len(units)):
            unit_words = words_of(units[j]["text"])
            seen.update(w for w in unit_words if w in target)
            count += len(unit_words)
            if count >= len(clip_words):
                score = len(seen) / max(len(target), 1)
                if best is None or score > best[2]:
                    best = (units[i]["start"], units[j]["end"], score)
                break
    return best if best and best[2] >= 0.6 else None


def cut(episode: Path, start: float, end: float, out: Path):
    """Cut + center-crop 16:9 -> 9:16 (1080x1920). Re-encodes for frame accuracy."""
    start = max(0.0, start - PAD_SECONDS)
    cmd = ["ffmpeg", "-y", "-ss", f"{start:.2f}", "-to", f"{end + PAD_SECONDS:.2f}",
           "-i", str(episode),
           "-vf", "crop=ih*9/16:ih,scale=1080:1920",
           "-c:v", "libx264", "-crf", "20", "-preset", "veryfast",
           "-c:a", "aac", "-b:a", "128k", str(out)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(f"ffmpeg failed on {out.name}:\n{result.stderr[-2000:]}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python cut_shorts.py <slug>")
        return
    slug = sys.argv[1]
    episode = ROOM11_OUT / "episodes" / f"{slug}.mp4"
    script = ROOM11_OUT / "scripts" / f"{slug}.md"
    for p in (episode, script):
        if not p.exists():
            sys.exit(f"Missing: {p}\nFinish the episode in Room 11 first.")

    clips = load_clip_texts(script)
    if not clips:
        sys.exit("No [CLIP] markers in the script. Room 11's episode-format.md "
                 "requires 3-5 — add them and rerun.")
    units = load_transcript_units(episode)

    out_dir = SHORTS_DIR / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest, skipped = [], []

    for n, text in enumerate(clips, 1):
        hit = match_clip(words_of(text), units)
        if not hit:
            skipped.append(n)
            print(f"short-{n}: NO MATCH in transcript (below 60% overlap) — "
                  "skipped, not guessing. Check the script vs the spoken audio.")
            continue
        start, end, score = hit
        length = end - start
        band = "" if MIN_LEN <= length <= MAX_LEN else \
            f"  WARNING: {length:.0f}s is outside the {MIN_LEN}-{MAX_LEN}s band"
        out = out_dir / f"short-{n}.mp4"
        cut(episode, start, end, out)
        manifest.append({"file": out.name, "start": round(start, 2),
                         "end": round(end, 2), "seconds": round(length, 1),
                         "match_score": round(score, 2), "spoken_text": text,
                         "title": "", "caption": "", "posted": False})
        print(f"short-{n}: {start:.1f}s -> {end:.1f}s ({length:.0f}s, "
              f"match {score:.0%}){band}")

    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2),
                                           encoding="utf-8")
    print(f"\n{len(manifest)} short(s) in {out_dir}"
          + (f" — {len(skipped)} skipped: {skipped}" if skipped else ""))
    print('Next: say "caption the shorts" (embedded-captions), then '
          '"title the shorts" (AI fills manifest titles/captions).')


if __name__ == "__main__":
    main()
