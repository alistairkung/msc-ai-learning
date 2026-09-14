"""Readable deterministic Form 1040 arithmetic for the tutorial case.

This mirrors the lecturer's `compute_return(...)` stage but expands the logic
into named steps so it reads like ordinary backend/business-rule code.
"""

from collections import defaultdict
from collections.abc import Callable

from .manual_tax_rules import (
    STANDARD_DEDUCTION_2024_SINGLE,
    tax_2024_single,
)


TaxFunction = Callable[[float], int | float]


def _normalise_line_key(line: object) -> str:
    """Convert values such as 'Line 1a' or '1a' into the canonical key."""
    return str(line).replace("Line", "").strip()


def apply_placements_to_lines(placements: list[dict]) -> defaultdict[str, float]:
    """Put each model placement onto its selected Form 1040 line."""
    lines: defaultdict[str, float] = defaultdict(float)

    for placement in placements:
        line_key = _normalise_line_key(placement["line"])

        if line_key == "none":
            continue

        lines[line_key] += float(placement["amount"])

    return lines


def compute_form_1040_lines(
    placements: list[dict],
    standard_deduction: int = STANDARD_DEDUCTION_2024_SINGLE,
    tax_function: TaxFunction = tax_2024_single,
) -> dict[str, int]:
    """Compute the deterministic Form 1040 lines used in Tutorial 1.

    There is intentionally no LLM in this function. By the time this stage is
    reached, placement decisions and tax rules should already have been
    externalised and validated.
    """
    lines = apply_placements_to_lines(placements)

    # ------------------------------------------------------------------
    # Income
    # ------------------------------------------------------------------
    wage_lines = (
        lines["1a"],
        lines["1b"],
        lines["1c"],
        lines["1d"],
        lines["1e"],
        lines["1f"],
        lines["1g"],
        lines["1h"],
    )
    total_wages = sum(wage_lines)
    lines["1z"] = total_wages

    other_income_lines = (
        lines["2b"],
        lines["3b"],
        lines["4b"],
        lines["5b"],
        lines["6b"],
        lines["7"],
        lines["8"],
    )
    total_income = total_wages + sum(other_income_lines)
    lines["9"] = total_income

    adjustments_to_income = lines["10"]
    adjusted_gross_income = total_income - adjustments_to_income
    lines["11"] = adjusted_gross_income

    # ------------------------------------------------------------------
    # Deductions and taxable income
    # ------------------------------------------------------------------
    lines["12"] = standard_deduction

    qualified_business_income_deduction = lines["13"]
    total_deductions = standard_deduction + qualified_business_income_deduction
    lines["14"] = total_deductions

    taxable_income = max(adjusted_gross_income - total_deductions, 0)
    lines["15"] = taxable_income

    # ------------------------------------------------------------------
    # Tax
    # ------------------------------------------------------------------
    income_tax = tax_function(taxable_income)
    lines["16"] = income_tax

    additional_tax = lines["17"]
    tax_before_credits = income_tax + additional_tax
    lines["18"] = tax_before_credits

    child_and_dependent_credit = lines["19"]
    schedule_3_credit = lines["20"]
    total_credits = child_and_dependent_credit + schedule_3_credit
    lines["21"] = total_credits

    tax_after_credits = max(tax_before_credits - total_credits, 0)
    lines["22"] = tax_after_credits

    other_taxes = lines["23"]
    total_tax = tax_after_credits + other_taxes
    lines["24"] = total_tax

    # ------------------------------------------------------------------
    # Withholding and payments
    # ------------------------------------------------------------------
    total_withholding = lines["25a"] + lines["25b"] + lines["25c"]
    lines["25d"] = total_withholding

    refundable_credits = lines["27"] + lines["28"] + lines["29"] + lines["31"]
    lines["32"] = refundable_credits

    total_payments = total_withholding + lines["26"] + refundable_credits
    lines["33"] = total_payments

    # ------------------------------------------------------------------
    # Refund or amount owed
    # ------------------------------------------------------------------
    overpayment = max(total_payments - total_tax, 0)
    lines["34"] = overpayment

    # The tutorial assumes the whole overpayment is refunded.
    lines["35a"] = overpayment

    amount_owed = max(total_tax - total_payments, 0)
    lines["37"] = amount_owed

    return {line_key: round(value) for line_key, value in lines.items()}
