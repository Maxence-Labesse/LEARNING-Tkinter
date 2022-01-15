"""Resize window according to sliders values

"""
import tkinter.ttk as ttk
from tkinter import *


def resize_window():
    """when button is pressed, resize window according
    to sliders values

    """
    root.geometry(str(horizontal_slider.get()) + "x" + str(vertical_slider.get()))


# Global window settings
root = Tk()
root.title("Title")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# Vertical & horizontal sliders
vertical_slider = Scale(root, from_=200, to=500)
vertical_slider.pack()
horizontal_slider = Scale(root, from_=200, to=500, orient=HORIZONTAL)
horizontal_slider.pack()

resize_window_button = Button(root, text="Resize window", command=resize_window).pack()

# Loop for dynamic screen
root.mainloop()
