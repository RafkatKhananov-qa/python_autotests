import requests

token = '54ac8771ede4a2e702f7b53be62989fc'

response = requests.post('https://pokemonbattle.me:5000/pokemons', json = {
    'name': 'Веномот',
    'photo': 'https://www.youloveit.ru/uploads/gallery/main/162/venomoth.png'
}, headers = {'Content-Type': 'application/json', 'trainer_token': '54ac8771ede4a2e702f7b53be62989fc'} )

print(response.text) 

response_confirm = requests.put('https://pokemonbattle.me:5000/pokemons', json = {
    "pokemon_id": 3048,
    "name": "Венонат",
    'photo': 'https://www.youloveit.ru/uploads/gallery/main/162/venomoth.png'
}, headers = {'Content-Type': 'application/json', 'trainer_token': '54ac8771ede4a2e702f7b53be62989fc'})
print(response_confirm.text)

response_answer = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', json = {
    "pokemon_id": 3048,
}, headers = {'Content-Type': 'application/json', 'trainer_token': '54ac8771ede4a2e702f7b53be62989fc'})
print(response_answer.text)