from rgbmatrix import graphics
import time

def event_goal(oc, font, col, event):
    graphics.DrawText(oc, font, 16-4*6//2, 17+6//2, col, 'GOAL')
    time.sleep(1)

def event_card(oc, font, col, event):
    graphics.DrawText(oc, font, 16-4*6//2, 17+6//2, col, 'CARD')
    time.sleep(1)

def event_sub(oc, font, col, event):
    graphics.DrawText(oc, font, 16-4*6//2, 17+6//2, col, 'Substitute')
    time.sleep(1)
