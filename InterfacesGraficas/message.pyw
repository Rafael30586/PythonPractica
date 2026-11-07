from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Aprender a codear en Codemy.com")

# showinfo, shwwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    messagebox.showinfo("Este es mi popup", "Hola mundo")

def popup2():
    messagebox.showwarning("ESte es mi popup", "Cuidado")

def popup3():
    respuesta = messagebox.askyesno("Este es mi popup", "Sí o no") # respuesta es true o false
    print(respuesta) # según la opción que elijamos
    if respuesta == True:
        Label(root, text="clickeaste yes").pack()
    else:
        Label(root, text="clockeaste no").pack()

def popup4():
    respuesta = messagebox.askquestion("Este es mi popup", "Sí o no") # respuesta es yes o no
    # dependiendo de lo que se elija
    if respuesta == "yes":
        Label(root, text="clickeaste yes").pack()
    elif respuesta == "no":
        Label(root, text="clickeaste no").pack()



Button(root, text="popup", command=popup).pack()
Button(root, text="popup2", command=popup2).pack()
Button(root, text="popup3", command=popup3).pack()
Button(root, text="popup4", command=popup4).pack()


root.mainloop()