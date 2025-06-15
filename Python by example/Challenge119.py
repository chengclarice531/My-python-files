def pick_num():
    import random
    low_num = int(input("Enter the low number: "))
    high_num = int(input("Enter the high number: "))
    comp_num = random.randint(low_num, high_num)
    return comp_num
def first_guess():
    print("I am thinking of a number...")
    guess = int(input("Guess the number: "))
    return guess
def check_guess(comp_num, guess):
    while guess != comp_num:
        if guess < comp_num:
            print("Too low, try again.")
        elif guess > comp_num:
            print("Too high, try again.")
        guess = int(input("Guess the number: "))
    print("Correct, you win")
def main():
    comp_num = pick_num()
    guess = first_guess()
    check_guess(comp_num, guess)

try:
    main()
except ValueError:
    print("You must enter a number")