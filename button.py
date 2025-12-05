from tkinter import *

window = Tk()
window.geometry('350x200')

window.title("Galaxy")
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=1, row=0)

def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)
    btn.configure(state='disabled')

btn = Button(window, text="Click me!", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()