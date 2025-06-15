import random
num = random.randrange(1,5)
user = int(input("Pick a number between 1 and 5: "))
if num == user:
    print("Well done")
elif num < user:
    print("Too high")
    user = int(input("Pick a number between 1 and 5: "))
    if num == user:
        print("Correct")
    else:
        print("You lose")
elif num > user:
    print("Too low")
    user = int(input("Pick a number between 1 and 5: "))
    if num == user:
        print("Correct")
    else:
        print("You lose")