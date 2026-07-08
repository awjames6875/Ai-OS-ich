# SKILL — Episode Format (load before writing any episode script)

Turns ONE published blog post into a 2-3 minute spoken narration script.
The blog is the verified source of truth. The episode RETELLS it — never invents.

## Hard Rules
1. Facts, stats, and citations come ONLY from the source blog post. Nothing new.
2. Language rules from /config/client-config.md apply to every spoken + on-screen word.
3. 280-420 spoken words total (~140 wpm = 2-3 minutes). Count them.
4. No paid API call (HeyGen, ElevenLabs) without Adam's explicit approval, every time.

## Structure (the blog sandwich, spoken)
| Beat | Time | What happens |
|---|---|---|
| Cold-open hook | 0:00-0:10 | The blog's story moment or contrarian line — never "hi, I'm Adam" |
| The turn (answer) | 0:10-0:40 | Plain-language answer to the question — AEO rule: answered inside the first 30 seconds |
| The story | 0:40-1:30 | The blog's story, compressed. One parent, one moment. |
| The science | 1:30-2:00 | The blog's real citation, spoken plainly ("researchers at X found...") + source name on screen |
| Three steps | 2:00-2:30 | The blog's action steps, numbered out loud |
| Sermon close | 2:30-3:00 | Hope + belonging, Adam's voice. Soft CTA: safeharborbehavioralhealth.com / (918) 553-5746 |

## Voice
- Load VOICE_DNA.md (adam-voice-learning) BEFORE writing. Non-negotiable.
- Write for the EAR, not the eye: short sentences, contractions, no headings read aloud.
- Talk to ONE parent, not an audience.

## Clip Moments (for Room 12 / OpusClip)
Mark 3-5 moments in the script with `[CLIP]` — self-contained 15-45 second stretches
that work with zero context: the hook, the turn, one story beat, one step, the close.

## Script File Format (output/scripts/<slug>.md)
```
---
slug: <slug>
lane: avatar | real
source_blog: content/blog/<slug>.md
word_count: <n>
---
[CLIP] <spoken text...>

<spoken text...>

ON SCREEN: <any on-screen text, one line per cue>
```

## Lane Notes
- **Avatar lane:** script text goes to HeyGen as-is (PAID — approval gate first).
- **Real lane:** script becomes Adam's teleprompter copy. Same structure, same rules.
- Either lane: captions + packaging happen locally (embedded-captions skill, free).
