word = input("Enter a word: ")
first = word[0]
rest = word[1:]
if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
    new_word = word + "way"
else:
    new_word = rest + first + "ay"
print(new_word.lower())