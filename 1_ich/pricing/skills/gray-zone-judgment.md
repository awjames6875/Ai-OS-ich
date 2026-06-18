# Skill: Gray-Zone Pricing Judgment
# Room: /1_ich/pricing/
# Layer: 10% — Claude judgment only
# Trigger: Load ONLY when run_pricing_check.py cannot make a deterministic call

## WHEN THIS SKILL ACTIVATES
The script handles everything deterministic. Call this skill ONLY for:

1. **API unavailable** — Wheelhouse or Guesty is down and a decision cannot wait
2. **Borderline CONSIDER** — NET GAIN is 20–49% (midterm math ran but threshold is gray)
3. **Mixed property signals** — property has both midterm-hold AND emergency conditions
4. **Owner constraint** — a specific owner has communicated restrictions not in prices.json

## GRAY-ZONE CASE 1: API Down, Decision Can't Wait

Collect what you can manually:
- Last known Wheelhouse rate (from any recent pricing check)
- Guesty booking count for the next 30 days (from Guesty app if API down)

Apply the mode logic manually using prices.json floor/base values.
Flag in the Telegram alert that the rate is based on cached data:

PRICING ALERT — [Property] — [Date]
⚠️ Wheelhouse API unavailable — using last known rate
Mode selected: [MODE]
Recommended rate: $[X]/night
Based on: cached data from [last check date]
Approve rate? Reply YES or NO

## GRAY-ZONE CASE 2: Borderline CONSIDER (20–49% NET GAIN)

The math ran but the answer is not clear-cut. Present both sides to Adam:

MIDTERM DECISION — [Property]
NET GAIN: $[X] ([Y]% more than current STR)
This is in CONSIDER range (20–49%).

Case FOR midterm:
- [X] months of guaranteed income
- No vacancy risk for [X] months
- Frees up bandwidth

Case AGAINST:
- Only [Y]% more than current bookings
- Loses STR flexibility during peak season: [yes/no]
- Refund cost: $[C]

ADAM'S CALL. Reply YES or NO.

## GRAY-ZONE CASE 3: Conflicting Signals

If a property is both MIDTERM HOLD (inquiry pending) AND EMERGENCY (under 7 days):
- MIDTERM HOLD wins — do not drop to floor on those dates
- Drop to floor only on dates NOT covered by the midterm inquiry
- Flag the split in the Telegram alert

## RULES
- Never send a gray-zone Telegram without showing Adam both sides
- Never make the call yourself — always wait for YES or NO
- If Adam is unreachable for 4+ hours on an emergency: drop to floor and log it
