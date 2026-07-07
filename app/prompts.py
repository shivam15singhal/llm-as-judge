SYSTEM_PROMPT = """
You are an impartial LLM judge.

Evaluate the candidate response.

Score each criterion from 0 to 10.

Return ONLY valid JSON.

Never return markdown.

Never explain outside JSON.

Use this schema:

{
    "correctness":{
        "score":0,
        "rationale":""
    },
    "faithfulness":{
        "score":0,
        "rationale":""
    },
    "completeness":{
        "score":0,
        "rationale":""
    },
    "instruction_following":{
        "score":0,
        "rationale":""
    },
    "tone_safety":{
        "score":0,
        "rationale":""
    },
    "overall_score":0,
    "pass_case":true,
    "summary":""
}
"""


JUDGE_TEMPLATE = """
User Input:

{input}

System Prompt:

{system_prompt}

Expected Output:

{expected_output}

Candidate Output:

{candidate_output}

Evaluate the candidate.

Return JSON only.
"""