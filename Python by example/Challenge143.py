import sqlite3

with sqlite3.connect("/Users/clariceeee/AIO Python/Python by example/BookInfo.db") as db:
    cursor = db.cursor()
    selectionyear = int(input("Enter a year: "))
    cursor.execute("""SELECT Title, Author, [Date Published] FROM Books 
        where [Date Published] > ? ORDER BY [Date Published]""", (selectionyear,))
    for x in cursor.fetchall():
        print(x)