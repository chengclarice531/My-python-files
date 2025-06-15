list = {}
for i in range(4):
    Name = input("Enter a name: ").capitalize()
    Age = int(input(f"Enter {Name}'s age: "))
    Shoesize = int(input(f"Enter {Name}'s shoe size: "))
    list[Name] = {"Age": Age, "Shoe size": Shoesize}
print("Name Age")
for i in list:
    print(i, list[i]["Age"])
"""Sample data:
Name    Age Shoe size
John    34  39
Ken     23  38
Jenny   50  36
Mary    44  37"""