from tkinter import *

root = Tk()

e = Entry(root, width=60, bg="#540e6f", fg="#d5c365", borderwidth=5)
e.pack()
e.insert(0,"Ingresá tu nombre: ")

def myClick():
    saludo = "Hola "+ e.get()
    myLabel = Label(root, text=saludo)
    myLabel.pack()

myButton = Button(root, text="Ingresá tu nombre", padx=50, pady=20, command=myClick, fg="#3af5ca", bg="#37976e")
myButton2 = Button(root, text="Hola", state=DISABLED)

myButton.pack()
myButton2.pack()    

root.mainloop()