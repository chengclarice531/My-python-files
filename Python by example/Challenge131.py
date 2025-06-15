from tkinter import *
import csv

def create_file():
    file = open("People list.csv", "w")
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
window.geometry("400x200")

button_create = Button(text = "Create", command = create_file, justify = "center")
button_create.place(x=150,y=10,width=100,height=30)

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

window.mainloop()