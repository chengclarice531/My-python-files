import sqlite3

def view_book():
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)

def add_to_book():
    new_id = int(input("Enter the ID: "))
    new_first_name = input("Enter the first name: ")
    new_surname = input("Enter the surname: ")
    new_phonenumber = input("Enter the phone number: ")
    cursor.execute("""INSERT OR IGNORE INTO Names(ID, [First Name], Surname, [Phone Number])
        VALUES(?, ?, ?, ?)""", (new_id, new_first_name, new_surname, new_phonenumber))
    db.commit()

def search_surname():
    search = input("Enter the surname you want to find: ")
    cursor.execute("SELECT * FROM Names WHERE Surname = ?", (search,))
    for x in cursor.fetchall():
        print(x)

def delete_person():
    delete_id = int(input("Enter the ID you want to delete: "))
    cursor.execute("DELETE FROM Names where ID = ?", (delete_id,))
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)

with sqlite3.connect("/Users/clariceeee/AIO Python/Python by example/PhoneBook.db") as db:
    cursor = db.cursor()

def main():
    again = "y"
    while again == "y":
        print("Main Menu")
        print("1) View phone book\n2) Add to phone book\n3) Search for surname\n4) Delete person from phone book\n5) Quit")
        selection =int(input("Enter your selection: "))
        if selection == 1:
            view_book()
        elif selection == 2:
            add_to_book()
        elif selection == 3:
            search_surname()
        elif selection == 4:
            delete_person()
        elif selection == 5:
            again = "n"
        else:
            print("Incorrect number input!!")

main()
db.close()
