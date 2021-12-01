"""
display image
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

# display image
my_img = ImageTk.PhotoImage(Image.open("../images/image1.png"))
my_label = Label(image=my_img)
my_label.pack()

# button to quit app
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
