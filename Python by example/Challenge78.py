TV_programme = ["The Simpsons", "Friends", "Game of Thrones", "Stranger Things"]
for i in TV_programme:
    print(i)
show = input("Enter a TV programme: ")
position = int(input("Enter a position: "))
TV_programme.insert(position, show)
for i in TV_programme:
    print(i)