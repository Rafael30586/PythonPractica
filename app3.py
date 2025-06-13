import math # Este módulo permite utiliza muchas funciones como, por ejemplo, logaritmos

print(math.log10(100))

#x = "1" + 1 Esto da error, no lo concatena como pasa en otros lenguajes

cadena = "496"
print(type(cadena)) #La función type devuelve el tipo de dato de la variable

int(cadena) #Conversión de un string a entero

#Si hacemos casting pasando a boolean un string "" o un número 0, nos da false, la mayoría de los otros valores darán true

age = 24

if 18<age<=65: # En python, a diferencia de otros lenguajes, se puede usar esta expresión matemática en condicionales
    print("Elegible")

for number in range(3): #Imprime desde 0 hasta 2
    print("Attempt",number)

for number in range(2,6): #Imprime desde 2 hasta 5
    print("Intento",number)

for number in range(1,10,2): #Imprime desde 1 hasta 9 yendo de dos en dos
    print("Hola",number)

for number in range(3):
    if number>5:
        print("Bueno")
        break
else: # Los else de los bucles for se ejecutan si el bucle no se detiene por una cuase distinta al range, en este caso el if no logra detenerlo así que el else se ejecuta
    print("Lo lograste")

for x in "Python": #Los strings son objetos iterables en python
    print(x)