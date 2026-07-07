import json

from app.judge import judge_case


with open(
    "evaluation/test_suites/sample_suite.json",
    encoding="utf-8",
) as f:

    suite = json.load(f)


flip_count = 0

total = len(suite)


for case in suite:

    first = judge_case(case)

    second = judge_case(case)

    print("=" * 60)

    print("Case:", case["id"])

    print("Run 1:", first.overall_score)

    print("Run 2:", second.overall_score)

    if first.overall_score != second.overall_score:

        flip_count += 1


consistency = (
    (total - flip_count)
    / total
) * 100

print()

print("Flip Count:", flip_count)

print(f"Consistency: {consistency:.2f}%")