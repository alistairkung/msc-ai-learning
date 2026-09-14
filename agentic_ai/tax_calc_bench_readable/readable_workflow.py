"""Readable reimplementation of the lecturer's TaxCalcBench chain.

This module keeps the same conceptual stages as Tutorial 1 but avoids nested
one-line lambdas so each state transition can be inspected independently.

IMPORTANT: ``load_generated_rules`` uses ``exec`` because the lecture's point is
that model-generated code can become an artifact that is validated and then
executed. ``exec`` is NOT a sandbox and should not be used on untrusted code in
production.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
import re
from collections.abc import Callable

from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

from .checks import SUBTOTAL_LINES, check_inventory, check_placements
from .manual_return import compute_form_1040_lines


TaxFunction = Callable[[float], int | float]


@dataclass(frozen=True)
class GeneratedTaxRules:
    standard_deduction: int | float
    tax_function: TaxFunction
    source_code: str


def build_inventory_chain(llm):
    """Stage 1: copy source facts into a structured inventory."""
    prompt = ChatPromptTemplate.from_template(
        """List every tax document in the taxpayer JSON below, with every non-zero numeric box.
Also give filing status and date of birth. Copy numbers exactly. Do not compute or interpret anything.

Return JSON only with this shape:
{{
  "filing_status": str,
  "date_of_birth": str,
  "boxes": [
    {{"document": str, "box": str, "what": str, "amount": number}}
  ]
}}

TAXPAYER JSON:
{taxpayer_json}
"""
    )
    return prompt | llm | JsonOutputParser()


def _extract_placements(parsed_output):
    """Accept either the lecturer's wrapper object or a bare placement list."""
    if isinstance(parsed_output, dict):
        return parsed_output["placements"]
    return parsed_output


def build_placement_chain(llm):
    """Stage 2: ask the model where each inventory item belongs on Form 1040."""
    prompt = ChatPromptTemplate.from_template(
        """You are preparing a 2024 US Form 1040.

FORM LINES:
{form}

TAXPAYER DOCUMENT BOXES:
{boxes}

For EACH box, choose the Form 1040 line on which its amount is entered.
If an amount first appears on a schedule, give the Form 1040 line that receives that schedule's total.
Never choose one of these subtotal lines: {subtotals}
Use "none" only when a box affects no Form 1040 line.
Do not add anything up. Return one placement per box.

Return JSON only:
{{
  "placements": [
    {{
      "document": str,
      "box": str,
      "amount": number,
      "entered_on": str,
      "line": str,
      "why": str
    }}
  ]
}}
"""
    )

    return (
        prompt
        | llm
        | JsonOutputParser()
        | RunnableLambda(_extract_placements)
    )


def build_rules_chain(llm):
    """Stage 3: externalise tax knowledge as executable Python rules."""
    prompt = ChatPromptTemplate.from_template(
        """A 2024 US Form 1040 is being prepared for a {filing_status} filer born {date_of_birth}.
Income includes: {income_kinds}.

Write Python that defines exactly:
1. STANDARD_DEDUCTION: the applicable 2024 standard deduction as a number.
2. def tax(taxable_income): a function implementing the 2024 tax calculation for line 16.

Requirements:
- standard library only;
- tax(...) must work for any non-negative taxable income;
- return a whole-dollar number;
- output Python code only, with no prose before or after it.
"""
    )

    return prompt | llm | StrOutputParser()


def rules_input(inventory: dict) -> dict:
    income_kinds = sorted({box["what"] for box in inventory["boxes"]})
    return {
        "filing_status": inventory["filing_status"],
        "date_of_birth": inventory["date_of_birth"],
        "income_kinds": ", ".join(income_kinds),
    }


def code_only(text: str) -> str:
    """Extract the first fenced code block when the model adds markdown fences."""
    if "```" not in text:
        return text.strip()

    fenced = text.split("```", 1)[1]
    fenced = re.sub(r"^\w*\n", "", fenced, count=1)
    return fenced.split("```", 1)[0].strip()


def load_generated_rules(code: str) -> GeneratedTaxRules:
    """Load and sanity-check the two generated artifacts from Stage 3.

    This mirrors the tutorial's educational use of exec. It is not a secure
    production technique for executing arbitrary model output.
    """
    cleaned_code = code_only(code)
    namespace: dict = {}

    exec(cleaned_code, namespace)

    standard_deduction = namespace["STANDARD_DEDUCTION"]
    tax_function = namespace["tax"]

    assert isinstance(standard_deduction, (int, float))
    assert standard_deduction >= 0
    assert callable(tax_function)

    # Same style of lightweight sanity check as the lecturer's notebook.
    for taxable_income in (0, 20_000, 99_000, 150_000):
        result = tax_function(taxable_income)
        assert isinstance(result, (int, float))
        assert result >= 0

    return GeneratedTaxRules(
        standard_deduction=standard_deduction,
        tax_function=tax_function,
        source_code=cleaned_code,
    )


