# SKILL — Shorts Format (load before captioning or titling shorts)

Rules for turning episode clips into postable vertical shorts.
The spoken content is LOCKED — these rules shape the container only.

## Cut Rules (enforced by cut_shorts.py)
1. 15-45 seconds per short. The script warns outside this band.
2. 9:16 vertical, 1080x1920, center crop (episode subject is centered — avatar
   and teleprompter framing both put the face in the middle).
3. The cut starts ON the [CLIP] line — the hook is the first spoken second.
   No intros, no logos, no "wait for it".

## Caption Rules (embedded-captions skill, per short)
1. Captions ALWAYS — most viewers watch muted.
2. Default identity: `anchor` (quiet verbatim rail — the words must read).
   Adam can pick a louder identity per short; recommend one, let him choose.
3. Captions are VERBATIM — never paraphrase, never add words (honesty lock).
4. Contrast rules: run the skill's own probes; never bare light text on bright.

## Title + Post Caption Rules (the AI step — "title the shorts")
1. Load VOICE_DNA.md first. Titles sound like Adam, not like a marketer.
2. Question-first titles (AEO): lead with the real question the clip answers —
   the same question the Reddit thread and blog answered.
3. Language rules from /config/client-config.md apply to every word.
4. Soft CTA ONLY on the close-clip (the sermon-close short):
   safeharborbehavioralhealth.com / (918) 553-5746. All other shorts: no CTA.
5. No fabricated stats in captions — only what is spoken in the clip.
6. Hashtags: 3-5, plain (#parenting #recovery #oklahoma tier) — no spam walls.

## Posting Rules (Adam, by hand)
1. Watch every short before posting. Approval = you posting it.
2. Never schedule/auto-post from this room.
3. After posting the batch: `python code/log_shorts.py <slug>`.
