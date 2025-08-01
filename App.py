from tkinter import *
from tkinter import ttk


class App:
    def __init__(self):
        pass
        
    def init(self):
        root = Tk()
        root.title("Chloes Gift")
        frm = ttk.Frame(root, padding=100)
        frm.grid()
        ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
        root.mainloop()
    
    