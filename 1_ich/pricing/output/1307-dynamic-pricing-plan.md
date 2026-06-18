# 1307 S Indianapolis — Dynamic Pricing Plan

Built June 4, 2026 | Status: AWAITING ADAM APPROVAL
No changes go live until Adam replies YES per rule.

---

## WHY IT'S NOT BOOKING — DIAGNOSIS (from live Wheelhouse data)

| Finding | Current setting | Problem |
|---|---|---|
| 1 | Min stay = 2 nights, global | One-night gaps literally CANNOT book. The Jun 4 orphan night was unbookable inventory. |
| 2 | Last-minute discount = AGG (most aggressive) | Avg successful rate ~$100 vs $110 base — Wheelhouse is discounting hard and it's STILL not filling. Price may not be the real blocker. |
| 3 | No minimum price floor set | minimum_price_rules_v3 is EMPTY. AGG discounting with no floor can keep sliding. Your prices.json floor is $85 — Wheelhouse doesn't know that. |
| 4 | Gap night = REC (default) | No orphan-night strategy of your own. |
| 5 | June recs $90–139 | Rates look market-reasonable; the structural issues above are more likely culprits than price level. |

---

## THE PLAN — 4 LAYERS

### Layer 1: Adam's Orphan-Night Premium (+60%)

**Rule:** Any 1-night gap between bookings prices at +60% (≈$176 vs $110 base).

**Logic:** A one-night stay costs a full cleaning/turnover. If someone takes it, it has to pay like 1.6 nights.

**API:** `gap_night` preference, type CUS:
```json
{"gap_night": {"type": "CUS", "custom": [
  {"gap": 1, "adjacent": "left", "adjustment": 60, "day_of_week": [0,1,2,3,4,5,6]},
  {"gap": 1, "adjacent": "right", "adjustment": 60, "day_of_week": [0,1,2,3,4,5,6]}
]}}
```

⚠️ **Known issue:** The preview/simulation endpoint returns a 500 server error on gap_night payloads (the API is beta — base_price previews work fine, so this is their bug, not a wrong key). Plan: apply via PUT, immediately read back price_recommendations to verify, roll back to `{"type":"REC"}` if it misbehaves. Contact Wheelhouse API support about the 500 — they advertise fast API support.

**Honest tradeoff:** Industry practice is the OPPOSITE — discount gap nights 10–35% to fill them (PriceLabs, Hostfully, Wheelhouse default all do this). Premium pricing means most orphan nights stay empty, but the ones that book are profitable. With cleaning costs on a $110 property, that's a defensible call — just know you're trading occupancy for margin on those nights.

### Layer 2: Fill the two big gaps (Jun 18–24, Jun 28–Jul 3)

Real Tulsa demand in window:
- **Juneteenth festival** (Greenwood District) — weekend of Jun 19–20. 1307 is minutes from Greenwood. Hold rates UP, don't discount: custom rate $135–145 Fri/Sat.
- **Wilco at Cain's Ballroom Jul 1** + July 4th weekend — 1307 is close to Cain's. Custom rate $140+ for Jul 1, $145+ Jul 3–4.
- Plain midweek nights (Jun 22–24, Jun 29–30): let AGG last-minute discount work, floored at $95.

### Layer 3: Floor protection (do this regardless)

Add minimum price rule: **$85 floor** (matches prices.json). One API call. Prevents AGG discount from ever dropping below your number.

### Layer 4: Weekly cadence (already your system)

Monday: run pricing check → look at next 14 days → approve gap fills via Telegram. The orphan rule then runs itself inside Wheelhouse.

---

## EXECUTION CHECKLIST (each needs YES)

1. [ ] PUT gap_night +60% rule (with verify + rollback plan)
2. [ ] PUT minimum price floor $85
3. [ ] PUT custom rates: Jun 19–20 @ $140, Jul 1 @ $140, Jul 3–4 @ $145
4. [ ] Leave min stay at 2 globally (gap-night rules handle the 1-night exceptions)
5. [ ] Email Wheelhouse support re: preview 500 on gap_night

## EXPECTED OUTCOME

Gap nights stop being dead inventory: big gaps get event-priced or discount-filled; 1-night orphans either earn 1.6x or stay empty by design. Revenue impact of proper gap management runs 4–11% annually per industry data — on 1307 that's roughly $1,500–4,000/yr. (Approximate — verify against your own numbers after 60 days.)

## SOURCES

- Live Wheelhouse RM API data (preferences + price recommendations, June 4)
- Gap-night strategy: Hostfully, PriceLabs, Crestcove guides
- Tulsa events: tulsa.events, Songkick (Wilco @ Cain's Jul 1), Bandsintown
