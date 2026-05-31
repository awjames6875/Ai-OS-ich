# Adam James — AI Operating System
# Root Routing Table (Layer 1)
# Version 1.0 | May 2026

## WHO I AM
Name: Adam James
Location: Tulsa, Oklahoma
GitHub: awjames6875
Personal brand: @adamspeakslife
Builder: Vibe coder — AI tools, not traditional code

## CONTEXT LOADING RULES (Read This First)
This is Level 1. Load ONLY this file first.
Identify the task type. Then load Level 2.
Never load multiple business contexts at once.
Never load all skills at once.

Level 1: This file only (~500 tokens) — ALWAYS
Level 2: One room CONTEXT.md — ONLY after task identified
Level 3: One skill file — ONLY when executing that skill

## ROUTING TABLE

### ICH Tasks → /ich/
Triggers: furnished finder, zillow, quooa, guesty,
          wheelhouse, property, lease, tenant,
          corporate housing, midterm, short-term,
          maintenance, jerry, cleaning, pricing,
          owner report, booking, inquiry

Sub-routing:
- Pricing questions → /ich/pricing/CONTEXT.md
- Inquiry responses → /ich/inquiries/CONTEXT.md
- Midterm vs short-term decisions → /ich/midterm-decisions/CONTEXT.md
- Lease and signing → /ich/leasing/CONTEXT.md
- Maintenance tickets → /ich/maintenance/CONTEXT.md
- Social content for ICH → /ich/content/CONTEXT.md
- Owner reports → /ich/owner-reports/CONTEXT.md

### Safe Harbor Tasks → /safe-harbor/
Triggers: safe harbor, daycare, after-school,
          emotional wellness, counselor, medicaid,
          sooner care, credentialing, partner,
          apollo, jamal, body and brain, CPT 90853

Sub-routing:
- Partner outreach → /safe-harbor/partner-outreach/CONTEXT.md
- Parent communications → /safe-harbor/parent-comms/CONTEXT.md
- Credentialing → /safe-harbor/credentialing/CONTEXT.md
- Content → /safe-harbor/content/CONTEXT.md

### GrowthGenix Tasks → /growthgenix/
Triggers: growthgenix, client, agency, proposal,
          automation, install, setup, tax prep,
          grynd house, deandre

Sub-routing:
- Client intake → /growthgenix/client-intake/CONTEXT.md
- Proposals → /growthgenix/proposals/CONTEXT.md
- Content → /growthgenix/content/CONTEXT.md

### Personal Brand Tasks → /adam-personal/
Triggers: adamspeakslife, memoir, identity theft,
          reputation, google, content, video,
          script, post, instagram, tiktok,
          show your work, podcast

Sub-routing:
- Content and scripts → /adam-personal/content/CONTEXT.md
- Reputation → /adam-personal/reputation/CONTEXT.md
- Memoir → /adam-personal/memoir/CONTEXT.md

### Marketing Tasks → /marketing/
Triggers: marketing, copywriting, seo, ads,
          conversion, funnel, email campaign,
          corey haines

## GLOBAL RULES (Apply Everywhere)

### ICH Non-Negotiables
- MIDTERM ALWAYS FIRST. Short-term fills gaps only.
- Never auto-send anything without Telegram approval.
- Never confirm a booking without checking Guesty.
- Never quote a rate without checking Wheelhouse.

### Safe Harbor Non-Negotiables
- NEVER say: therapy, therapist, mental health treatment
- ALWAYS say: emotional wellness, support sessions,
  licensed counselor
- B2B content: never mention dollar amounts —
  say new revenue stream
- Always include logo and website on all designs

### Adam ADHD Rules
- One task at a time
- Numbered steps always
- Copy-paste ready outputs always
- Redirect when adding new projects mid-conversation
- Honest when something is harder than expected
- Action over research always

## CONTENT MOMENT RULE
When Adam builds, breaks, fixes, or ships something
real — stop and say CONTENT MOMENT then run:
/adam-personal/content/skills/show-your-work.md

## DECISIONS LOG
All important decisions get logged to:
/decisions/[business]-decisions.jsonl
Read the last 50 lines at session start
for context continuity.

## REFERENCES
Shared knowledge lives in /references/
- property-list.md — all 9 ICH properties
- wheelhouse-api.md — pricing API docs
- guesty-api.md — calendar API docs
- avail-process.md — lease workflow
- openclaw-internals.md — Phase 2 reference


## MODEL ROUTING

Haiku — default for all tasks:
- Morning pricing check
- Maintenance routing  
- Inquiry intake
- Calendar checks
- Telegram alerts

Sonnet — switch automatically when:
- Writing midterm decision analysis
- Drafting guest responses
- Content and video scripts
- Anything requiring judgment calls

CONTEXT LIMIT RULE:
If conversation exceeds 80% context window
→ summarize to /decisions/[business]-decisions.jsonl
→ start fresh session with summary as context
This prevents running out of context mid-task.

## 60-30-10 BUILD RULE — Apply To Every Room

Before writing any code in any room, split the work into 3 layers:

| Layer | % | What goes here |
|---|---|---|
| Scripts | 60% | Predictable steps — fetch data, check availability, route events, math, file I/O |
| Database | 30% | Structured data — property list, decisions log, inquiry history, availability cache |
| AI (Claude) | 10% | Judgment only — draft replies, gray-zone pricing calls, content, voice |

**Rule:** If a task has a deterministic answer (same input = same output every time), it is a script. Not a Claude prompt.

**Before building any skill or CONTEXT.md, ask:**
1. Which steps here are just math or data fetching? → Script
2. What data needs to be stored and queried? → Database
3. What requires real judgment or Adam's voice? → Claude
