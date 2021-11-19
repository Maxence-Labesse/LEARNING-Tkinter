import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox

# First widget: global window
root = Tk()
root.title("Title")
root.iconbitmap("icon2.ico")
style = ttk.Style()
style.theme_use('clam')


# showinfo, showwarning, showerror, askquestion, asqkokcancel, askyesno

def popup():
    messagebox.showinfo(title="This is my popup", message="Hello world!")
    messagebox.showwarning(title="This is my popup", message="Hello world!")
    messagebox.showerror(title="This is my popup", message="Hello world!")
    response = messagebox.askyesno(title="This is my pop", message="Is everything ok?")
    if response == 1:
        txt = "You clicked yes"
    else:
        txt = "You clicked no"

    Label(root, text=txt).pack()

    response = messagebox.askquestion(title="This is my pop", message="Is everything ok?")
    if response == "yes":
        txt = "You clicked yes"
    else:
        txt = "You clicked no"

    Label(root, text=txt).pack()


ttk.Button(root, text="Popup", command=popup).pack()

# Loop for dynamic screen
root.mainloop()
