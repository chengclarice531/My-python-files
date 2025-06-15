import csv
def add_to_file():
    with open("Salaries.csv", "a") as file:
        Name = input("Enter a name: ").capitalize()
        Salary = input(f"Enter {Name}'s salary: ")
        NewItem = Name + ", " + Salary + "\n"
        file.write(str(NewItem))

def view_file():
    with open("Salaries.csv") as file:
        for i, row in enumerate(file):
            print(i,row)
def main():
    again = 'y'
    while again == 'y':
        print("1) Add to file")
        print("2) View all records")
        print("3) Quit program\n")
        selection = int(input("Enter the number of your selection: "))
        if selection == 1:
            add_to_file()
        elif selection == 2:
            view_file()
        elif selection == 3:
            again = 'no'
        else:
            print("Wrong number enter!!!")

try:
    main()
except ValueError:
    print("You must enter a number. Please run the program again.")
except TypeError:
    print("You must enter a valid number. Please run the program again.")


