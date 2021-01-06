
def event_goal(oc, font, event):
    graphics.DrawText(oc, font, 16-4*6//2, 17+6//2, white, 'GOAL')
    time.sleep(1)

def event_card(oc, font, event):
    graphics.DrawText(oc, font, 16-4*6//2, 17+6//2, white, 'CARD')
    time.sleep(1)

def event_sub(event):
    graphics.DrawText(oc, font, 16-4*6//2, 17+6//2, white, 'Substitute')
    time.sleep(1)
