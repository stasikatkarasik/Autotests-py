import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '09933cb230515db94ccc4671e067aa84'
HEADER = {'Content-Type': 'application/json' , 'trainer_token' : TOKEN }

body_pokemon = {
    "name": "Буcинка",
    "photo_id": 8
}

body_new_name = {
    "pokemon_id": "168939",
    "name": "Булочка"
}

body_catch = {
    "pokemon_id": "168939"
}

'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemon)
print(response.text)'''

'''response = requests.patch(url = f'{URL}/pokemons' , headers = HEADER, json = body_new_name)
print(response.text)'''

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response.text)
