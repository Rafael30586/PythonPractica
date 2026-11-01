from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Aprender a codear en Codemy.com")

frame = LabelFrame(root, text="This is my frame", padx=20, pady=20) # padx y pady son el padding interno del frame
frame.pack(padx=50, pady=50) # este padding separa al frame de la raíz

b = Button(frame, text="don't click here",padx=10, pady=10) # padx y pady son el padding interno del botón
# b.pack()
b2 = Button(frame, text="or here")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()
