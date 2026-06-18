# Wheelhouse RM API Reference

Layer 3 reference | Built June 2026 | Verified against live API ✅

---

## QUICK FACTS

| Item | Value |
|---|---|
| Base URL | `https://api.usewheelhouse.com/ss_api/v1` |
| Auth header | `X-Integration-Api-Key: <key>` |
| Key location | `.env` → `WHEELHOUSE_API_KEY` (key prefix `rma_`) |
| Rate limit | ~20 requests/minute by default (per Wheelhouse docs — verify if hitting 429s) |
| Status | API is in **beta** — response formats may change |
| Docs | https://api.usewheelhouse.com/wheelhouse_rm_api |

**Verified working June 4, 2026:** `GET /listings` returned all ICH properties with HTTP 200.

---

## CRITICAL: HOW TO IDENTIFY A LISTING

Every per-listing endpoint needs TWO things:

1. `listing_id` in the URL path — the channel's listing ID
2. `?channel=wheelhouse` query param — required on every call

Get both from `GET /listings`. For ICH, listings are channel `wheelhouse` and the ID is the `wheelhouse_id` field (e.g., `51075786` for OAK1206).

```
GET /listings/51075786/kpis?channel=wheelhouse
```

---

## ICH PROPERTY → WHEELHOUSE ID MAP (active listings, June 2026)

| Nickname | Address | wheelhouse_id |
|---|---|---|
| OAK1206 | 1206 Oakwood Dr, Broken Arrow | 51075786 |
| 1307 | 1307 S Indianapolis Ave, Tulsa | 50453315 |
| 4016 | 4016 E 51st Pl, Tulsa | 37146042 |
| 1348 | 1348 S Pittsburg Ave, Tulsa | 35554523 |
| 1432 | 1432 A East 38th St, Tulsa | 30803636 |
| SOU3701 | 3701 S Richmond Ave, Tulsa | 30803639 |
| SOU4518 | 4518 S Quaker Ave, Tulsa | 30798588 |
| SOU6308 | 6308 South 1st Place, Broken Arrow | 23614774 |
| 1506 | 1506 S Florence Pl, Tulsa | 23603106 |

⚠️ Duplicate listings exist (e.g., two OAK1206 entries, multiple 1307/4809 variants) — old inactive duplicates from re-listing. **Always use the IDs above (the active ones).** Account also has 40+ inactive/legacy listings; ignore unless reactivating.

Inactive in Wheelhouse: SM4809, SOU1501, SOU1503, SOU1312, Utica6715, WES410, SOU1642, SOU1136, plus legacy duplicates.

**To refresh this map:** `GET /listings` and read `nickname` + `wheelhouse_id` + `is_active`.

---

## ENDPOINTS THAT MATTER FOR ICH

### 1. List all properties (READ)
```
GET /listings
```
Optional: `?include_managed_listings=true`
Returns: id, wheelhouse_id, nickname, address, bedrooms, is_active, channel_ids.

### 2. Morning pricing check (READ) — feeds run_pricing_check.py
```
GET /listings/{listing_id}/kpis?channel=wheelhouse&days=30
```
Returns: `occupancy`, `adjusted_occupancy`, `booked`, `available_nights`, `average_nightly_rate`, `nightly_revpar`, `last_booked_at`.
Use `occupancy` as the `--booking-pct` input to run_pricing_check.py.

### 3. Daily price recommendations (READ)
```
GET /listings/{listing_id}/price_recommendations?channel=wheelhouse
```
Optional: `&attribution=true` — adds per-factor breakdown (`attr_seasonality`, `attr_local_demand`, `attr_availability`, `attr_time`, etc.) — useful for owner reports in plain language.
Returns per stay_date: `price`, `min_stay`, `custom_type`.
NOTE: 423 response = recommendations still generating, retry shortly.

### 4. Set a custom rate (WRITE) — the "change the price" call
```
PUT /listings/{listing_id}/custom_rates?channel=wheelhouse
```
Body:
```json
{
  "start_date": "2026-06-10",
  "end_date": "2026-06-20",
  "rate_type": "fixed",
  "currency": "USD",
  "sunday": 95, "monday": 95, "tuesday": 95, "wednesday": 95,
  "thursday": 95, "friday": 110, "saturday": 110
}
```
- `rate_type: "fixed"` = absolute nightly price (requires currency)
- `rate_type: "adjustment"` = percent multiplier on Wheelhouse rec (110 = +10%)
- 409 = another write in progress for this listing, retry after it finishes
- Delete: `DELETE /listings/{listing_id}/custom_rates` (date range)
- Bulk: `PUT|DELETE /listings/{listing_id}/bulk_custom_rates`

