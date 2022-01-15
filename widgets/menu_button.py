"""Choose sauces with menu button
"""
from tkinter import *


def show_selected_sauce():
    """show selected sauces

    """
    global selected_sauce_label

    l_sauces = []

    # check which sauces have been selected
    if mayo_sauce.get() == 1:
        l_sauces.append("mayo")
    if ketchup.get() == 1:
        l_sauces.append("ketchup")

    # prepare text to display
    if len(l_sauces) == 1:
        txt = l_sauces[0]
    elif len(l_sauces) > 1:
        txt = l_sauces[0] + " & " + l_sauces[1]
    else:
        txt = "no sauce selected"

    selected_sauce_label.destroy()
    selected_sauce_label = Label(window, text="Sauces: " + txt)
    selected_sauce_label.grid(row=2, columnspan=2, padx=10, )


# global window settings
window = Tk()
window.title("Menu_button widget")
window.iconbitmap("../images/icon2.ico")
window.geometry('200x150')

# init sauce label
selected_sauce_label = Label(window, text="Sauces: Any")

# menu button
my_menu_button = Menubutton(window, text='Choose sauces', activebackground='blue')
my_menu_button.grid(row=0, columnspan=2, padx=10, pady=10, ipadx=44)
# create menu
my_menu_button.menu = Menu(my_menu_button, tearoff=0)
my_menu_button["menu"] = my_menu_button.menu
# create options
mayo_sauce = IntVar()
ketchup = IntVar()
my_menu_button.menu.add_checkbutton(label='mayo', variable=mayo_sauce)
my_menu_button.menu.add_checkbutton(label='ketchup', variable=ketchup)

# button that show selection(s)
show_sauces_button = Button(window, text="Show Selection", command=show_selected_sauce)
show_sauces_button.grid(row=1, columnspan=2, padx=10, ipadx=40)

window.mainloop()
