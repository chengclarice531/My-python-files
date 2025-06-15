numbers = [123, 567, 908, 198]
for i in numbers:
    print(i)
num = int(input("Enter a three digit number: "))
if num in numbers:
    index = numbers.index(num)
    print(f"{num} is in position {index}. ")
else:
    print("That is not in the list")