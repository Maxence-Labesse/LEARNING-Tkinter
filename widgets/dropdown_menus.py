"""
select a single option in a dropdown menu
"""
import tkinter.ttk as ttk
from tkinter import *
from PIL import ImageTk, Image

# Global window settings
root = Tk()
root.title("Title")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

def show():
    """
    show selection
    """
    Label(root, text=var.get()).pack()


# dropdown menu options and variables
options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
var = StringVar()
var.set("Monday")
# dropdown button
drop = OptionMenu(root, var, *options)
drop.pack()

# button to show selection
myButton = Button(root, text="Show Selection", command=show)
myButton.pack()

# Loop for dynamic screen
root.mainloop()
