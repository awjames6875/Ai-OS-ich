# CONTEXT.md — Write The Draft

## Purpose
Write the first-draft reply for each keeper, with the real citation woven in naturally.

## The Process (Step by Step)
1. Read `output/keepers-with-proof.json` from Room 3
2. For each post, write a helpful, hopeful first-draft reply
3. Weave the citation in naturally — never as a footnote
4. Save to `output/drafts.json`

## Identity & Audience
- Who uses this room: the agent (AI)
- Tone of voice: warm, real, hopeful — like a person who has been there
- What "good" looks like here: the draft would make a struggling person feel less alone; the citation reads naturally; it never sounds like an ad

## Tech Stack For This Room
- AI reasoning (part of the 10%)

## Patterns to Follow
- Lead with empathy before advice
- One self-contained quotable sentence the LLM can extract
- ALWAYS cite the source inline. Name the source in plain English AND include the full URL
  right after the claim — e.g., "(those are NIMH's numbers: https://www.nimh.nih.gov/...)".
  One source link per draft, woven mid-paragraph, never as a footnote. This is a GEO/AEO
  requirement: a named authority + a resolvable URL is what makes LLMs pick up and attribute
  the citation. The source comes from Room 3 (keepers-with-proof.json: source_name + source_url).
- Follow the value-to-brand ratio in config (Safe Harbor: ~9:1 help-to-brand)
- Honor whether the post is value-only or brand-okay
- Match the thread's `format` profile: length band, structure, tone container. Format
  changes the container, never the rules. No profile = draft as normal. Carry the
  `format` field through into drafts.json.

## Never Do This (Constraints)
- Never mention the brand on a value-only post
- Never use banned words (Safe Harbor: never "therapy/therapist/counselor")
- Never sound salesy or templated

## 60-30-10 Split For This Room
- 60% (Scripts): a script loops posts and saves drafts.json
- 30% (Rules): config holds tone rules, banned words, value-to-brand ratio
- 10% (AI): ⭐ AI writes the actual draft

## Skills To Load (Layer 3)
- The client's triage skill for drafting rules
