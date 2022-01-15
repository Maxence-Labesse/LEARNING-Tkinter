"""image viewer

"""
from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image


def update_status(img_nb):
    """
    update status label according to image number
    """
    status = ttk.Label(root, text="Image " + str(img_nb) + " of " + str(len(image_list)),
                       relief=SUNKEN, anchor=E)
    return status


def change_image(direction):
    global current_image_id
    global displayed_image
    global forward_button
    global backward_button
    global status_bar

    # according to direction, select new image and buttons state
    if direction == 'next':
        current_image_id += 1

        if current_image_id == len(image_list):
            forward_button_state = DISABLED
        else:
            forward_button_state = NORMAL

        backward_button_state = NORMAL

    if direction == 'back':
        current_image_id -= 1

        if current_image_id == 1:
            backward_button_state = DISABLED
        else:
            backward_button_state = NORMAL

        forward_button_state = NORMAL

    # display new image
    displayed_image.grid_forget()
    displayed_image = Label(image=image_list[current_image_id - 1])  # because list index starts at 0
    displayed_image.grid(row=0, column=0, columnspan=3)

    # update forward and backward buttons
    forward_button.grid_forget()
    forward_button = ttk.Button(root, text=">>", command=lambda: change_image('next'),
                                state=forward_button_state)
    forward_button.grid(row=1, column=2, pady=10)
    backward_button.grid_forget()
    backward_button = ttk.Button(root, text="<<", command=lambda: change_image('back'),
                                 state=backward_button_state)
    backward_button.grid(row=1, column=0)

    # update status bar
    status_bar = update_status(current_image_id)
    status_bar.grid(row=2, column=0, columnspan=3, sticky=W + E)


# Global window settings
root = Tk()
root.title("Title")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# images
my_img1 = ImageTk.PhotoImage((Image.open("../images/image1.png")).resize((400, 400), Image.ANTIALIAS))
my_img2 = ImageTk.PhotoImage((Image.open("../images/image2.png")).resize((400, 400), Image.ANTIALIAS))
my_img3 = ImageTk.PhotoImage((Image.open("../images/image3.png")).resize((400, 400), Image.ANTIALIAS))
image_list = [my_img1, my_img2, my_img3]

# init image id
current_image_id = 1

# display image
displayed_image = Label(image=my_img1)
displayed_image.grid(row=0, column=0, columnspan=3)

# forward and back buttons
backward_button = ttk.Button(root, text="<<", command=lambda: change_image('back'), state=DISABLED)
backward_button.grid(row=1, column=0)
forward_button = ttk.Button(root, text=">>", command=lambda: change_image('next'))
forward_button.grid(row=1, column=2, pady=10)

# exit button
exit_button = ttk.Button(root, text="Exit program", command=root.quit)
exit_button.grid(row=1, column=1)

# status bar
status_bar = update_status(current_image_id)
status_bar.grid(row=2, column=0, columnspan=3, sticky=W + E)

root.mainloop()
