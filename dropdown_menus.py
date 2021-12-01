import tkinter.ttk as ttk
from tkinter import *
from PIL import ImageTk, Image

# First widget: global window
root = Tk()
root.title("Title")
root.iconbitmap("icon2.ico")
style = ttk.Style()
style.theme_use('clam')


def show():
    myLabel = Label(root, text=var.get()).pack()


options = ["z", "Tuesday", "Wednesday", "Thursday", "Friday"]

var = StringVar()
var.set("Monday")

drop = OptionMenu(root, var, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show)
myButton.pack()

# Loop for dynamic screen
root.mainloop()