def run_imperative_workflow(
    *,
    taxpayer_json: str,
    llm,
    form_text: str,
    line_keys: list[str],
    renderer: Callable[[str, dict[str, int]], str] | None = None,
) -> dict:
    """Run the lecturer's architecture as straightforward imperative Python.

    Read this function before the LCEL version below. It intentionally makes
    every intermediate artifact a named variable.
    """
    taxpayer = json.loads(taxpayer_json)

    # Stage 1 — LLM copies source facts into a structured inventory.
    inventory_chain = build_inventory_chain(llm)
    inventory = inventory_chain.invoke({"taxpayer_json": taxpayer_json})

    # Gate 1 — reject numeric facts the model invented.
    check_inventory(inventory, taxpayer)

    # Stage 2 — LLM chooses where each copied fact belongs on the form.
    placement_chain = build_placement_chain(llm)
    placements = placement_chain.invoke(
        {
            "form": form_text,
            "boxes": json.dumps(inventory["boxes"], indent=2),
            "subtotals": ", ".join(sorted(SUBTOTAL_LINES)),
        }
    )

    # Gate 2 — make sure every box was placed once and no subtotal was chosen.
    check_placements(placements, inventory, set(line_keys))

    # Stage 3 — LLM expresses tax knowledge as executable Python rules.
    rules_chain = build_rules_chain(llm)
    rules_code = rules_chain.invoke(rules_input(inventory))

    # Gate 3 — load/sanity-check the generated artifacts before using them.
    rules = load_generated_rules(rules_code)

    # Stage 4 — ordinary Python executes the form arithmetic deterministically.
    lines = compute_form_1040_lines(
        placements,
        standard_deduction=rules.standard_deduction,
        tax_function=rules.tax_function,
    )

    state = {
        "taxpayer_json": taxpayer_json,
        "inventory": inventory,
        "placements": placements,
        "rules": rules,
        "lines": lines,
    }

    # Optional boundary adapter: turn structured lines into benchmark text.
    if renderer is not None:
        state["return_text"] = renderer(inventory["filing_status"], lines)

    return state


def build_lcel_workflow(
    *,
    llm,
    form_text: str,
    line_keys: list[str],
    renderer: Callable[[str, dict[str, int]], str] | None = None,
):
    """Build the same workflow in LCEL using named stage functions.

    The point of this version is to show that LCEL is just state enrichment and
    sequential contracts. Named helpers are used instead of nested lambdas.
    """
    inventory_chain = build_inventory_chain(llm)
    placement_chain = build_placement_chain(llm)
    rules_chain = build_rules_chain(llm)
    allowed_lines = set(line_keys)

    def create_inventory(state: dict) -> dict:
        return inventory_chain.invoke({"taxpayer_json": state["taxpayer_json"]})

    def validate_inventory_state(state: dict) -> dict:
        taxpayer = json.loads(state["taxpayer_json"])
        check_inventory(state["inventory"], taxpayer)
        return state

    def create_placements(state: dict) -> list[dict]:
        return placement_chain.invoke(
            {
                "form": form_text,
                "boxes": json.dumps(state["inventory"]["boxes"], indent=2),
                "subtotals": ", ".join(sorted(SUBTOTAL_LINES)),
            }
        )

    def validate_placement_state(state: dict) -> dict:
        check_placements(
            state["placements"],
            state["inventory"],
            allowed_lines,
        )
        return state

    def create_rules(state: dict) -> GeneratedTaxRules:
        generated_code = rules_chain.invoke(rules_input(state["inventory"]))
        return load_generated_rules(generated_code)

    def calculate_lines(state: dict) -> dict[str, int]:
        rules = state["rules"]
        return compute_form_1040_lines(
            state["placements"],
            standard_deduction=rules.standard_deduction,
            tax_function=rules.tax_function,
        )

    workflow = (
        RunnablePassthrough.assign(
            inventory=RunnableLambda(create_inventory)
        )
        | RunnableLambda(validate_inventory_state)
        | RunnablePassthrough.assign(
            placements=RunnableLambda(create_placements)
        )
        | RunnableLambda(validate_placement_state)
        | RunnablePassthrough.assign(
            rules=RunnableLambda(create_rules)
        )
        | RunnablePassthrough.assign(
            lines=RunnableLambda(calculate_lines)
        )
    )

    if renderer is None:
        return workflow

    def render_from_state(state: dict) -> str:
        return renderer(state["inventory"]["filing_status"], state["lines"])

    return workflow | RunnablePassthrough.assign(
        return_text=RunnableLambda(render_from_state)
    )
