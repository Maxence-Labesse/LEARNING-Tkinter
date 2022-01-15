"""select a single option in a dropdown menu
"""
import tkinter.ttk as ttk
from tkinter import *
from PIL import ImageTk, Image


def show_selected_option():
    """show dropdown selected option

    """
    Label(root, text=day_dropdown_var.get()).pack()


# Global window settings
root = Tk()
root.title("Dropdown menu")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# dropdown menu options and widget
options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
day_dropdown_var = StringVar()
day_dropdown_var.set("Monday")
# dropdown button
day_dropdown = OptionMenu(root, day_dropdown_var, *options)
day_dropdown.pack()

# button to show selection
show_button = Button(root, text="Show Selection", command=show_selected_option)
show_button.pack()

# Loop for dynamic screen
root.mainloop()
