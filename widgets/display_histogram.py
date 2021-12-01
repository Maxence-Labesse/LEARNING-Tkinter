"""
Create an app that displays histogram for data
"""
import tkinter.ttk as ttk
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(200000, 25000, 5000)

# Global window settings
root = Tk()
root.title("Title")
root.iconbitmap("icon2.ico")
style = ttk.Style()
style.theme_use('clam')


def graph():
    """
    when "Graph it!" button is pressed, displays histogram
    """
    plt.hist(data, 200)
    plt.show()


# Button to display graph
my_button = Button(root, text="Graph it!", command=graph)
my_button.pack()

# Loop for dynamic screen
root.mainloop()
