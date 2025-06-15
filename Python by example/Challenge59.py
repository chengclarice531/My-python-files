import random
colour = random.choice(["black","white", "blue", "red", "yellow"])
correct = False
while correct == False:
    guess = input("Pick one colour: black, white, blue, red, yellow ").lower()
    if guess == colour:
        print("Well done")
        correct = True
    else:
        if colour == "black":
            print("You are such a BLACK luck guy.")
        if colour == "white":
            print("Too naive to choose WHITE")
        if colour == "blue":
            print("You probably feeling BLUE right now.")
        if colour == "red":
            print("Is your face looks RED right now?")
        if colour == "yellow":
            print("I bet your future is as bright as yellow.")

