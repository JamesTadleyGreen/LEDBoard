# imports
import json
from Display.image_parser import imageParser
import csv
import ast
import time


# TODO Read in the next match date and set a cron job


# Parse the match data
# sample_past_match_data = open("../tmp.txt", "r").read()
# sample_past_match_data = json.loads(json_data)

def extract_past_football_data(json_data):
    fixture = json_data['api']['fixtures'][0]
    hometeam, homelogo = fixture['homeTeam']['team_name'], fixture['homeTeam']['logo']
    awayteam, awaylogo = fixture['awayTeam']['team_name'], fixture['awayTeam']['logo']
    venue = fixture['venue']
    homegoals = fixture['goalsHomeTeam']
    awaygoals = fixture['goalsAwayTeam']
    elapsed = fixture['elapsed']
    return {'venue': venue, 'elapsed': elapsed, 'home': [hometeam, homegoals, homelogo], 'away': [awayteam, awaygoals, awaylogo]}

def tla_parse(team):
    """Lookup the three letter abbbreviation for a team

    Args:
        team (str): The team name

    Returns:
        str: the TLA for the team
    """
    with open("./Data/tla.csv") as csv_file:
        for line in csv.reader(csv_file, delimiter=","):
            if line[1] == team:
                return line[0]
    return 'NAN'

def extract_most_recent_event(string_data, event_no=0):
    """[summary]

    Args:
        string_data (str): The dictionary data for the live game as a string
        event_no (int): The number of events seen so far, to know if there's been a new event

    Returns:
        tuple: list of data and the number of events seen so far
    """
    tmp = None
    game_data = ast.literal_eval(string_data)
    new_events = len(game_data['events']) - event_no
    if new_events:
        return game_data['events'][-new_events:], len(game_data['events'])
    return None, event_no

def display_event(event):
    event_dict = {'Goal': event_goal, 'Card': event_card, 'subst': event_sub}
    return event_dict[event](event)

def event_goal(event):
    print('goal')
    pass

def event_card(event):
    print('card')
    pass

def event_sub(event):
    print('sub')
    pass

def display_game():
    pass

def sample_live_data(data):
    events = 0
    with open(data) as csv_file:
        for line in csv.reader(csv_file, delimiter="\n"):
            new_events, events = extract_most_recent_event(line[0], events)
            if new_events is not None:
                for event in new_events:
                    display_event(event['type'])
            display_game()
            print(new_events, events)
            time.sleep(1)

sample_live_data('game.txt')