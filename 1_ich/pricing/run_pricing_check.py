"""
ICH Pricing Mode Selector
60% layer — deterministic logic only. No Claude involvement here.

Usage:
  python run_pricing_check.py --property "1307 Indianapolis Ave" \
      --booking-pct 25 --days-out 10 --midterm-pending false

Outputs: mode name + recommended action + Telegram message text.
Adam approves before any rate is changed.
"""

import argparse
import json
import sys
from pathlib import Path

PRICES_FILE = Path(__file__).parent / "prices.json"


def load_prices():
    with open(PRICES_FILE) as f:
        return json.load(f)


def select_mode(has_pending_midterm: bool, booking_pct: float, days_out: int) -> str:
    """
    Pure deterministic mode selection.
    Priority order matches CONTEXT.md rules exactly.
    """
    if has_pending_midterm:
        return "MIDTERM_HOLD"
    if booking_pct >= 70:
        return "HEALTHY"
    if days_out <= 7 and booking_pct == 0:
        return "EMERGENCY"
    if booking_pct < 30:
        return "GAP_FILL"
    return "HEALTHY"


def calculate_rate(mode: str, property_data: dict, rules: dict) -> dict:
    base = property_data["base_rate"]
    floor = property_data["floor_rate"]

    if mode == "MIDTERM_HOLD":
        increase = rules["midterm_hold_increase_pct"] / 100
        recommended = round(base * (1 + increase))
        action = f"Raise STR minimum to ${recommended}/night ({rules['midterm_hold_increase_pct']}% above base)"
    elif mode == "GAP_FILL":
        recommended = base
        action = f"Drop to market rate: ${recommended}/night (base price)"
    elif mode == "EMERGENCY":
        recommended = floor
        action = f"Drop to floor price: ${recommended}/night"
    else:  # HEALTHY
        recommended = base
        action = "No action needed. Hold current rate."

    return {"rate": recommended, "action": action}


def build_telegram_message(property_name: str, mode: str, rate_info: dict,
                            booking_pct: float, days_out: int) -> str:
    lines = [
        f"PRICING CHECK — {property_name}",
        f"Mode: {mode}",
        f"Booked (next 30 days): {booking_pct:.0f}%",
        f"Days to first open night: {days_out}",
        f"",
        f"Action: {rate_info['action']}",
        f"",
        f"Approve? Reply YES or NO",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="ICH Pricing Mode Selector")
    parser.add_argument("--property", required=True, help="Property address (must match prices.json key)")
    parser.add_argument("--booking-pct", type=float, required=True, help="Percent booked next 30 days (0-100)")
    parser.add_argument("--days-out", type=int, required=True, help="Days until first open night")
    parser.add_argument("--midterm-pending", required=True, choices=["true", "false"],
                        help="Is a midterm inquiry pending for these dates?")
    args = parser.parse_args()

    data = load_prices()
    props = data["properties"]
    rules = data["mode_rules"]

    if args.property not in props:
        print(f"ERROR: '{args.property}' not found in prices.json")
        print("Available properties:", list(props.keys()))
        sys.exit(1)

    prop = props[args.property]
    if not prop["str_active"]:
        print(f"ERROR: {args.property} is not an STR property. Do not apply pricing modes.")
        sys.exit(1)

    has_midterm = args.midterm_pending == "true"
    mode = select_mode(has_midterm, args.booking_pct, args.days_out)
    rate_info = calculate_rate(mode, prop, rules)
    telegram = build_telegram_message(args.property, mode, rate_info, args.booking_pct, args.days_out)

    print(f"\nMode selected: {mode}")
    print(f"Recommended rate: ${rate_info['rate']}/night")
    print(f"\n--- Telegram message (send to Adam for approval) ---\n")
    print(telegram)
    print("\n--- End message ---")
    print("\nDo NOT change Wheelhouse until Adam replies YES.")


if __name__ == "__main__":
    main()
