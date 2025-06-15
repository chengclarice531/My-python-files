import random
num = random.randrange(1,10)
i = False
while i == False:
    user = int(input("Enter a number: "))
    if user < num:
        print("Too low")
    elif user > num:
        print("Too high")
    if num == user:
        i = True