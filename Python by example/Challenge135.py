from tkinter import *

def click_me():
    select = selectcolour.get()
    window.configure(bg = select)

window = Tk()
window.configure(bg = "grey")
window.title("Colour Selector")
window.geometry("500x400")

selectcolour = StringVar(window)
selectcolour.set("Select colour")
colour_list = OptionMenu(window, selectcolour, "red","blue","purple")
colour_list.place(x=200,y=150)

button_click = Button(text = "Click me", command = click_me, justify = "center")
button_click.place(x=300,y=150,width=100,height=30)

window.mainloop()