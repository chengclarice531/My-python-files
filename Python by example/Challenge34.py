print("1) Square\n2) Triangle")
num = int(input("Enter a number: "))
if num == 1:
    length = float(input("Enter the length of square: "))
    print(round(length ** 2, 2))
elif num == 2:
    base = float(input("Enter the base of the tirangle: "))
    height = float(input("Enter the height of the triangle: "))
    print(round(base * height, 2))
else:
    print("Invalid number entered")