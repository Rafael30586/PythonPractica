personajes = ["Mario","Link","Samus","Cloud"]
personajes.sort()
print(personajes) # La lisa es ordenada alfabéticamente
print(personajes[2]) # Accediendo a un elemento de la lista según su index

masterChief = "Master Chief mató tres covenant"
x = masterChief.split(" ") #Este método transforma un String en una lista. Como argumento le pasamos el separador que queramos (en este caso el separador es el espacio vacío)
print(x)

print(set(x)) # conversión de lista a un set

lugares = {"Arcadis","Lindblum","Green hill","Dry dry desert","Lea Monde"} # ejemplo de un set. No se puede acceder a los elementos por su index porque no están ordenados
print(lugares) # Se puede accerder a los elementos de un set con un bucle for


