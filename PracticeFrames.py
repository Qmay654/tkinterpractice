from tkinter import *
from PIL import ImageTk, Image

# Setting up the window color and size
root = Tk()
root.configure(bg="grey")
root.geometry("1500x800")

frame = LabelFrame(root, text='This is a frame', padx=50, pady=200)
frame.grid(padx=20, pady=10, column=0, row=0)
frame2 = LabelFrame(root, text='This is a frame', padx=600, pady=125)
frame2.grid(padx=20, pady=10, column=1, row=1)

text1 = Label(frame, text = 'Hellow')
text1.pack()
text2 = Label(frame2, text = 'goodbye')
text2.pack()


root.mainloop()