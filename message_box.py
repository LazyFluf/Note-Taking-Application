from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Galaxy Coding')
window.geometry('400x400')

def clicked():
    messagebox.showinfo('message title', 'message text')

btn = Button(window, text='click here', command=clicked)
btn.grid(column=0, row=0)

window.mainloop()