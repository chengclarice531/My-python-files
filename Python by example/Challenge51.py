num = 10
while num > 0:
    print(f"{num} green bottles sitting on the wall,\n{num} green bottles sitting on the wall,\nAnd if one green bottle should accidentally fall,")
    bottle = int(input("How many green bottles will be sitting on the wall? "))
    num -= 1
    if num == bottle:
        print(f"There'll be {num} green bottles sitting on the wall.")
    else:
        print("No, try again")
print("There are no more green bottles sitting on the wall.")