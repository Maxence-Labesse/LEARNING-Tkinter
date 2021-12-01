"""
Create an app to count the number of clicks.
"""
import tkinter.ttk as ttk
from tkinter import *
from PIL import ImageTk, Image

# Global window settings
root = Tk()
root.title("Title")
root.iconbitmap("icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# init click number
click_number = 0

# Loop for dynamic screen
root.mainloop()
