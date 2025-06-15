i = 0
invite_list = []
while i < 3:
    invite_name = input("Enter the name you want to invite to a party: ")
    invite_list.append(invite_name)
    i += 1
enter = input("Do you want to add another? (yes/no)").lower()
if enter == "yes":
    add = True
else:
    add = False
while add == True:
    invite_name = input("Enter the name you want to invite to a party: ")
    invite_list.append(invite_name)
    enter = input("Do you want to add another? (yes/no)").lower()
    if enter == "yes":
        add = True
    else:
        add = False
number = len(invite_list)
print(f"You have invited {number} people to the party. ")
    
