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

def delete_record():
    with open("Salaries.csv") as file:
        reader = csv.reader(file)
        reader = list(reader)
        for i, row in enumerate(reader):
            print(f"Record {i}: {', '.join(row)}")
        index = int(input("Which record do you want to delete? "))
        del reader[index]
    with open("Salaries.csv", "w") as file:
        for row in reader:
            NewRecord = ", ".join(row) + "\n"
            file.write(NewRecord)

def main():
    again = 'y'
    while again == 'y':
        print("1) Add to file")
        print("2) View all records")
        print("3) Delete a record")
        print("4) Quit program\n")
        selection = int(input("Enter the number of your selection: "))
        if selection == 1:
            add_to_file()
        elif selection == 2:
            view_file()
        elif selection == 3:
            delete_record()
        elif selection == 4:
            again = 'n'
        else:
            print("Wrong number enter!!!")

try:
    main()
except ValueError:
    print("You must enter a number. Please run the program again.")
except TypeError:
    print("You must enter a valid number. Please run the program again.")


