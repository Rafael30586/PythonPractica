from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Aprender a codear en Codemy.com")

def open():    
    top = Toplevel()
    lbl = Label(top, text="Hola mundo").pack()
    btn2 = Button(top, text="close window", command=top.destroy)
    btn2.pack()


btn = Button(root, text="Abrir segunda ventana", command=open).pack()



root.mainloop()