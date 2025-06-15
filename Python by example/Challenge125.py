import random
from tkinter import *

def rolling_die():
    output_txt = Message(text = " ")
    die = random.randint(1,6)
    output_txt["text"] = die
    output_txt["fg"] = "black"
    output_txt["bg"] = "light blue"
    output_txt["justify"] = "center"
    output_txt.place(x = 190, y = 80, width = 100, height = 30)

window = Tk()
window.title("Rolling a six-sided die")
window.geometry("500x300")

button1 = Button(text = "Click here to roll the die", command = rolling_die)
button1.place(x = 100, y = 37, width = 300, height = 25)

window.mainloop()