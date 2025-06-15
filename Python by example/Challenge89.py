from array import *
import random
integers = array('i',[])
for i in range(5):
    num = random.randint(1,100)
    integers.append(num)
for i in integers:
    print(i)
