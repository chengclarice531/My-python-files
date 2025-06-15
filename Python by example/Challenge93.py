from array import *
numbers = array('i', [])
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
numbers = sorted(numbers)
remove1 = int(input("Select one number to be removed: "))
numbers.remove(remove1)
newArray = array('i',[remove1])