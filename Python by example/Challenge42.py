total = 0
for i in range(0,5):
    num = int(input("Enter a number: "))
    include = input("Include this number in the total? (y/n): ")
    if include == 'y':
        total += num
print("The total is:", total)