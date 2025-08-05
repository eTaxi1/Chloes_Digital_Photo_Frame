import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self, master):
        self.master = master
        self.image = tk.PhotoImage(file="Images/roger.png")
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill="both", expand=True)
        self.image_label = tk.Label(self.frame, image=self.image)
        self.image_label.image = self.image
        self.image_label.place(relx=0.5, rely=0.5, anchor="center")

    
    
    
    