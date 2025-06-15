from tkinter import *
def click():
    name = entry_box.get()
    message = str("Hello " + name)
    output["text"] = message
    output["fg"] = "black"
    output["bg"] = "light blue"


window = Tk()
window.title("What's your name?")
window.geometry("450x100")

label = Label(text = "Enter your name: ")
label.place(x = 10, y = 10, width = 150, height = 25)

entry_box = Entry(text = " ")
entry_box ["bg"] = "blue"
entry_box ["fg"] = "white"
entry_box ["relief"] = "flat"
entry_box ["justify"] = "center"
entry_box.place(x = 165, y = 10, width = 120, height = 25)

button = Button(text = "Press me", command = click)
button.place(x = 165, y = 37, width = 120, height = 25)

output = Message(text = " ")
output.place(x = 10, y = 60, width = 430, height = 30)
output["bg"] = "light pink"
output["fg"] = "black"
window.mainloop()


