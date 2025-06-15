from tkinter import *
import csv

def show_file():
    output_box.delete(0,END)
    file = open("People list.csv", "r")
    for row in file:
        output_box.insert(END, row)
    file.close()
        
def save_item():
    name = entry_name.get()
    age = entry_age.get()
    with open("People list.csv", "a") as file:
        new_record = name + ", " + age + "\n"
        file.write(new_record)
    entry_name.delete(0,END)
    entry_age.delete(0,END)

window = Tk()
window.title("People list")
window.geometry("400x400")

enter_name = Label(text = "Name:", justify = "center")
enter_name.place(x=1,y=50,width=100,height=30)

enter_age = Label(text = "Age:", justify = "center")
enter_age.place(x=1,y=81,width=100,height=30)

entry_name = Entry(justify = "center")
entry_name.place(x=105,y=50,width=100,height=30)

entry_age = Entry(justify = "center")
entry_age.place(x=105,y=81,width=100,height=30)

button_save = Button(text = "Save", command = save_item, justify = "center")
button_save.place(x=210,y=60,width=100,height=30)

button_show = Button(text = "Show", command = show_file, justify = "center")
button_show.place(x=150,y=115,width=100,height=30)

output_box = Listbox()
output_box.place(x=10,y=150,width=300,height=200)

window.mainloop()