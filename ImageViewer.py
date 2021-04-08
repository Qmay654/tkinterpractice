from tkinter import *
from PIL import ImageTk, Image

# Setting the stuff up
root = Tk()
root.title("Icons, Images, and Exits")
root.iconbitmap('C:/ImageViewer/hnet.com-image.ico')

# Defining the images
myimg1 = ImageTk.PhotoImage(Image.open('C:/ImageViewer/dice.png'))
myimg2 = ImageTk.PhotoImage(Image.open('C:/ImageViewer/image2.png'))
myimg3 = ImageTk.PhotoImage(Image.open('C:/ImageViewer/image3.png'))

# Making a list of the images
imagelist = [myimg1, myimg2, myimg3]

# Placing the image
label = Label(image=myimg1)
label.grid(row=0, column=0, columnspan=3)


# forward button function
def forward(image_number):
    global label
    global foward_button
    global back_button

    # getting rid of the image
    label.grid_forget()

    # redefining the image and the buttons
    label = Label(image=imagelist[image_number - 1])
    foward_button = Button(root, text='>>', command=lambda: forward(image_number + 1))
    back_button = Button(root, text='<<', command=lambda: back(image_number - 1))

    # if the button is the last image, disable the button
    if image_number == len(imagelist):
        foward_button = Button(root, text='>>', state=DISABLED)

    # place the buttoms back on the screen
    label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    foward_button.grid(row=1, column=2)
    return


# back button function 
def back(image_number):
    global label
    global foward_button
    global back_button

    # getting rid of the image
    label.grid_forget()

    # redefining the image and the buttons
    label = Label(image=imagelist[image_number - 1])
    foward_button = Button(root, text='>>', command=lambda: forward(image_number + 1))
    back_button = Button(root, text='<<', command=lambda: back(image_number - 1))

    # if the button is the last image, disable the button
    if image_number == 1:
        back_button = Button(root, text='<<', state=DISABLED)

    # place the buttoms back on the screen
    label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    foward_button.grid(row=1, column=2)

    return


# Making and placing the buttons
back_button = Button(root, text='<<', state=DISABLED)
button_quit = Button(root, text="Exit", command=root.quit)
foward_button = Button(root, text='>>', command=lambda: forward(2))

# placing the buttons for the first time
back_button.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
foward_button.grid(row=1, column=2)

root.mainloop()

