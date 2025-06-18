import datetime

personajes = ["Mario", "Link", "Samus", "Cloud"]
personajes.sort()
print(personajes)  # La lisa es ordenada alfabéticamente
print(personajes[2])  # Accediendo a un elemento de la lista según su index

masterChief = "Master Chief mató tres covenant"
# Este método transforma un String en una lista. Como argumento le pasamos el separador que queramos (en este caso el separador es el espacio vacío)
x = masterChief.split(" ")
print(x)

print(set(x))  # conversión de lista a un set

# ejemplo de un set. No se puede acceder a los elementos por su index porque no están ordenados
lugares = {"Arcadis", "Lindblum", "Green hill", "Dry dry desert", "Lea Monde"}
print(lugares)  # Se puede accerder a los elementos de un set con un bucle for (acá en python se parece al foreach de java)

juego = {"Nombre": "Super Mario bros 3", # Ejemplo de diccionario, se parece mucho al formato json
         "Puntaje": 10, "Desarrollador": "Nintendo"}

print(juego["Desarrollador"]) # Para acceder a los datos de un diccionario se utiliza la llave, no se usa index.


fecha_de_hoy = datetime.datetime.now()
print(fecha_de_hoy)
otra_fecha = datetime.datetime(2024,8,13)
print(otra_fecha)
fecha_3 = datetime.datetime(2023,9,25,17,46,12) # Constructor que acepta año, mes, día, hora, minutos, segundos
print(type(fecha_3))
print(fecha_3)
fecha_4_cadena = "4.12.2021"
fecha_4 = datetime.datetime.strptime(fecha_4_cadena,"%d.%m.%Y") # Este método acepta un string y lo transforma en fecha. También hay que pasarle el formato como segundo argumento, lo caul, está detallado en la documentación
print(fecha_4)
diferencia_de_tiempo = fecha_de_hoy - otra_fecha
print(diferencia_de_tiempo) # Las fechas pueden restarse y te dan la cantidad de días , horas, minutos, etc
fecha_5 = datetime.datetime(2022,9,25,17,46,12)
fecha_6 = datetime.datetime(2022,9,25,17,47,15)
diferencia_de_tiempo2 = fecha_6 - fecha_5
print(type(diferencia_de_tiempo2))
print(diferencia_de_tiempo2.total_seconds()) # El método total_seconds transforma un objeto de clase timedelta en segundos (float). El time delta se obtiene como rsultado de restar dos objetos datetime