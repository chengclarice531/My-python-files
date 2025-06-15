alphabet = ["a","b","c","d","e","f",
            "g","h","i","j","k","l","m","n","o",
            "p","q","r","s","t","u","v","w","x",
            "y","z"," "]

def get_data():
    message = input("Enter a message: ").lower()
    num = int(input("Enter a number: "))
    if num == 0 or num>26:
        while num == 0 or num>26:
            num = int(input("Out of range, please enter a number again: "))
    data = (message,num)
    return data

def make_code(message,num):
    new_word = ""
    for x in message:
        y = alphabet.index(x)
        y += num
        if y > 26:
            y = y - 27
        char = alphabet[y]
        new_word = new_word + char
    print(new_word)

def decode_code(message,num):
    new_word = ""
    for x in message:
        y = alphabet.index(x)
        y -= num
        if y < 0:
            y = y + 27
        char = alphabet[y]
        new_word = new_word + char
    print(new_word)

def main():
    again = "y"
    while again == "y":
        print("1) Make a code\n2) Decode a message\n3) Quit")
        selection = int(input("Enter your selection: "))
        if selection == 1:
            (message,num) = get_data()
            make_code(message,num)
        elif selection == 2:
            (message,num) = get_data()
            decode_code(message,num)
        elif selection == 3:
            again = "n"
        else:
            print("Wrong number entered!!!")

main()