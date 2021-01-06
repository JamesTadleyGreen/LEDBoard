def logo(oc, team='home', offset=0):
    if team == 'home':
        logo = fdp.imageParser(home_logo, (32,32))
    else:
        logo = fdp.imageParser(away_logo, (32,32))
    pl = logo.pixel_list()
    for x in range(32):
        for y in range(32):
            oc.SetPixel(x+offset, y, pl[x][y][0]*brightness, pl[x][y][1]*brightness, pl[x][y][2]*brightness)

def background(oc):
    logo(oc, team='home')
    logo(oc, team='away', offset=32)

def draw_score_borders(oc):
    for x in [0,7]:
        graphics.DrawLine(oc, 12+x, 11, 12+x, 19, black)
        graphics.DrawLine(oc, 12+32+x, 11, 12+32+x, 19, black)
    for x in range(1,7):
        graphics.DrawLine(oc, 12+x, 10, 12+x, 20, black)
        graphics.DrawLine(oc, 12+32+x, 10, 12+32+x, 20, black)

def draw_score(oc, home_score, away_score):
    graphics.DrawText(oc, font, 16-6//2, 17+6//2, white, home_score)
    graphics.DrawText(oc, font, 16+32-6//2, 17+6//2, white, away_score)

def draw_team_borders():
    for x in range(3*4+1):
        graphics.DrawLine(oc, 15-4//2*3+x, 1, 15-4//2*3+x, 7, black)
        graphics.DrawLine(oc, 15+32-4//2*3+x, 1, 15+32-4//2*3+x, 7, black)

def draw_team_names(oc, home_team, away_team):
    graphics.DrawText(oc, small_font, 16-4*3//2, 7, white, home_team)
    graphics.DrawText(oc, small_font, 16+32-4*3//2, 7, white, away_team)
        