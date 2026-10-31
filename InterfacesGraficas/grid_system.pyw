from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hola mundo")
myLabel2 = Label(root, text="Mi nombre es Rafael")
myLabel3 = Label(root, text="The legend of Zelda")
myLabel4 = Label(root, text="Metroid")
# myLabel.pack()
myLabel5 = Label(root, text="Final fantasy")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=2, column=4) # este se queda en la columna 2 a pesar de haber colocado 4, porque es relativo a
# los otros
myLabel4.grid(row=3, column=2, columnspan=2) # columnspan sirve para que la etiqueta ocupe más de una columna
myLabel5.grid(row=4, column=2, rowspan=2)

root.mainloop()
