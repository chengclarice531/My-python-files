import random
def get_colour():
    colour = ["red", "orange","yellow","green","blue","indigo","violet"]
    colour1 =random.choice(colour)
    colour2 =random.choice(colour)
    colour3 =random.choice(colour)
    colour4 =random.choice(colour)
    Generate = (colour1,colour2,colour3,colour4)
    return Generate

def input_data():
    print("The colours are red, orange, yellow, green, blue, indigo, violet")
    try_again = True
    while try_again == True:
        guess1 = input("Enter your first colour: ").lower()
        if guess1 != "red" and guess1 != "orange" and guess1 != "yellow" and guess1 != "green" and guess1 != "blue" and guess1 != "indigo" and guess1 != "violet":
            print("Incorrect input!")
        else:
            try_again = False
    try_again = True
    while try_again == True:
        guess2 = input("Enter your second colour: ").lower()
        if guess2 != "red" and guess2 != "orange" and guess2 != "yellow" and guess2 != "green" and guess2 != "blue" and guess2 != "indigo" and guess2 != "violet":
            print("Incorrect input!")
        else:
            try_again = False
    try_again = True
    while try_again == True:
        guess3 = input("Enter your third colour: ").lower()
        if guess3 != "red" and guess3 != "orange" and guess3 != "yellow" and guess3 != "green" and guess3 != "blue" and guess3 != "indigo" and guess3 != "violet":
            print("Incorrect input!")
        else:
            try_again = False
    try_again = True
    while try_again == True:
        guess4 = input("Enter your fourth colour: ").lower()
        if guess4 != "red" and guess4 != "orange" and guess4 != "yellow" and guess4 != "green" and guess4 != "blue" and guess4 != "indigo" and guess4 != "violet":
            print("Incorrect input!")
        else:
            try_again = False
    data = (guess1,guess2,guess3,guess4)
    return data

def check(colour1,colour2,colour3,colour4,guess1,guess2,guess3,guess4):
    correct = 0
    wrong_place = 0
    if guess1 == colour1:
        correct += 1
    elif guess1 == colour2 or guess1 == colour3 or guess1 == colour4:
        wrong_place += 1
    if guess2 == colour2:
        correct += 1
    elif guess2 == colour1 or guess2 == colour3 or guess2 == colour4:
        wrong_place += 1
    if guess3 == colour3:
        correct += 1
    elif guess3 == colour1 or guess3 == colour2 or guess3 == colour4:
        wrong_place += 1
    if guess4 == colour4:
        correct += 1
    elif guess4 == colour1 or guess4 == colour2 or guess4 == colour3:
        wrong_place += 1
    print(f"Correct colour in the correct place: {correct}")
    print(f"Correct colour but in the wrong place: {wrong_place}")
    print()
    return correct

def main():
    (colour1,colour2,colour3,colour4) = get_colour()
    print("Welcome to Mastermind!")
    print("You have to guess the four colours I have chosen.")
    print("You will be told how many colours you have guessed correctly and how many are correct but in the wrong place.")
    score = 0
    play = True
    while play == True:
        (guess1,guess2,guess3,guess4) = input_data()
        correct = check(colour1,colour2,colour3,colour4,guess1,guess2,guess3,guess4)
        if correct == 4:
            play = False
        score += 1
    print("Congrats!")
    print(f"You took {score} guesses")

main()