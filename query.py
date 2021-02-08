import requests
import json

BASE_URL = 'https://pokeapi.co'
url = 'http://pokeapi.co/api/v1/pokemon/charizard/'
response = requests.get(url)

def query_pokeapi(resource_url):
    url = '{0}{1}'.format(BASE_URL, resource_url)
