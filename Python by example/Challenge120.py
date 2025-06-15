def Addition():
    import random
    num1 = random.randint(5,20)
    num2 = random.randint(5,20)
    guess = int(input(f"{num1} + {num2} =  "))
    ans = num1 + num2
    return guess, ans

def Subtraction():
    import random
    num1 = random.randint(25,50)
    num2 = random.randint(1,25)
    guess = int(input(f"{num1} - {num2} =  "))
    ans = num1 - num2
    return guess, ans

def check(guess, ans):
    if guess == ans:
        print("Correct")
    else:
        print(f"Incorrect, the answer is {ans}.")

def main():
    print("1) Addition\n2) Subtraction")
    enter = int(input("Enter 1 or 2: "))
    if enter == 1:
        guess, ans = Addition()
        check(guess, ans)
    elif enter == 2:
        guess, ans = Subtraction()
        check(guess, ans)
    else:
        print("Invaild number!!!!")

try:
    main()
except ValueError:
    print("You must enter a number")