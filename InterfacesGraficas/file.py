from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()
root.title("Aprender a codear en Codemy.com")


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/User/Desktop/ProgramacionRafael/Imagenes/Juegos", title="Seleccioná un archivo", filetypes=(("png files", "*.png"),("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="Open file", command=open).pack()

root.mainloop()