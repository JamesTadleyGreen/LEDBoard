# Using https://rapidapi.com/api-sports/api/api-football/endpoints

import requests
from keys import API_KEY
import json

last_url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/league/524/last/1"
live_url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/live"
next_url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/league/"
id_url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/id/"

querystring = {"timezone":"Europe/London"}

headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
    }

def get_live_data(url, id): # TODO this will pull out multiple games if there are multiple in the same league
    tmp = ''
    for fixture in json.loads(requests.request("GET", url, headers=headers, params=querystring).text)['api']['fixtures']:
        if fixture['fixture_id'] == id:
            return fixture
    return None

def get_next_games(league=2790, no_games=10):
    url = f"{next_url}{league}/next/{no_games}"
    return json.loads(requests.request("GET", url, headers=headers, params=querystring).text)

def get_game_by_id(id):
    url = f"{id_url}{id}"
    return json.loads(requests.request("GET", url, headers=headers, params=querystring).text)

# print(get_live_data(live_url, 2790))
#print(get_next_games())