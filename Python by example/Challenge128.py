from tkinter import *

def km_to_miles():
    km = float(entry_km.get())
    ans_miles = 0.6214 * km
    entry_miles.delete(0, END)
    entry_miles.insert(0, round(ans_miles, 2))
    entry_km.delete(0, END)
def miles_to_km():
    miles = float(entry_miles.get())
    ans_km = 1.6093 * miles
    entry_km.delete(0, END)
    entry_km.insert(0, round(ans_km, 2))
    entry_miles.delete(0, END)

window = Tk()
window.title("Converting between km and miles")
window.geometry("500x500")

entry_km = Entry(bg = "grey", fg = "white", justify = "center")
entry_km.place(x=1,y=1,width=100,height=25)

entry_miles = Entry(bg = "wheat", fg = "white", justify = "center")
entry_miles.place(x=1,y=50,width=100,height=25)

label_km = Label(text = "kilometre", bg = "plum", fg = "white", justify = "center")
label_km.place(x=150,y=1,width=100,height=25)

label_miles = Label(text = "miles", bg = "chocolate", fg = "white", justify = "center")
label_miles.place(x=150,y=50,width=100,height=25)

button_convert_to_miles = Button(text = "Convert", command = km_to_miles, bg = "salmon", fg = "white", justify = "center")
button_convert_to_miles.place(x=300,y=1,width=100,height=25)

button_convert_to_km = Button(text = "Convert", command = miles_to_km, bg = "gold", fg = "white", justify = "center")
button_convert_to_km.place(x=300,y=50,width=100,height=25)

"""output_box = Message(text = "", bg = "aqua", fg = "white")
output_box.place(x=150,y=100,width=100,height=50)"""
window.mainloop()