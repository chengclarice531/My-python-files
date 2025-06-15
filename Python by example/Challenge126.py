from tkinter import *
ans = 0
def add():
    global ans
    num = entry_box.get()
    num = int(num)
    ans = int(ans)
    ans = num + ans
    answer_box["text"] = ans
    answer_box ["bg"] = "red"
    answer_box ["fg"] = "white"
    answer_box ["relief"] = "groove"
def reset():
    global ans
    ans = 0
    answer_box["text"] = ans
    answer_box ["bg"] = "green"
    answer_box ["fg"] = "white"
    answer_box ["relief"] = "sunken"

window = Tk()
window.title("Total")
window.geometry("800x400")

enter_a_num = Label(text = "Enter a number: ", bg="blue", fg="white", relief="flat", justify="center")
enter_a_num.place(x = 1, y = 1, width = 100, height = 25)

entry_box = Entry(bg="pink", fg="white", relief="raised", justify="center")
entry_box.place(x=100, y=1, width=110, height=25)

button_add = Button(text = "Add", command = add, bg="white", fg="black", relief="raised", justify="center")
button_add.place(x = 210, y = 1, width = 80, height = 25)

total = Label(text = "Total: ", bg="orange", fg="white", relief="sunken", justify="center")
total.place(x = 1, y = 30, width = 80, height = 25)

answer_box = Message(text = "0", bg="yellow", fg="white", relief="raised", justify="center")
answer_box.place(x = 90, y = 30, width = 120, height = 25)

button_reset = Button(text = "RESET", command = reset, bg="white", fg="black", relief="raised", justify="center")
button_reset.place(x = 210, y = 30, width = 80, height = 25)

window.mainloop()