from tkinter import *
from tkinter import Button

root = Tk()
root.title("Icons, Images, and Exits")
root.iconbitmap('C:/Users/QuentynMay/Downloads/hnet.com-image.ico')

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
