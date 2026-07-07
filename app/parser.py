import json
import re

from pydantic import ValidationError

from app.logger import logger
from app.schemas import JudgeVerdict


def parse_verdict(raw_response: str) -> JudgeVerdict:
    """
    Parse Gemini JSON output.

    If Gemini returns malformed JSON,
    attempt automatic recovery.
    """

    try:

        data = json.loads(raw_response)

    except json.JSONDecodeError:

        logger.warning(
            "Malformed JSON received. Attempting recovery..."
        )

        data = recover_json(raw_response)

    try:

        return JudgeVerdict.model_validate(data)

    except ValidationError as error:

        logger.exception(
            "Verdict schema validation failed."
        )

        raise error


def recover_json(text: str):

    text = text.replace("```json", "")

    text = text.replace("```", "")

    match = re.search(
        r"\{.*\}",
        text,
        re.DOTALL,
    )

    if match:

        return json.loads(match.group())

    raise ValueError(
        "Unable to recover JSON."
    )