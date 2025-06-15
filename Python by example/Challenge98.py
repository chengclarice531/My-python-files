d_list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
row = int(input("Choose a row to display (0-3): "))
print(d_list[row])
NewValue = int(input("A new value for the row: "))
d_list[row].append(NewValue)
print(d_list[row])