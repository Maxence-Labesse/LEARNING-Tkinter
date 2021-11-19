import tkinter.ttk as ttk
from tkinter import *
from PIL import ImageTk, Image

# First widget: global window
root = Tk()
root.title("Title")
root.iconbitmap("icon2.ico")
style = ttk.Style()
style.theme_use('clam')

var = IntVar()

myLabel = Label(root)


def show():
    global myLabel
    myLabel.destroy()
    txt = var.get()
    myLabel = Label(root, text=txt)
    myLabel.pack()


c = Checkbutton(root, text="Check this box", variable=var, command=show)
c.pack()

# Loop for dynamic screen
root.mainloop()
