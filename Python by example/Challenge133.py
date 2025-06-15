from tkinter import *

def show_name():
    name = entry_name.get()
    display_text = f"Hello {name}"
    output_box["text"] = display_text
    entry_name.delete(0,END)

window = Tk()
window.title("Names")
window.wm_iconbitmap("/Users/clariceeee/AIO Python/Python by example/Strips.ico")
window.configure(background = "lavender")
window.geometry("500x400")

logo = PhotoImage(file="/Users/clariceeee/AIO Python/Python by example/Slough house_logo.gif")
logoimage = Label(image = logo)
logoimage.image = logo # Keep a reference to avoid garbage collection
logoimage.pack()
logoimage.place(x=30,y=20,width=200,height=150)

enter_your_name = Label(text = "Enter your name:", bg = "black", fg = "white", justify = "center")
enter_your_name.place(x=5,y=200,width=100,height=25)

entry_name = Entry(bg = "white", fg = "grey", justify = "center")
entry_name.place(x=106,y=200,width=200,height=25)

button_pressme = Button(text = "Press me", command = show_name, bg = "red", fg = "black", justify = "center")
button_pressme.place(x=5,y=300,width=100,height=25)

output_box = Message(bg = "white", fg = "black", justify = "center")
output_box.place(x=106,y=300,width=200,height=40)

window.mainloop()