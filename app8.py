def funcion(*args): # Un parámetro precedido por un asterisco permite pasar tantos argumentos como queramos y armará con ellos una tupla
    print(args)

funcion(1,True,False,"Hello",6.91)

funcion([True, 4.103, "Good bye"]) # Se le puede pasar una lista

funcion((False, "Sonic", 5)) # También se le puede pasar una tupla

def otra_funcion(**args): # Un parámetro precedido por dos asteriscos permite pasar tantos argumentos como uno quiera del tipo clave valor, y con ellos hará un diccionario
    print(args)

otra_funcion(x="Manzana",y=True,z=0.192)

