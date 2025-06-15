list = {}
for i in range(4):
    Name = input("Enter a name: ").capitalize()
    Age = int(input(f"Enter {Name}'s age: "))
    Shoesize = int(input(f"Enter {Name}'s shoe size: "))
    list[Name] = {"Age": Age, "Shoe size": Shoesize}
Name1 = input("Enter a name to display his/her age and shoe size: ").capitalize()
print("Age Shoe size")
print(list[Name1])
"""Sample data:
Name    Age Shoe size
John    34  39
Ken     23  38
Jenny   50  36
Mary    44  37"""