from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Aprender a codear en Codemy.com")
# root.iconbitmap('C:/Users/User/Desktop/ProgramacionRafael/Imagenes/Iconos/juegos/Samus.jpg') # Aparentemente
# esto funciona con archivos .ico

my_img = ImageTk.PhotoImage(Image.open("C:/Users/User/Desktop/ProgramacionRafael/Imagenes/dockerizacionJava.png"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text='Exit program', command=root.quit)
button_quit.pack()

root.mainloop()

