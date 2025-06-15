from array import *
numbers = array('i', [68,18,90,13,43])
print(numbers)
num = int(input("Enter a number in the array: "))
guess = False
while not guess:
    if num in numbers:
        position = numbers.index(num)
        print(f"{num} is in the list at position {position}.")
        guess = True
    else:
        print(f"{num} is not in the list.")
        num = int(input("Enter a number in the array: "))