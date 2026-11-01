from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Aprender a codear en Codemy.com")

r = IntVar() # Esta es una variable especial de tkinter que acepta números enteros
ejemplo = StringVar() # Variable especial de tkinter que acepta strings
r.set(2)

pizza = StringVar()
pizza.set("Pepperoni")


TOPPINGS = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion")
]

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack() 

# Radiobutton(root, text="option 1" , variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="option 2" , variable=r, value=2, command=lambda: clicked(r.get())).pack()

# myLabel = Label(root, text=pizza.get())
# myLabel.pack() 

myButton = Button(root, text="click me!", command=lambda: clicked(pizza.get()))
myButton.pack()


root.mainloop()