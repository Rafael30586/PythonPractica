# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que 
# ha cumplido (desde 1 hasta su edad).

edad = int(input("Escriba su edad: "))

for anio in range(edad):
    print(anio+1)
    
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos 
# los números impares desde 1 hasta ese número separados por comas.

numeroEntero = int(input("Ingrese un número entero positivo"))
cadenaNumeros = ""

for numero in range(numeroEntero):
    if (numero+1) % 2 != 0:
        cadenaNumeros = cadenaNumeros + str(numero+1) + ", "

print(cadenaNumeros)
