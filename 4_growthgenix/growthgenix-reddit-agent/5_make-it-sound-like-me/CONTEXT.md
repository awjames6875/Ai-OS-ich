# CONTEXT.md — Make It Sound Like Me ⭐

## Purpose
Run every draft through the client's voice clone so it sounds unmistakably like them. This is the quality gate — no draft moves forward until it sounds human and authentic.

## The Process (Step by Step)
1. Read `output/drafts.json` from Room 4
2. Read the client's voice file from the path in config
3. Rewrite each draft in the client's authentic voice
4. Check it clears the bar: "would this make someone at 2am feel less alone and more hopeful?"
5. Save to `output/final-drafts.json`

## Identity & Audience
- Who uses this room: the agent (AI), using the voice clone
- Tone of voice: exactly the client's — their phrases, rhythm, signature moves
- What "good" looks like here: a stranger couldn't tell AI wrote it; it sounds like the client on their best day

## Tech Stack For This Room
- AI reasoning (the most important slice of the 10%)
- Voice DNA file (Safe Harbor/Adam: VOICE_DNA.md)

## Patterns to Follow
- Match signature phrases (Adam: "See, the thing is...", "Here's what you need to understand")
- Match rhythm — short punches, lists of three, CAPS for emphasis
- End with empowerment / hope
- Preserve the draft's format matching (length band, structure from the `format` field) —
  the voice rewrite must not inflate a short casual reply into an essay. Carry `format`
  through into final-drafts.json.

## Never Do This (Constraints)
- Never let a draft pass that sounds generic or AI-written
- Never lose the hope — that's the whole point
- Never skip this room to save time

## 60-30-10 Split For This Room
- 60% (Scripts): a script loops drafts and saves final-drafts.json
- 30% (Rules): the voice DNA file is the constraint (the "factory" config)
- 10% (AI): ⭐⭐ AI does the voice rewrite — the single most important AI task in the whole agent

## Skills To Load (Layer 3)
- adam-voice-learning (or the client's equivalent voice clone skill)
