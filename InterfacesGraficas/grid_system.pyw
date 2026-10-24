from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hola mundo")
myLabel2 = Label(root, text="Mi nombre es Rafael")
myLabel3 = Label(root, text="The legend of Zelda")
# myLabel.pack()

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=2, column=4) # este se queda en la columna 2 a pesar de haber colocado 4, porque es relativo a
# los otros

root.mainloop()
