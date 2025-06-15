from array import *
numbers = array('f',[10.5, 28.4, 29.2, 42.8, 90.5])
tryagain = True
while tryagain == True:
    divide = int(input("Enter a number between 2 and 5: "))
    if divide < 2 or divide > 5:
        print("Error, please enter again! ")
    else:
        tryagain = False
for i in numbers:
    ans = i / divide
    print(round(ans, 2))