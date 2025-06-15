x = open("Names.txt", "r")
print(x.read())
x.close()

name = input("Enter a name from above: ").capitalize()
name = name + "\n"
y = open("Names2.txt", "w")
y.close()
x = open("Names.txt", "r")
for i in x:
    if i != name:
        y = open("Names2.txt", "a")
        y.write(i)
        y.close()
x.close()
