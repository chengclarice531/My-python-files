Firstnum = int(input("Enter first number: "))
Secondnum = int(input("Enter second number: "))
if Firstnum > Secondnum:
    print(f"{Firstnum} is greater than {Secondnum}.")
elif Secondnum > Firstnum:
    print(f"{Secondnum} is greater than {Firstnum}.")
else:
    print(f"{Firstnum} is equal to {Secondnum}.")