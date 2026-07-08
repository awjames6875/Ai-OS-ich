# CONTEXT.md — Find The Proof

## Purpose
Research one real, verifiable citation for each keeper — the thing that helps AI engines cite the client.

## The Process (Step by Step)
1. Read `output/keepers.json` from Room 2
2. For each keeper, web-search for ONE real supporting fact or source
3. Attach the citation to the keeper
4. Save to `output/keepers-with-proof.json`

## Identity & Audience
- Who uses this room: the agent (AI), with web search
- What "good" looks like here: every citation is real and verifiable; if none is found, the post gets no citation rather than a fake one

## Tech Stack For This Room
- Web search
- AI reasoning (this is part of the 10%)

## Patterns to Follow
- One citation maximum per post
- Use credible sources (AAP, federal law, established orgs)
- Write the fact in plain language a stressed parent could understand

## Never Do This (Constraints)
- NEVER invent a study, statistic, author, or URL
- Never attach a citation you couldn't verify
- Never use more than one citation per post

## 60-30-10 Split For This Room
- 60% (Scripts): a script loops through keepers and saves results
- 30% (Rules): citation rules (real only, one max) live in config and this CONTEXT
- 10% (AI): ⭐ AI does the actual research and judgment of what's credible

## Skills To Load (Layer 3)
- None — uses web search directly
