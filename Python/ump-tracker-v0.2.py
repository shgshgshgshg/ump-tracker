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
INNINGS_TOTAL = input('How many innings will be played? ')

while True:
    if outs == 3:
        print('balls: ' + str(balls))
        print('strikes: ' + str(strikes))
        print('outs: ' + str(outs))
        print(HOME_TEAM + ': ' + str(home_score))
        print(AWAY_TEAM + ': ' + str(away_score))
        print('')
        inning += 1
        continue
    elif top_inn:
        top_inn = False
        continue
    elif inning == INNINGS_TOTAL and top_inn and home_score > away_score:
        print('balls: ' + str(balls))
        print('strikes: ' + str(strikes))
        print('outs: ' + str(outs))
        print(HOME_TEAM + ': ' + str(home_score))
        print(AWAY_TEAM + ': ' + str(away_score))
        print('Inning: ' + str(inning))
        print(HOME_TEAM + ' wins!')
    elif inning == INNINGS_TOTAL and top_inn == False and away_score > home_score:
        print('balls: ' + str(balls))
        print('strikes: ' + str(strikes))
        print('outs: ' + str(outs))
        print(HOME_TEAM + ': ' + str(home_score))
        print(AWAY_TEAM + ': ' + str(away_score))
        print('Inning: ' + str(inning))
        print(AWAY_TEAM + ' wins!')

    options = ['[s] strike', '[b] ball', '[f] foul', '[p] points modifier', '[x] modify other']
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
    elif idx == 4:
        print("To determine what to change, write 's' for strike,")
        print("'b' for balls, and 'o' for outs. Then write the number.")
        modifier = input('')
        modified = modifier.split()
        if modified[0] == 'b':
            balls += int(modified[1])
            print('ball')
        elif modified[0] == 's':
            strikes += int(modified[1])
            print('strike')
        elif modified[0] == 'o':
            outs += int(modified[1])
            print('out')
    if strikes == 3:
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
    print('Inning: ' + str(inning))
    print('------------------------------------------')