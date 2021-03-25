from tkinter import *
from PIL import ImageTk,Image

root = Tk()

e = Entry(root, width=50, bg='#814234', fg='#f19234', borderwidth=7)
e.pack()
e.insert(0,"Your name: ")


def myclick():
    mlabel = Label(root, text=e.get())  # You can do any python-like text things in these text areas
    mlabel.pack()


button = Button(root, text='Enter your name', padx=50, pady=10, command=myclick, fg='blue',
                bg='pink')  # (where the button is going, text in the button, size of button, what to do after click, word color, background color
button.pack()
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