### 5. Reservations (READ)
```
GET /listings/{listing_id}/reservations?channel=wheelhouse
```
Filter by stay date or booked date. Paginated.

### 6. Preview before committing (READ — simulation)
```
POST /preferences/{listing_id}/preview
```
Send hypothetical preference changes, get projected pricing back. Nothing saves. Use before any bulk strategy change.

### 7. Preferences (READ/WRITE — the strategy controls)
```
GET  /preferences?{batch params}        — batch read
PUT  /preferences                       — batch update
GET  /preferences/{listing_id}          — single listing
PUT  /preferences/{listing_id}          — single update
PUT  /preferences/{listing_id}/{setting} — one setting only
POST /preferences/{listing_id}/copy     — copy settings between listings
GET  /preferences/{listing_id}/changelog — 90-day audit log
GET  /preferences/{listing_id}/long_term_discounts
```
Controls base price, min/max, seasonality, occupancy pacing, demand sensitivity, last-minute discounts.

### 8. Other reads
```
GET /listings/{listing_id}                          — single listing detail
GET /listings/{listing_id}/pricing_tier             — pricing tier
GET /listings/{listing_id}/recent_changes           — last-change timestamps
GET /listings/{listing_id}/base_price_recommendation — base price options + credibility score
GET /listings/{listing_id}/checkin_checkout         — check-in/out calendar
GET /listings/{listing_id}/min_max_prices           — min/max price calendar
GET /listings/{listing_id}/monthly_seasonality      — seasonality factors
GET /listings/{listing_id}/tags  (PUT to update)    — user tags
GET /listings/{listing_id}/flags                    — system flags
```

---

## ERROR CODES

| Code | Meaning | Action |
|---|---|---|
| 401 | Bad/missing API key | Check `.env` |
| 403 | No access to listing, OR read-only key on PUT/DELETE | Check key permissions |
| 404 | Listing not found | Check listing_id + channel param |
| 409 | Concurrent write in progress | Wait, retry |
| 422 | Listing not in a Wheelhouse market | Can't price this one |
| 423 | Recommendations still generating | Retry after brief delay |
| 429 | Rate limited (~20 req/min) | Slow down, batch calls |

---

## ICH NON-NEGOTIABLES (from root CLAUDE.md — apply to every API use)

1. **MIDTERM ALWAYS FIRST.** Never drop rates on dates with a pending midterm inquiry.
2. **Never change a rate without Telegram approval from Adam.** API write calls (PUT custom_rates, PUT preferences) happen ONLY after Adam replies YES.
3. **Never quote a rate without checking Wheelhouse first** — use price_recommendations.
4. Run `run_pricing_check.py` (60% script layer) for mode selection — the API only feeds it data and executes the approved result.

---

## COPY-PASTE TEST COMMAND (PowerShell, from Adam's machine)

```powershell
$key = (Get-Content C:\Users\1alph\adam-ai-os\.env | Select-String "WHEELHOUSE_API_KEY").ToString().Split("=")[1]
Invoke-RestMethod -Uri "https://api.usewheelhouse.com/ss_api/v1/listings" -Headers @{"X-Integration-Api-Key"=$key} | Select-Object nickname, wheelhouse_id, is_active
```

---

## KNOWN GAPS / UNCERTAINTIES

- Wheelhouse marketing mentions a `GET /price_calendar` endpoint (price + availability + booking state in one call). It does NOT appear in the current beta docs dump — may be newer than the docs page, or renamed. Verify in live docs before relying on it.
- Rate limit (20/min) is from Wheelhouse's announcement, not confirmed by testing.
- API is beta — re-verify response shapes before building anything load-bearing.
- Claude's sandbox cannot reach api.usewheelhouse.com directly (network allowlist). API calls from Cowork sessions go through the Chrome browser route; scripts run fine from Adam's machine directly.
