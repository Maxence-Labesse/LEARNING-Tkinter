"""Create an app that displays a graph
"""
import tkinter.ttk as ttk
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

# generate random normal sample
random_data = np.random.normal(200000, 25000, 5000)


def plot_histogram(data):
    """when "Graph it!" button is pressed, displays histogram

    """
    plt.hist(data, 200)
    plt.show()


# Global window settings
root = Tk()
root.title("Plot graph")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# Button to display histogram
plot_histogram_button = Button(root, text="Plot graph!", command=lambda: plot_histogram(random_data))
plot_histogram_button.pack()

# Loop for dynamic screen
root.mainloop()
