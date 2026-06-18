# ICH Pricing Plan — June 4 to July 3, 2026

Source: Wheelhouse RM API (live pull, June 4) | Status: AWAITING ADAM APPROVAL
Rule check: No rate changes until Adam confirms pending midterms + replies YES.

---

## ACTION NEEDED (2 properties)

### 1. SOU6308 — 3701 S 1st Pl, Broken Arrow — GAP_FILL 🔴 (biggest leak)

| Metric | Value |
|---|---|
| Open nights (next 30d) | 28 of 30 |
| Booked | ~10% |
| Current asking rate | ~$210/night |
| Base rate (prices.json) | $142 |
| Floor | $142 |

**Problem:** Asking $210 — that's 48% above base on a nearly empty calendar.
**Recommended action:** Drop to base $142/night for Jun 4 – Jul 3.
**API call ready:** PUT custom_rates, rate_type=fixed, $142 all days.
**HOLD IF:** a midterm inquiry is pending on these dates → instead raise to $195 (base +37%).

### 2. 1307 — 1307 S Indianapolis — HEALTHY, but watch the gap 🟡

| Metric | Value |
|---|---|
| Booked (next 30d) | ~52% |
| Open gaps | Jun 18–24 (7 nights), Jun 28–Jul 3 (6 nights), tonight Jun 4 |
| Current avg rate | ~$100/night |
| Base / Floor | $110 / $85 |

**Mode:** HEALTHY (52% is between thresholds) → hold base $110.
**Trigger to act:** If Jun 18–24 gap is still unbooked on **Jun 11** (7 days out), drop that range to floor $85.
**HOLD IF:** midterm pending → raise STR minimum to $151 (base +37%).

---

### 3. 4016 — 4016 E 51st Pl — VACANT, CALENDAR STILL BLOCKED 🔴

**Adam confirmed June 4: tenant moved out, property is available now.** Wheelhouse still shows 0 open nights — the calendar is blocked in Guesty and hiding the vacancy.

| Metric | Value |
|---|---|
| Actual status | VACANT (per Adam) |
| Wheelhouse shows | 0 available nights (stale block) |
| Base / Floor | $97 / $105 ⚠️ floor above base — known anomaly in prices.json |

**Steps (in order):**

1. Unblock the calendar in Guesty (RM API can't do this — availability syncs from Guesty)
2. MIDTERM FIRST: list on Furnished Finder + Zillow before optimizing STR
3. STR gap-fill underneath: 0% booked + available today = EMERGENCY mode → floor price. BUT floor ($105) is above base ($97) — recommend listing STR at $97 until base/floor get fixed in prices.json
4. Re-run pricing check once calendar unblocks and Wheelhouse re-syncs

---

## NO ACTION — FULL OR BLOCKED (6 properties)

| Property | Status | Note |
|---|---|---|
| OAK1206 | Booked through Jul 31 | Reservation Dec 31 → Jul 31 (midterm tenant) ✅ |
| SOU3701 | Booked | Confirmed by Adam June 4 ✅ |
| 1506 | Booked | Confirmed by Adam June 4 ✅ |
| 1348 | 0 open nights | Likely midterm in place — unconfirmed |
| 1432 | 0 open nights | Likely midterm in place — unconfirmed |
| SOU4518 | 0 open nights | Likely midterm in place — unconfirmed |

1348 / 1432 / SOU4518: if any of these are blocked-but-empty rather than tenant-occupied, that's hidden vacancy (same as what happened with 4016) — worth a 2-minute Guesty scan.

---

## DATA HONESTY NOTES

- Reservations endpoint is paginated; I used KPI `available_nights` as the authoritative open-night count. 1307's gap dates are derived from page-1 reservations and matched KPIs within 3 nights — verify exact gap edges in Guesty before quoting.
- Avg nightly rates on blocked properties (1432 shows $8, 1506 shows $53) are calculation artifacts of empty calendars — ignore them.
- KPI window = next 30 days from June 4, 2026.

---

## APPROVAL CHECKLIST (updated June 4 after Adam's input)

1. [x] Midterm status: 1506 booked, SOU3701 booked, 4016 vacant (tenant moved out)
2. [ ] Adam replies YES/NO to SOU6308 drop to $142
3. [ ] Adam replies YES/NO to 1307 floor-drop trigger (auto-flag on Jun 11)
4. [ ] Adam unblocks 4016 calendar in Guesty
5. [ ] 4016 midterm listing goes up (Furnished Finder / Zillow)
6. [ ] Adam confirms 1348 / 1432 / SOU4518 have tenants (not stale blocks)
