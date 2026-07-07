import time

from google import genai

from app.config import settings
from app.logger import logger
from app.prompts import (
    SYSTEM_PROMPT,
    JUDGE_TEMPLATE,
)

client = genai.Client(
    api_key=settings.gemini_api_key
)


def judge_case(test_case):

    prompt = JUDGE_TEMPLATE.format(
        input=test_case["input"],
        system_prompt=test_case["system_prompt"],
        expected_output=test_case.get(
            "expected_output",
            "",
        ),
        candidate_output=test_case["candidate_output"],
    )

    logger.info("=" * 70)
    logger.info("JUDGE PROMPT")
    logger.info(prompt)

    start = time.perf_counter()

    response = client.models.generate_content(
        model=settings.judge_model,
        contents=[
            SYSTEM_PROMPT,
            prompt,
        ],
    )

    latency = time.perf_counter() - start

    logger.info(
        f"Judge latency: {latency:.2f} sec"
    )

    usage = response.usage_metadata

    logger.info(
        f"Prompt Tokens: {usage.prompt_token_count}"
    )

    logger.info(
        f"Completion Tokens: {usage.candidates_token_count}"
    )

    logger.info(
        f"Total Tokens: {usage.total_token_count}"
    )

    raw_response = response.text.strip()

    logger.info("RAW RESPONSE")
    logger.info(raw_response)

    return raw_response