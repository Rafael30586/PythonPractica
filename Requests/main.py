import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/204")

textoDePokemon = response.text # Devuelve un string
listaDePokemon = response.json() # Devuelve un diccionario

print(type(listaDePokemon))


contador = 0

for caracteristica in listaDePokemon:
    if contador == 14:
        print(caracteristica)
    contador += 1

