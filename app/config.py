from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()


class Settings(BaseModel):

    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")

    judge_model: str = os.getenv(
        "JUDGE_MODEL",
        "gemini-2.5-flash",
    )

    generator_model: str = os.getenv(
        "GENERATOR_MODEL",
        "gemini-2.5-flash",
    )

    log_directory: Path = Path("logs")

    report_directory: Path = Path(
        "evaluation/reports"
    )


settings = Settings()

settings.log_directory.mkdir(
    parents=True,
    exist_ok=True,
)

settings.report_directory.mkdir(
    parents=True,
    exist_ok=True,
)