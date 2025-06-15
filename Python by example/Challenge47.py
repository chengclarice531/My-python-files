num1 = int(input("Enter a number please: "))
num2 = int(input("Enter another number please: "))
total = num1 + num2
yes = "yes"
while yes == "yes":
    yes = input("Do you want to add another number? (yes/no): ").lower()
    if yes == "yes":
        num = int(input("Enter a number please: "))
        total += num
print(f"The total is {total}.")