# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre 
# por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

masterias = ["Matemática", "Química", "Lengua", "Física", "Historia"]

for materia in masterias:
    print(f"Yo estudio {materia}")

# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

numeros = [1,2,3,4,5,6,7,8,9,10]
numeros.reverse()

numeros_invertidos_texto = ""

for numero in numeros:
    if numero > 1:
        numeros_invertidos_texto = numeros_invertidos_texto + str(numero) + ","
    else: 
        numeros_invertidos_texto = numeros_invertidos_texto + str(numero)

print(numeros_invertidos_texto)

