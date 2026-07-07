import json

from app.judge import judge_case

with open(
    "evaluation/test_suites/adversarial_probes.json",
    encoding="utf-8",
) as f:

    probes = json.load(f)


passed = 0

for probe in probes:

    verdict = judge_case(probe)

    print("=" * 70)

    print("Probe Type :", probe["type"])

    print("Overall :", verdict.overall_score)

    print("Pass :", verdict.pass_case)

    print(verdict.summary)

    if not verdict.pass_case:
        passed += 1

print()

print(
    "Judge correctly rejected",
    passed,
    "out of",
    len(probes),
)