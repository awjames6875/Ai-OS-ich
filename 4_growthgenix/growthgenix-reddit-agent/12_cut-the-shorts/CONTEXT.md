# CONTEXT.md — Cut The Shorts

## Purpose
Turn a finished Room 11 episode (16:9, 2-3 min) into 3-5 vertical shorts (9:16,
15-45s) with styled captions — the in-house clipper. $0 per clip, everything runs
locally: the episode script's [CLIP] markers say WHERE to cut (deterministic), local
Whisper says WHEN (timestamps), ffmpeg does the cutting, the embedded-captions skill
does the styling. Adam posts by hand. This is a GrowthGenix asset — no OpusClip
subscription, and it runs the same for every future client.

## The Process (Step by Step) — per finished episode
1. Run `python code/cut_shorts.py <slug>`
   -> transcribes the episode locally (Whisper, free — reuses the transcript if it
      already exists), matches each [CLIP] paragraph from the Room 11 script to
      timestamps, cuts + center-crops each clip to 1080x1920
   -> shorts land in output/shorts/<slug>/short-N.mp4 + manifest.json
2. Say **"caption the shorts"** — the agent runs the embedded-captions skill on each
   short (`anchor` identity default — words must read; Adam can pick a louder one)
3. Say **"title the shorts"** — AI fills each manifest entry's title + caption in
   Adam's voice (question-first titles, rules in skills/shorts-format.md)
4. ADAM: watch each short (~30s each). Your approval = posting it.
5. Post by hand (TikTok / Reels / Shorts). Then run
   `python code/log_shorts.py <slug>` so this episode never gets clipped twice.

## Identity & Audience
- Who uses this room: Adam + the agent, once per finished episode (~20 min total)
- What "good" looks like here: a short that hooks in the first second, reads clean
  with captions muted, and stands alone with zero context

## Never Do This (Constraints — LOCKED)
- NEVER auto-post anywhere. Adam watches every short and posts by hand — same rule
  as Room 7.
- NEVER call a paid API. This room is 100% local (Whisper, ffmpeg, captions). If a
  step ever needs a paid service, ask Adam first, every time.
- Captions NEVER change the spoken words — verbatim only (honesty lock).
- Language rules from /config/client-config.md apply to every title, caption, and
  on-screen word.

## 60-30-10 Split For This Room
- 60% (Scripts): cut_shorts.py (transcribe -> match -> cut -> manifest) +
  log_shorts.py (tracking) + the embedded-captions pipeline's own scripts
- 30% (Rules): skills/shorts-format.md + config/client-config.md + the [CLIP]
  markers Room 11 already authored
- 10% (AI): titles + post captions in Adam's voice — judgment work only

## Skills To Load (Layer 3)
- skills/shorts-format.md — cut, caption, and title rules (load before steps 2-3)
- embedded-captions — the caption pipeline (agent runs it per short)
- adam-voice-learning (VOICE_DNA.md) — before writing titles/captions
