from tkinter import *

root = Tk()

e = Entry(root)
"""
Options:
- width=50
- bg="blue": background color
- fg="white": foreground color (font)
- borderWidth=50
"""
e.pack()

def myClick():
    hello = "hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Enter your name", command=myClick)
myButton.pack()

root.mainloop()
