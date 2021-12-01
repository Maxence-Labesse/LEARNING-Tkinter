"""
Build calculator
"""
import tkinter.ttk as ttk
from tkinter import *

# Global window settings
root = Tk()
root.title("Title")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')


def number_click(number):
    """
    when you click on number, update screen (until you click on an operation)
    """
    # get numeric field current number
    current = numeric_field.get()
    # concat clicked number to current number
    numeric_field.delete(0, END)
    numeric_field.insert(0, str(current) + str(number))


def button_clear():
    """
    clear screen
    """
    numeric_field.delete(0, END)


def button_operation(operation):
    """
    Save fist number of operation (screen) and type of operation, until "=" is selected
    """
    global first_number
    global math
    first_number = float(numeric_field.get())
    math = operation
    numeric_field.delete(0, END)


def button_equal():
    """
    compute operation for first number in memory and second number on screen
    """
    second_number = numeric_field.get()
    numeric_field.delete(0, END)
    if math == "+":
        numeric_field.insert(0, first_number + float(second_number))
    elif math == "-":
        numeric_field.insert(0, first_number - float(second_number))
    elif math == "x":
        numeric_field.insert(0, first_number * float(second_number))
    elif math == "/":
        numeric_field.insert(0, first_number / float(second_number))


# Creating input field and buttons
numeric_field = ttk.Entry(root, width=35)

button0 = ttk.Button(root, text="0", padding="20 20 20 20", command=lambda: number_click(0))
button1 = ttk.Button(root, text="1", padding="20 20 20 20", command=lambda: number_click(1))
button2 = ttk.Button(root, text="2", padding="20 20 20 20", command=lambda: number_click(2))
button3 = ttk.Button(root, text="3", padding="20 20 20 20", command=lambda: number_click(3))
button4 = ttk.Button(root, text="4", padding="20 20 20 20", command=lambda: number_click(4))
button5 = ttk.Button(root, text="5", padding="20 20 20 20", command=lambda: number_click(5))
button6 = ttk.Button(root, text="6", padding="20 20 20 20", command=lambda: number_click(6))
button7 = ttk.Button(root, text="7", padding="20 20 20 20", command=lambda: number_click(7))
button8 = ttk.Button(root, text="8", padding="20 20 20 20", command=lambda: number_click(8))
button9 = ttk.Button(root, text="9", padding="20 20 20 20", command=lambda: number_click(9))
buttonClear = ttk.Button(root, text="Clear", padding="80 20 80 20", command=button_clear)
buttonAdd = ttk.Button(root, text="+", padding="20 20 20 20", command=lambda: button_operation("+"))
buttonSubtract = ttk.Button(root, text="-", padding="20 20 20 20", command=lambda: button_operation("-"))
buttonMultiply = ttk.Button(root, text="x", padding="20 20 20 20", command=lambda: button_operation("*"))
buttonDivide = ttk.Button(root, text="/", padding="20 20 20 20", command=lambda: button_operation("/"))
buttonEqual = ttk.Button(root, text="=", padding="80 20 80 20", command=button_equal)

# Positioning
numeric_field.grid(row=0, column=0, columnspan=3)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button0.grid(row=4, column=0)
buttonClear.grid(row=4, column=1, columnspan=2)
buttonAdd.grid(row=5, column=0)
buttonEqual.grid(row=5, column=1, columnspan=2)
buttonSubtract.grid(row=6, column=0)
buttonMultiply.grid(row=6, column=1)
buttonDivide.grid(row=6, column=2)

# Loop for dynamic screen
root.mainloop()
