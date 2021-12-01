"""
Create a window with menu button that allows to select multiple options
"""
from tkinter import *

# global window settings
window = Tk()
window.title("condiments")
window.iconbitmap("../images/icon2.ico")
window.geometry('200x150')

# init label
my_label = Label(window, text="Sauces: Any")


def show():
    global my_label

    l_sauces = []
    if mayo_sauce.get() == 1: l_sauces.append("mayo")
    if ketchup.get() == 1: l_sauces.append("ketchup")
    if len(l_sauces) == 1:
        txt = l_sauces[0]
    elif len(l_sauces) > 1:
        txt = l_sauces[0] + " & " + l_sauces[1]
    else:
        txt = "any"
    my_label.destroy()
    my_label = Label(window, text="Sauces: " + txt)
    my_label.grid(row=2, columnspan=2, padx=10, )


# menu button
menub = Menubutton(window, text='Choose sauces', activebackground='blue')
menub.grid(row=0, columnspan=2, padx=10, pady=10, ipadx=44)
# create options
menub.menu = Menu(menub, tearoff=0)
menub["menu"] = menub.menu
mayo_sauce = IntVar()
ketchup = IntVar()
menub.menu.add_checkbutton(label='mayo', variable=mayo_sauce)
menub.menu.add_checkbutton(label='ketchup', variable=ketchup)

# button that show selection(s)
myButton = Button(window, text="Show Selection", command=show)
myButton.grid(row=1, columnspan=2, padx=10, ipadx=40)

window.mainloop()
