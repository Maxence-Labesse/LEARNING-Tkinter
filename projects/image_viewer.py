"""
image viewer
"""
from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image

# Global window settings
root = Tk()
root.title("Title")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# images to dispay
my_img1 = ImageTk.PhotoImage((Image.open("../images/image1.png")).resize((400, 400), Image.ANTIALIAS))
my_img2 = ImageTk.PhotoImage((Image.open("../images/image2.png")).resize((400, 400), Image.ANTIALIAS))
my_img3 = ImageTk.PhotoImage((Image.open("../images/image3.png")).resize((400, 400), Image.ANTIALIAS))
image_list = [my_img1, my_img2, my_img3]

current_image_nb = 1


def update_status(img_nb):
    """
    update status label according to image number
    """
    status = ttk.Label(root, text="Image " + str(img_nb) + " of " + str(len(image_list)), relief=SUNKEN, anchor=E)
    return status


def forward():
    global current_image_nb
    global my_label
    global button_forward
    global button_back
    global status

    # next image number
    current_image_nb += 1

    # disable forward button if last image
    if current_image_nb == len(image_list):
        forward_button_state = DISABLED
    else:
        forward_button_state = NORMAL

    # update widgets
    # display image
    my_label.grid_forget()
    my_label = Label(image=image_list[current_image_nb - 1])  # because list index starts at 0
    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid_forget()
    button_forward = ttk.Button(root, text=">>", command=forward, state=forward_button_state)
    button_forward.grid(row=1, column=2, pady=10)
    button_back.grid_forget()
    button_back = ttk.Button(root, text="<<", command=back)
    button_back.grid(row=1, column=0)
    status = update_status(current_image_nb)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back():
    global current_image_nb
    global my_label
    global button_forward
    global button_back
    global status

    # next image number
    current_image_nb -= 1

    # disable forward button if last image
    if current_image_nb == 1:
        back_button_state = DISABLED
    else:
        back_button_state = NORMAL

    # update widgets
    # display image
    my_label.grid_forget()
    my_label = Label(image=image_list[current_image_nb - 1])  # because list index starts at 0
    my_label.grid(row=0, column=0, columnspan=3)
    # button forward
    button_forward = ttk.Button(root, text=">>", command=forward)
    button_forward.grid(row=1, column=2, pady=10)
    # button back
    button_back = ttk.Button(root, text="<<", command=back, state=back_button_state)
    button_back.grid(row=1, column=0)
    # status bar
    status = update_status(current_image_nb)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


# display image
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)
# forward and back buttons
button_back = ttk.Button(root, text="<<", command=back, state=DISABLED)
button_back.grid(row=1, column=0)
button_forward = ttk.Button(root, text=">>", command=forward)
button_forward.grid(row=1, column=2, pady=10)
# exit button
button_exit = ttk.Button(root, text="Exit program", command=root.quit)
button_exit.grid(row=1, column=1)
# status bar
status = update_status(current_image_nb)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)

"""
def forward(image_number):
    global my_label
    global button_forward
    global button_back
    global status

    my_label.grid_forget()
    my_label = ttk.Label(image=image_list[image_number])
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
    my_label = ttk.Label(image=image_list[image_number])
    button_forward = ttk.Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = ttk.Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = ttk.Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = ttk.Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
"""

root.mainloop()
