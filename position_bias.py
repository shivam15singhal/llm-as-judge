from app.bias import compare_answers

question = "What is Python?"

system_prompt = "Answer briefly."

answer_a = "Python is a programming language."

answer_b = "Python is a programming language used for many applications."

print("=" * 60)
print("FORWARD ORDER (A -> B)")
print("=" * 60)

forward = compare_answers(
    question,
    system_prompt,
    answer_a,
    answer_b,
)

print(forward)

print()

print("=" * 60)
print("REVERSE ORDER (B -> A)")
print("=" * 60)

reverse = compare_answers(
    question,
    system_prompt,
    answer_b,
    answer_a,
)

print(reverse)

print()

winner_forward = forward["winner"]
winner_reverse = reverse["winner"]

# Convert reverse winner back to original perspective
if winner_reverse == "A":
    reverse_original = "B"
else:
    reverse_original = "A"

flip = winner_forward != reverse_original

print("=" * 60)
print("RESULT")
print("=" * 60)

print("Forward Winner :", winner_forward)
print("Reverse Winner :", reverse_original)
print("Flip Rate      :", "100%" if flip else "0%")