import csv
with open("Books.csv") as file:
    # row_with_row_counter is an enumerate object that gives us both the index and the row
    row_with_row_counter = enumerate(csv.reader(file))
    # Loop through one row at the time, with a row counter i, row is the entire row
    for i, row in row_with_row_counter:
        print(i, row)