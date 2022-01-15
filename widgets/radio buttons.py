"""choose a pizza with radiobutton

"""
import tkinter.ttk as ttk
from tkinter import *


def show_selected_pizza(value):
    """show selected pizza

    """
    myLabel = Label(root, text=value)
    myLabel.pack()


# Global window settings
root = Tk()
root.title("Title")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# radiobutton options and related modes
d_pizza_codes = [
    ("Pepperoni", "Pep"),
    ("Cheese", "Che"),
    ("Muschroom", "Mus"),
    ("Onion", "Oni")
]
# radiobutton var
pizza_var = StringVar()
pizza_var.set("Pepperoni")
# radiobutton
for pizza, code in d_pizza_codes:
    Radiobutton(root, text=pizza, variable=pizza_var, value=code).pack(anchor=W)

# Button to show pizza
show_pizza_button = ttk.Button(root, text="show selection", command=lambda: show_selected_pizza(pizza_var.get()))
show_pizza_button.pack()

# Loop for dynamic screen
root.mainloop()
