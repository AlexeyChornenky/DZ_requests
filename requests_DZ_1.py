import requests
import json
import pprint

response = requests.get("https://akabab.github.io/superhero-api/api/all.json")
x = response.json()

hero_intelligence = {}
for hero in x:
    if hero["name"] == "Thanos" or hero["name"] == "Hulk" or hero["name"] == "Captain America":
        dict_hero = {hero["name"]: hero["powerstats"]["intelligence"]}
        hero_intelligence.update(dict_hero)
print(f'Самый умный супергерой {max(hero_intelligence)}')