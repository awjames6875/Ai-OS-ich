# ICH Pricing Room — CONTEXT.md
# Layer 2 — Rules for /1_ich/pricing/

## PURPOSE
Decides nightly pricing for all 8 active STR properties.
Midterm always wins. Short-term fills gaps only.

---

## 60-30-10 SPLIT

| Layer | % | What lives here |
|-------|---|----------------|
| **Script** | 60% | `run_pricing_check.py` — mode selection, rate math, Telegram message |
| **Data** | 30% | `prices.json` — base rate, floor rate, mode thresholds per property |
| **Claude** | 10% | `skills/gray-zone-judgment.md` — API outages, borderline CONSIDER calls, conflicting signals |

**Rule:** If the inputs are known (booking %, days out, midterm pending), run the script.
Only load the gray-zone skill when the script cannot produce a deterministic answer.

---

## THE 4 PRICING MODES (reference — logic lives in the script)

| Mode | Triggers when | Action |
|------|--------------|--------|
| MIDTERM HOLD | Midterm inquiry pending for those dates | Raise STR min 35–40% on those dates |
| GAP FILL | No midterm pending AND under 30% booked next 30 days | Drop to base (market) rate |
| EMERGENCY | Under 7 days out AND still 0% booked | Drop to floor price |
| HEALTHY | 70%+ booked OR midterm confirmed | No action needed |

---

## HOW TO RUN

```bash
python 1_ich/pricing/run_pricing_check.py \
  --property "1307 Indianapolis Ave" \
  --booking-pct 25 \
  --days-out 10 \
  --midterm-pending false
```

Script outputs: mode selected + recommended rate + Telegram message ready to send.

**After running:** Send the Telegram message to Adam. Wait for YES before touching Wheelhouse.

For gray-zone situations: load `skills/gray-zone-judgment.md`.

---

## WHAT THIS ROOM CHECKS
1. Guesty — current bookings + booking % for next 30 days
2. Pending midterm inquiries — check with Adam or decisions log
3. `prices.json` — base and floor rates (source of truth, not property-list.md)

---

## APPROVAL RULE
Always send a Telegram alert before ANY rate change.
Never push a change without Adam saying yes.
Script produces the message. Adam approves. You update Wheelhouse.
