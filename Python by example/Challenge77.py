i = 0
invite_list = []
while i < 3:
    invite_name = input("Enter the name you want to invite to a party: ")
    invite_list.append(invite_name.capitalize())
    i += 1
print(invite_list)
enter = input("Please type a name on the list: ").capitalize()
print(f"{enter} is in position {invite_list.index(enter)}. ")
remove = input(f"Do you want {enter} to come to the party? (yes/no) ").lower()
if remove == "no":
    invite_list.remove(enter)
print(invite_list)
    
