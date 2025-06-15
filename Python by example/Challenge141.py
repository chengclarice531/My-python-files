import sqlite3

with sqlite3.connect("/Users/clariceeee/AIO Python/Python by example/BookInfo.db") as db:
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Authors(
        Name text,
        [Place of Birth] text)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
        ID integer PRIMARY KEY,
        Title text,
        Author text,
        [Date Published] integer)""")
    
    cursor.execute("""INSERT OR IGNORE INTO Authors(Name, [Place of Birth])
        VALUES("Agatha Christie", "Torquay")""")
    cursor.execute("""INSERT OR IGNORE INTO Authors(Name, [Place of Birth])
        VALUES("Cecelia Ahern", "Dublin")""")
    cursor.execute("""INSERT OR IGNORE INTO Authors(Name, [Place of Birth])
        VALUES("J.K. Rowling", "Bristol")""")
    cursor.execute("""INSERT OR IGNORE INTO Authors(Name, [Place of Birth])
        VALUES("Oscar Wilde", "Dublin")""")
    
    cursor.execute("""INSERT OR IGNORE INTO Books(ID, Title, Author, [Date Published])
        VALUES(1, "De Profundis", "Oscar Wilde", 1905)""")
    cursor.execute("""INSERT OR IGNORE INTO Books(ID, Title, Author, [Date Published])
        VALUES(2, "Harry Potter and the chamber of secrets", "J.K. Rowling", 1998)""")
    cursor.execute("""INSERT OR IGNORE INTO Books(ID, Title, Author, [Date Published])
        VALUES(3, "Harry Potter and the prisoner of Azkaban", "J.K. Rowling", 1999)""")
    cursor.execute("""INSERT OR IGNORE INTO Books(ID, Title, Author, [Date Published])
        VALUES(4, "Lyrebird", "Cecelia Ahern", 2017)""")
    cursor.execute("""INSERT OR IGNORE INTO Books(ID, Title, Author, [Date Published])
        VALUES(5, "Murder on the Orient Express", "Agatha Christie", 1934)""")
    cursor.execute("""INSERT OR IGNORE INTO Books(ID, Title, Author, [Date Published])
        VALUES(6, "Perfect", "Cecelia Ahern", 2017)""")
    cursor.execute("""INSERT OR IGNORE INTO Books(ID, Title, Author, [Date Published])
        VALUES(7, "The marble collector", "Cecelia Ahern", 2016)""")
    cursor.execute("""INSERT OR IGNORE INTO Books(ID, Title, Author, [Date Published])
        VALUES(8, "The murder on the links", "Agatha Christie", 1923)""")
    cursor.execute("""INSERT OR IGNORE INTO Books(ID, Title, Author, [Date Published])
        VALUES(9, "The picture of Dorian Gray", "Oscar Wilde", 1890)""")
    cursor.execute("""INSERT OR IGNORE INTO Books(ID, Title, Author, [Date Published])
        VALUES(10, "The secret adversary", "Agatha Christie", 1921)""")
    cursor.execute("""INSERT OR IGNORE INTO Books(ID, Title, Author, [Date Published])
        VALUES(11, "The seven dials mystery", "Agatha Christie", 1929)""")
    cursor.execute("""INSERT OR IGNORE INTO Books(ID, Title, Author, [Date Published])
        VALUES(12, "The year I met you", "Cecelia Ahern", 2014)""")
    
    db.commit()