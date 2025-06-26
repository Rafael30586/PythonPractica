import os
import shutil

ruta="C:/Users/User/Downloads"

tipos=["Imágenes","PDFs","Videos","Documentos de texto"]

for carpeta in tipos:
    ruta_carpeta = os.path.join(ruta, carpeta)
    #print(type(ruta_carpeta)) muestra que es de tipo string

    if not os.path.exists(ruta_carpeta): # Comprueba si la carpeta ya existe
        os.makedirs(ruta_carpeta) # Si la carpeta no existía, la crea

for archivo in os.listdir(ruta):
    if archivo.endswith(".jpg") or archivo.endswith(".png"):
        shutil.move(os.path.join(ruta,archivo), os.path.join(ruta,"Imágenes",archivo))
    elif archivo.endswith(".pdf"):
        shutil.move(os.path.join(ruta,archivo), os.path.join(ruta,"PDFs",archivo))
    elif archivo.endswith(".docx") or archivo.endswith(".txt"):
        shutil.move(os.path.join(ruta,archivo), os.path.join(ruta,"Documentos de texto",archivo))
    elif archivo.endswith(".mp4"):
        shutil.move(os.path.join(ruta,archivo), os.path.join(ruta,"Videos",archivo))
    