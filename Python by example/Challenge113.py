import csv
with open("Books.csv", "a+") as file:
    records = int(input("How many records do you add to 'Books.csv'? "))
    for i in range(records):
        book = input("Enter a book name: ").title()
        author = input("Enter the author's name: ").title()
        year = input("Enter the book's year of publish: ")
        newrecord = book + ", " + author + ", " + year + "\n"
        file.write(newrecord)
    author_check = input("Enter a author's name: ").title()
    count = 0
    file.seek(0)
    for row in file:
        if author_check in str(row):
            book_check = row.split(", ")
            print(book_check[0].strip())
            count += 1
    if count == 0:
        print(f"{author_check} did not write any books in this list." )