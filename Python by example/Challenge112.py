import csv
with open("Books.csv", "a+") as file:
    book = input("Enter a book name: ").title()
    author = input("Enter the author's name: ").title()
    year = input("Enter the book's year of publish: ")
    newrecord = book + ", " + author + ", " + year + "\n"
    file.write(newrecord)
    file.seek(0)
    for row in file:
        print(row, end="")