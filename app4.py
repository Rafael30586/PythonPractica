def saludar(first_name, last_name): #Ejemplo de función
    print(f"Hola {first_name} {last_name}")

saludar("Rafael","Alvarez")

def get_saludo(nombre):
    return f"Hola {nombre}" #Así se retornan valores

mensaje = get_saludo("Rafael")
print(mensaje)

print(saludar("Pablo","Gimenez")) #Imprime "none" porque eso es lo que devuelven las funciones por defecto, a menos que la función tenga un valor de retorno  

def incrementar(numero,por):
    return numero + por

print(incrementar(48, por=3)) #Cuando llamamos a una función podemos colocar el nombre del parámetro al momento de pasar el argumento. Sirve para que el código sea más legible en ocasiones

def incrementar2(numero, por=17): #Podemos darle un valor por defecto a los parámetros cuando creamos una función. Estos parámetros nunca se escriben antes de los parámetros obligatorios
    return numero + por

print(incrementar2(103)) #Darle un segundo argumento a esta función es opcional porque el segundo parámetro ya viene con un valor por defecto

# def incrementar3(numero=34, por){...  Da error porque el parámetro opcional está antes que el obligatorio

def multiply(*numbers): #El asterisco sirve para que podamos pasarle como argumento un elemento iterable a la función
    for number in numbers:
        print(number)

multiply(4,9,10,34)