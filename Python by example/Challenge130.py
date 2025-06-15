from tkinter import *
import csv

def add_num():
    num = entry_box.get()
    if num.isdigit():
        num_list.insert(END,num)
    else:
        entry_box.delete(0,END)
def clear():
    num_list.delete(0, END)

def save():
    tmp_list = num_list.get(0,END)
    with open("Number list.csv", "a") as file:
        for number in tmp_list:
            new_record = str(number) + "\n"
            file.write(new_record)
            
window = Tk()
window.title("Did you enter a whole number?")
window.geometry("500x250")

enter_a_num = Label(text = "Enter a number: ", justify = "center")
enter_a_num.place(x=1,y=1,width=100,height=25)

entry_box = Entry(justify = "center")
entry_box.place(x=150,y=1,width=100,height=25)

button_check = Button(text = "Check", command = add_num, justify = "center")
button_check.place(x=300,y=1,width=80,height=25)

num_list = Listbox()
num_list.place(x=11,y=50,width=240,height=150)

button_clear = Button(text = "Clear", command = clear, justify = "center")
button_clear.place(x=300,y=125,width=80,height=25)

button_save = Button(text = "Save", command = save, justify = "center")
button_save.place(x=300,y=150,width=80,height=25)

window.mainloop()