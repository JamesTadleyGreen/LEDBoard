#!/usr/bin/env python
# Display a runtext with double-buffering.
import Football.football_data_parse as fdp
import Football.football_get_data as fgd
from Football.Animations.static import background, draw_team_borders, draw_team_names, draw_score_borders, draw_score, draw_time_border, draw_time
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import json
import ast


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("--brightness", help="The brightness of the screen", default=30, type=int)
        self.match_id = 592330
    
    def run(self):
        brightness = self.args.brightness/100
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        
        font = graphics.Font()
        font.LoadFont("../../../../../fonts/7x13.bdf")
        small_font = graphics.Font()
        small_font.LoadFont("../../../../../fonts/4x6.bdf")
        
        max_col = 255 * brightness
        white = graphics.Color(max_col, max_col, max_col)
        red = graphics.Color(max_col,0,0)
        blue = graphics.Color(0,0,max_col)
        green = graphics.Color(0,max_col,0)
        black = graphics.Color(0,0,0)
        
        width = offscreen_canvas.width
        height = offscreen_canvas.height

        timestep = 3*60

        # Sample football data
        #pre_game_data = str(fgd.get_game_by_id(self.match_id)) #TODO
        pre_game_data = "{'api': {'results': 10, 'fixtures': [{'fixture_id': 592330, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-16T12:30:00+00:00', 'event_timestamp': 1610800200, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Not Started', 'statusShort': 'NS', 'elapsed': 0, 'venue': 'Molineux Stadium', 'referee': 'Michael Oliver, England', 'homeTeam': {'team_id': 39, 'team_name': 'Wolves', 'logo': 'https://media.api-sports.io/football/teams/39.png'}, 'awayTeam': {'team_id': 60, 'team_name': 'West Brom', 'logo': 'https://media.api-sports.io/football/teams/60.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}, {'fixture_id': 592324, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-16T15:00:00+00:00', 'event_timestamp': 1610809200, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Not Started', 'statusShort': 'NS', 'elapsed': 0, 'venue': 'Elland Road', 'referee': None, 'homeTeam': {'team_id': 63, 'team_name': 'Leeds', 'logo': 'https://media.api-sports.io/football/teams/63.png'}, 'awayTeam': {'team_id': 51, 'team_name': 'Brighton', 'logo': 'https://media.api-sports.io/football/teams/51.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}, {'fixture_id': 592329, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-16T15:00:00+00:00', 'event_timestamp': 1610809200, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Not Started', 'statusShort': 'NS', 'elapsed': 0, 'venue': 'London Stadium', 'referee': None, 'homeTeam': {'team_id': 48, 'team_name': 'West Ham', 'logo': 'https://media.api-sports.io/football/teams/48.png'}, 'awayTeam': {'team_id': 44, 'team_name': 'Burnley', 'logo': 'https://media.api-sports.io/football/teams/44.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}, {'fixture_id': 592323, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-16T17:30:00+00:00', 'event_timestamp': 1610818200, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Not Started', 'statusShort': 'NS', 'elapsed': 0, 'venue': 'Craven Cottage', 'referee': None, 'homeTeam': {'team_id': 36, 'team_name': 'Fulham', 'logo': 'https://media.api-sports.io/football/teams/36.png'}, 'awayTeam': {'team_id': 49, 'team_name': 'Chelsea', 'logo': 'https://media.api-sports.io/football/teams/49.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}, {'fixture_id': 592325, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-16T20:00:00+00:00', 'event_timestamp': 1610827200, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Not Started', 'statusShort': 'NS', 'elapsed': 0, 'venue': 'King Power Stadium', 'referee': None, 'homeTeam': {'team_id': 46, 'team_name': 'Leicester', 'logo': 'https://media.api-sports.io/football/teams/46.png'}, 'awayTeam': {'team_id': 41, 'team_name': 'Southampton', 'logo': 'https://media.api-sports.io/football/teams/41.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}, {'fixture_id': 592322, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-17T12:00:00+00:00', 'event_timestamp': 1610884800, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Match Postponed', 'statusShort': 'PST', 'elapsed': 0, 'venue': 'Villa Park', 'referee': None, 'homeTeam': {'team_id': 66, 'team_name': 'Aston Villa', 'logo': 'https://media.api-sports.io/football/teams/66.png'}, 'awayTeam': {'team_id': 45, 'team_name': 'Everton', 'logo': 'https://media.api-sports.io/football/teams/45.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}, {'fixture_id': 592328, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-17T14:00:00+00:00', 'event_timestamp': 1610892000, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Not Started', 'statusShort': 'NS', 'elapsed': 0, 'venue': 'Bramall Lane', 'referee': None, 'homeTeam': {'team_id': 62, 'team_name': 'Sheffield Utd', 'logo': 'https://media.api-sports.io/football/teams/62.png'}, 'awayTeam': {'team_id': 47, 'team_name': 'Tottenham', 'logo': 'https://media.api-sports.io/football/teams/47.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}, {'fixture_id': 592326, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-17T16:30:00+00:00', 'event_timestamp': 1610901000, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Not Started', 'statusShort': 'NS', 'elapsed': 0, 'venue': 'Anfield', 'referee': None, 'homeTeam': {'team_id': 40, 'team_name': 'Liverpool', 'logo': 'https://media.api-sports.io/football/teams/40.png'}, 'awayTeam': {'team_id': 33, 'team_name': 'Manchester United', 'logo': 'https://media.api-sports.io/football/teams/33.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}, {'fixture_id': 592327, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-17T19:15:00+00:00', 'event_timestamp': 1610910900, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Not Started', 'statusShort': 'NS', 'elapsed': 0, 'venue': 'Etihad Stadium', 'referee': None, 'homeTeam': {'team_id': 50, 'team_name': 'Manchester City', 'logo': 'https://media.api-sports.io/football/teams/50.png'}, 'awayTeam': {'team_id': 52, 'team_name': 'Crystal Palace', 'logo': 'https://media.api-sports.io/football/teams/52.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}, {'fixture_id': 592321, 'league_id': 2790, 'league': {'name': 'Premier League', 'country': 'England', 'logo': 'https://media.api-sports.io/football/leagues/39.png', 'flag': 'https://media.api-sports.io/flags/gb.svg'}, 'event_date': '2021-01-18T20:00:00+00:00', 'event_timestamp': 1611000000, 'firstHalfStart': None, 'secondHalfStart': None, 'round': 'Regular Season - 19', 'status': 'Not Started', 'statusShort': 'NS', 'elapsed': 0, 'venue': 'Emirates Stadium', 'referee': None, 'homeTeam': {'team_id': 42, 'team_name': 'Arsenal', 'logo': 'https://media.api-sports.io/football/teams/42.png'}, 'awayTeam': {'team_id': 34, 'team_name': 'Newcastle', 'logo': 'https://media.api-sports.io/football/teams/34.png'}, 'goalsHomeTeam': None, 'goalsAwayTeam': None, 'score': {'halftime': None, 'fulltime': None, 'extratime': None, 'penalty': None}}]}}"
        pre_match = ast.literal_eval(pre_game_data)['api']['fixtures'][0]
        # Load in teams
        # Home data
        home_team = pre_match['homeTeam']['team_name']
        home_tla = fdp.tla_parse(home_team)
        home_logo = pre_match['homeTeam']['logo']
        # Away data
        away_team = pre_match['awayTeam']['team_name']
        away_tla = fdp.tla_parse(away_team)
        away_logo = pre_match['awayTeam']['logo']

        # Useful functions
        def solid_background(col):
            for x in range(width):
                for y in range(height):
                    offscreen_canvas.SetPixel(x, y, col.red, col.green, col.blue)





        # Display ------------------------------------------------------------------------------------------------------------
        # Splash screen for 5 mins before the game
        offscreen_canvas.Clear()
        background(offscreen_canvas, home_logo, away_logo, brightness)
        offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
        print('background')
        #time.sleep(5*60 + timestep) #TODO
        
        # Perform an API call every timestep and display the data
        event_count=0
        while True:
            game_data = str(fgd.get_live_data(fgd.live_url, self.match_id))
            print(game_data)
            if game_data != 'None': # Cause I string the thing above stupidly
                new_events, event_count = fdp.extract_most_recent_event(game_data, event_count)
            else:
                break
            if new_events is None:
                print('no events')
                pass
            else:
                print('new events')
                for event in new_events:
                    # Display any events
                    offscreen_canvas.Clear()
                    fdp.display_event(offscreen_canvas, font, white, event['type'])
                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            # Display the score
            offscreen_canvas.Clear()
            # Draw the logos, names, score and time
            background(offscreen_canvas, home_logo, away_logo, brightness)
            draw_team_borders(offscreen_canvas, black)
            draw_team_names(offscreen_canvas, home_tla, away_tla, small_font, white)
            draw_score_borders(offscreen_canvas, black)
            game_time, home_goals, away_goals = fdp.extract_goaline(game_data)
            draw_score(offscreen_canvas, str(home_goals), str(away_goals), font, red)
            draw_time_border(offscreen_canvas, black)
            draw_time(offscreen_canvas,str(game_time))
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            # Wait the timestep until calling the API
            time.sleep(timestep)
        # Pause program at end # TODO add in logic displaying the final result and set up for the next game
        print('game end')
        input()



# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
