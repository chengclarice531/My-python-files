from tkinter import *
def add_name():
    NewName = entry_box.get()
    output_box.insert(END, NewName.capitalize())
    output_box["bg"] = "light blue"
    output_box["fg"] = "black"
    output_box["justify"] = "left"
    entry_box.delete(0, END)
def clear():
    output_box.delete(0, END)
    output_box["bg"] = "white"
    output_box ["fg"] = "black"

window = Tk()
window.title("Name List")
window.geometry("500x500")

enter_a_name = Label(text = "Enter a name:", bg = "grey", fg = "white", justify = "center")
enter_a_name.place(x=1,y=1,width=100,height=25)

entry_box = Entry( text = " ", bg = "white", fg = "black", justify = "center")
entry_box.place(x=151,y=1,width=100,height=25)

button_add = Button(text = "Add", command = add_name, bg = "pink", fg = "black", justify = "center")
button_add.place(x=301,y=1,width=80,height=25)

output_box = Listbox(bg = "light blue", fg = "black", justify = "left")
output_box.place(x=1,y=40,width=250,height=100)

button_clear = Button(text = "clear", command = clear, bg = "green", fg = "white", justify = "center")
button_clear.place(x=301,y=90,width=80,height=25)

window.mainloop()