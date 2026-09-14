"""Print the lecturer case using only the readable manual Python path.

Run from the repository root:

    python -m agentic_ai.tax_calc_bench_readable.demo_manual
"""

from .lecturer_case import EXPECTED_KEY_LINES, PLACEMENTS
from .manual_return import compute_form_1040_lines
from .manual_tax_rules import calculate_2024_single_tax_breakdown


def main() -> None:
    taxable_income = 142_745
    breakdown = calculate_2024_single_tax_breakdown(taxable_income)

    print("2024 single-filer tax calculation")
    print("=" * 36)
    print(f"taxable income: {taxable_income:,.0f}")
    print()

    for contribution in breakdown.contributions:
        if contribution.taxable_amount == 0:
            continue

        upper = (
            "∞"
            if contribution.upper_bound is None
            else f"{contribution.upper_bound:,.0f}"
        )
        print(
            f"{contribution.lower_bound:>9,.0f} -> {upper:>9}  "
            f"taxable {contribution.taxable_amount:>9,.0f}  "
            f"x {contribution.rate:>5.0%}  "
            f"= {contribution.tax_amount:>10,.2f}"
        )

    print()
    print(f"unrounded tax: {breakdown.unrounded_tax:,.2f}")
    print(f"line 16 tax:   {breakdown.rounded_tax:,.0f}")

    lines = compute_form_1040_lines(PLACEMENTS)

    print("\nKey Form 1040 lines")
    print("=" * 36)
    for line_key, expected in EXPECTED_KEY_LINES.items():
        actual = lines[line_key]
        marker = "OK" if actual == expected else "MISMATCH"
        print(
            f"Line {line_key:>3}: {actual:>9,}  "
            f"expected {expected:>9,}  {marker}"
        )


if __name__ == "__main__":
    main()
