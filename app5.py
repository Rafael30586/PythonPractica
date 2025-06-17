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
