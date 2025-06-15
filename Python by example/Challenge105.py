import random
file = open("Numbers.txt", "w")
for i in range(5):
    num = random.randint(0,1000)
    file.write(f"{num},")
file.close()