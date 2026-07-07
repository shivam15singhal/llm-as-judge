import json

from app.judge import judge_case

with open(
    "evaluation/test_suites/sample_suite.json",
    encoding="utf-8",
) as f:

    suite = json.load(f)

for case in suite:

    print("=" * 60)

    print("CASE", case["id"])

    verdict = judge_case(case)

    print(verdict)