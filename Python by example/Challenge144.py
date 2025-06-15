import sqlite3

with sqlite3.connect("/Users/clariceeee/AIO Python/Python by example/BookInfo.db") as db:
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Authors")
    for x in cursor.fetchall():
        print(x)
    selectionname = input("Enter an author's name: ")
    cursor.execute("""SELECT * FROM Books 
    WHERE Author = ?""", (selectionname,))
    file = open("/Users/clariceeee/AIO Python/Python by example/Bookdetails.txt", "w")
    for x in cursor.fetchall():
        NewRecord = str(x[0]) + " - " + x[1] + " - " + x[2] + " - " + str(x[3])+ "\n"
        file.write(NewRecord)
    file.close()