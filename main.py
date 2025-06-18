import module  # Así es como se importan los módulos                                  
from module2 import incrementar # Así se importa una función específica de un módulo
import module3 as m3 # Así se importa un módulo con un alias
import os # Módulo que ya viene con python


module.saludar("Sonic", "the hedgehog")
print(module.juego)

incrementar(45, 8)

print(m3.un_personaje)

print(os.name)
