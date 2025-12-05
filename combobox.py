from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("Galaxy")

window.geometry('350x200')

combo = Combobox(window)

combo['values'] = (1, 2, 3, 4, 5, "Text")

combo.current(2)

combo.grid(column=0, row=0)

lbl = Label(window, text="Hello")
lbl.grid(column=1, row=4)

def clicked():
    if combo.get() != "Text":
        lbl.configure(text="You picked " + combo.get() + "!")
    else:
        lbl.configure(text="")

btn = Button(window, text="Click me", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()