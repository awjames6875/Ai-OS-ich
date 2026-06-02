# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

# Adam James — AI Operating System
Root Routing Table (Layer 1) | Version 1.0 | May 2026

## WHO I AM
Name: Adam James
Location: Tulsa, Oklahoma
GitHub: awjames6875
Personal brand: @adamspeakslife
Builder: Vibe coder — AI tools, not traditional code

---

## ARCHITECTURE: 3-Layer Context Loading System

This repository uses Jake Van Clief's 3-Layer Folder Architecture:

**Level 1: Root CLAUDE.md** (~500 tokens)
- Always loaded first
- Contains routing table and global rules
- Never load multiple business contexts simultaneously

**Level 2: Room CONTEXT.md files** 
- One room = one business function
- Load ONLY after task type identified
- Each numbered room folder (1_ich/, 2_safe-harbor/, etc.) contains CONTEXT.md
- CONTEXT.md lives INSIDE room folders, never at root

**Level 3: Skill files**
- Load ONLY when executing that specific skill
- Lives inside room folders under `/skills/`

### Key Architecture Rules
- ❌ NEVER create CONTEXT.md at root level
- ✅ Root contains CLAUDE.md only
- ✅ Every room folder MUST have its own CONTEXT.md
- ✅ Room folders are numbered (1_intake, 2_verification, etc.)
- ✅ Room names describe the WORK that happens there
- ✅ Always run `/init` after bootstrapping a new project

---

## REPOSITORY STRUCTURE

```
adam-ai-os/
├── 1_ich/                    # Integrity Corporate Housing business
│   ├── pricing/              # Dynamic pricing decisions
│   ├── inquiries/            # Guest inquiry handling
│   ├── leasing/              # Lease signing workflow
│   ├── maintenance/          # Maintenance routing
│   ├── midterm-decisions/    # Midterm vs short-term analysis
│   ├── owner-reports/        # Owner reporting
│   └── content/              # ICH social content
├── 2_safe-harbor/            # Safe Harbor daycare/after-school
│   ├── partner-outreach/     # Partner acquisition
│   ├── parent-comms/         # Parent communications
│   ├── credentialing/        # Provider credentialing
│   └── content/              # Safe Harbor content
├── 3_adam-personal/          # Personal brand (@adamspeakslife)
│   ├── content/              # Scripts and posts
│   ├── reputation/           # Reputation management
│   └── memoir/               # Memoir writing
├── 4_growthgenix/            # GrowthGenix agency
│   ├── client-intake/
│   ├── proposals/
│   └── content/
├── marketing/                # Marketing/copywriting work
├── goviralbro/              # Social media coaching system (see below)
├── references/              # Shared knowledge base
│   ├── property-list.md     # All 9 ICH properties
│   ├── guesty-api.md        # Calendar API docs
│   └── wheelhouse-api.md    # Pricing API docs
└── decisions/               # Decision logs (JSONL format)
```

---

## ROUTING TABLE

Identify task type first, then load the appropriate Level 2 CONTEXT.md.

### ICH Tasks → 1_ich/
**Triggers:** furnished finder, zillow, quooa, guesty, wheelhouse, property, lease, tenant, corporate housing, midterm, short-term, maintenance, jerry, cleaning, pricing, owner report, booking, inquiry

**Sub-routing:**
- Pricing questions → `1_ich/pricing/CONTEXT.md`
- Inquiry responses → `1_ich/inquiries/CONTEXT.md`
- Midterm vs short-term decisions → `1_ich/midterm-decisions/CONTEXT.md`
- Lease and signing → `1_ich/leasing/CONTEXT.md`
- Maintenance tickets → `1_ich/maintenance/CONTEXT.md`
- Social content for ICH → `1_ich/content/CONTEXT.md`
- Owner reports → `1_ich/owner-reports/CONTEXT.md`

### Safe Harbor Tasks → 2_safe-harbor/
**Triggers:** safe harbor, daycare, after-school, emotional wellness, counselor, medicaid, sooner care, credentialing, partner, apollo, jamal, body and brain, CPT 90853

**Sub-routing:**
- Partner outreach → `2_safe-harbor/partner-outreach/CONTEXT.md`
- Parent communications → `2_safe-harbor/parent-comms/CONTEXT.md`
- Credentialing → `2_safe-harbor/credentialing/CONTEXT.md`
- Content → `2_safe-harbor/content/CONTEXT.md`

### GrowthGenix Tasks → 4_growthgenix/
**Triggers:** growthgenix, client, agency, proposal, automation, install, setup, tax prep, grynd house, deandre

**Sub-routing:**
- Client intake → `4_growthgenix/client-intake/CONTEXT.md`
- Proposals → `4_growthgenix/proposals/CONTEXT.md`
- Content → `4_growthgenix/content/CONTEXT.md`

