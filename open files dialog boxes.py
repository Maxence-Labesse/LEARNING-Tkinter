import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

# First widget: global window
root = Tk()
root.title("Title")
root.iconbitmap("icon2.ico")
style = ttk.Style()
style.theme_use('clam')

root.filename = filedialog.askopenfilename(initialdir="C:/Users/maxen/PycharmProjects/Tkinter/images",
                                           title="Select a file",
                                           filetypes=(("png files", "*.png"), ("ico files", "*.ico")))


# ("all files", "*.*")
# Loop for dynamic screen
def open():
    global my_img
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_label = Label(image=my_img)
    my_label.pack()


my_btn = ttk.Button(root, text="Open file", command=open).pack()

root.mainloop()
