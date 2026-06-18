# ICH Event Pricing Playbook

Layer 3 reference | 1_ich/pricing | Created 2026-06-18 from Adam's input
Used by: daily-pricing-sweep.md (Step 0 — events first, then Wheelhouse, then adjust)

---

## PROPERTY → LOCATION MAP

Events only matter by proximity. Raise event premiums for the **downtown/midtown cluster**; the suburban units get little to no event lift.

| Nick | Cluster | Distance to downtown | Event-sensitive? | Source |
|---|---|---|---|---|
| 1307 | Midtown / near downtown | close | YES | Adam confirmed |
| 1506 | Midtown (near 1307) | close | YES | Adam confirmed |
| SOU4518 | Between S Tulsa & downtown | ~10 min | YES (moderate) | Adam confirmed |
| SOU3701 | South-ish | ~12 min | YES (moderate) | Adam confirmed |
| SOU6308 | S Tulsa (Broken Arrow), furthest | far | N/A — LONG-TERM ONLY (HOA 31+ days) | Adam confirmed |
| 1348 | Tulsa (S Pittsburg) | near downtown | N/A — LONG-TERM RENTAL (exclude from event pricing) | Adam confirmed 2026-06-18 |
| 1432 | Tulsa (E 38th St) | near downtown | N/A — LONG-TERM RENTAL (exclude from event pricing) | Adam confirmed 2026-06-18 |
| 4016 | Tulsa (E 51st Pl) | near downtown (assumed) | LIKELY — CONFIRM | "most are near downtown" |
| OAK1206 | Broken Arrow (1206 Oakwood) | suburban, far ⚠️ | PROBABLY NOT — CONFIRM | address is Broken Arrow, not downtown |

⚠️ OAK1206 and SOU6308 have Broken Arrow addresses — likely outside downtown event pull. Confirm OAK1206; 4016/1348/1432 default to "near downtown" per Adam but not individually confirmed.

---

## EVENT → PRICE-SPIKE RULES (downtown/midtown cluster)

| Event | Location | Raise | Status |
|---|---|---|---|
| Black Wall Street / Juneteenth | Greenwood District (downtown) | **+40%** | Adam set |
| Tulsa State Fair | Expo Square (21st & Yale, midtown) | **+35%** | Adam set |
| Mayfest | Downtown | **+35%** | Adam set |
| TU / ORU / OU-Tulsa graduations | midtown / south / downtown | RAISE (% TBD — confirm) | Adam: "definitely raise" |
| Conventions @ Cox Business Center | Downtown | RAISE (% TBD — confirm) | Adam: yes |
| Concerts @ Cox **concert hall** | Downtown | minimal / skip | Adam: "not so much" |
| Concerts @ BOK Center / Cain's Ballroom | Downtown | RAISE (% TBD — confirm) | implied by prior event rates |
| Gathering Place events | Riverside | **IGNORE — does not move demand** | Adam confirmed |

Graduation / convention / concert percentages are not yet set — flag for Adam, don't guess.

---

## METHOD (per Adam, 2026-06-18)

1. Search area events FIRST for the pricing window.
2. Map each event to the affected cluster (above).
3. Pull live Wheelhouse occupancy.
4. Apply the spike % for confirmed events on downtown/midtown units; gap-fill soft no-event nights.
5. **Backtest goal:** compare last summer (2025) actuals to this summer on event dates, and size the spike from what actually happened — see "Historical backtest" below.

---

## HISTORICAL BACKTEST — feasibility note

Adam wants spikes sized from last-year-vs-this-year performance. Wheelhouse path:
- `GET /listings/{id}/kpis` is forward-looking only (no historical date range).
- `GET /listings/{id}/reservations` CAN filter by stay date / booked date → pull summer 2025 actual booked nights + realized rates around each event date. This is the historical source.
- Caveats: reservations endpoint is paginated (page 1 only by default — must page through); gives realized booked ADR, NOT last year's asking rates or the full demand curve; API is beta. Test on one property/event before scaling.
