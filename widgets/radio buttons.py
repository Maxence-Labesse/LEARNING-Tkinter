"""
select one pizza option with radiobutton
"""
import tkinter.ttk as ttk
from tkinter import *

# Global window settings
root = Tk()
root.title("Title")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')


def show(value):
    """
    when button is pressed, show selection
    """
    myLabel = ttk.Label(root, text=value)
    myLabel.pack()


# radiobutton options and related modes
TOPPINGS = [
    ("Pepperoni", "Pep"),
    ("Cheese", "Che"),
    ("Muschroom", "Mus"),
    ("Onion", "Oni")
]
# radiobutton var
pizza = StringVar()
pizza.set("Pepperoni")
# radiobutton
for text, mode in TOPPINGS:
    ttk.Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

# Button to show pizza
myButton = ttk.Button(root, text="show selection", command=lambda: show(pizza.get()))
myButton.pack()

# Loop for dynamic screen
root.mainloop()
