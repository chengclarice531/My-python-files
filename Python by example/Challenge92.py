import array as arr
user = arr.array('i', [])
random_num = arr.array('i', [])
for i in range(3):
    num = int(input("Enter a number: "))
    user.append(num)
import random
for i in range(5):
    num = random.randint(1,100)
    random_num.append(num)
user.extend(random_num)
user = sorted(user)
for i in user:
    print(i)
