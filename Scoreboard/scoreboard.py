#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("--players", help="The number of players", default=2, type=int)
        self.parser.add_argument("--brightness", help="The brightness of the screen", default=30, type=int)

    def run(self):
        brightness = self.args.brightness/100
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../../../fonts/7x13.bdf")
        max_col = 255 * brightness
        white = graphics.Color(max_col, max_col, max_col)
        red = graphics.Color(max_col,0,0)
        blue = graphics.Color(0,0,max_col)
        green = graphics.Color(0,max_col,0)
        black = graphics.Color(0,0,0)
        width = offscreen_canvas.width
        height = offscreen_canvas.height
        players = self.args.players
        player_score = [0]*players
        choice = ''

        # Useful functions
        def background(col):
            for x in range(width):
                for y in range(height):
                    offscreen_canvas.SetPixel(x, y, col.red, col.green, col.blue)
            return offscreen_canvas

        def set_up_background():
            set_up_background_list = []
            x_lim = width
            for y in range(height):
                for x in range(x_lim):
                    if x%2==0 and (x-y)%2==0:
                        set_up_background_list.append(offscreen_canvas.SetPixel(x, y, max_col, 0, 0))
                    else:
                        set_up_background_list.append(offscreen_canvas.SetPixel(x, y, max_col, 0, 155*brightness))
                for x in range(x_lim, width):
                    if x%2==0 and (x-y)%2==0:
                        set_up_background_list.append(offscreen_canvas.SetPixel(x, y, 0, 0, max_col))
                    else:
                        set_up_background_list.append(offscreen_canvas.SetPixel(x, y, 0, 155*brightness, max_col))
                x_lim -= 2
            return tuple(set_up_background_list)

        def set_up_text():
            set_up_players = graphics.DrawText(offscreen_canvas, font, 0*width//players, 10, white, 'Player')
            return set_up_players

        def swipe(oc, left_col=white, right_col=red, speed=0.01, direction='l'):
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            if direction == 'l':
                pos = width
                while pos >= 0:
                    offscreen_canvas.Clear()
                    for x in range(width):
                        if x < pos:
                            graphics.DrawLine(offscreen_canvas, x, 0, x, height, left_col)
                        else:
                            graphics.DrawLine(offscreen_canvas, x, 0, x, height, right_col)
                    pos -= 1
                    time.sleep(speed)
                    oc = self.matrix.SwapOnVSync(offscreen_canvas)
            if direction == 'r':
                pos = 0
                while pos <= width:
                    offscreen_canvas.Clear()
                    for x in range(width):
                        if x < pos:
                            graphics.DrawLine(offscreen_canvas, x, 0, x, height, left_col)
                        else:
                            graphics.DrawLine(offscreen_canvas, x, 0, x, height, right_col)
                    pos += 1
                    time.sleep(speed)
                    oc = self.matrix.SwapOnVSync(offscreen_canvas)

        def tmp_text_type(oc, x, y, col=white, text='Hello World', speed=0.5):
            text = ' ' + text
            if x=='mid':
                x = width//2 - (len(text)+1)*3
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            for i in range(len(text)):
                oc.Clear()
                graphics.DrawText(offscreen_canvas, font, x+6*i, y, col, text[i])
                oc = self.matrix.SwapOnVSync(offscreen_canvas)
                time.sleep(speed)

        def text_type(oc, x, y, col=white, text='Hello World', speed=0.5, back=black):
            text = ' ' + text
            if x=='mid':
                x = width//2 - (len(text)+2)*3
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            for i in range(len(text)):
                offscreen_canvas = background(back)
                graphics.DrawText(offscreen_canvas, font, x, y, col, text[:i+1])
                oc = self.matrix.SwapOnVSync(offscreen_canvas)
                time.sleep(speed)

        def scroll_text(oc, col=white, text='Hello World', speed=0.05):
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            pos = width
            len = 0
            while pos + len > 0:
                offscreen_canvas.Clear()
                len = graphics.DrawText(offscreen_canvas, font, pos, 21, col, text)
                pos -= 1
                time.sleep(speed)
                oc = self.matrix.SwapOnVSync(offscreen_canvas)

        def match_point(oc):
            scroll_text(oc, text='MATCH POINT')

        def sudden_death(oc):
            swipe(oc, white, red, 0.005)
            swipe(oc, red, blue, 0.005, 'r')
            swipe(oc, blue, white, 0.005)
            tmp_text_type(oc, 'mid', 10, text='SUDDEN', col=red)
            tmp_text_type(oc, 'mid', 20, text='DEATH', col=blue)
            text_type(oc, 'mid', 10, text='SUDDEN', col=red)
            text_type(oc, 'mid', 20, text='DEATH', col=blue)

        def amend_scores():
            scores = input('Input the correct scores, seperated by a space (e.g. 5 4): ')
            return [int(s) for s in scores.split(' ')]

        def winner(oc, ps):
            if ps[0]>=ps[1]: # If it's a draw player 1 wins cause I cba to fix for draw
                winner = red
            else:
                winner = blue
            swipe(oc, white, winner, 0.005)
            while True:
                text_type(oc, 'mid', 21, white, 'WINNER', back=winner)
                oc.Clear()

        offscreen_canvas.Clear()
        set_up_background()
        offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

        input()
        while True:
            player_strings = [str(i) for i in player_score]
            def draw_scores(l):
                scores_list = []
                scores_list.append(graphics.DrawText(offscreen_canvas, font, 5, 15, black, l[0]))
                scores_list.append(graphics.DrawText(offscreen_canvas, font, 64-5-len(l[1])*6, 25, black, l[1]))
                return tuple(scores_list)

            offscreen_canvas.Clear()
            set_up_background()
            draw_scores(player_strings)

            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            choice = int(input('1: Team 1, 2: Team 2, 0: Match Point, -1: Sudden Death, 3: Amend Scores ---> '))
            if choice == 0:
                match_point(offscreen_canvas)
            elif choice == -1:
                sudden_death(offscreen_canvas)
            elif choice in [1,2]:
                player_score[choice-1] += 1
            elif choice == 3:
                player_score = amend_scores()
            elif choice == 100:
                winner(offscreen_canvas, player_score)
            else:
                pass

# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
