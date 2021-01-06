# Using https://rapidapi.com/api-sports/api/api-football/endpoints

import requests
from keys import API_KEY
import json

last_url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/league/524/last/1"
live_url = "https://api-football-v1.p.rapidapi.com/v2/fixtures/live"

querystring = {"timezone":"Europe/London"}

headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
    }

def get_live_data(url, league=2790):
    tmp = []
    print(json.loads(requests.request("GET", url, headers=headers, params=querystring).text)['api']['fixtures'])
    for fixture in requests.request("GET", url, headers=headers, params=querystring).text)['api']['fixtures']:
        if fixture['league_id'] == league:
            tmp.append(fixture)
    return tmp

# f = open("tmp.txt", "w")
# f.write(response.text)
# f.close()

# print(get_live_data(live_url, 2790))