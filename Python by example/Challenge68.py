import random
i = random.randrange(3,10,1)
line = random.randrange(50,100,25)
angle = random.randrange(36, 60, 1)
import turtle
for j in range(0,i):
    turtle.forward(line)
    turtle.right(angle)
turtle.exitonclick()