import json
from pathlib import Path

from app.config import settings


def save_report(results, filename="suite_report.json"):

    report = {}

    report["total_cases"] = len(results)

    passed = sum(r["pass"] for r in results)

    report["pass_rate"] = round(
        passed / len(results) * 100,
        2,
    )

    report["mean_score"] = round(
        sum(r["overall_score"] for r in results)
        / len(results),
        2,
    )

    report["results"] = results

    output = settings.report_directory / filename

    with open(output, "w", encoding="utf-8") as f:

        json.dump(
            report,
            f,
            indent=4,
        )

    return output