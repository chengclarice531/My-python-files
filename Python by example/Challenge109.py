print("1) Create a new file\n2) Display the file\n 3) Add a new item to the file")
select = int(input("Make a selection 1, 2 or 3: "))
if select == 1:
    subject = input("Enter a school subject: ").capitalize()
    x = open("Subject.txt", "w")
    x.write(subject + "\n")
    x.close()
elif select == 2:
    x = open("Subject.txt", "r")
    print(x.read())
elif select == 3:
    subject = input("Enter a school subject: ").capitalize()
    x = open("Subject.txt", "a")
    x.write(subject + "\n")
    x.close()
    x = open("Subject.txt", "r")
    print(x.read())
else:
    print("Invalid selection. Please choose 1, 2, or 3.")