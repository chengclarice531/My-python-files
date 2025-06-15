import sqlite3

with sqlite3.connect("/Users/clariceeee/AIO Python/Python by example/BookInfo.db") as db:
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Authors")
    for x in cursor.fetchall():
        print(x)
    birth_selection = input("Enter a place of birth: ")
    cursor.execute("SELECT Title, Author, [Date Published] FROM Authors JOIN Books ON Authors.Name = Books.Author WHERE [Place of Birth] = ?", (birth_selection,))
    for x in cursor.fetchall():
        print(x)
