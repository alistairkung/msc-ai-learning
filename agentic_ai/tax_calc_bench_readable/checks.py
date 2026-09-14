"""Readable validation gates from the FTEC5660 TaxCalcBench workflow."""

from collections import Counter


SUBTOTAL_LINES = {
    "1z",
    "9",
    "11",
    "14",
    "15",
    "18",
    "21",
    "22",
    "24",
    "25d",
    "32",
    "33",
    "34",
    "37",
}


def numbers_in(value) -> list[float]:
    """Recursively collect numeric values from nested JSON-like data."""
    if isinstance(value, dict):
        numbers = []
        for child in value.values():
            numbers.extend(numbers_in(child))
        return numbers

    if isinstance(value, list):
        numbers = []
        for child in value:
            numbers.extend(numbers_in(child))
        return numbers

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return [float(value)]

    return []


def check_inventory(inventory: dict, taxpayer: dict) -> None:
    """Fail if the LLM invents a numeric amount absent from source JSON.

    This mirrors the lecturer's lightweight hallucination check. It is not a
    full proof that every source field was copied correctly or completely.
    """
    source_numbers = set(numbers_in(taxpayer))

    invented_amounts = []
    for box in inventory["boxes"]:
        amount = float(box["amount"])
        if amount not in source_numbers:
            invented_amounts.append(amount)

    assert not invented_amounts, (
        f"Inventory contains numbers not present in source: {invented_amounts}"
    )


def check_placements(
    placements: list[dict],
    inventory: dict,
    allowed_line_keys: set[str],
) -> None:
    """Check completeness and validity of the model's placement decisions."""
    source_amounts = Counter(float(box["amount"]) for box in inventory["boxes"])
    placed_amounts = Counter(float(item["amount"]) for item in placements)

    assert source_amounts == placed_amounts, (
        f"Dropped amounts: {dict(source_amounts - placed_amounts)}; "
        f"extra amounts: {dict(placed_amounts - source_amounts)}"
    )

    for placement in placements:
        line_key = str(placement["line"]).replace("Line", "").strip()

        assert line_key == "none" or line_key in allowed_line_keys, (
            f"Unknown line: {placement['line']}"
        )
        assert line_key not in SUBTOTAL_LINES, (
            f"Model chose subtotal line directly: {placement['line']}"
        )
