from tkinter import *

def change_pic():
    num = entry.get()
    artname = num + ".gif"
    photo = PhotoImage(file = "/Users/clariceeee/AIO Python/Python by example/" + artname)
    photobox.image = photo
    photobox["image"] = photo
    photobox.pack()
    photobox.update()

window = Tk()
window.title("Select photo")
window.geometry("500x400")

art = PhotoImage(file = "/Users/clariceeee/AIO Python/Python by example/1.gif")
photobox = Label(window, image = art)
photobox.image = art
photobox.pack()
photobox.place(x=10,y=10,width=200,height=200)

label =Label(text = "Select Art number:")
label.place(x=200,y=220,width=120,height=25)

entry = Entry(text="",justify="center")
entry.place(x=330,y=220,width=100,height=25)

button = Button(text = "See Art", command = change_pic)
button.place(x=330,y=250,width=100,height=25)

window.mainloop()