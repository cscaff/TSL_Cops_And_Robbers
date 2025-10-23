from operator import itemgetter
from entities import Robber, Cop, _next_Cop


def updateState(_inputs_and_cells):
    currentState, Robber.x, Robber.y, Cop.x, Cop.y = itemgetter('currentState',
        'Robber.x', 'Robber.y', 'Cop.x', 'Cop.y')(_inputs_and_cells)
    if currentState == 0:
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y):
            print('Condition at line 9')
            print('Condition at line 9')
            print('Condition at line 9')
            print('Condition at line 9')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 17')
            print('Condition at line 16')
            print('Condition at line 15')
            print('Condition at line 14')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 24')
            print('Condition at line 22')
            print('Condition at line 20')
            print('Condition at line 18')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 31')
            print('Condition at line 28')
            print('Condition at line 25')
            print('Condition at line 22')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 38')
            print('Condition at line 34')
            print('Condition at line 30')
            print('Condition at line 26')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 45')
            print('Condition at line 40')
            print('Condition at line 35')
            print('Condition at line 30')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 53')
            print('Condition at line 47')
            print('Condition at line 41')
            print('Condition at line 35')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 61')
            print('Condition at line 54')
            print('Condition at line 47')
            print('Condition at line 40')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 68')
            print('Condition at line 60')
            print('Condition at line 52')
            print('Condition at line 44')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 75')
            print('Condition at line 66')
            print('Condition at line 57')
            print('Condition at line 48')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 82')
            print('Condition at line 72')
            print('Condition at line 62')
            print('Condition at line 52')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 89')
            print('Condition at line 78')
            print('Condition at line 67')
            print('Condition at line 56')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 4
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 96')
            print('Condition at line 84')
            print('Condition at line 72')
            print('Condition at line 60')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y
            currentState = 5
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 103')
            print('Condition at line 90')
            print('Condition at line 77')
            print('Condition at line 64')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            currentState = 5
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 110')
            print('Condition at line 96')
            print('Condition at line 82')
            print('Condition at line 68')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x:
            print('Condition at line 115')
            print('Condition at line 100')
            print('Condition at line 85')
            print('Condition at line 70')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x:
            print('Condition at line 120')
            print('Condition at line 104')
            print('Condition at line 88')
            print('Condition at line 72')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 125')
            print('Condition at line 108')
            print('Condition at line 91')
            print('Condition at line 74')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x:
            print('Condition at line 130')
            print('Condition at line 112')
            print('Condition at line 94')
            print('Condition at line 76')
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 135')
            print('Condition at line 116')
            print('Condition at line 97')
            print('Condition at line 78')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 140')
            print('Condition at line 120')
            print('Condition at line 100')
            print('Condition at line 80')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 145')
            print('Condition at line 124')
            print('Condition at line 103')
            print('Condition at line 82')
            currentState = 20
        elif Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 150')
            print('Condition at line 128')
            print('Condition at line 106')
            print('Condition at line 84')
            currentState = 20
    elif currentState == 1:
        print('Condition at line 155')
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            print('Condition at line 156')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 6
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 161')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 165')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 169')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 172')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 175')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 178')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 181')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 184')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 186')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 188')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 190')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 192')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 194')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 196')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 198')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 200')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 202')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 204')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 206')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 208')
            currentState = 20
        elif Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 210')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 212')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 214')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 216')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y:
            print('Condition at line 218')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y:
            print('Condition at line 220')
            currentState = 20
        elif Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 222')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 224')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 226')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 228')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 230')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 232')
            currentState = 20
    elif currentState == 2:
        print('Condition at line 234')
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y):
            print('Condition at line 235')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 8
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 241')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 246')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 9
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 251')
            _next_Cop.y = Cop.y + 1
            currentState = 10
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 254')
            _next_Cop.y = Cop.y + 1
            currentState = 10
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 257')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 10
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 262')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 264')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 266')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 268')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 270')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 272')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 274')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 276')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 278')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 280')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 282')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 284')
            currentState = 20
        elif Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 286')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 288')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y >= Robber.y:
            print('Condition at line 290')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y >= Robber.y:
            print('Condition at line 292')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y:
            print('Condition at line 294')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y:
            print('Condition at line 296')
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 298')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 300')
            currentState = 20
    elif currentState == 3:
        print('Condition at line 302')
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            print('Condition at line 303')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 309')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 314')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 11
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 318')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 322')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 326')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 330')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 332')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 334')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 336')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 338')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 340')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 342')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 344')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 346')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 348')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y:
            print('Condition at line 350')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y:
            print('Condition at line 352')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            print('Condition at line 354')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            print('Condition at line 356')
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 358')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 360')
            currentState = 20
        elif Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 362')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y >= Robber.y:
            print('Condition at line 364')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y >= Robber.y:
            print('Condition at line 366')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y >= Robber.y:
            print('Condition at line 368')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y >= Robber.y:
            print('Condition at line 370')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 372')
            currentState = 20
    elif currentState == 4:
        print('Condition at line 374')
        if (Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y):
            print('Condition at line 375')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 380')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 384')
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 387')
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 391')
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 395')
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 398')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 402')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 406')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 410')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 414')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 418')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 422')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 426')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 430')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 434')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 438')
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 442')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 446')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 450')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 454')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 457')
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 461')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 465')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 469')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 473')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 476')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 479')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            print('Condition at line 482')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 485')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 488')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 491')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y
            currentState = 13
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 495')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y
            currentState = 13
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 499')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y
            currentState = 14
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 503')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            currentState = 14
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 507')
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 15
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 512')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 15
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 517')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y - 1
            currentState = 15
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 522')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 15
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 527')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y - 1
            currentState = 16
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 531')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 534')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 537')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 540')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 543')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 546')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 549')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 552')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 555')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 557')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 559')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 561')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 563')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 566')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 569')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 572')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 575')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 578')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 581')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 584')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 587')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 589')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 591')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 593')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 595')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 597')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 599')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 601')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 604')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 607')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 610')
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 613')
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 616')
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 619')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 621')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 623')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 625')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 628')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 631')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 634')
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 637')
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 640')
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 643')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 645')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 647')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 649')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 651')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 653')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 655')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 657')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            print('Condition at line 659')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 661')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 663')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 665')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 667')
            currentState = 20
    elif currentState == 5:
        print('Condition at line 669')
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y):
            print('Condition at line 670')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 8
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 676')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 681')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 686')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 691')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 9
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 696')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 699')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 702')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 705')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 707')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 709')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 711')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 713')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 715')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x:
            print('Condition at line 717')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x:
            print('Condition at line 719')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 721')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 723')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 725')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 727')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 729')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x:
            print('Condition at line 731')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 733')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 735')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 737')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 739')
            currentState = 20
    elif currentState == 6:
        print('Condition at line 741')
        if (Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and
            Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y):
            print('Condition at line 742')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 745')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 747')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 749')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 751')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 753')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 755')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 757')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 759')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 761')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 763')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 765')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 767')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 769')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 771')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 773')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 775')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 777')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 779')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 781')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 783')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 785')
            currentState = 20
        elif Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 787')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 789')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y >= Robber.y:
            print('Condition at line 791')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y >= Robber.y:
            print('Condition at line 793')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y:
            print('Condition at line 795')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y:
            print('Condition at line 797')
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 799')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 801')
            currentState = 20
    elif currentState == 7:
        print('Condition at line 803')
        if (Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            print('Condition at line 804')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 807')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 809')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 811')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 813')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 815')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 817')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 819')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 821')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 823')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 825')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 827')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 829')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 831')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 833')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 835')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 837')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 839')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x:
            print('Condition at line 841')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x:
            print('Condition at line 843')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 845')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 847')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 849')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 851')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 853')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x:
            print('Condition at line 855')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 857')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 859')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 861')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 863')
            currentState = 20
    elif currentState == 8:
        print('Condition at line 865')
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            print('Condition at line 866')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 6
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 871')
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 874')
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 877')
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 880')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 883')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 886')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 889')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 892')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 895')
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 19
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 899')
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 19
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 903')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 905')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 907')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 909')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 911')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 913')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 915')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 917')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y:
            print('Condition at line 919')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 921')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 923')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y:
            print('Condition at line 925')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            print('Condition at line 927')
            currentState = 20
        elif Cop.x > Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 929')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            print('Condition at line 931')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 933')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 935')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 937')
            currentState = 20
        elif Cop.x > Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 939')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 941')
            currentState = 20
        elif Cop.x > Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 943')
            currentState = 20
    elif currentState == 9:
        print('Condition at line 945')
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            print('Condition at line 946')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 6
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 951')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 954')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 957')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 960')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 963')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 966')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 969')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 971')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 973')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 975')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 977')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 979')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 981')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 983')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 985')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 987')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 989')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 991')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 993')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 995')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 997')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 999')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1001')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x:
            print('Condition at line 1003')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x:
            print('Condition at line 1005')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x:
            print('Condition at line 1007')
            currentState = 20
    elif currentState == 10:
        print('Condition at line 1009')
        if (Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            print('Condition at line 1010')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1015')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y < Robber.y:
            print('Condition at line 1019')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1022')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1025')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1028')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1031')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y < Robber.y:
            print('Condition at line 1034')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1037')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1040')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1043')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1046')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1049')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1052')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1054')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1056')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1058')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1060')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1062')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1064')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1066')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1068')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1070')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1072')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y < Robber.y:
            print('Condition at line 1074')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1076')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y >= Robber.y:
            print('Condition at line 1078')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1080')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1082')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1084')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y:
            print('Condition at line 1086')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1088')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1092')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1096')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y:
            print('Condition at line 1098')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1100')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y >= Robber.y:
            print('Condition at line 1102')
            currentState = 20
    elif currentState == 11:
        print('Condition at line 1104')
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            print('Condition at line 1105')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1109')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1112')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 1115')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1118')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1121')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1123')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1125')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1127')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1129')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1131')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1133')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1135')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y:
            print('Condition at line 1137')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1139')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1141')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1143')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            print('Condition at line 1145')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            print('Condition at line 1147')
            currentState = 20
        elif Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1149')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1151')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1153')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1155')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1157')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 1159')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1161')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 1163')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 1165')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y:
            print('Condition at line 1167')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1169')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1171')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1173')
            currentState = 20
    elif currentState == 12:
        print('Condition at line 1175')
        if (Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and
            Cop.y == Robber.y and Cop.y <= Robber.y):
            print('Condition at line 1176')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 1180')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1183')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1185')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1187')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1189')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1191')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1193')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1195')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1197')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            print('Condition at line 1199')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1201')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y:
            print('Condition at line 1203')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1205')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1207')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1209')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y:
            print('Condition at line 1211')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            print('Condition at line 1213')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y > Robber.y:
            print('Condition at line 1215')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1217')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1219')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1221')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1223')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1225')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1227')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1229')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1231')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1233')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1235')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1237')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 1239')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 1241')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1243')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1245')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1247')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1249')
            currentState = 20
    elif currentState == 13:
        print('Condition at line 1251')
        if Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 1252')
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1254')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 1256')
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1260')
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 1264')
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1268')
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 1272')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1276')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 1280')
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1282')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 1284')
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1288')
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 1292')
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1296')
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 1300')
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1304')
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y:
            print('Condition at line 1308')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1310')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1312')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1314')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1316')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            print('Condition at line 1318')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and Cop.y < Robber.y:
            print('Condition at line 1320')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            print('Condition at line 1322')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y < Robber.y:
            print('Condition at line 1324')
            currentState = 20
        elif Cop.x == Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1326')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            print('Condition at line 1328')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y < Robber.y:
            print('Condition at line 1330')
            currentState = 20
        elif Cop.x > Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1332')
            currentState = 20
        elif Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1334')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1336')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1339')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1342')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1344')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1346')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1349')
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1352')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1355')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1358')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1360')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1363')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1366')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1368')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1371')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1374')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1376')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1379')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1381')
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1384')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1387')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1389')
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1392')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1394')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1397')
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1400')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1403')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1405')
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1408')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1411')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1414')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1416')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1419')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1421')
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1424')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1427')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1429')
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1432')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1434')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1437')
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1440')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1443')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1446')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1448')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1450')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1453')
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1456')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1459')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1461')
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.y == Robber.y:
            print('Condition at line 1464')
            currentState = 20
        elif Cop.x == Robber.x and Cop.y == Robber.y:
            print('Condition at line 1466')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.y == Robber.y:
            print('Condition at line 1469')
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.y == Robber.y:
            print('Condition at line 1472')
            currentState = 20
        elif Cop.x == Robber.x and Cop.y == Robber.y:
            print('Condition at line 1474')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.y == Robber.y:
            print('Condition at line 1477')
            _next_Cop.y = Cop.y - 1
            currentState = 20
    elif currentState == 14:
        print('Condition at line 1480')
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            print('Condition at line 1481')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 6
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1486')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1489')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1492')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1494')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1496')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1498')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1500')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1502')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1504')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1506')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1508')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1510')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1512')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1514')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 1516')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1518')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1520')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1522')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1524')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x:
            print('Condition at line 1526')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x:
            print('Condition at line 1528')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x:
            print('Condition at line 1530')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1532')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1534')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1536')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1538')
            currentState = 20
    elif currentState == 15:
        print('Condition at line 1540')
        if (Cop.x != Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and
            Cop.y > Robber.y and Cop.y < Robber.y):
            print('Condition at line 1541')
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            print('Condition at line 1545')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1548')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1551')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1554')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 8
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1559')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1564')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1569')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1574')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 9
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1579')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            print('Condition at line 1581')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1583')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1585')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1587')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y:
            print('Condition at line 1589')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1591')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 1593')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1595')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1597')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 1599')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1601')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y:
            print('Condition at line 1603')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1605')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1607')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1609')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1611')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1613')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1615')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1617')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1619')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1621')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1623')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1625')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1627')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1629')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1631')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1633')
            currentState = 20
    elif currentState == 16:
        print('Condition at line 1635')
        if (Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and
            Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y):
            print('Condition at line 1636')
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1640')
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1643')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 8
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1648')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1653')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1658')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1663')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 9
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1668')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1671')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1674')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1677')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1680')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1683')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            print('Condition at line 1685')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1687')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1689')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1691')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y:
            print('Condition at line 1693')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1695')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y:
            print('Condition at line 1697')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1699')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1701')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 1703')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1705')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y <= Robber.y:
            print('Condition at line 1707')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1709')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1711')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1713')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1715')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1717')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1719')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1721')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1723')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1725')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1727')
            currentState = 20
    elif currentState == 17:
        print('Condition at line 1729')
        if Cop.x == Robber.x and Cop.x > Robber.x:
            print('Condition at line 1730')
            currentState = 20
        elif Cop.x >= Robber.x:
            print('Condition at line 1732')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x < Robber.x:
            print('Condition at line 1734')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x:
            print('Condition at line 1736')
            currentState = 20
    elif currentState == 18:
        print('Condition at line 1738')
        if Cop.x != Robber.x:
            print('Condition at line 1739')
            currentState = 20
        elif Cop.x > Robber.x:
            print('Condition at line 1741')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x:
            print('Condition at line 1743')
            currentState = 20
    elif currentState == 19:
        print('Condition at line 1745')
        if Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1746')
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.y != Robber.y:
            print('Condition at line 1749')
            currentState = 20
        elif Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1751')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1753')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1755')
            currentState = 20
    elif currentState == 20:
        print('Condition at line 1757')
        if (Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            print('Condition at line 1758')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1762')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1765')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1768')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1770')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1772')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1774')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1776')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1778')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1780')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1782')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1784')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1786')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1788')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1790')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x:
            print('Condition at line 1792')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x:
            print('Condition at line 1794')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1796')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1798')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1800')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1802')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 1804')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x:
            print('Condition at line 1806')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1808')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1810')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1812')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1814')
            currentState = 20
    return {'currentState': currentState, 'Cop.x': _next_Cop.x, 'Cop.y':
        _next_Cop.y}
