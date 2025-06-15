from tkinter import *

def add_info():
    name = name_entry.get()
    name_entry.delete(0,END)
    gender = selectgender.get()
    NewRecord = name + ", " + gender + "\n"
    output_box.insert(END, NewRecord)

window = Tk()
window.title("Peronal data")
window.geometry("500x400")

name_label = Label(text = "Enter your name:", justify = "center")
name_label.place(x=20,y=20,width=150,height=30)

name_entry = Entry(text = "", justify = "center")
name_entry.place(x=171,y=20,width=100,height=30)

gender_label = Label(text = "Select your gender:", justify = "center")
gender_label.place(x=20,y=60,width=150,height=30)

selectgender = StringVar(window)
selectgender.set("M/F")
gender_list = OptionMenu(window, selectgender, "Male", "Female")
gender_list.place(x=171,y=60,width=100,height=30)

button_add = Button(text = "Add" , command = add_info)
button_add.place(x=300,y=40,width=100,height=30)

output_box = Listbox()
output_box.place(x=10,y=100,width=250,height=100)

window.mainloop()
