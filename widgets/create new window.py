"""Open a window from main one

"""
import tkinter.ttk as ttk
from tkinter import *
from PIL import ImageTk, Image


def open_new_window():
    """when "Open Second Window" button is pressed, an image is
    displayed in a new window

    """
    global my_img  # Or it doesn't work

    # Opening a new window
    new_window = Toplevel()
    new_window.title("New window")
    new_window.iconbitmap("../images/icon2.ico")

    # "New window" label
    Label(new_window, text="New window").pack()
    # image
    my_img = ImageTk.PhotoImage((Image.open("../images/image1.png")).resize((400, 400), Image.ANTIALIAS))
    Label(new_window, image=my_img).pack()
    # button to close the new window
    ttk.Button(new_window, text="Close window", command=new_window.destroy).pack()


# Global window settings
root = Tk()
root.title("Open window widget")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# button to open the new window
open_window_button = ttk.Button(root, text="Open Second Window", command=open_new_window)
open_window_button.pack()

# Loop for dynamic screen
root.mainloop()
