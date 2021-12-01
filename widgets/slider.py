"""
Resize window according to sliders values
"""
import tkinter.ttk as ttk
from tkinter import *

# Global window settings
root = Tk()
root.title("Title")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')


def slide():
    """
    when button is pressed, resize window according to sliders and print horizontal slider value
    """
    ttk.Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


# Vertical & horizontal sliders
vertical = Scale(root, from_=200, to=500)
vertical.pack()
horizontal = Scale(root, from_=200, to=500, orient=HORIZONTAL)
horizontal.pack()

my_btn = Button(root, text="Resize window", command=slide).pack()

# Loop for dynamic screen
root.mainloop()
