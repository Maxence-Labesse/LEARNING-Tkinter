"""open files dialog box to choose an image to display

"""
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


def show_image():
    """show image

    """
    global my_img
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_label = Label(image=my_img)
    my_label.pack()


# Global window settings
root = Tk()
root.title("Title")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# select image
# define initial folder and files extensions
root.filename = filedialog.askopenfilename(initialdir="C:/",
                                           title="Select an image",
                                           filetypes=(("png files", "*.png"), ("ico files", "*.ico")))
# button so select file
show_image_button = ttk.Button(root, text="select image", command=show_image)
show_image_button.pack()

# Loop for dynamic screen
root.mainloop()
