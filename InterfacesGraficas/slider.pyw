from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Aprender a codear en Codemy.com")
root.geometry("400x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack()


def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(2*(horizontal.get()))+"x"+str(2*(vertical.get())))

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()


my_btn = Button(root, text="Clickeame", command=slide).pack()

root.mainloop()