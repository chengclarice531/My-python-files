def add_item():
    NewItem = input("Enter a name: ").title()
    NameList.append(NewItem)

def change_item():
    view_item()
    Index = int(input("Enter the index of the name you wanna change: "))
    NewItem = input("Enter a new name: ").title()
    NameList[Index] = NewItem

def del_item():
    view_item()
    Index = int(input("Enter the index of the name you wanna delete: "))
    del NameList[Index]

def view_item():
    for i, name in enumerate(NameList):
        print(i,name)
    
def main():
    again = "y"
    while again == "y":
        print("1. Add a name")
        print("2. Change a name")
        print("3. Delete a name")
        print("4. View all names.")
        print("5. Quit.")
        select = int(input("What do you want to do (1-5)? "))
        if select == 1:
            NameList = add_item()
        elif select == 2:
            NameList = change_item()
        elif select == 3:
            NameList = del_item()
        elif select == 4:
            NameList = view_item()
        elif select == 5:
            again = "n"
        else:
            print("Wrong number enter!!!")

NameList = []
try:
    main()
except ValueError:
    print("You must enter a number. Please run the program again.")
except IndexError:
    print("You must enter a valid index number. Please run the program again.")