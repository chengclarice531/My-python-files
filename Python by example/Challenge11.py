Largenum = int(input("Enter a number over 100: "))
while Largenum <= 100 or Largenum < 0:
    print("The number is not over 100.")
    Largenum = int(input("Enter a number over 100: "))
Smallnum = int(input("Enter a number under 10: "))
while Smallnum >= 10 or Smallnum < 0:  
    print("The number is not under 10.")
    Smallnum = int(input("Enter a number under 10: "))
times = Largenum // Smallnum
print(f"{Smallnum} goes into {Largenum} a total of {times} times.")
