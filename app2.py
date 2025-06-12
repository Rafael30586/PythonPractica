course = "Python \"programming\"" #La barra invertida permite escribir comillas y otros caracteres en un string
course2 = "Python \n programming" #LA barra invertida con la n es un salto de línea
print(course)
print(course2)

first = "Rafael"
last = "Alvarez"
full = f"{first} {last}" #Una forma de concatenar strings sin usar signos +. Se llaman formatted strings

mezclita = f"{len(first)}    {5*2}" 

FIRST = first.upper() #Un ejemplo de como se usan los métodos de string
#El método strip() quita los espacios en blanco a un string
esta = "Raf" in first #Muestra si la secuencia de caracteres se encuentra en la cadena. Retorna un boolean
noEsta = "Raf" not in first
print(full)
print(mezclita)
print(FIRST) 
print(esta)
print(noEsta)

print(10/3)
print(10//3) #Las dos barras dividen pero devuelven un número entero (sin los decimales)
print(10**2) # Potenciación