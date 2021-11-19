from tkinter import *

# First widget: global window
root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text="Hello world!")
myLabel2 = Label(root, text="My name is Max")
myLabel3 = Label(root, text="         ")

# Position Labels on the screen
myLabel1.grid(row=0, column=0)
myLabel3.grid(row=1, column=5)
myLabel2.grid(row=1, column=1)

"""
Other way (since Python is OO)
myLabel1 = Label(root, text="Hello world!").grid(row=0, column=0)
But it's more confusing in a large program
"""

# Loop for dynamic screen
root.mainloop()
