from array import *
integers = array('i', [])
i = 0
while i < 5:
    num = int(input("Enter a number: "))
    if num >= 10 and num <= 20:
        integers.append(num)
        i +=1
    else:
        print("Outside the range")
print("Thank you")
for i in integers:
    print(i)