"""
Create an app to notify whether a checkbox is checked
"""
import tkinter.ttk as ttk
from tkinter import *

# Global window settings
root = Tk()
root.title("Title")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# initiate my_label
my_label = Label(text="")
# initiate checkbox var
var = StringVar()
var.set("Off")


def show():
    """
    when "Show Selection" button is pressed, delete last label and displays another one according to box checking
    """
    global my_label
    # delete last label
    my_label.destroy()
    # displays checkbox state
    txt = var.get()
    my_label = Label(root, text=txt)
    my_label.pack()


# checkbox
c = Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off")
c.pack()

# button that show selection
myButton = Button(root, text="Show Selection", command=show)
myButton.pack()

# Loop for dynamic screen
root.mainloop()
