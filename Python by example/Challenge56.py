import random
num = random.randrange(1,10)
i = False
while i == False:
    user = int(input("Enter a number: "))
    if num == user:
        i = True