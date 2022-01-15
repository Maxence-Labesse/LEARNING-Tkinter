"""display message boxes

- showinfo,
- showwarning,
- showerror,
- askokcancel,
- askyesno
"""
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox


def display_messages():
    """display different types of messageboxes

    """
    # info
    messagebox.showinfo(title="This is and info", message="Hello world!")
    # warning
    messagebox.showwarning(title="This is a warning", message="Be careful world!")
    # error
    messagebox.showerror(title="This is an error", message="Wrong world!")
    # yes/no questions
    yes_no_answer = messagebox.askyesno(title="This is a yes no question", message="Is everything ok?")
    if yes_no_answer == 1:
        txt = "You clicked yes"
    else:
        txt = "You clicked no"
    Label(root, text=txt).pack()


# Global window settings
root = Tk()
root.title("Title")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# button to display messageboxes
ttk.Button(root, text="Popup", command=display_messages).pack()

# Loop for dynamic screen
root.mainloop()
