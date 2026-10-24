from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="look! i clicked a button!!")
    myLabel.pack()

myButton = Button(root, text="Click me!", padx=50, pady=20, command=myClick, fg="#3af5ca", bg="#37976e")
myButton2 = Button(root, text="Hola", state=DISABLED)

myButton.pack()
myButton2.pack()    

root.mainloop()