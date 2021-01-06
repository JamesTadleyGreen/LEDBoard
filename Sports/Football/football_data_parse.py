# imports
import json
from Football.Animations.Display.image_parser import imageParser
import Football.Animations.events as events
import csv
import ast
import time
import os


# TODO Read in the next match date and set a cron job


# Parse the match data
sample_past_match_data = open("../tmp.txt", "r").read()
sample_past_match_data = ast.literal_eval(sample_past_match_data)

def extract_past_football_data(json_data):
    hometeam, homelogo = json_data['homeTeam']['team_name'], json_data['homeTeam']['logo']
    awayteam, awaylogo = json_data['awayTeam']['team_name'], json_data['awayTeam']['logo']
    venue = json_data['venue']
    homegoals = json_data['goalsHomeTeam']
    awaygoals = json_data['goalsAwayTeam']
    elapsed = json_data['elapsed']
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

def display_event(oc, font, col, event):
    event_dict = {'Goal': events.event_goal, 'Card': events.event_card, 'subst': events.event_sub}
    return event_dict[event](oc, font, col, event)

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

def extract_live_data(data):
    tmp = []
    with open(data) as csv_file:
        for line in csv.reader(csv_file, delimiter="\n"):
            tmp.append(line)
    return tmp

# print(os.listdir())
#sample_live_data('../game.txt')