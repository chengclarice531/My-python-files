num = int(input("Enter a number: "))
name = input('Enter a name: ')
if num < 10:
    for i in range(0,num):
        print(name)
else:
    for i in range(0,3):
        print("Too high")