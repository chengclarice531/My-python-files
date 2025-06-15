new_password = input("Enter your new password: ")
confirm = input("Please enter your new password again: ")
if new_password == confirm:
    print("Thank you")
elif new_password.lower() == confirm.lower():
    print("They must be in the same case")
else:
    print("Incorrect")