import csv
with open("Books.csv") as file:
    start_year = int(input("Enter a starting year: "))
    end_year = int(input("Enter an end year: "))
    for row in file:
        row_check = row.split(", ")
        year = int(row_check[2])
        if year in range(start_year, end_year+1):
            book = row_check[0]
            print(f"{book} is published in {year}")

