"""
Press a button to open a new window that displays a new window
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


def open():
    """
    when "Open Second Window" button is pressed, an image is displayed in a new window
    """
    global my_img  # Or it doesn't work

    # Opening a new window
    top = Toplevel()
    top.title("Title Top")
    top.iconbitmap("icon2.ico")

    # Label
    ttk.Label(top, text="Hello world").pack()
    # Image display
    my_img = ImageTk.PhotoImage((Image.open("../images/image1.png")).resize((400, 400), Image.ANTIALIAS))
    Label(top, image=my_img).pack()
    # button to close the new window
    ttk.Button(top, text="Close window", command=top.destroy).pack()


# button to open the new window
btn = ttk.Button(root, text="Open Second Window", command=open)
btn.pack()

# Loop for dynamic screen
root.mainloop()