### Personal Brand Tasks → 3_adam-personal/
**Triggers:** adamspeakslife, memoir, identity theft, reputation, google, content, video, script, post, instagram, tiktok, show your work, podcast

**Sub-routing:**
- Content and scripts → `3_adam-personal/content/CONTEXT.md`
- Reputation → `3_adam-personal/reputation/CONTEXT.md`
- Memoir → `3_adam-personal/memoir/CONTEXT.md`

### Marketing Tasks → marketing/
**Triggers:** marketing, copywriting, seo, ads, conversion, funnel, email campaign, corey haines

Load: `marketing/CONTEXT.md`

### GoViralBro Tasks → goviralbro/
**Triggers:** viral, goviralbro, competitor analysis, hook, script, angle, discover, analyze, social media coaching, content pipeline

**Commands:** `/viral:setup`, `/viral:onboard`, `/viral:discover`, `/viral:angle`, `/viral:script`, `/viral:analyze`, `/viral:update-brain`

See [goviralbro/README.md](goviralbro/README.md) for full pipeline documentation.

---

## GOVIRALBRO INTEGRATION

GoViralBro is a trainable social media coaching system integrated as a git submodule.

### Pipeline Flow
```
DISCOVER → ANGLE → SCRIPT → POST → ANALYZE
   ↑                                    |
   └──── feedback loop (brain evolves) ─┘
```

### Key Components
- **Agent brain:** `goviralbro/data/agent-brain.json` (evolving system memory)
- **Recon module:** Python competitor analysis (`goviralbro/recon/`)
- **Scoring engine:** Topic scoring (`goviralbro/scoring/`)
- **Skills:** Bundled discovery skills (`goviralbro/skills/`)
- **Schemas:** JSON Schema contracts (`goviralbro/schemas/`)

### Python Environment
```bash
cd goviralbro
pip install -r requirements.txt
```

Dependencies: Flask, yt-dlp, reportlab, google-api-python-client, python-dotenv

### Data Storage
- JSONL format for topics, angles, hooks, scripts
- JSON for agent brain and templates
- Analytics stored in `goviralbro/data/analytics/`

---

## GLOBAL RULES (Apply Everywhere)

### ICH Non-Negotiables
- **MIDTERM ALWAYS FIRST.** Short-term fills gaps only.
- Never auto-send anything without Telegram approval.
- Never confirm a booking without checking Guesty.
- Never quote a rate without checking Wheelhouse.

### Safe Harbor Non-Negotiables
- **NEVER say:** therapy, therapist, mental health treatment
- **ALWAYS say:** emotional wellness, support sessions, licensed counselor
- B2B content: never mention dollar amounts — say "new revenue stream"
- Always include logo and website on all designs

### Adam ADHD Rules
- One task at a time
- Numbered steps always
- Copy-paste ready outputs always
- Redirect when adding new projects mid-conversation
- Honest when something is harder than expected
- Action over research always

---

## CONTENT MOMENT RULE

When Adam builds, breaks, fixes, or ships something real — stop and say **CONTENT MOMENT** then run:
`/adam-personal/content/skills/show-your-work.md`

---

## DECISIONS LOG

All important decisions get logged to:
`/decisions/[business]-decisions.jsonl`

Read the last 50 lines at session start for context continuity.

---

## REFERENCES

Shared knowledge lives in `/references/`:
- `property-list.md` — all 9 ICH properties
- `wheelhouse-api.md` — pricing API docs
- `guesty-api.md` — calendar API docs
- `avail-process.md` — lease workflow
- `build-rules.md` — build patterns
- `model-rules.md` — model selection

---

## MODEL ROUTING

**Haiku** — default for all tasks:
- Morning pricing check
- Maintenance routing
- Inquiry intake
- Calendar checks
- Telegram alerts

**Sonnet** — switch automatically when:
- Writing midterm decision analysis
- Drafting guest responses
- Content and video scripts
- Anything requiring judgment calls

**Context Limit Rule:**
If conversation exceeds 80% context window:
1. Summarize to `/decisions/[business]-decisions.jsonl`
2. Start fresh session with summary as context

---

## 60-30-10 BUILD RULE (Apply To Every Room)

Before writing any code in any room:

| Layer | % | What goes here |
|---|---|---|
| **Scripts** | 60% | Predictable steps — fetch data, check availability, route events, math, file I/O |
| **Database** | 30% | Structured data — property list, decisions log, inquiry history, availability cache |
| **AI (Claude)** | 10% | Judgment only — draft replies, gray-zone pricing calls, content, voice |

**Rule:** If a task has a deterministic answer, it is a script. Not a Claude prompt.

Before building any skill or CONTEXT.md, ask:
1. Which steps here are just math or data fetching? → Script
2. What data needs to be stored and queried? → Database
3. What requires real judgment or Adam's voice? → Claude