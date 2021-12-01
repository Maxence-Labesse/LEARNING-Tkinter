"""
Create an app to count the number of clicks.
"""
import tkinter.ttk as ttk
from tkinter import *

# Global window settings
root = Tk()
root.title("Title")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# init click number
click_number = 0


def click():
    """
    when button in clicked, display and increment click number
    """
    global click_number
    # display click number
    my_label = Label(root, text="Click number " + str(click_number))
    my_label.pack()
    # increment
    click_number += 1


# Button to click
myButton = Button(root, text="Click Me!", command=click)
myButton.pack()

root.mainloop()

"""
Button Options:
- state=DISABLED : Disabled and grayed out button
- padx=50: Define button width
- pasy=50: Define button height
- command=myClick: associate an action
- fg=”blue”: font color
- bg=”#0000000”: bg color
"""
