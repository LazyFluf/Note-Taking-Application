import tkinter as tk

window = tk.Tk()
window.title('Galaxy Code')
window.geometry('400x400')

lbl = tk.Label(window, width=50, height=20, text='empty', font=('Arial Bold', 9))
lbl.pack()

def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        lbl.config(text='I love Python!')
    elif (var1.get() == 0) & (var2.get() == 1):
        lbl.config(text='I love C++!')
    elif (var1.get() == 0) & (var2.get() == 0):
        lbl.config(text='I love neither!')
    else:
        lbl.config(text='I love both!')

var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()

window.mainloop()