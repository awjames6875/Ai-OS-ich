# HANDOFF — Session Briefing (written July 8, 2026, late night)

Read this first next session. Pipeline root:
`4_growthgenix/growthgenix-reddit-agent/` (client #1 = Safe Harbor Behavioral Health)

## 1. WHAT GOT DONE (July 7-8 overnight — Day 2, video lane)

- **Environment verified** — Node v22.17.0, FFmpeg installed.
- **HyperFrames installed** — `npx skills add heygen-com/hyperframes --all` (20 skills:
  hyperframes core/CLI/animation, embedded-captions, media-use, etc.).
- **Room 11_make-the-episode built + smoke-tested** — turns a published blog into a
  2-3 min episode. Decisions locked with Adam: source = published blogs (they trace to
  real Reddit questions), lane split = HeyGen avatar ~70% / real Adam on camera ~30%
  (picker suggests real every 3rd episode), length 2-3 min. `pick_episode_topic.py`
  queues the next unused blog; `log_episode.py` prevents repeats;
  `skills/episode-format.md` = the spoken blog sandwich (answer in first 30s for AEO,
  [CLIP] markers for Room 12). Bug fixed: claude-mem's CLAUDE.md stub in content/blog/
  counted as a published post (excluded by name — same fix publish_blog.py got).
- **Render pipe PROVEN, $0** — hyperframes 0.7.42, lint/validate 0 errors, 10s MP4
  rendered locally in 23s: `11_make-the-episode/output/pipe-test.mp4`. Adam watched it.
- **Room 12_cut-the-shorts built + tested — IN-HOUSE clipper** (Adam reversed the
  earlier "OpusClip now" call mid-build; no subscription, sellable GrowthGenix asset).
  `cut_shorts.py <slug>`: local Whisper transcript -> matches the Room 11 script's
  [CLIP] paragraphs to word timestamps (refuses to guess under 60% overlap) -> ffmpeg
  cut + center-crop to 1080x1920 -> manifest.json. Then: "caption the shorts"
  (embedded-captions, anchor default, verbatim only) -> "title the shorts" (AI,
  question-first titles) -> ADAM posts by hand -> `log_shorts.py <slug>`.
  Verified end-to-end on fixtures (match, no-match, band warning, true 9:16 output).
- **Routing updated** — master CLAUDE.md has rows for Rooms 11+12 and a Video Lane
  section. Full detail: `tasks/todo.md` (Day 2 checklist + review).

## 2. CURRENT STATE — The 12 Rooms

Rooms 1-10 unchanged (daily Reddit pipeline + monthly blogs/citations/originals).
New video lane, per published blog:

| Room | Does |
|---|---|
| 11_make-the-episode | Blog -> 2-3 min episode script (Adam's voice) -> avatar (HeyGen, PAID-gated) or real-Adam render -> local captions/packaging |
| 12_cut-the-shorts | Episode -> 3-5 vertical shorts: Whisper + [CLIP] match + ffmpeg (all local, $0) -> embedded-captions -> AI titles -> human posts |

## 3. NEXT UP — First real episode (episode #1 already queued)

1. Queue is loaded: `young-child-meltdowns-aggression-shame`, avatar lane
   (`11_make-the-episode/output/episode-queue.json`)
2. Say **"write the episode"** — drafts the script (free; VOICE_DNA.md first)
3. HeyGen avatar setup + **Adam's explicit approval before the first paid render**
4. First real run also proves: Whisper on real speech, embedded-captions on a real
   short (both untested on real audio — fixtures only so far)

**HARD GATE: no paid API calls (HeyGen/ElevenLabs/Apify) without Adam's explicit
approval. Ask first, every time.**

## 4. OPEN ITEMS

- HeyGen avatar of Adam: not yet created/configured — blocker for the avatar lane.
- Blog sandwich AEO upgrade (FAQ blocks, answer-first sections) — still offered, not
  built. Adam says the word.
- Live slug-confirmation prompt in publish_blog.py still untested with a real draft
  (`--preview` first is the safe habit).
- Room 11/12 output folders (episodes, shorts, scripts, queues) stay LOCAL — the
  pipeline's own .gitignore already excludes every room's output/ directory.
- claude-mem keeps spraying stub CLAUDE.md files at junk paths (nested
  4_growthgenix/..., a literal `~/` folder) when scripts run from inside room dirs —
  cleaned twice now (July 7 + 8). Check for them before every commit.
