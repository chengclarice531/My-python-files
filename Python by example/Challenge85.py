name = input("Enter your name: ")
count = 0
for i in name:
    if i == "a" or i =="e" or i == "i" or i == "o" or i == "u":
        count += 1
print("There are", count, "vowels in your name.")