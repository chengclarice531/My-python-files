invite = "yes"
count = 0
while invite == "yes":
    name = input("Name of the person that you want to invite to a party: ")
    count+=1
    print(f"{name} has now been invited.")
    invite = input("Do you want to invite others? (yes/no) ").lower()
print(f"There are {count} people coming to the party")