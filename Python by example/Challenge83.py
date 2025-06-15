word = input("Enter a word in uppercase: ")
while not word.isupper():
    print("Please enter a word in uppercase.")
    word = input("Enter a word in uppercase: ")
print("Congrats!")
