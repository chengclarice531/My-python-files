from tkinter import *
import sqlite3

def add_data():
    name = entry_name.get()
    grade = entry_grade.get()
    with sqlite3.connect("/Users/clariceeee/AIO Python/Python by example/TestScores.db") as db:
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Results(
            Name text,
            Grade integer)""")
        cursor.execute("""INSERT INTO Results(Name,Grade)
        VALUES(?,?)""",(name,grade))
        db.commit()
def clear_window():
    entry_grade.delete(0,END)
    entry_name.delete(0,END)
    window.focus()

window = Tk()
window.title("TestScores")
window.geometry("500x400")

label_name = Label(text = "Enter student's name: ", justify = "center")
label_name.place(x=10,y=10,width=150,height=30)

entry_name = Entry(justify = "center")
entry_name.place(x=161,y=10,width=125,height=30)

label_grade = Label(text = "Enter student's grade: ", justify = "center")
label_grade.place(x=10,y=50,width=150,height=30)

entry_grade = Entry(justify = "center")
entry_grade.place(x=161,y=50,width=125,height=30)

button_add = Button(text = "Add", command = add_data, justify = "center")
button_add.place(x=161,y=90,width=80,height=30)

button_clear = Button(text = "Clear", command = clear_window, justify = "center")
button_clear.place(x=260,y=90,width=80,height=30)

window.mainloop()