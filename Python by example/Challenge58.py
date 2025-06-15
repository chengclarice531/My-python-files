import random
i = 0
score = 0
while i < 5:
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    user = int(input(f"{num1} + {num2} = ? "))
    ans = num1 + num2
    if user == ans:
        score += 1
    i += 1
print(f"You got {score} out of 5 in this math quiz")