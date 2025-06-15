import csv
import random
Score = 0
Name = input("Enter your name: ").title()
x = random.randint(0,100)
y = random.randint(0,100)
Q1 = f"{x} + {y}"
A1 = int(input(f"{Q1} = "))
Correct1 = x + y
if A1 == Correct1:
    Score += 1
z = random.randint(0,100)
w = random.randint(0,100)
Q2 = f"{z} - {w}"
A2 = int(input(f"{Q2} = "))
Correct2 = z - w
if A2 == Correct2:
    Score += 1
with open("MathQuiz.csv", "a") as file:
    NewRecord = f"{Name}, {Q1}, {A1}, {Q2}, {A2}, {Score}\n"
    file.write(NewRecord)