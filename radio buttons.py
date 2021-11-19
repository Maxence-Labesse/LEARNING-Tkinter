import tkinter.ttk as ttk
from tkinter import *

# First widget: global window
root = Tk()
root.title("Radio buttons")
root.iconbitmap("icon2.ico")
style = ttk.Style()
style.theme_use('clam')


######## 1 ########
# r = IntVar()
# r.set("2")
# ttk.Radiobutton(root, text="Option1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# ttk.Radiobutton(root, text="Option2", variable=r, value=2, command=lambda: clicked(r.get())).pack()


######## 2 ########
def clicked(value):
    myLabel = ttk.Label(root, text=value)
    myLabel.pack()


TOPPINGS = [
    ("Pepperoni", "Pep"),
    ("Cheese", "Che"),
    ("Muschroom", "Mus"),
    ("Onion", "Oni")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in TOPPINGS:
    ttk.Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

""" Other way to display the radio button selected"""
myButton = ttk.Button(root, text="Click me!", command=lambda: clicked(pizza.get()))
myButton.pack()

# Loop for dynamic screen
root.mainloop()
