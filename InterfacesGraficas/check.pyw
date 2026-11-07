from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Aprender a codear en Codemy.com")
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="check this box", variable=var, onvalue="sí", offvalue="no")
c.deselect() # Esto se usa por un tema de un bug 
c.pack()

myButton = Button(root, text="Mostrar selección", command=show).pack()

root.mainloop()