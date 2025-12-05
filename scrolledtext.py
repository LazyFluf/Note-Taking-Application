import tkinter as tk
from tkinter.scrolledtext import ScrolledText

window = tk.Tk()
window.title('Scrolled Text Widget')
window.geometry('400x400')

st = ScrolledText(window, width=40, height=10)
st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()