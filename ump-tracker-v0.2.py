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
    if strikes == 2:
        options.pop(2)
    elif outs == 3:
        print('balls: ' + str(balls))
        print('strikes: ' + str(strikes))
        print('outs: ' + str(outs))
        print(HOME_TEAM + ' ' + str(home_score))
        print(AWAY_TEAM + ' ' + str(away_score))
        print('')
        break

    options = ['[s] strike', '[b] ball', '[f] foul']
    menu = TerminalMenu(options)
    idx = menu.show()
    print(idx)

    if idx == 0:
        strikes += 1
    elif idx == 1:
        balls += 1
    elif idx == 2:
        if strikes in (0, 1):
            strikes += 1
        else:
            pass

    if outs == 3:
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
    print('')