import array as arr
numbers = arr.array('i', [12, 12, 90, 89, 65])
print(numbers)
num = int(input("Enter a number in the array: "))
repeat = numbers.count(num)
print(f"{num} is in the list {repeat} times.")