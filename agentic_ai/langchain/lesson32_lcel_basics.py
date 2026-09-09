from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


def build_summary_prompt():
    summary_prompt_string = """
    Summarise the incident below in one concise sentence.
    Preserve the key event and any material risk.
    
    Incident:
    {incident}
    """
    return ChatPromptTemplate.from_template(summary_prompt_string)


def build_summary_chain(llm):
    prompt = build_summary_prompt()
    return prompt | llm | StrOutputParser()


def build_extraction_prompt():
    extract_prompt = """
    Extract structured risk information from the case text below.
    
    Case text:
    {case_text}
    
    Return a JSON object with exactly these keys:
    - "risk_type": string
    - "priority": string
    
    Do not include commentary or markdown.
    """

    return ChatPromptTemplate.from_template(extract_prompt)


def build_extraction_chain(llm):
    prompt = build_extraction_prompt()

    return prompt | llm | JsonOutputParser()


def build_two_stage_chain(llm):
    extraction_chain = {"risk_summary": build_extraction_chain(llm)}
    escalation_string = """
    You are reviewing an extracted payment-risk assessment.
    
    Risk assessment:
    {risk_summary}
    
    Recommend one next operational action.
    Choose from:
    - allow
    - manual_review
    - block
    
    Give the action and one short reason.
    """
    escalation_prompt = ChatPromptTemplate.from_template(escalation_string)

    return extraction_chain | escalation_prompt | llm | StrOutputParser()
