"""Practice tests for Lesson 34: stateful LCEL pipelines.

Implement the matching functions in ``lesson34_stateful_lcel_practice.py``.
Work through these tests in order. The tests deliberately describe behaviour
without providing the implementation.
"""

import pytest
from langchain_core.language_models.fake_chat_models import FakeListChatModel

from lesson34_stateful_lcel_practice import (
    build_extraction_chain,
    build_payment_pipeline,
    determine_review_route,
    validate_extraction,
)


# ---------------------------------------------------------------------------
# Phase 1: deterministic Python stages
# ---------------------------------------------------------------------------


def test_determine_review_route_sends_high_value_payment_to_manual_review():
    state = {
        "payment_note": "Customer sent USD 15,000.",
        "extracted": {"amount": 15_000, "currency": "USD"},
    }

    assert determine_review_route(state) == "MANUAL_REVIEW"


def test_determine_review_route_keeps_lower_value_payment_standard():
    state = {
        "payment_note": "Customer sent USD 500.",
        "extracted": {"amount": 500, "currency": "USD"},
    }

    assert determine_review_route(state) == "STANDARD"


def test_validate_extraction_returns_the_same_valid_state():
    state = {
        "payment_note": "Customer sent USD 500.",
        "extracted": {"amount": 500, "currency": "USD"},
    }

    result = validate_extraction(state)

    # A gate validates the state; it should not replace or silently repair it.
    assert result is state


@pytest.mark.parametrize(
    "extracted",
    [
        {"currency": "USD"},
        {"amount": "500", "currency": "USD"},
        {"amount": -1, "currency": "USD"},
        {"amount": 500},
        {"amount": 500, "currency": "US"},
    ],
)
def test_validate_extraction_rejects_invalid_contracts(extracted):
    state = {"payment_note": "Some payment note", "extracted": extracted}

    with pytest.raises((AssertionError, ValueError, TypeError)):
        validate_extraction(state)


# ---------------------------------------------------------------------------
# Phase 2: LLM extraction
# ---------------------------------------------------------------------------


def test_build_extraction_chain_returns_structured_payment_facts():
    llm = FakeListChatModel(
        responses=['{"amount": 15000, "currency": "USD"}']
    )

    chain = build_extraction_chain(llm)
    result = chain.invoke({"payment_note": "Customer sent USD 15,000."})

    assert result == {"amount": 15_000, "currency": "USD"}


# ---------------------------------------------------------------------------
# Phase 3: state enrichment + gate + deterministic computation
# ---------------------------------------------------------------------------


def test_payment_pipeline_preserves_input_and_enriches_state():
    llm = FakeListChatModel(
        responses=['{"amount": 15000, "currency": "USD"}']
    )

    pipeline = build_payment_pipeline(llm)
    result = pipeline.invoke({"payment_note": "Customer sent USD 15,000."})

    assert result == {
        "payment_note": "Customer sent USD 15,000.",
        "extracted": {"amount": 15_000, "currency": "USD"},
        "review_route": "MANUAL_REVIEW",
    }


def test_payment_pipeline_uses_standard_route_for_lower_value_payment():
    llm = FakeListChatModel(
        responses=['{"amount": 500, "currency": "USD"}']
    )

    pipeline = build_payment_pipeline(llm)
    result = pipeline.invoke({"payment_note": "Customer sent USD 500."})

    assert result["extracted"] == {"amount": 500, "currency": "USD"}
    assert result["review_route"] == "STANDARD"


def test_payment_pipeline_fails_before_routing_when_extraction_is_invalid():
    llm = FakeListChatModel(
        responses=['{"amount": "15000", "currency": "USD"}']
    )

    pipeline = build_payment_pipeline(llm)

    with pytest.raises((AssertionError, ValueError, TypeError)):
        pipeline.invoke({"payment_note": "Customer sent USD 15,000."})
