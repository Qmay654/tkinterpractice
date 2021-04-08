from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Icons, Images, and Exits")
root.iconbitmap('C:/ImageViewer/hnet.com-image.ico')

myimg= ImageTk.PhotoImage(Image.open('C:/ImageViewer/dice.png'))
label = Label(image=myimg)
label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
