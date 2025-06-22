# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de 
# aviso si la divisa no está en el diccionario.

divisas = {"Euro":'€','Dollar':'$','Yen':'¥'}
nombre_divisa = input("Ingrese el nombre de la divisa")
nombre_divisas = list(divisas.keys()) # el método keys() retorna un objeto de clase dict_keys. En esta línea lo estoy pasando a lista para que sea más fácil de manejar
#print(type(nombre_divisas))
se_encuentra_la_divisa = nombre_divisas.count(nombre_divisa)
#print(type(se_encuentra_la_divisa))
if se_encuentra_la_divisa >= 1:
    print(divisas[nombre_divisa])
else: 
    print("La divisa no se encuentra") # Mejorar el ejercicio para que qcepte la moneda sin importar si está en mayúscula o minúscula