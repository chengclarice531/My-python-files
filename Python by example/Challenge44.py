invitenum = int(input("How many people do you want to invite to a party? "))
if invitenum < 10:
    for i in range(0,invitenum):
        name = input("Who do you want to invite? ")
        print(f"{name} has been invited")
elif invitenum >= 10:
    print("Too many people")