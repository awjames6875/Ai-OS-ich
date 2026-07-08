# TODO — Day 2: Video Lane (Room 11 + test render)

## Done
- [x] Step 1 — Verify Node 22+ (v22.17.0) and FFmpeg (2026 build) installed
- [x] Step 2 — `npx skills add heygen-com/hyperframes --all` (20 skills installed)

## Step 3 — Build Room 11_make-the-episode — DONE
Decisions locked with Adam: source = published blogs (trace to real Reddit questions),
lane split = HeyGen avatar ~70% / real Adam ~30%, length = 2-3 min,
Room 12 shorts = OpusClip now, in-house clipper later.
- [x] Created `11_make-the-episode/` with CONTEXT.md, code/, output/, skills/
- [x] `code/pick_episode_topic.py` (60%): picks next published blog not yet an
      episode, suggests lane (every 3rd = real), writes output/episode-queue.json.
      Excludes claude-mem's CLAUDE.md stub (same bug publish_blog.py had). Smoke-tested.
- [x] `code/log_episode.py` (60%): logs finished episodes so topics never repeat. Tested.
- [x] `skills/episode-format.md` (30% rules): blog sandwich spoken — hook, answer
      in first 30s (AEO), story, science, 3 steps, sermon close; [CLIP] markers for OpusClip
- [x] AI step (10%): "write the episode" documented in CONTEXT.md
- [x] Master CLAUDE.md: routing table row + Video Lane section added

## Step 4 — Test render (prove the pipe) — DONE
- [x] `npx hyperframes init pipe-test --example warm-grain` (hyperframes 0.7.42)
- [x] Lint + validate: 0 errors (stock-example warnings only)
- [x] Rendered locally, ZERO paid APIs: 10.0s MP4, 2.6 MB, 23s render time
      -> proof saved: 11_make-the-episode/output/pipe-test.mp4
      (stock example is 10s, not 15 — pipe proof is identical, didn't hack timings)

## Step 5 — Room 12_cut-the-shorts — DONE (in-house clipper)
Adam reversed the OpusClip decision mid-build: in-house clipper NOW, no subscription.
- [x] `code/cut_shorts.py` (60%): local Whisper transcript -> matches the Room 11
      script's [CLIP] paragraphs to word timestamps (>=60% overlap or it refuses to
      guess) -> ffmpeg cut + center-crop to 1080x1920 -> manifest.json with empty
      title/caption fields for the AI step. Zero paid APIs.
- [x] `code/log_shorts.py` (60%): batch tracking, dedup tested
- [x] `skills/shorts-format.md` (30%): 15-45s band, hook-first cuts, captions always
      (anchor default, verbatim only), question-first titles, CTA only on close-clip
- [x] CONTEXT.md + master CLAUDE.md routing row + Video Lane rewrite
- [x] Verified end-to-end on fixtures: [CLIP] parse, 100% match with correct
      timestamps, no-match branch skips cleanly, band warning fires, output is true
      1080x1920. Fixtures cleaned up.

## Hard gate
NO paid API calls (HeyGen, ElevenLabs, HiggsField, Apify) without Adam's explicit
approval. Ask first, every time. The step-4 test render is 100% local and free.

## Open questions for Adam (blocking step 3)
1. Episode source: published blog posts (recommended) or question bank directly?
2. Episode format: faceless explainer (free, local) vs HeyGen avatar (paid)?
3. Target episode length?

## Review (July 7-8, 2026, late night)
Day 2 COMPLETE — all 5 steps. Environment verified (Node 22.17, FFmpeg), 20
HyperFrames skills installed, Rooms 11 AND 12 built, smoke-tested, and wired into
the master router. The whole video lane is $0 so far: render pipe proven with a
real local MP4, and the shorts clipper is 100% local (Whisper + ffmpeg +
embedded-captions — Adam dropped OpusClip mid-build in favor of building our own,
which is also a sellable GrowthGenix asset). New code is 4 small Python scripts
(~250 lines), all style-matched to Room 8. One bug found + fixed: claude-mem's
CLAUDE.md stub in content/blog/ counted as a published post (excluded by name,
same fix publish_blog.py got).

Still open before the first REAL episode:
1. HeyGen avatar setup + Adam's approval before any paid render (hard gate)
2. VOICE_DNA.md loaded when drafting the first episode script
3. Whisper transcription untested on real speech (pipe-test.mp4 is silent —
   exercised via fake transcript fixtures instead); first real episode proves it
4. embedded-captions run end-to-end on a real short (identity pick: anchor default)
