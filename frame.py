import tkinter.ttk as ttk
from tkinter import *

# First widget: global window
root = Tk()
root.title("Frame")
root.iconbitmap("icon2.ico")
style = ttk.Style()
style.theme_use('clam')

frame = ttk.LabelFrame(root, text="This is my frame", padding='20 20 20 20')
frame.pack(padx=10, pady=10)

b = ttk.Button(frame, text="Don't click here")
b.pack()

# Loop for dynamic screen
root.mainloop()
