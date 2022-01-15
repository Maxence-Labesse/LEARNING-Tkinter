"""display an image
"""
import tkinter.ttk as ttk
from tkinter import *
from PIL import ImageTk, Image

# Global window settings
root = Tk()
root.title("Display image")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# display image
my_img = ImageTk.PhotoImage(Image.open("../images/image1.png"))
Label(image=my_img).pack()

# button to quit app
exit_button = Button(root, text="Exit Program", command=root.quit)
exit_button.pack()

root.mainloop()
