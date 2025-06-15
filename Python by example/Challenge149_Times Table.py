from tkinter import *

def view():
    number = entry_num.get()
    number = int(number)
    for i in range(1,13):
        answer = number * i
        output_box.insert(END,(i, "x", number, "=", answer))
    entry_num.delete(0,END)

def clear():
    entry_num.delete(0,END)
    output_box.delete(0,END)

window = Tk()
window.title("Times Table")
window.geometry("500x300")

label_num = Label(text = "Enter a number:", justify = "center")
label_num.place(x=10,y=10,width=100,height=30)

entry_num = Entry(text = "", justify = "center")
entry_num.place(x=120,y=10,width=120,height=30)

button_view = Button(text = "View Times Table", command = view, justify = "center")
button_view.place(x=250,y=10,width=120,height=30)

output_box = Listbox()
output_box.place(x=120,y=45,width=120,height=200)

button_clear = Button(text = "Clear", command = clear, justify = "center")
button_clear.place(x=250,y=45,width=120,height=30)

window.mainloop()