# SKILL: Daily Pricing Sweep

Layer 3 skill | Room: 1_ich/pricing | Created June 4, 2026
Trigger: every morning (scheduled), or Adam says "pricing sweep", "check my prices", "pricing check"

---

## WHAT THIS SKILL DOES

Pulls live data from the Wheelhouse RM API for every active ICH property, finds open nights and pricing problems, and produces ONE approval-ready report. It NEVER changes a rate on its own.

## HARD RULES (from root CLAUDE.md — never violate)

1. MIDTERM ALWAYS FIRST — never discount dates with a pending midterm inquiry
2. NO rate changes without Adam's explicit YES
3. Never quote a rate without checking Wheelhouse first
4. RATE RECOMMENDATIONS COME FROM WHEELHOUSE DATA ONLY. Derive every target rate from live Wheelhouse signals: current asking rate, actual booked ADR (`average_nightly_rate`), occupancy, and open nights. prices.json base/floor is a FLOOR + SANITY reference ONLY — it is NEVER the basis for a target rate. The stored base can be stale or wrong (e.g. wrong bedroom count, as on 4016), so anchoring a recommendation to it is a defect. If prices.json conflicts with the live data, FLAG the conflict — do not price off the stored base.

## PREREQUISITES

- API key: `.env` → `WHEELHOUSE_API_KEY` (header: `X-Integration-Api-Key`)
- Endpoint reference: `references/wheelhouse-api.md`
- Base/floor rates: `1_ich/pricing/prices.json`
- Listing IDs: channel is **guesty**; use the Guesty `id` field from GET /listings (NOT wheelhouse_id — that 404s)

## ACTIVE LISTING IDS (refresh monthly via GET /listings?exclude_inactive=true)

| Nickname | Guesty listing_id |
|---|---|
| OAK1206 | 67db1f005a70b00010532f92 |
| 1307 | 67687f121abbc70012013983 |
| 4016 | 64c00f499bf247002eb5fe2d |
| 1348 | 6456011de22cec00402859e3 |
| 1432 | 61d6139043d7ef00352ecd98 |
| SOU3701 | 61d6029ba9389600356cbac3 |
| SOU4518 | 61d5bec5689765003b1afc5b |
| SOU6308 | 5ec6d45cbeb57a002d879683 |
| 1506 | 5e8d09dccf4658002c2926a4 |

## STEPS

### Step 0 — Check local events FIRST (standing rule, added 2026-06-18 by Adam)

ALWAYS look up Tulsa-area events for the pricing window BEFORE pulling Wheelhouse, then adjust accordingly. Order is: **events → Wheelhouse occupancy → recommendation.**

- Web-search the demand drivers for the next 30–45 days: concerts (BOK Center, Cain's Ballroom, Tulsa Theater, Cox Business Center), sports, festivals (Tulsa State Fair, Mayfest, Gathering Place), graduations (TU, ORU, OU-Tulsa), conventions, and holidays.
- Verify each date against the venue/official source — do NOT trust hand-entered event rates without confirming the date.
- Only events NEAR a property's cluster matter. Map each event to the affected properties before recommending a premium (downtown/BOK/Cain's vs. south Tulsa vs. midtown). If property→venue proximity is unknown, FLAG it instead of guessing.
- On high-demand dates near a property: recommend RAISE. On soft open dates with no demand driver: recommend gap-fill DROP. Always cross-check the live Wheelhouse occupancy before finalizing.

### Step 1 — Pull data (rate limit: ~20 req/min, space calls 3.5s)

For each active listing:
```
GET /listings/{id}/kpis?channel=guesty&days=30
```
Capture: occupancy, available_nights, booked, average_nightly_rate.

NOTE: In Cowork sessions the sandbox cannot reach api.usewheelhouse.com — run API calls through the Chrome browser (navigate a tab to api.usewheelhouse.com, then fetch() via JS from that origin). For long batches, kick off async into `window.__x` and poll — CDP calls time out at 45s.

### Step 1b — Pull the COMP signal (Wheelhouse market data — added 2026-06-18)

