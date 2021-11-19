from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Look! I clicked!")
    myLabel.pack()


myButton = Button(root, text="Click Me!", command=myClick)
"""
Options:
- state=DISABLED : Disabled and grayed out button
- padx=50: Define button width
- pasy=50: Define button height
- command=myClick: associate an action
- fg=”blue”: font color
- bg=”#0000000”: bg color


"""
myButton.pack()

root.mainloop()
