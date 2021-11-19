from tkinter import *
import tkinter.ttk as ttk

# First widget: global window
root = Tk()
root.title("Simple calculator")

style = ttk.Style()
style.theme_use('clam')

# Creating input field and buttons
numericField = ttk.Entry(root, width=35)


def button_click(number):
    # numericField.delete(0, END)
    current = numericField.get()
    numericField.delete(0, END)
    numericField.insert(0, str(current) + str(number))


def button_clear():
    numericField.delete(0, END)


def button_add():
    first_number = numericField.get()
    global f_number
    global math
    math = "+"
    f_number = float(first_number)
    numericField.delete(0, END)


def button_subtract():
    first_number = numericField.get()
    global f_number
    global math
    math = "-"
    f_number = float(first_number)
    numericField.delete(0, END)


def button_multiply():
    first_number = numericField.get()
    global f_number
    global math
    math = "x"
    f_number = float(first_number)
    numericField.delete(0, END)


def button_divide():
    first_number = numericField.get()
    global f_number
    global math
    math = "/"
    f_number = float(first_number)
    numericField.delete(0, END)


def button_equal():
    second_number = numericField.get()
    numericField.delete(0, END)
    if math == "+":
        numericField.insert(0, f_number + float(second_number))
    elif math == "-":
        numericField.insert(0, f_number - float(second_number))
    elif math == "x":
        numericField.insert(0, f_number * float(second_number))
    elif math =="/":
        numericField.insert(0, f_number / float(second_number))


button0 = ttk.Button(root, text="0", padding="20 20 20 20", command=lambda: button_click(0))
button1 = ttk.Button(root, text="1", padding="20 20 20 20", command=lambda: button_click(1))
button2 = ttk.Button(root, text="2", padding="20 20 20 20", command=lambda: button_click(2))
button3 = ttk.Button(root, text="3", padding="20 20 20 20", command=lambda: button_click(3))
button4 = ttk.Button(root, text="4", padding="20 20 20 20", command=lambda: button_click(4))
button5 = ttk.Button(root, text="5", padding="20 20 20 20", command=lambda: button_click(5))
button6 = ttk.Button(root, text="6", padding="20 20 20 20", command=lambda: button_click(6))
button7 = ttk.Button(root, text="7", padding="20 20 20 20", command=lambda: button_click(7))
button8 = ttk.Button(root, text="8", padding="20 20 20 20", command=lambda: button_click(8))
button9 = ttk.Button(root, text="9", padding="20 20 20 20", command=lambda: button_click(9))
buttonClear = ttk.Button(root, text="Clear", padding="80 20 80 20", command=button_clear)
buttonAdd = ttk.Button(root, text="+", padding="20 20 20 20", command=button_add)
buttonSubtract = ttk.Button(root, text="-", padding="20 20 20 20", command=button_subtract)
buttonMultiply = ttk.Button(root, text="x", padding="20 20 20 20", command=button_multiply)
buttonDivide = ttk.Button(root, text="/", padding="20 20 20 20", command=button_divide)
buttonEqual = ttk.Button(root, text="=", padding="80 20 80 20", command=button_equal)

# Positioning
numericField.grid(row=0, column=0, columnspan=3)
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
