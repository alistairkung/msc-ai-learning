from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

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
    if state["extracted"]["amount"] >= MANUAL_REVIEW_THRESHOLD:
        return MANUAL_REVIEW
    return STANDARD


def validate_extraction(state):
    """Validate the extracted payment contract and return the same state.

    Required contract:
    - state contains 'extracted';
    - extracted contains 'amount' and 'currency';
    - amount is int/float and >= 0;
    - currency is a three-character string.

    Invalid state should fail loudly rather than being silently repaired.
    """
    extracted = state["extracted"]

    assert extracted is not None
    assert "amount" in extracted
    assert "currency" in extracted
    assert isinstance(extracted["amount"], (int, float))
    assert isinstance(extracted["currency"], str)
    assert extracted["amount"] >= 0
    assert len(extracted["currency"]) == 3

    return state


def build_extraction_chain(llm):
    """Build an LCEL chain extracting amount and currency from payment_note."""
    prompt_string = """
        Extract amount and currency from the following payment details.

        Payment details:
        {payment_note}    
            
        Return a JSON object with exactly these keys:
        - "amount": number
        - "currency": string
    """

    prompt = ChatPromptTemplate.from_template(prompt_string)

    return prompt | llm | JsonOutputParser()


def build_payment_pipeline(llm):
    """Build the stateful payment pipeline exercised by the tests.

    Intended architecture:

    input state
        -> preserve state + assign structured LLM extraction under 'extracted'
        -> deterministic validation gate
        -> preserve state + assign deterministic 'review_route'
        -> enriched state
    """
    return (
        RunnablePassthrough.assign(extracted=build_extraction_chain(llm))
        | RunnableLambda(validate_extraction)
        | RunnablePassthrough.assign(
            review_route=RunnableLambda(determine_review_route)
        )
    )
