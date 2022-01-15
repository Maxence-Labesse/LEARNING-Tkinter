"""build calculator

"""
import tkinter.ttk as ttk
from tkinter import *


def select_number(number):
    """when number is selected on calculator, add it to the
    equation screen (until you click on an operation)

    Parameters
    ----------
    number: int
        select operation

    """
    # get current number on screen
    current = numeric_field.get()
    # concat clicked number to current number and display it
    numeric_field.delete(0, END)
    numeric_field.insert(0, str(current) + str(number))


def clear_screen():
    """clear screen

    """
    numeric_field.delete(0, END)


def add_operation(operation):
    """when operation is selected on calculator,
    save current number and operation

    Parameters
    ----------
    operation: str
        selected operation

    """
    global first_number
    global saved_operation
    first_number = float(numeric_field.get())
    saved_operation = operation
    numeric_field.delete(0, END)


def button_equal():
    """compute operation for first number in
    memory and second number on screen
    """
    second_number = numeric_field.get()
    numeric_field.delete(0, END)

    if saved_operation == "+":
        numeric_field.insert(0, first_number + float(second_number))
    elif saved_operation == "-":
        numeric_field.insert(0, first_number - float(second_number))
    elif saved_operation == "x":
        numeric_field.insert(0, first_number * float(second_number))
    elif saved_operation == "/":
        numeric_field.insert(0, first_number / float(second_number))


# Global window settings
root = Tk()
root.title("Title")
root.iconbitmap("../images/icon2.ico")
style = ttk.Style()
style.theme_use('clam')

# Creating input field and numbers/operations buttons
numeric_field = ttk.Entry(root, width=35)
button0 = ttk.Button(root, text="0", padding="20 20 20 20", command=lambda: select_number(0))
button1 = ttk.Button(root, text="1", padding="20 20 20 20", command=lambda: select_number(1))
button2 = ttk.Button(root, text="2", padding="20 20 20 20", command=lambda: select_number(2))
button3 = ttk.Button(root, text="3", padding="20 20 20 20", command=lambda: select_number(3))
button4 = ttk.Button(root, text="4", padding="20 20 20 20", command=lambda: select_number(4))
button5 = ttk.Button(root, text="5", padding="20 20 20 20", command=lambda: select_number(5))
button6 = ttk.Button(root, text="6", padding="20 20 20 20", command=lambda: select_number(6))
button7 = ttk.Button(root, text="7", padding="20 20 20 20", command=lambda: select_number(7))
button8 = ttk.Button(root, text="8", padding="20 20 20 20", command=lambda: select_number(8))
button9 = ttk.Button(root, text="9", padding="20 20 20 20", command=lambda: select_number(9))
buttonClear = ttk.Button(root, text="Clear", padding="80 20 80 20", command=clear_screen)
buttonAdd = ttk.Button(root, text="+", padding="20 20 20 20", command=lambda: add_operation("+"))
buttonSubtract = ttk.Button(root, text="-", padding="20 20 20 20", command=lambda: add_operation("-"))
buttonMultiply = ttk.Button(root, text="x", padding="20 20 20 20", command=lambda: add_operation("x"))
buttonDivide = ttk.Button(root, text="/", padding="20 20 20 20", command=lambda: add_operation("/"))
buttonEqual = ttk.Button(root, text="=", padding="80 20 80 20", command=button_equal)

# Positioning buttons
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
