import json
import statistics


with open(
    "evaluation/reports/config_b.json",
    encoding="utf-8",
) as f:

    report = json.load(f)


scores = []

for result in report["results"]:

    scores.append(
        result["overall_score"]
    )


print()

print("Scores:", scores)

print("Minimum:", min(scores))

print("Maximum:", max(scores))

print(
    "Average:",
    round(
        statistics.mean(scores),
        2,
    ),
)

print(
    "Standard Deviation:",
    round(
        statistics.pstdev(scores),
        2,
    ),
)