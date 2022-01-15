"""get input (text strings) from the user
"""
import tkinter.ttk as ttk
from tkinter import *

# Global window settings
root = Tk()
root.title("Entry widget")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')


def submit_name():
    """display user name and welcome him

    """
    hello = "hello " + name_entry.get()
    hello_label = Label(root, text=hello)
    hello_label.pack()


# input field
name_entry = Entry(root)
name_entry.pack()

# button to show filled text
submit_name_button = Button(root, text="Enter your name", command=submit_name)
submit_name_button.pack()

root.mainloop()
