first_line = input("Enter the first line of a nursery rhyme: ")
length_line = len(first_line)
print(f"There are {length_line} letters in the first line, including spaces.")
starting_num = int(input("A starting number? "))
ending_num = int(input("A ending number? "))
starting_num -= 1
ending_num += 1
print(first_line[starting_num:ending_num])