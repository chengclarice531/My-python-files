d_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row  = int(input("Enter the row number (0-3): "))
column = int(input("Enter the column number (0-2): "))
result = d_list[row][column]
print(f"The value at row {row} and column {column} is: {result}")