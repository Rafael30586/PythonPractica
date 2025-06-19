personajes = ["Link", "MasterChief", "Sephiroth", "Knuckles"]
esta = "Link" in personajes # El prefijo in sirve, entre otras cosas, para saber si un determinado elemento está dentro de un array
personajes2 = ("Pit", "Bowser", "Snake", "Steiner", "Ramza")
esta2 = "Ramza" in personajes2
no_esta = "Jaster" not in personajes

print(esta)
print(esta2)
print(no_esta)

# print("Hola"*3.65) da error.