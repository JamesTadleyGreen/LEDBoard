#!/usr/bin/env python
# Display a runtext with double-buffering.
import Football.football_data_parse as fdp
import Football.Animations.events as events
from Football.Animations.static import background, draw_team_borders, draw_team_names, draw_score_borders, draw_score
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import json


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("--brightness", help="The brightness of the screen", default=30, type=int)

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

        # Temp football data
        extracted_data = fdp.extract_past_football_data(fdp.sample_past_match_data)
        # Home data
        home_team = extracted_data['home'][0]
        home_tla = fdp.tla_parse(home_team)
        home_logo = extracted_data['home'][-1]
        # Away data
        away_team = extracted_data['away'][0]
        print(away_team)
        away_tla = fdp.tla_parse(away_team)
        away_logo = extracted_data['away'][-1]

        # Useful functions
        def solid_background(col):
            for x in range(width):
                for y in range(height):
                    offscreen_canvas.SetPixel(x, y, col.red, col.green, col.blue)





        # Display ------------------------------------------------------------------------------------------------------------
        i=0
        while True:
            offscreen_canvas.Clear()
            background(offscreen_canvas)
            draw_team_borders(offscreen_canvas)
            draw_team_names(offscreen_canvas, home_tla, away_tla)
            draw_score_borders(offscreen_canvas)
            draw_score(offscreen_canvas, str(i%10),'0')
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            #time.sleep(1)
            i+=1
        # Pause
        input()



# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
