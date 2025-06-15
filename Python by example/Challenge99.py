d_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("Choose a row to display (0-3): "))
print(d_list[row])
column = int(input("Choose a column to display (0-2): "))
result = d_list[row][column]
print(f"The value at row {row} and column {column} is: {result}")
change = input("Do you want to change the value (yes/no)? ").lower()
if change == "yes":
    NewValue = int(input("A new value for the row: "))
    d_list[row][column] = NewValue
print(d_list[row])