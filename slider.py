import tkinter.ttk as ttk
from tkinter import *
from PIL import ImageTk, Image

# First widget: global window
root = Tk()
root.title("Title")
root.iconbitmap("icon2.ico")
root.geometry("400x400")
style = ttk.Style()
style.theme_use('clam')

vertical = Scale(root, from_=200, to=500)
vertical.pack()


def slide():
    my_label = ttk.Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


horizontal = Scale(root, from_=200, to=500, orient=HORIZONTAL
                   # command=slide
                   )
horizontal.pack()

""" # Button that display value of the slide 
def slide():
    my_label = ttk.Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x400")
"""
my_btn = Button(root, text="Click Me!", command=slide).pack()

# Loop for dynamic screen
root.mainloop()
