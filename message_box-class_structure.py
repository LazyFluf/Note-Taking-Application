from tkinter import *
from tkinter import messagebox

class App(Tk):
    def __init__(window):
        super().__init__()
        window.title('Galaxy Coding')
        window.geometry('400x400')
        def clicked():
            qst = messagebox.askyesno('message title', 'message content')
            if qst == True:
                lbl.configure(text='Yes')
            else:
                lbl.configure(text='No')
        btn = Button(window, text='click here', command=clicked)
        lbl = Label(window, text='Hello there!')
        btn.pack()
        lbl.pack()

if __name__ == '__main__':
    app = App()
    app.mainloop()