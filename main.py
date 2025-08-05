import tkinter as tk
from App import App


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.master.title("Chloes Gift")
    app.master.minsize(500,500)
    root.mainloop()