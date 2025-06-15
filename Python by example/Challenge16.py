raining = input("Is it raining today?")
raining = raining.lower()
if raining == "yes" :
    windy = input("Is it windy?")
    windy = windy.lower()
    if windy == "yes" :
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")
