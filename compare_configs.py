import json

from app.comparison import declare_winner


with open(
    "evaluation/reports/config_a.json",
    encoding="utf-8",
) as f:

    config_a = json.load(f)

with open(
    "evaluation/reports/config_b.json",
    encoding="utf-8",
) as f:

    config_b = json.load(f)


winner = declare_winner(
    config_a,
    config_b,
)

print()

print("=" * 50)

print("Config A")

print(config_a["mean_score"])

print()

print("Config B")

print(config_b["mean_score"])

print()

print("Winner:")

print(winner)