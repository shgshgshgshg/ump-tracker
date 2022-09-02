from unittest import skip
from simple_term_menu import TerminalMenu

strikes = 0
balls = 0
outs = 0
home_score = int(0)
away_score = int(0)
HOME_TEAM = 'BOS'
AWAY_TEAM = 'NYY'
top_inn = True
inning = 1
point_mod = int()

while True:
    if strikes == 2:
        options.pop(2)
    elif outs == 3:
        print('balls: ' + str(balls))
        print('strikes: ' + str(strikes))
        print('outs: ' + str(outs))
        print(HOME_TEAM + ': ' + str(home_score))
        print(AWAY_TEAM + ': ' + str(away_score))
        print('')
        break

    options = ['[s] strike', '[b] ball', '[f] foul', '[p] points modifier']
    menu = TerminalMenu(options)
    idx = menu.show()

    if idx == 0:
        strikes += 1
    elif idx == 1:
        balls += 1
    elif idx == 2:
        if strikes in (0, 1):
            strikes += 1
        else:
            pass
    elif idx == 3:
        point_mod = input('')
        if top_inn:
            away_score = int(away_score) + int(point_mod)
        else:
            home_score = int(home_score) + int(point_mod)
        point_mod = 0

    if outs == 3:
        if top_inn == False:
            inning += 1
            continue
        else:
            top_inn == False
            continue
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
    print(HOME_TEAM + ': ' + str(home_score))
    print(AWAY_TEAM + ': ' + str(away_score))
    print('------------------------------------------')