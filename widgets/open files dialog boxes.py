"""
Choose an image to display
"""
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

# Global window settings
root = Tk()
root.title("Title")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# choose path for files to select and specify available types of files ("all files", "*.*")
root.filename = filedialog.askopenfilename(initialdir="C:/Users/maxen/PycharmProjects/Tkinter/images",
                                           title="Select a file",
                                           filetypes=(("png files", "*.png"), ("ico files", "*.ico")))


def open():
    """
    when button is pressed, open selected file
    """
    global my_img
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_label = Label(image=my_img)
    my_label.pack()


# button so select file
my_btn = ttk.Button(root, text="Open file", command=open).pack()

# Loop for dynamic screen
root.mainloop()
