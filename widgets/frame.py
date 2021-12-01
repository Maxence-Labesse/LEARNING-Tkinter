"""
isolate a part of a window as a frame
"""
import tkinter.ttk as ttk
from tkinter import *

# Global window settings
root = Tk()
root.title("Title")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# frame
frame = ttk.LabelFrame(root, text="This is my frame", padding='20 20 20 20')
frame.pack(padx=10, pady=10)

# frame button
b = ttk.Button(frame, text="Don't click here")
b.pack()

# Loop for dynamic screen
root.mainloop()
