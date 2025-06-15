direction = input("Which direction you wants to count(up or down)? ")
direction = direction.lower()
if direction == "up":
    topnum = int(input("Top number please? "))
    for i in range(1,topnum+1):
        print(i)
elif direction == "down":
    downnum = int(input("Enter a number below 20? "))
    for i in range(20,downnum-1,-1):
        print(i)
else:
    print("I don't understand.")