import Football.football_data_parse as fdp
from rgbmatrix import graphics

def logo(oc, logo, offset=0, brightness=30/100):
    logo = fdp.imageParser(logo, (32,32))
    pl = logo.pixel_list()
    for x in range(32):
        for y in range(32):
            oc.SetPixel(x+offset, y, pl[x][y][0]*brightness, pl[x][y][1]*brightness, pl[x][y][2]*brightness)

def background(oc, home_logo, away_logo, brightness=30/100):
    logo(oc, home_logo, brightness=brightness)
    logo(oc, away_logo, offset=32, brightness=brightness)

def draw_score_borders(oc, col):
    for x in [0,7]:
        graphics.DrawLine(oc, 12+x, 11, 12+x, 19, col)
        graphics.DrawLine(oc, 12+32+x, 11, 12+32+x, 19, col)
    for x in range(1,7):
        graphics.DrawLine(oc, 12+x, 10, 12+x, 20, col)
        graphics.DrawLine(oc, 12+32+x, 10, 12+32+x, 20, col)

def draw_score(oc, home_score, away_score, font, col):
    graphics.DrawText(oc, font, 16-6//2, 17+6//2, col, home_score)
    graphics.DrawText(oc, font, 16+32-6//2, 17+6//2, col, away_score)

def draw_team_borders(oc, col):
    for x in range(3*4+1):
        graphics.DrawLine(oc, 15-4//2*3+x, 1, 15-4//2*3+x, 7, col)
        graphics.DrawLine(oc, 15+32-4//2*3+x, 1, 15+32-4//2*3+x, 7, col)

def draw_team_names(oc, home_team, away_team, font, col):
    graphics.DrawText(oc, font, 16-4*3//2, 7, col, home_team)
    graphics.DrawText(oc, font, 16+32-4*3//2, 7, col, away_team)

def draw_time_border(oc, col):
    pass

def draw_time(oc, time):
    print(time)
