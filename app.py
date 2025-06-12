print("Hello world")
print("*" * 10)

x = 4
y = 6.902
cadena = "comillas "
cadena2 = 'comillas simples '
cadena3 = """Hola
¿todo bien?
"""
otraVariable = False
print(x+y)
print(2*cadena)
print(4*cadena2)

a = len(cadena)  # devuelve la cantidad de caracteres que tiene el string
b = cadena[2]  # Sería el tercer caracter de la cadena
c = cadena2[-1]  # Es el ultimo caracter del string
d = cadena2[0:3]  # Son los tres primeros caracteres de la cadena
e = cadena[1:] # Va desde el segundo caracter hasta el último
f = cadena[:4] # Desde el primero hasta el cuarto
g = cadena3[:] # Toda la cadena completa
print(g)

