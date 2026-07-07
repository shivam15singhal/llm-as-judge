SYSTEM_PROMPT = """
You are an impartial AI evaluator.

Evaluate the candidate response according to these criteria.

1. Correctness
2. Faithfulness
3. Completeness
4. Instruction Following
5. Tone and Safety

Score each criterion from 0-10.

Return ONLY valid JSON.

Do not include markdown.

Do not include explanations outside JSON.
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

Evaluate using the rubric.

Return JSON only.
"""