Wheelhouse IS a comp engine. Use it instead of scraping neighbors. For the downtown/midtown cluster:
```
GET /listings/{id}/price_recommendations?channel=guesty&attribution=true
GET /listings/{id}/base_price_recommendation?channel=guesty
```
Read these fields:
- `data[].attr_local_demand` — the COMP/event signal. High positive (+10 to +40) = the market is pricing in real demand for that date (event confirmed). Negative = soft date (gap-fill candidate). Compare an event date to a nearby baseline date to size the spike.
- `data[].custom_type` = "fixed" means a manual rate is already set; `attr_user_adjustment` shows how far Adam's manual rate sits above/below the market rec.
- `base_price_recommended` / `_conservative` / `_aggressive` — market base options. `anchor_credibility` (0–100) on the base_price endpoint tells you how trustworthy.

⚠️ CAVEAT (critical): `base_price_recommended` is UNRELIABLE for any unit that sat on a long-term tenant — historical anchoring drags the base rec absurdly low (observed 2026-06-18: 1506 rec $84 vs base $225; 1348 $72; 1432 $21). For those units, IGNORE base_rec and use the per-date `price` + `base_price_aggressive` instead. Flag the conflict; never recommend dropping a base to an LT-corrupted number.

Method: event `local_demand` confirms or denies a premium → apply Adam's event % (see event-pricing-playbook.md) where comps agree; flag where they diverge (e.g. a manual premium on a date the comps show as soft).

### Step 2 — Classify each property (logic from run_pricing_check.py)

| Mode | Condition | Action |
|---|---|---|
| MIDTERM_HOLD | Pending midterm inquiry | Raise STR min +37% above base |
| HEALTHY | booked ≥ 70% | Hold |
| EMERGENCY | ≤7 days out AND 0% booked | Drop to floor |
| GAP_FILL | booked < 30% | Drop to base |
| BLOCKED? | available_nights = 0 AND no reservations | FLAG — possible stale block (the 4016 problem) |

ALWAYS ask Adam which properties have pending midterms before recommending any drop.

### Step 3 — Check price-level sanity per property (prices.json)

- Asking rate > 130% of base with low occupancy → flag (the SOU6308 problem)
- minimum_price_rules_v3 empty → flag missing floor
- available_nights = 0 → verify it's a tenant, not a stale calendar block

### Step 4 — Produce the report

Format (keep it ADHD-friendly — leads with actions, numbered):
```
PRICING SWEEP — [date]
NEEDS ACTION:
1. [property]: [mode] — [one-line recommended action] — YES/NO?
WATCH:
- [property]: [what to watch, trigger date]
FULL/OK: [list]
DATA FLAGS: [stale blocks, anomalies]
```
Save to: `1_ich/pricing/output/sweep-[YYYY-MM-DD].md`

### Step 5 — On Adam's YES only

Execute via API:
- Rate change: `PUT /listings/{id}/custom_rates?channel=guesty` (rate_type fixed/adjustment, per-day-of-week values)
- Floor: `PUT /preferences/{id}?channel=guesty` body `{"minimum_price_rules_v3":[{"type":"global","priority":1,"value":N}]}`
- Always read back after writing to verify; 409 = concurrent write, wait and retry

## KNOWN ISSUES (as of June 2026)

1. **gap_night CUS bug:** PUT/preview with `gap_night: {type:"CUS", custom:[...]}` returns 500 even with the documented example payload. Wheelhouse-side bug (beta API). Workaround: set gap-night rules in the Wheelhouse dashboard UI; re-test the API monthly. Adam's standing rule when it works: 1-night gaps price +60%, all days, both adjacencies.
2. **Reservations endpoint pagination:** page 1 only by default — use KPI `available_nights` as authoritative open-night count.
3. **4016 floor anomaly:** prices.json floor ($105) > base ($97). Fix pending.
4. **Single-setting endpoint** (`PUT /preferences/{id}/{setting}`) only accepts CON/REC/AGG presets — custom rules must go through the full preferences PUT.

## STANDING DECISIONS LOG

- 2026-06-04: 1307 floor set to $85 via API ✅
- 2026-06-04: 1307 event rates: Jun 19–20 $140, Jul 1 $140, Jul 3–4 $145 (Juneteenth/Wilco/July 4) ✅
- 2026-06-04: 1307 orphan-night +60% — BLOCKED by Wheelhouse bug, set manually in dashboard
- 2026-06-04: SOU6308 drop $210→$142 — proposed, NOT yet approved by Adam
