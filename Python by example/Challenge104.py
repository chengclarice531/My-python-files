list = {}
for i in range(4):
    Name = input("Enter a name: ").capitalize()
    Age = int(input(f"Enter {Name}'s age: "))
    Shoesize = int(input(f"Enter {Name}'s shoe size: "))
    list[Name] = {"Age": Age, "Shoe size": Shoesize}
name_remove = input("Enter a name to remove his/her data: ").capitalize()
del list[name_remove]
print("Name Age Shoe size")
for i in list:
    print(i, list[i]["Age"], list[i]["Shoe size"])

"""Sample data:
Name    Age Shoe size
John    34  39
Ken     23  38
Jenny   50  36
Mary    44  37"""