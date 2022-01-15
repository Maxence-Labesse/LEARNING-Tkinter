"""Create an app to count the number of clicks.

Button Options:
- state=DISABLED : Disabled and grayed out button
- padx=50: Define button width
- pasy=50: Define button height
- command=myClick: associate an action
- fg=”blue”: font color
- bg=”#0000000”: bg color

"""
import tkinter.ttk as ttk
from tkinter import *


def increment_click():
    """
    when "Click Me!" button is pressed, display and increment click
    number

    """
    global click_count
    # display click number
    my_label = Label(root, text="Click number " + str(click_count))
    my_label.pack()
    # increment
    click_count += 1


# Global window settings
root = Tk()
root.title("Button widget")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# init click number
click_count = 0

# Button to click
click_button = Button(root, text="Click Me!", command=increment_click)
click_button.pack()

root.mainloop()
