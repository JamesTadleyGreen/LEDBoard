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
#sample_past_match_data = open("../tmp.txt", "r").read()
#sample_past_match_data = ast.literal_eval(sample_past_match_data)

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
    return team[:3] # If it can't find the name in the database just use thefirst three letters

def extract_most_recent_event(string_data, event_no=0):
    """[summary]

    Args:
        string_data (str): The dictionary data for the live game as a string
        event_no (int): The number of events seen so far, to know if there's been a new event

    Returns:
        tuple: list of data and the number of events seen so far
    """
    tmp = None
    game_data = ast.literal_eval(str(string_data))
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

def extract_goaline(string_data):
    """[summary]

    Args:
        string_data (str): The dictionary data for the live game as a string

    Returns:
        tuple: timestamp and goaline
    """
    game_data = ast.literal_eval(string_data)
    return game_data['elapsed'], game_data['goalsHomeTeam'], game_data['goalsAwayTeam']

next_games = "{'api': {'results': 10, 'fixtures': [{'fixture_id': 592330, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-16T12:30:00+00:00', 'event_timestamp': 1610800200, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Not Started', 'statusShort': 'NS', 'elapsed': 0, 'venue': 'Molineux Stadium', 'referee': None, 'homeTeam': {'team_id': 39, 'team_name': 'Wolves', 'logo': 'https://media.api-sports.io/football/teams/39.png'}, 'awayTeam': {'team_id': 60, 'team_name': 'West Brom', 'logo': 'https://media.api-sports.io/football/teams/60.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}, {'fixture_id': 592329, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-16T15:00:00+00:00', 'event_timestamp': 1610809200, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Not Started', 'statusShort': 'NS', 'elapsed': 0, 'venue': 'London Stadium', 'referee': None, 'homeTeam': {'team_id': 48, 'team_name': 'West Ham', 'logo': 'https://media.api-sports.io/football/teams/48.png'}, 'awayTeam': {'team_id': 44, 'team_name': 'Burnley', 'logo': 'https://media.api-sports.io/football/teams/44.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}, {'fixture_id': 592324, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-16T15:00:00+00:00', 'event_timestamp': 1610809200, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Not Started', 'statusShort': 'NS', 'elapsed': 0, 'venue': 'Elland Road', 'referee': None, 'homeTeam': {'team_id': 63, 'team_name': 'Leeds', 'logo': 'https://media.api-sports.io/football/teams/63.png'}, 'awayTeam': {'team_id': 51, 'team_name': 'Brighton', 'logo': 'https://media.api-sports.io/football/teams/51.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}, {'fixture_id': 592323, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-16T17:30:00+00:00', 'event_timestamp': 1610818200, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Not Started', 'statusShort': 'NS', 'elapsed': 0, 'venue': 'Craven Cottage', 'referee': None, 'homeTeam': {'team_id': 36, 'team_name': 'Fulham', 'logo': 'https://media.api-sports.io/football/teams/36.png'}, 'awayTeam': {'team_id': 49, 'team_name': 'Chelsea', 'logo': 'https://media.api-sports.io/football/teams/49.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}, {'fixture_id': 592325, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-16T20:00:00+00:00', 'event_timestamp': 1610827200, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Not Started', 'statusShort': 'NS', 'elapsed': 0, 'venue': 'King Power Stadium', 'referee': None, 'homeTeam': {'team_id': 46, 'team_name': 'Leicester', 'logo': 'https://media.api-sports.io/football/teams/46.png'}, 'awayTeam': {'team_id': 41, 'team_name': 'Southampton', 'logo': 'https://media.api-sports.io/football/teams/41.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}, {'fixture_id': 592322, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-17T12:00:00+00:00', 'event_timestamp': 1610884800, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Match Postponed', 'statusShort': 'PST', 'elapsed': 0, 'venue': 'Villa Park', 'referee': None, 'homeTeam': {'team_id': 66, 'team_name': 'Aston Villa', 'logo': 'https://media.api-sports.io/football/teams/66.png'}, 'awayTeam': {'team_id': 45, 'team_name': 'Everton', 'logo': 'https://media.api-sports.io/football/teams/45.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}, {'fixture_id': 592328, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-17T14:00:00+00:00', 'event_timestamp': 1610892000, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Not Started', 'statusShort': 'NS', 'elapsed': 0, 'venue': 'Bramall Lane', 'referee': None, 'homeTeam': {'team_id': 62, 'team_name': 'Sheffield Utd', 'logo': 'https://media.api-sports.io/football/teams/62.png'}, 'awayTeam': {'team_id': 47, 'team_name': 'Tottenham', 'logo': 'https://media.api-sports.io/football/teams/47.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}, {'fixture_id': 592326, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-17T16:30:00+00:00', 'event_timestamp': 1610901000, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Not Started', 'statusShort': 'NS', 'elapsed': 0, 'venue': 'Anfield', 'referee': None, 'homeTeam': {'team_id': 40, 'team_name': 'Liverpool', 'logo': 'https://media.api-sports.io/football/teams/40.png'}, 'awayTeam': {'team_id': 33, 'team_name': 'Manchester United', 'logo': 'https://media.api-sports.io/football/teams/33.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}, {'fixture_id': 592327, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-17T19:15:00+00:00', 'event_timestamp': 1610910900, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Not Started', 'statusShort': 'NS', 'elapsed': 0, 'venue': 'Etihad Stadium', 'referee': None, 'homeTeam': {'team_id': 50, 'team_name': 'Manchester City', 'logo': 'https://media.api-sports.io/football/teams/50.png'}, 'awayTeam': {'team_id': 52, 'team_name': 'Crystal Palace', 'logo': 'https://media.api-sports.io/football/teams/52.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}, {'fixture_id': 592321, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-18T20:00:00+00:00', 'event_timestamp': 1611000000, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Not Started', 'statusShort': 'NS', 'elapsed': 0, 'venue': 'Emirates Stadium', 'referee': None, 'homeTeam': {'team_id': 42, 'team_name': 'Arsenal', 'logo': 'https://media.api-sports.io/football/teams/42.png'}, 'awayTeam': {'team_id': 34, 'team_name': 'Newcastle', 'logo': 'https://media.api-sports.io/football/teams/34.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}]}}"
priority_teams = ['Wolves', 'Liverpool']

def choose_next_game(game_dict):
    game_data = ast.literal_eval(game_dict)['api']['fixtures']
    team_list = []
    for fixture in game_data:
        team_list.append(fixture['homeTeam']['team_name'])
        team_list.append(fixture['awayTeam']['team_name'])
    for team in priority_teams:
        if team in team_list:
            return game_data[team_list.index(team)//2]
    return None

# print(os.listdir())
#sample_live_data('../game.txt')
# print(choose_next_game(next_games))