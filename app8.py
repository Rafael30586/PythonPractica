def funcion(*args): # Un parámetro precedido por un asterisco permite pasar tantos argumentos como queramos y armará con ellos una tupla
    print(args)

funcion(1,True,False,"Hello",6.91)

def otra_funcion(**args): # Un parámetro precedido por dos asteriscos permite pasar tantos argumentos como uno quiera del tipo clave valor, y con ellos hará un diccionario
    print(args)

otra_funcion(x="Manzana",y=True,z=0.192)