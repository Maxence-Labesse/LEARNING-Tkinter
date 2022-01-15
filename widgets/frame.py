"""isolate a part of a window as a frame
"""
import tkinter.ttk as ttk
from tkinter import *

# Global window settings
root = Tk()
root.title("Frame")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# frame
my_frame = ttk.LabelFrame(root, text="This is my frame", padding='20 20 20 20')
my_frame.pack(padx=10, pady=10)

# frame button
frame_button = ttk.Button(my_frame, text="This button belongs to the frame")
frame_button.pack()

# Loop for dynamic screen
root.mainloop()
