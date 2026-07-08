"""
render_avatar_episode.py — Room 11: Make The Episode (avatar lane render).
PAID API (HeyGen). The gate is baked in: nothing renders until Adam types RENDER.

Renders the queued episode script through Adam's HeyGen photo avatar ("Aj" group)
speaking with his cloned "Adam Studio voice".

    python render_avatar_episode.py           # full episode -> output/episodes/<slug>.mp4
    python render_avatar_episode.py --test    # first [CLIP] only (~30s) -> <slug>.test.mp4
    python render_avatar_episode.py --look <look_id>   # override the avatar look
    python render_avatar_episode.py --confirm RENDER   # Adam types RENDER in the
        command itself (for shells with no interactive stdin, e.g. the ! prefix)

On a quota/credit error HeyGen fails safely (error message, no charge) — the
script prints it verbatim and stops.
"""

import json
import re
import sys
import time
from pathlib import Path

import requests

BASE = Path(__file__).resolve().parents[1]
PROJECT = BASE.parent
QUEUE = BASE / "output" / "episode-queue.json"
SCRIPTS = BASE / "output" / "scripts"
EPISODES = BASE / "output" / "episodes"
ENV_LOCAL = PROJECT / ".env.local"

API = "https://api.heygen.com"
# Client-specific (Safe Harbor / Adam). Moves to config/client-config.md when
# client #2 arrives.
DEFAULT_LOOK_ID = "3ece824cc5994c7eaa0d18a8c1d87f14"  # "The Confident Professional" (motion)
VOICE_ID = "b69a640fc30d492e91464ad365ddec6b"          # "Adam Studio voice" (Adam's clone)
WPM = 140
POLL_SECONDS = 15
MAX_WAIT_MINUTES = 30


def load_api_key() -> str:
    for line in ENV_LOCAL.read_text(encoding="utf-8").splitlines():
        if line.startswith("HEYGEN_API_KEY="):
            return line.split("=", 1)[1].strip()
    sys.exit(f"HEYGEN_API_KEY not found in {ENV_LOCAL}")


def spoken_text(script_path: Path, test_only: bool) -> str:
    """The script minus frontmatter, ON SCREEN cues, and [CLIP] markers.
    test_only -> just the first [CLIP] paragraph."""
    body = re.sub(r"^---.*?---", "", script_path.read_text(encoding="utf-8"),
                  flags=re.DOTALL)
    paras = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
    paras = [p for p in paras if not p.upper().startswith("ON SCREEN:")]
    if test_only:
        paras = [p for p in paras if p.startswith("[CLIP]")][:1]
        if not paras:
            sys.exit("No [CLIP] paragraph found for --test.")
    text = "\n\n".join(paras).replace("[CLIP]", "")
    return re.sub(r"[ \t]+", " ", text).strip()


def confirm_or_abort(queue: dict, text: str, look_id: str, test_only: bool):
    words = len(text.split())
    print(f"Episode:  {queue['title']}")
    print(f"Mode:     {'TEST (first clip only)' if test_only else 'FULL episode'}")
    print(f"Words:    {words}  (~{words / WPM:.1f} min of avatar video)")
    print(f"Look:     {look_id}" + ("  (default: The Confident Professional)"
                                    if look_id == DEFAULT_LOOK_ID else "  (override)"))
    print(f"Voice:    Adam Studio voice ({VOICE_ID})")
    print("\nThis is a PAID HeyGen render. Credits will be spent.")
    if "--confirm" in sys.argv:
        if sys.argv[sys.argv.index("--confirm") + 1] == "RENDER":
            print("Confirmed via --confirm RENDER (typed by Adam in the command).")
            return
        sys.exit("Aborted: --confirm must be exactly RENDER. Nothing was sent to HeyGen.")
    try:
        answer = input('Type RENDER to proceed (anything else aborts): ').strip()
    except EOFError:
        sys.exit("\nAborted: no interactive keyboard here. Rerun with "
                 "--confirm RENDER (you type it in the command). "
                 "Nothing was sent to HeyGen.")
    if answer != "RENDER":
        sys.exit("Aborted. Nothing was sent to HeyGen.")


def main():
    test_only = "--test" in sys.argv
    look_id = DEFAULT_LOOK_ID
    if "--look" in sys.argv:
        look_id = sys.argv[sys.argv.index("--look") + 1]

    queue = json.loads(QUEUE.read_text(encoding="utf-8"))
    slug = queue["slug"]
    script_path = SCRIPTS / f"{slug}.md"
    if not script_path.exists():
        sys.exit(f"Missing script: {script_path}\nSay \"write the episode\" first.")

    text = spoken_text(script_path, test_only)
    confirm_or_abort(queue, text, look_id, test_only)

    headers = {"x-api-key": load_api_key(), "Content-Type": "application/json"}
    payload = {
        "title": f"{slug}{'-test' if test_only else ''}",
        "video_inputs": [{
            "character": {"type": "talking_photo", "talking_photo_id": look_id},
            "voice": {"type": "text", "voice_id": VOICE_ID, "input_text": text},
        }],
        "dimension": {"width": 1920, "height": 1080},
    }
    resp = requests.post(f"{API}/v2/video/generate", headers=headers,
                         json=payload, timeout=60)
    body = resp.json()
    if resp.status_code != 200 or body.get("error"):
        sys.exit(f"HeyGen refused the render (no charge on quota errors):\n"
                 f"HTTP {resp.status_code}: {json.dumps(body.get('error') or body, indent=2)}")
    video_id = body["data"]["video_id"]
    print(f"Render started: video_id={video_id}. Polling every {POLL_SECONDS}s...")

    deadline = time.time() + MAX_WAIT_MINUTES * 60
    while time.time() < deadline:
        time.sleep(POLL_SECONDS)
        status = requests.get(f"{API}/v1/video_status.get",
                              headers=headers, params={"video_id": video_id},
                              timeout=60).json().get("data") or {}
        state = status.get("status")
        print(f"  {state}")
        if state == "completed":
            out = EPISODES / (f"{slug}.test.mp4" if test_only else f"{slug}.mp4")
            out.parent.mkdir(parents=True, exist_ok=True)
            video = requests.get(status["video_url"], timeout=300)
            out.write_bytes(video.content)
            print(f"\nDone: {out}  ({len(video.content) / 1e6:.1f} MB)")
            if test_only:
                print("Watch it. Quality gate: does it read as AI-slop? "
                      "If it passes, run without --test for the full episode.")
            else:
                print("Next: python ../../12_cut-the-shorts/code/cut_shorts.py " + slug)
            return
        if state == "failed":
            sys.exit(f"Render FAILED: {json.dumps(status.get('error'), indent=2)}")
    sys.exit(f"Timed out after {MAX_WAIT_MINUTES} min. Check the video in your "
             f"HeyGen dashboard (video_id={video_id}).")


if __name__ == "__main__":
    main()
