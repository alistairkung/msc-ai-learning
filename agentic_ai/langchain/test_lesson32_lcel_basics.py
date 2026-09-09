from langchain_core.prompts import ChatPromptTemplate
from langchain_core.language_models.fake_chat_models import FakeListChatModel

from agentic_ai.langchain.lesson32_lcel_basics import (
    build_extraction_chain,
    build_extraction_prompt,
    build_summary_chain,
    build_summary_prompt,
    build_two_stage_chain,
)


def test_build_summary_prompt_has_expected_variable():
    prompt = build_summary_prompt()

    assert isinstance(prompt, ChatPromptTemplate)
    assert prompt.input_variables == ["incident"]


def test_build_summary_chain_returns_string():
    llm = FakeListChatModel(responses=["Possible duplicate payment requiring review."])

    chain = build_summary_chain(llm)

    result = chain.invoke(
        {"incident": "Two payments for GBP 4,200 were sent to the same beneficiary."}
    )

    assert result == "Possible duplicate payment requiring review."
    assert isinstance(result, str)


def test_build_extraction_prompt_has_expected_variable():
    prompt = build_extraction_prompt()

    assert isinstance(prompt, ChatPromptTemplate)
    assert prompt.input_variables == ["case_text"]


def test_build_extraction_chain_returns_dict():
    llm = FakeListChatModel(
        responses=['{"risk_type": "new_beneficiary", "priority": "high"}']
    )

    chain = build_extraction_chain(llm)

    result = chain.invoke(
        {
            "case_text": (
                "Customer attempted three high-value transfers "
                "to a newly created beneficiary."
            )
        }
    )

    assert result == {
        "risk_type": "new_beneficiary",
        "priority": "high",
    }
    assert isinstance(result, dict)


def test_build_two_stage_chain_passes_extracted_value_forward():
    llm = FakeListChatModel(
        responses=[
            '{"risk_type": "new_beneficiary", "priority": "high"}',
            "Escalate for manual review due to a high-priority new-beneficiary risk.",
        ]
    )

    chain = build_two_stage_chain(llm)

    result = chain.invoke(
        {
            "case_text": (
                "Customer attempted three high-value transfers "
                "to a newly created beneficiary."
            )
        }
    )

    assert result == (
        "Escalate for manual review due to a high-priority " "new-beneficiary risk."
    )
    assert isinstance(result, str)
