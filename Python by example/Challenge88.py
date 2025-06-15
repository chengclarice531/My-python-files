from array import *
# the code above imports the array module and all its functions
"""import array as arr
# the code above imports the array module and renames it to arr"""
numbers = array('i', [])
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
numbers = sorted(numbers)
print("The sorted numbers are:")
numbers.reverse()
print(numbers)
