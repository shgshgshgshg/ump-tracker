from unittest import skip
from simple_term_menu import TerminalMenu

strikes = 0
balls = 0
outs = 0
home_score = 0
away_score = 0
HOME_TEAM = 'BOS'
AWAY_TEAM = 'NYY'
top_inn = True
point_mod = int()

while True:
    options = ['[s] strike', '[b] ball', '[f] foul', '[h] hit']
    menu = TerminalMenu(options)
    idx = menu.show()
    print(idx)

    if idx == 0:
        strikes += 1
    elif idx == 1:
        balls += 1
    elif idx == 2 and strikes == 0 or 1:
        strikes += 1
    elif idx == 2 and strikes == 2:
        pass
    elif idx == 3:
        point_mod = input('modify pts by: ')
        if top_inn:
            away_score += point_mod
        else:
            home_score += point_mod

    if outs == 3:
        if top_inn:
            top_inn = False
        else:
            top_inn = True
        break
    elif strikes == 3:
        outs += 1
        strikes = 0
        balls = 0
    elif balls == 4:
        strikes = 0
        balls = 0

    print('balls: ' + str(balls))
    print('strikes: ' + str(strikes))
    print('outs: ' + str(outs))
    print(HOME_TEAM + ' ' + str(home_score))
    print(AWAY_TEAM + ' ' + str(away_score))