from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.iconbitmap("icon2.ico")
style = ttk.Style()
print(style.theme_names())
style.theme_use('clam')

my_img1 = ImageTk.PhotoImage((Image.open("images/image1.png")).resize((400, 400), Image.ANTIALIAS))
my_img2 = ImageTk.PhotoImage((Image.open("images/image2.png")).resize((400, 400), Image.ANTIALIAS))
my_img3 = ImageTk.PhotoImage((Image.open("images/image3.png")).resize((400, 400), Image.ANTIALIAS))
image_list = [my_img1, my_img2, my_img3]

status = ttk.Label(root, text="Image 1 of " + str(len(image_list)), relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back
    global status

    my_label.grid_forget()
    my_label = ttk.Label(image=image_list[image_number - 1])
    button_forward = ttk.Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = ttk.Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == len(image_list):
        button_forward = ttk.Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = ttk.Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(image_number):
    global my_label
    global button_forward
    global button_back
    global status

    my_label.grid_forget()
    my_label = ttk.Label(image=image_list[image_number - 1])
    button_forward = ttk.Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = ttk.Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = ttk.Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = ttk.Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = ttk.Button(root, text="<<", command=lambda: back, state=DISABLED)
button_exit = ttk.Button(root, text="Exit program", command=root.quit)
button_forward = ttk.Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)

root.mainloop()
