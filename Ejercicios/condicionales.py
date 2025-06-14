#Escribir un programa que almacene la cadena de caracteres "contraseña" en una variable,
#pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por
#el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas

contraseña = "contraseña"

print("¿Cual es la contraseña?")
intentoDelUsuario = input().lower()

if intentoDelUsuario == contraseña:
    print("La contraseña introducida es la correcta")
else:
    print("Contraseña incorrecta")


#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
#Si el divisor es cero el programa debe mostrar un error

dividendo = int(input("Ingrese el dividendo"))
divisor = int(input("Ingrese el divisor"))

if divisor != 0:
    print("Resultado: ")
    print(dividendo/divisor)
else: 
    print("El divisor no debe ser igaul a cero")

#Escribir un programa que pida al usuario un número y diga si es par o impar

numero = int(input("Ingresar un número entero"))
if numero%2 == 0:
    print("El número es par")
else:
    print("El número es impar")