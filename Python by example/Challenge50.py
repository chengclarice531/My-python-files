guess = False
while not guess:
    num = int(input("Enter a number between 10 and 20: "))
    if num < 10:
        print("Too low")
    elif num > 20:
        print("Too high")
    else:
        guess = True
print("Thank you")