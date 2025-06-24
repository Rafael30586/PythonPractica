personajes = ["Link", "MasterChief", "Sephiroth", "Knuckles"]
esta = "Link" in personajes # El prefijo in sirve, entre otras cosas, para saber si un determinado elemento está dentro de un array
personajes2 = ("Pit", "Bowser", "Snake", "Steiner", "Ramza")
esta2 = "Ramza" in personajes2
no_esta = "Jaster" not in personajes

print(esta)
print(esta2)
print(no_esta)

# print("Hola"*3.65) da error.

juego1 = "Halo combat evolved"
juego2 = "Sonic 3"

print(juego1,juego2) # Ejemplo de cómo se "concatenan" strings al usar la función print()


class Vehiculo:
    def __init__(self):
        pass


class Moto(Vehiculo): # La clase moto hereda de la clase vehiculo
    def __init__(self):
        super().__init__()

class Vehiculo_Electrico:
    def __init__(self):
        pass

class Bicicleta_Electrica(Vehiculo,Vehiculo_Electrico): # Ejemplo de herencia múltiple en python
    def __init__(self): # Hereda el constructor de la clase Vehiculo porque se le da preferencia al primero
        super().__init__()