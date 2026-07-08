# CONTEXT.md — Make The Episode

## Purpose
Turn a published blog post into a 2-3 minute video episode. The blog already traces back
to a real Reddit question (Room 2 found it, Room 3 verified the citation, Room 8 published
it) — the episode is that same answer retold on camera. Each episode gets embedded on its
blog post (VideoObject schema + transcript) and uploaded to YouTube, so the video, the
blog, and the Reddit reply all reinforce the same question. Room 12 cuts shorts from it.

## Two Lanes (who is on camera)
- **Avatar lane (~70%)** — HeyGen avatar of Adam delivers the script. PAID per render.
- **Real-Adam lane (~30%)** — Adam records himself delivering the same script.
  This lane is the authenticity anchor — recovery and parenting audiences trust a real face.
- The picker suggests the lane (every 3rd episode = real). Adam can always override.

## The Process (Step by Step)
1. Run `python code/pick_episode_topic.py`
   -> picks the next published blog not yet made into an episode, suggests the lane,
      writes output/episode-queue.json
2. Say **"write the episode"** — AI drafts the 2-3 min narration script from the blog
   (VOICE_DNA.md FIRST, rules in skills/episode-format.md, facts ONLY from the blog)
   -> script lands in output/scripts/<slug>.md with 3-5 clip moments marked for Room 12
3. ADAM: read the script (~3 min). Your approval = moving to render.
4. Render the episode:
   - Avatar lane: HeyGen render — **PAID. Adam approves before every call. No exceptions.**
   - Real lane: Adam records himself reading the script, drops the file in output/raw/
5. Package locally (free): captions via the embedded-captions skill + ffmpeg
   -> final MP4 in output/episodes/<slug>.mp4
6. Run `python code/log_episode.py <slug>` — appends to output/episodes-log.json so the
   picker never repeats a topic. Then: embed on the blog post + upload to YouTube by hand,
   and hand the MP4 to Room 12 (OpusClip) for shorts.

## Identity & Audience
- Who uses this room: Adam + the agent, weekly-ish (one episode per published blog)
- What "good" looks like here: an episode that sounds like Adam talking to one parent,
  answers the question in the first 30 seconds, and gives Room 12 3-5 cuttable moments

## Never Do This (Constraints — LOCKED)
- NEVER call HeyGen, ElevenLabs, or ANY paid API without Adam's explicit approval — ask
  first, every single time
- NEVER add a fact, stat, or citation that is not in the source blog post (the blog is
  the verified source of truth; the episode retells, never invents)
- NEVER auto-upload or auto-publish anywhere — Adam embeds and uploads by hand
- Language rules from /config/client-config.md apply to every spoken and on-screen word

## 60-30-10 Split For This Room
- 60% (Scripts): pick_episode_topic.py picks + assigns lane; log_episode.py tracks;
  ffmpeg/captions packaging is deterministic
- 30% (Rules): skills/episode-format.md + config/client-config.md + the source blog post
- 10% (AI): rewriting the blog into spoken narration in Adam's voice — judgment work only

## Skills To Load (Layer 3)
- skills/episode-format.md — episode structure + lane rules (load before writing)
- adam-voice-learning (VOICE_DNA.md) — mandatory before drafting
- embedded-captions + hyperframes — for the local packaging step (render/captions)
