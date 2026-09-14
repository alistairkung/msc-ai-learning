import json

import pytest
from langchain_core.language_models.fake_chat_models import FakeListChatModel

from agentic_ai.tax_calc_bench_readable.lecturer_case import (
    EXPECTED_KEY_LINES,
    INVENTORY,
    PLACEMENTS,
)
from agentic_ai.tax_calc_bench_readable.manual_return import compute_form_1040_lines
from agentic_ai.tax_calc_bench_readable.manual_tax_rules import (
    STANDARD_DEDUCTION_2024_SINGLE,
    calculate_2024_single_tax_breakdown,
    tax_2024_single,
)
from agentic_ai.tax_calc_bench_readable.readable_workflow import (
    build_lcel_workflow,
    run_imperative_workflow,
)


RELEVANT_LINE_KEYS = [
    "1a",
    "8",
    "25a",
    "25b",
    "1z",
    "9",
    "11",
    "12",
    "14",
    "15",
    "16",
    "18",
    "21",
    "22",
    "24",
    "25d",
    "32",
    "33",
    "34",
    "35a",
    "37",
]

FORM_TEXT = "\n".join(f"Line {key}: demo label" for key in RELEVANT_LINE_KEYS)

GENERATED_RULES = """STANDARD_DEDUCTION = 14600

def tax(taxable_income):
    brackets = [
        (11600, 0.10),
        (47150, 0.12),
        (100525, 0.22),
        (191950, 0.24),
        (243725, 0.32),
        (609350, 0.35),
    ]
    total = 0
    previous = 0
    for limit, rate in brackets:
        if taxable_income > previous:
            total += (min(taxable_income, limit) - previous) * rate
            previous = limit
    if taxable_income > previous:
        total += (taxable_income - previous) * 0.37
    return round(total)
"""


def fake_llm_for_lecturer_case():
    return FakeListChatModel(
        responses=[
            json.dumps(INVENTORY),
            json.dumps({"placements": PLACEMENTS}),
            GENERATED_RULES,
        ]
    )


def test_manual_tax_breakdown_exposes_each_bracket_for_lecturer_case():
    breakdown = calculate_2024_single_tax_breakdown(142_745)

    taxable_amounts = [item.taxable_amount for item in breakdown.contributions]
    tax_amounts = [item.tax_amount for item in breakdown.contributions]

    assert taxable_amounts[:4] == [11_600, 35_550, 53_375, 42_220]
    assert taxable_amounts[4:] == [0, 0, 0]
    assert tax_amounts[:4] == pytest.approx(
        [1_160, 4_266, 11_742.5, 10_132.8]
    )
    assert breakdown.unrounded_tax == pytest.approx(27_301.3)
    assert breakdown.rounded_tax == 27_301


def test_manual_tax_function_matches_lecturer_line_16():
    assert tax_2024_single(142_745) == 27_301


def test_manual_return_matches_key_lines_printed_in_tutorial():
    lines = compute_form_1040_lines(PLACEMENTS)

    for line_key, expected in EXPECTED_KEY_LINES.items():
        assert lines[line_key] == expected


def test_manual_return_uses_expected_standard_deduction():
    lines = compute_form_1040_lines(PLACEMENTS)

    assert lines["12"] == STANDARD_DEDUCTION_2024_SINGLE
    assert lines["15"] == 142_745


def test_imperative_workflow_makes_each_artifact_visible():
    state = run_imperative_workflow(
        taxpayer_json=json.dumps(INVENTORY),
        llm=fake_llm_for_lecturer_case(),
        form_text=FORM_TEXT,
        line_keys=RELEVANT_LINE_KEYS,
    )

    assert state["inventory"] == INVENTORY
    assert state["placements"] == PLACEMENTS
    assert state["rules"].standard_deduction == 14_600
    assert state["lines"]["16"] == 27_301
    assert state["lines"]["37"] == 14_066


def test_lcel_workflow_has_same_observable_result_as_imperative_version():
    workflow = build_lcel_workflow(
        llm=fake_llm_for_lecturer_case(),
        form_text=FORM_TEXT,
        line_keys=RELEVANT_LINE_KEYS,
    )

    result = workflow.invoke({"taxpayer_json": json.dumps(INVENTORY)})

    assert result["inventory"] == INVENTORY
    assert result["placements"] == PLACEMENTS
    assert result["lines"]["16"] == 27_301
    assert result["lines"]["37"] == 14_066
