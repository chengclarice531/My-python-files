import csv
with open("Books.csv") as file:
    reader = csv.reader(file)
    reader = list(reader)  # Convert the reader object to a list to print it
    reader_with_number = enumerate(reader)
    for i, row in reader_with_number:
        print(i, row)
remove_index = int(input("Which row do you wish to delete? "))
del reader[remove_index]
i = 0
for row in reader:
    print(i, row)
    i += 1
row_change = int(input("Which row do you wish to make changes? "))
x = 0
for column in reader[row_change]:
    y = x, reader[row_change][x]
    print(y)
    x += 1
column_change = int(input("Enter a column to make changes: "))
value = input("New value: ")
reader[row_change][column_change] = value
with open("Books.csv", "w+") as file:
    for row in reader:
        NewRecord = ",".join(row) + "\n"
        file.write(NewRecord)
    reader_with_number = enumerate(csv.reader(file))
    for i, row1 in reader_with_number:
        print(i, row1)
    