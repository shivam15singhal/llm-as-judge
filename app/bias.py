import json

from google import genai

from app.config import settings
from app.logger import logger
from app.prompts import PAIRWISE_PROMPT

client = genai.Client(
    api_key=settings.gemini_api_key
)


def compare_answers(question, system_prompt, answer_a, answer_b):

    prompt = PAIRWISE_PROMPT.format(
        input=question,
        system_prompt=system_prompt,
        answer_a=answer_a,
        answer_b=answer_b,
    )

    response = client.models.generate_content(
        model=settings.judge_model,
        contents=prompt,
    )

    raw = response.text.strip()

    raw = raw.replace("```json", "")
    raw = raw.replace("```", "")

    logger.info(raw)

    return json.loads(raw)