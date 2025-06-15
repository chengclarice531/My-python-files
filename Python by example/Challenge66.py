import random
import turtle
for i in range(0,8):
    colour = random.choice(['red', 'green', 'blue', 'yellow', 'purple', 'orange'])
    turtle.color(colour)
    turtle.begin_fill()
    turtle.forward(100)
    turtle.right(45)
    turtle.end_fill()
turtle.exitonclick()