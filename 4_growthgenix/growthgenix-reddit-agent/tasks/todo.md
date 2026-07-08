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

## Tier 1 dress rehearsal — PASSED (July 8, ~1:30 AM)
Full pipeline tested on REAL speech, $0 spent:
- [x] Episode #1 script written for real (KEEPER, awaiting Adam's review):
      11_make-the-episode/output/scripts/young-child-meltdowns-aggression-shame.md
      (408 words, 5 [CLIP] moments, voice source = adam-voice-learning SKILL.md
      since no standalone VOICE_DNA.md exists)
- [x] Stand-in narration: Windows TTS -> 3:14 test episode (robot voice, TEST ONLY)
- [x] whisper.cpp v1.9.1 installed (Adam approved): C:\Users\1alph\tools\whisper-cpp\
      Release\whisper-cli.exe, wired via HYPERFRAMES_WHISPER_PATH (setx, persistent)
- [x] Bug found + root-cause fixed in cut_shorts.py: `transcribe --json` prints
      METADATA pointing at transcript.json — now follows transcriptPath and stores
      the slug-specific sidecar
- [x] Result: 5/5 clips matched at 93-100%, all 26-33s (in band), all true
      1080x1920 with AAC audio. Whisper small.en transcribed 410 words in ~192s
      of speech.
- [x] All robot-voiced artifacts deleted (episode, transcript, shorts, WAV).
      Episode script kept.
Follow-up: CONTEXT.md/episode-format.md say "load VOICE_DNA.md" — should point at
adam-voice-learning SKILL.md instead.

## Tier 2 — real-Adam recording (NEXT, needs Adam ~10 min, $0)
Record yourself reading the episode script (16:9 landscape, one take fine), drop at
11_make-the-episode/output/episodes/young-child-meltdowns-aggression-shame.mp4,
then rerun cut_shorts + captions + titles. Output = REAL postable episode #1.

## Tier 3 — HeyGen avatar (paid, gated) — WIRED, awaiting Adam's RENDER
- [x] Keys in .env.local (HEYGEN_API_KEY + ELEVENLABS_API_KEY, gitignored)
- [x] Discovery (free reads): avatar group "Aj" (24 completed looks, 5 with motion,
      podcast-style looks uploaded Jul 8), voice = "Adam Studio voice" (his clone,
      b69a640f...). ElevenLabs NOT needed — HeyGen has voice+face. (EL key is also
      permission-scoped: no voices_read.)
- [x] render_avatar_episode.py built: --test renders first [CLIP] (~30s), typed
      RENDER gate verified (aborts clean), polls status, downloads to episodes/.
- [x] First run hit "Insufficient credit ('api' credits)" — failed safely, no
      charge. API credits are a separate wallet from web-app plan credits.
      Adam topped up. Also added --confirm RENDER flag (Adam types RENDER in
      the command itself) because the ! shell has no interactive stdin.
- [x] TEST RENDER DONE (July 8): Adam ran it with --confirm RENDER -> 18.2s clip,
      1920x1080 h264 + AAC, 3.3 MB, at output/episodes/
      young-child-meltdowns-aggression-shame.test.mp4. HeyGen skills
      (heygen-avatar/video/translate) also installed to .agents/skills/.
- [ ] ADAM: quality gate — does the test clip read as AI-slop or pass as you?
- [ ] If pass: full render (Adam runs, --confirm RENDER) -> clipper -> captions -> titles

Still open before the first REAL episode:
1. HeyGen avatar setup + Adam's approval before any paid render (hard gate)
2. VOICE_DNA.md loaded when drafting the first episode script
3. Whisper transcription untested on real speech (pipe-test.mp4 is silent —
   exercised via fake transcript fixtures instead); first real episode proves it
4. embedded-captions run end-to-end on a real short (identity pick: anchor default)
