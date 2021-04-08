from tkinter import *
from PIL import ImageTk, Image

# Setting up the window color and size
root = Tk()
root.configure(bg="grey")
root.geometry("1500x800")

# Make and place the frame
frame = LabelFrame(root, text='This is a frame', padx=50, pady=200)
frame.grid(padx=20, pady=10, column=0, row=0)

# Making and placing the inside frame
frame2 = LabelFrame(frame, padx=20, pady=20)
frame2.grid(column=1, row=1)

# Making the two buttons
button = Button(frame, text='hello I am a button', bg="Red")
button.grid(column=0, row=0)
button2 = Button(frame2, text='hello I am another button', bg="Red")
button2.pack()

root.mainloop()
