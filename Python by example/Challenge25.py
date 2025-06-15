first_name = input("Enter your first name: ")
if len(first_name) < 5:
    surname = input("Enter your surname: ")
    whole_name = first_name+surname
    whole_name = whole_name.upper()
    print(whole_name)
elif len(first_name) >= 5:
    first_name = first_name.lower()
    print(first_name)