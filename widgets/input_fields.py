"""
Input field
"""
import tkinter.ttk as ttk
from tkinter import *

# Global window settings
root = Tk()
root.title("Title")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')


def submit():
    """
    display entry
    """
    hello = "hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


# input field
e = Entry(root)
e.pack()

# button to show filled text
myButton = Button(root, text="Enter your name", command=submit)
myButton.pack()

root.mainloop()
