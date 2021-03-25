from tkinter import *

root = Tk()


def myclick():
    mlabel = Label(root, text="Why'd you click this?", fg='#9f36f1',bg='orange')
    mlabel.pack()

button = Button(root, text='Click this button', padx=50, pady=10, command = myclick, fg='blue', bg='pink') #(where the button is going, text in the button, size of button, what to do after click, word color, background color
button.pack()

root.mainloop()
