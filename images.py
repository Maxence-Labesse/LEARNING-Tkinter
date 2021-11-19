from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Icon, images and exit button")
root.iconbitmap('C:/Users/maxen/PycharmProjects/Tkinter/icon2.ico')

my_img = ImageTk.PhotoImage(Image.open("images/image1.png"))
my_label = Label(image = my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
