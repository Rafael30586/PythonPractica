import tkinter 

raiz = tkinter.Tk(screenName="ventana")
raiz.title("Ventana")
raiz.resizable(1,1)
# raiz.geometry("300x400") La raíz se adaptará al tamaño del contenedor interno (mi_frame en este caso)
raiz.config(bg="#0e74b3")

mi_frame = tkinter.Frame()

mi_frame.pack(side="left",anchor="n") # Los parámetros side y anchor sirven para definir como va a quedar el frame en caso de agrandar el tamaño de la raíz

mi_frame.config(bg="#80e352")

mi_frame.config(width="300", height="400")

raiz.mainloop()

