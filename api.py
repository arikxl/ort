import requests

req = requests.get("https://swapi.dev/api/people/1")
print(req.status_code)
person = req.json()
print(person)
print(person['name'])
print(person['films'])
print('films involved in: ')
for film in person['films']:
    req = requests.get(film)
    film = req.json()
    print('Film is: ', film['title'])
