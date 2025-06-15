number = int(input("Enter a number over 500: "))
if number <= 500:
    print("This number is below 500!!!!")
    number = int(input("Re-enter a number over 500: "))
import math
sq_num = math.sqrt(number)
print(round(sq_num, 2))