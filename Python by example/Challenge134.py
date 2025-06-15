from tkinter import *
import random

def check_answer():
    input = int(guess.get())
    if (num1+num2) == input:
        tick = PhotoImage(file = "/Users/clariceeee/AIO Python/Python by example/tick.png")
        tick = tick.subsample(2, 2)  # Resize the image if needed
        output_box.config(image=tick)
        output_box.image = tick
    else:
        cross = PhotoImage(file = "/Users/clariceeee/AIO Python/Python by example/cross.png")
        cross = cross.subsample(2, 2)  # Resize the image if needed
        output_box.config(image=cross)
        output_box.image = cross
    
    output_box.pack(side="left")


def next_question():
    global num1, num2
    num1 = random.randint(10,50)
    num2 = random.randint(10,50)
    question = f"{num1} + {num2} ="
    math_question.config(text = question)
    guess.delete(0,END)
    output_box.config(image='')
    output_box.image = None

window = Tk()
window.title("Math quizzzz")
window.configure(background = "lavender")
window.geometry("500x400")

num1 = random.randint(10,50)
num2 = random.randint(10,50)
question = f"{num1} + {num2} ="
math_question = Label(text = question, justify = "center")
math_question.place(x=5,y=5,width=200,height=30)

guess = Entry(text = "", bg="tomato", fg="black", justify = "center")
guess.place(x=250,y=5,width=100,height=30)

button_check = Button(text = "check", command = check_answer, fg = "black", justify = "center")
button_check.place(x=400,y=5,width=80,height=25)

output_box = Label()
output_box.place(x=100,y=40,width=150,height=150)

button_next = Button(text = "Next", command = next_question, fg = "black", justify = "center")
button_next.place(x=200,y=200,width=80,height=25)

window.mainloop()