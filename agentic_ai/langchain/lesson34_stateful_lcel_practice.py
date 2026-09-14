"""Lesson 34 practice: stateful LCEL pipelines.

Implement this file from the tests. Do not look back at Lesson 32's solution
unless a later hint explicitly calls for it.

Learning targets:
- structured LLM extraction;
- RunnablePassthrough.assign as state enrichment;
- RunnableLambda for deterministic Python stages;
- a fail-fast validation gate that returns valid state unchanged;
- explicit separation between probabilistic extraction and deterministic policy.
"""

MANUAL_REVIEW_THRESHOLD = 10_000
MANUAL_REVIEW = "MANUAL_REVIEW"
STANDARD = "STANDARD"


def determine_review_route(state):
    """Return MANUAL_REVIEW or STANDARD from state['extracted']['amount']."""
    raise NotImplementedError


def validate_extraction(state):
    """Validate the extracted payment contract and return the same state.

    Required contract:
    - state contains 'extracted';
    - extracted contains 'amount' and 'currency';
    - amount is int/float and >= 0;
    - currency is a three-character string.

    Invalid state should fail loudly rather than being silently repaired.
    """
    raise NotImplementedError


def build_extraction_chain(llm):
    """Build an LCEL chain extracting amount and currency from payment_note."""
    raise NotImplementedError


def build_payment_pipeline(llm):
    """Build the stateful payment pipeline exercised by the tests.

    Intended architecture:

    input state
        -> preserve state + assign structured LLM extraction under 'extracted'
        -> deterministic validation gate
        -> preserve state + assign deterministic 'review_route'
        -> enriched state
    """
    raise NotImplementedError
