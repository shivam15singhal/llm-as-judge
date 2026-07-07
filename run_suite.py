import json

from app.judge import judge_case
from app.report import save_report


with open(
    "evaluation/test_suites/sample_suite.json",
    encoding="utf-8",
) as f:

    suite = json.load(f)


results = []

for case in suite:

    verdict = judge_case(case)

    results.append(
        {
            "id": case["id"],
            "overall_score": verdict.overall_score,
            "pass": verdict.pass_case,
            "summary": verdict.summary,
        }
    )

    print("=" * 60)

    print("Case", case["id"])

    print("Score:", verdict.overall_score)

    print("Pass:", verdict.pass_case)


report = save_report(results)

print()

print("Report saved to:")

print(report)