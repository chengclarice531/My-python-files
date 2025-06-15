compnum = 50
guess = 0
times = 0
while guess != compnum:
    guess = int(input("Enter your guess: "))
    if guess < compnum:
        print("Your guess is too low")
    elif guess > compnum:
        print("Your guess is too high")
    times += 1
print(f"Well done, you took {times} attempts")