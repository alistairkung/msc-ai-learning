"""Readable manual tax rules used by the lecturer's TaxCalcBench case.

The tutorial's model-generated rules for the chosen case are:

- filing status: single
- 2024 standard deduction: 14,600
- 2024 single-filer tax brackets for ordinary taxable income

This module writes those rules explicitly so the arithmetic is easy to inspect.
It is an educational reconstruction of the tutorial example, not a general tax
engine and not tax advice.
"""

from dataclasses import dataclass


STANDARD_DEDUCTION_2024_SINGLE = 14_600


@dataclass(frozen=True)
class BracketContribution:
    """One slice of taxable income and the tax charged on that slice."""

    lower_bound: float
    upper_bound: float | None
    rate: float
    taxable_amount: float
    tax_amount: float


@dataclass(frozen=True)
class TaxBreakdown:
    taxable_income: float
    contributions: tuple[BracketContribution, ...]
    unrounded_tax: float
    rounded_tax: int


def _contribution(
    taxable_income: float,
    lower_bound: float,
    upper_bound: float | None,
    rate: float,
) -> BracketContribution:
    """Calculate the portion of income taxed inside one bracket."""
    if upper_bound is None:
        amount_in_bracket = max(taxable_income - lower_bound, 0)
    else:
        amount_in_bracket = max(
            min(taxable_income, upper_bound) - lower_bound,
            0,
        )

    return BracketContribution(
        lower_bound=lower_bound,
        upper_bound=upper_bound,
        rate=rate,
        taxable_amount=amount_in_bracket,
        tax_amount=amount_in_bracket * rate,
    )


def calculate_2024_single_tax_breakdown(taxable_income: float) -> TaxBreakdown:
    """Apply the same 2024 single-filer brackets generated in the tutorial.

    Writing every bracket explicitly is deliberate. The lecturer's generated
    function used a compact loop; this version optimizes for reading/debugging.
    """
    taxable_income = max(float(taxable_income), 0)

    contributions = (
        _contribution(taxable_income, 0, 11_600, 0.10),
        _contribution(taxable_income, 11_600, 47_150, 0.12),
        _contribution(taxable_income, 47_150, 100_525, 0.22),
        _contribution(taxable_income, 100_525, 191_950, 0.24),
        _contribution(taxable_income, 191_950, 243_725, 0.32),
        _contribution(taxable_income, 243_725, 609_350, 0.35),
        _contribution(taxable_income, 609_350, None, 0.37),
    )

    unrounded_tax = sum(item.tax_amount for item in contributions)

    return TaxBreakdown(
        taxable_income=taxable_income,
        contributions=contributions,
        unrounded_tax=unrounded_tax,
        rounded_tax=round(unrounded_tax),
    )


def tax_2024_single(taxable_income: float) -> int:
    """Return line-16 tax for the tutorial's simple single-filer case."""
    return calculate_2024_single_tax_breakdown(taxable_income).rounded_tax
