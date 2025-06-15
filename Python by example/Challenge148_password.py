import csv

def get_data():
    tmp = []
    with open("Password.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            tmp.append(row)
    return tmp
        
def create_id(tmp):
    again = True
    while again == True:
        user_id = input("Enter a new user ID: ").lower()
        inlist = False
        row = 0
        for y in tmp:
            if user_id == tmp[row][0]:
                print(f"{user_id} has been allocated")
                inlist = True
            row += 1
        if inlist == False:
            again = False
    return user_id

def create_password():
    password_again = True
    while password_again == True:
        new_password = input("Enter the password: ")
        num = ["0","1","2","3","4","5","6","7","8","9"]
        special_char = ["!","£","$","%","&","<","*","@"]
        score = 0
        uc = False
        lc = False
        nc = False
        sc = False
        length = len(new_password)
        if length >= 8:
            score += 1
        for x in new_password:
            if x.isupper():
                uc = True
            if x.islower():
                lc = True
            if x in num:
                nc = True
            if x in special_char:
                sc = True
        if uc == True:
            score += 1
        if lc == True:
            score += 1
        if nc == True:
            score += 1
        if sc == True:
            score += 1
        if score == 1 or score == 2:
            print("It is a weak password")
        if score == 3 or score == 4:
            print("This password could be improved")
            try_again = input("Do you want to try again? (y/n) ").lower()
            if try_again == "n":
                password_again = False
        if score == 5:
            print("This is a strong password")
            password_again = False
    return new_password

def find_user_id(tmp):
    again = True
    while again == True:
        user_id = input("Enter a user ID to change the password: ").lower()
        row = 0
        inlist = False
        for x in tmp:
            if user_id == tmp[row][0]:
                inlist = True
            row += 1
        if inlist == True:
            again = False
        else:
            print(f"{user_id} is not in the list.")
    return user_id
    
def add_data(user_id,tmp):
    new_password = create_password()
    for i, row in enumerate(tmp):
        if row[0] == user_id:
            tmp[i][1] = new_password
            break
    else:
        print("User ID not found.")
        return  # Exit early if user not found
    with open("Password.csv", "w") as file:
        for x, row in enumerate(tmp):
            NewRecord = row[0] + ", " + row[1] + "\n"
            file.write(NewRecord)

def display_id():
    tmp = get_data()
    x = 0
    for row in tmp:
        print(tmp[x][0])
        x += 1
def main():
    open("Password.csv", "a").close() 
    tmp = get_data()
    go_again = "y"
    while go_again == "y":
        print("1) Create a new User ID")
        print("2) Change a password")
        print("3) Display all User IDs")
        print("4) Quit")
        print()
        selection = int(input("Enter selection: "))
        if selection == 1:
            user_id = create_id(tmp)
            new_password = create_password()
            tmp.append([user_id, new_password])
            with open("Password.csv", "w") as file:
                x = 0
                for row in tmp:
                    NewRecord = tmp[x][0] + ", " + tmp[x][1] + "\n"
                    file.write(NewRecord)
                    x += 1
        elif selection == 2:
            user_id = find_user_id(tmp)
            add_data(user_id,tmp)
        elif selection == 3:
            display_id()
        elif selection == 4:
            go_again = "n"
        else:
            print("Wrong number entered")

main()
