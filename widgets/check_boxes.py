"""Create an app to notify whether a checkbox is checked

"""
import tkinter.ttk as ttk
from tkinter import *


def show_checkbox_state():
    """when "Show state" button is pressed, display last
    checkbox state

    """
    global displayed_image
    # delete last label
    checkbox_state_label.destroy()
    # displays checkbox state
    txt = state_var.get()
    checkbox_state_label = Label(root, text=txt)
    checkbox_state_label.pack()


# Global window settings
root = Tk()
root.title("Checkbox widget")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# initiate my_label
displayed_image = Label(text="")
# initiate checkbox var
state_var = StringVar()
state_var.set("Off")

# checkbox
my_checkbox = Checkbutton(root, text="Check this box", variable=state_var, onvalue="On", offvalue="Off")
my_checkbox.pack()

# button to display checkbox state
show_state_button = Button(root, text="Show state", command=show_checkbox_state)
show_state_button.pack()

# Loop for dynamic screen
root.mainloop()
