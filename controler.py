# imports
import json
from Display.image_parser import imageParser


# TODO Read in the next match date and set a cron job


# Parse the data
json_data = open("tmp.txt", "r").read()
data = json.loads(json_data)
json_formatted_str = json.dumps(data['api']['fixtures'][0], indent=2)

def extract_football_data(json_data):
    fixture = json_data['api']['fixtures'][0]
    hometeam, homelogo = fixture['homeTeam']['team_name'], fixture['homeTeam']['logo']
    awayteam, awaylogo = fixture['awayTeam']['team_name'], fixture['awayTeam']['logo']
    venue = fixture['venue']
    homegoals = fixture['goalsHomeTeam']
    awaygoals = fixture['goalsAwayTeam']
    elapsed = fixture['elapsed']
    return {'venue': venue, 'elapsed': elapsed, 'home': [hometeam, homegoals, homelogo], 'away': [awayteam, awaygoals, awaylogo]}

print(extract_football_data(data))

logo = imageParser(extract_football_data(data)['home'][-1], (32,32))
print(logo.pixel_list())