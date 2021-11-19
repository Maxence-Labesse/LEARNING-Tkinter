from tkinter import *

# First widget: global window
root = Tk()
root.geometry("400x400")

# Creating a Label Widget
myLabel = Label(root, text="Hello world!")

# Shoving it onto the screen
myLabel.pack()

# Loop for dynamic screen
root.mainloop()
