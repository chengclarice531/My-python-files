import sqlite3

try:
    with sqlite3.connect("/Users/clariceeee/AIO Python/Python by example/PhoneBook.db") as db:
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
            ID INTEGER PRIMARY KEY,
            [First Name] TEXT NOT NULL,
            Surname TEXT NOT NULL,
            [Phone Number] TEXT NOT NULL)""")
        cursor.execute("""INSERT OR IGNORE INTO Names(ID, [First Name], Surname, [Phone Number])
            VALUES(1, "Simon", "Howels", "01223 349752")""")
        cursor.execute("""INSERT OR IGNORE INTO Names(ID, [First Name], Surname, [Phone Number])
            VALUES(2, "Karen", "Philips", "01954 295773")""")
        cursor.execute("""INSERT OR IGNORE INTO Names(ID, [First Name], Surname, [Phone Number])
            VALUES(3, "Darren", "Smith", "01583 749012")""")
        cursor.execute("""INSERT OR IGNORE INTO Names(ID, [First Name], Surname, [Phone Number])
            VALUES(4, "Anne", "Jones", "01323 567322")""")
        cursor.execute("""INSERT OR IGNORE INTO Names(ID, [First Name], Surname, [Phone Number])
            VALUES(5, "Mark", "Smith", "01223 855534")""")
        db.commit()

except sqlite3.Error as e:
    print(f"An error occurred: {e}")