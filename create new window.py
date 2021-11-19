import tkinter.ttk as ttk
from tkinter import *
from PIL import ImageTk, Image

# First widget: global window
root = Tk()
root.title("Title")
root.iconbitmap("icon2.ico")
style = ttk.Style()
style.theme_use('clam')


def open():
    global my_img # Or it doesn't work
    top = Toplevel()
    top.title("Title Top")
    top.iconbitmap("icon2.ico")
    ttk.Label(top, text="Hello world").pack()
    my_img = ImageTk.PhotoImage((Image.open("images/image1.png")).resize((400, 400), Image.ANTIALIAS))
    my_label = Label(top, image=my_img).pack()
    btn2 = ttk.Button(top, text="Close window", command=top.destroy).pack()

btn = ttk.Button(root, text="Open Second Window", command=open)
btn.pack()

# Loop for dynamic screen
root.mainloop()
