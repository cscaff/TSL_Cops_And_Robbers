
from operator import itemgetter
from entities import Robber, Cop, _next_Cop

def log_condition(cond_str):
    print(f"[TRACE] Evaluating condition: {cond_str}")

def updateState(_inputs_and_cells):
    currentState, Robber.x, Robber.y, Cop.x, Cop.y = itemgetter('currentState',
        'Robber.x', 'Robber.y', 'Cop.x', 'Cop.y')(_inputs_and_cells)
    if currentState == 0:
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y):
            print('Condition at line 6')
            print('Condition at line 5')
            print('Condition at line 5')
            print('Condition at line 7')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 14')
            print('Condition at line 12')
            print('Condition at line 11')
            print('Condition at line 12')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 21')
            print('Condition at line 18')
            print('Condition at line 16')
            print('Condition at line 16')
            print('Condition at line 24')
            print('Condition at line 22')
            print('Condition at line 20')
            print('Condition at line 18')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 32')
            print('Condition at line 28')
            print('Condition at line 25')
            print('Condition at line 24')
            print('Condition at line 31')
            print('Condition at line 28')
            print('Condition at line 25')
            print('Condition at line 22')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 43')
            print('Condition at line 38')
            print('Condition at line 34')
            print('Condition at line 32')
            print('Condition at line 38')
            print('Condition at line 34')
            print('Condition at line 30')
            print('Condition at line 26')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 54')
            print('Condition at line 48')
            print('Condition at line 43')
            print('Condition at line 40')
            print('Condition at line 45')
            print('Condition at line 40')
            print('Condition at line 35')
            print('Condition at line 30')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 66')
            print('Condition at line 59')
            print('Condition at line 53')
            print('Condition at line 49')
            print('Condition at line 53')
            print('Condition at line 47')
            print('Condition at line 41')
            print('Condition at line 35')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 78')
            print('Condition at line 70')
            print('Condition at line 63')
            print('Condition at line 58')
            print('Condition at line 61')
            print('Condition at line 54')
            print('Condition at line 47')
            print('Condition at line 40')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 89')
            print('Condition at line 80')
            print('Condition at line 72')
            print('Condition at line 66')
            print('Condition at line 68')
            print('Condition at line 60')
            print('Condition at line 52')
            print('Condition at line 44')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 100')
            print('Condition at line 90')
            print('Condition at line 81')
            print('Condition at line 74')
            print('Condition at line 75')
            print('Condition at line 66')
            print('Condition at line 57')
            print('Condition at line 48')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 111')
            print('Condition at line 100')
            print('Condition at line 90')
            print('Condition at line 82')
            print('Condition at line 82')
            print('Condition at line 72')
            print('Condition at line 62')
            print('Condition at line 52')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 122')
            print('Condition at line 110')
            print('Condition at line 99')
            print('Condition at line 90')
            print('Condition at line 89')
            print('Condition at line 78')
            print('Condition at line 67')
            print('Condition at line 56')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 4
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 133')
            print('Condition at line 120')
            print('Condition at line 108')
            print('Condition at line 98')
            print('Condition at line 96')
            print('Condition at line 84')
            print('Condition at line 72')
            print('Condition at line 60')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y
            currentState = 5
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 144')
            print('Condition at line 130')
            print('Condition at line 117')
            print('Condition at line 106')
            print('Condition at line 103')
            print('Condition at line 90')
            print('Condition at line 77')
            print('Condition at line 64')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            currentState = 5
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 155')
            print('Condition at line 140')
            print('Condition at line 126')
            print('Condition at line 114')
            print('Condition at line 110')
            print('Condition at line 96')
            print('Condition at line 82')
            print('Condition at line 68')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x:
            print('Condition at line 164')
            print('Condition at line 148')
            print('Condition at line 133')
            print('Condition at line 120')
            print('Condition at line 115')
            print('Condition at line 100')
            print('Condition at line 85')
            print('Condition at line 70')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x:
            print('Condition at line 173')
            print('Condition at line 156')
            print('Condition at line 140')
            print('Condition at line 126')
            print('Condition at line 120')
            print('Condition at line 104')
            print('Condition at line 88')
            print('Condition at line 72')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 182')
            print('Condition at line 164')
            print('Condition at line 147')
            print('Condition at line 132')
            print('Condition at line 125')
            print('Condition at line 108')
            print('Condition at line 91')
            print('Condition at line 74')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x:
            print('Condition at line 191')
            print('Condition at line 172')
            print('Condition at line 154')
            print('Condition at line 138')
            print('Condition at line 130')
            print('Condition at line 112')
            print('Condition at line 94')
            print('Condition at line 76')
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 200')
            print('Condition at line 180')
            print('Condition at line 161')
            print('Condition at line 144')
            print('Condition at line 135')
            print('Condition at line 116')
            print('Condition at line 97')
            print('Condition at line 78')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 209')
            print('Condition at line 188')
            print('Condition at line 168')
            print('Condition at line 150')
            print('Condition at line 140')
            print('Condition at line 120')
            print('Condition at line 100')
            print('Condition at line 80')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 218')
            print('Condition at line 196')
            print('Condition at line 175')
            print('Condition at line 156')
            print('Condition at line 145')
            print('Condition at line 124')
            print('Condition at line 103')
            print('Condition at line 82')
            currentState = 20
        elif Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 227')
            print('Condition at line 204')
            print('Condition at line 182')
            print('Condition at line 162')
            print('Condition at line 150')
            print('Condition at line 128')
            print('Condition at line 106')
            print('Condition at line 84')
            currentState = 20
    elif currentState == 1:
        print('Condition at line 236')
        print('Condition at line 212')
        print('Condition at line 189')
        print('Condition at line 168')
        print('Condition at line 155')
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            print('Condition at line 241')
            print('Condition at line 216')
            print('Condition at line 192')
            print('Condition at line 170')
            print('Condition at line 156')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 6
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 250')
            print('Condition at line 224')
            print('Condition at line 199')
            print('Condition at line 176')
            print('Condition at line 161')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 258')
            print('Condition at line 231')
            print('Condition at line 205')
            print('Condition at line 181')
            print('Condition at line 165')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 266')
            print('Condition at line 238')
            print('Condition at line 211')
            print('Condition at line 186')
            print('Condition at line 169')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 273')
            print('Condition at line 244')
            print('Condition at line 216')
            print('Condition at line 190')
            print('Condition at line 172')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 280')
            print('Condition at line 250')
            print('Condition at line 221')
            print('Condition at line 194')
            print('Condition at line 175')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 287')
            print('Condition at line 256')
            print('Condition at line 226')
            print('Condition at line 198')
            print('Condition at line 178')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 294')
            print('Condition at line 262')
            print('Condition at line 231')
            print('Condition at line 202')
            print('Condition at line 181')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 301')
            print('Condition at line 268')
            print('Condition at line 236')
            print('Condition at line 206')
            print('Condition at line 184')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 307')
            print('Condition at line 273')
            print('Condition at line 240')
            print('Condition at line 209')
            print('Condition at line 186')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 313')
            print('Condition at line 278')
            print('Condition at line 244')
            print('Condition at line 212')
            print('Condition at line 188')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 319')
            print('Condition at line 283')
            print('Condition at line 248')
            print('Condition at line 215')
            print('Condition at line 190')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 325')
            print('Condition at line 288')
            print('Condition at line 252')
            print('Condition at line 218')
            print('Condition at line 192')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 331')
            print('Condition at line 293')
            print('Condition at line 256')
            print('Condition at line 221')
            print('Condition at line 194')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 337')
            print('Condition at line 298')
            print('Condition at line 260')
            print('Condition at line 224')
            print('Condition at line 196')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 343')
            print('Condition at line 303')
            print('Condition at line 264')
            print('Condition at line 227')
            print('Condition at line 198')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 349')
            print('Condition at line 308')
            print('Condition at line 268')
            print('Condition at line 230')
            print('Condition at line 200')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 355')
            print('Condition at line 313')
            print('Condition at line 272')
            print('Condition at line 233')
            print('Condition at line 202')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 361')
            print('Condition at line 318')
            print('Condition at line 276')
            print('Condition at line 236')
            print('Condition at line 204')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 367')
            print('Condition at line 323')
            print('Condition at line 280')
            print('Condition at line 239')
            print('Condition at line 206')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 373')
            print('Condition at line 328')
            print('Condition at line 284')
            print('Condition at line 242')
            print('Condition at line 208')
            currentState = 20
        elif Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 379')
            print('Condition at line 333')
            print('Condition at line 288')
            print('Condition at line 245')
            print('Condition at line 210')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 385')
            print('Condition at line 338')
            print('Condition at line 292')
            print('Condition at line 248')
            print('Condition at line 212')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 391')
            print('Condition at line 343')
            print('Condition at line 296')
            print('Condition at line 251')
            print('Condition at line 214')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 397')
            print('Condition at line 348')
            print('Condition at line 300')
            print('Condition at line 254')
            print('Condition at line 216')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y:
            print('Condition at line 403')
            print('Condition at line 353')
            print('Condition at line 304')
            print('Condition at line 257')
            print('Condition at line 218')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y:
            print('Condition at line 409')
            print('Condition at line 358')
            print('Condition at line 308')
            print('Condition at line 260')
            print('Condition at line 220')
            currentState = 20
        elif Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 415')
            print('Condition at line 363')
            print('Condition at line 312')
            print('Condition at line 263')
            print('Condition at line 222')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 421')
            print('Condition at line 368')
            print('Condition at line 316')
            print('Condition at line 266')
            print('Condition at line 224')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 427')
            print('Condition at line 373')
            print('Condition at line 320')
            print('Condition at line 269')
            print('Condition at line 226')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 433')
            print('Condition at line 378')
            print('Condition at line 324')
            print('Condition at line 272')
            print('Condition at line 228')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 439')
            print('Condition at line 383')
            print('Condition at line 328')
            print('Condition at line 275')
            print('Condition at line 230')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 445')
            print('Condition at line 388')
            print('Condition at line 332')
            print('Condition at line 278')
            print('Condition at line 232')
            currentState = 20
    elif currentState == 2:
        print('Condition at line 451')
        print('Condition at line 393')
        print('Condition at line 336')
        print('Condition at line 281')
        print('Condition at line 234')
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y):
            print('Condition at line 456')
            print('Condition at line 397')
            print('Condition at line 339')
            print('Condition at line 283')
            print('Condition at line 235')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 8
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 466')
            print('Condition at line 406')
            print('Condition at line 347')
            print('Condition at line 290')
            print('Condition at line 241')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 475')
            print('Condition at line 414')
            print('Condition at line 354')
            print('Condition at line 296')
            print('Condition at line 246')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 9
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 484')
            print('Condition at line 422')
            print('Condition at line 361')
            print('Condition at line 302')
            print('Condition at line 251')
            _next_Cop.y = Cop.y + 1
            currentState = 10
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 491')
            print('Condition at line 428')
            print('Condition at line 366')
            print('Condition at line 306')
            print('Condition at line 254')
            _next_Cop.y = Cop.y + 1
            currentState = 10
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 498')
            print('Condition at line 434')
            print('Condition at line 371')
            print('Condition at line 310')
            print('Condition at line 257')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 10
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 507')
            print('Condition at line 442')
            print('Condition at line 378')
            print('Condition at line 316')
            print('Condition at line 262')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 513')
            print('Condition at line 447')
            print('Condition at line 382')
            print('Condition at line 319')
            print('Condition at line 264')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 519')
            print('Condition at line 452')
            print('Condition at line 386')
            print('Condition at line 322')
            print('Condition at line 266')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 525')
            print('Condition at line 457')
            print('Condition at line 390')
            print('Condition at line 325')
            print('Condition at line 268')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 531')
            print('Condition at line 462')
            print('Condition at line 394')
            print('Condition at line 328')
            print('Condition at line 270')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 537')
            print('Condition at line 467')
            print('Condition at line 398')
            print('Condition at line 331')
            print('Condition at line 272')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 543')
            print('Condition at line 472')
            print('Condition at line 402')
            print('Condition at line 334')
            print('Condition at line 274')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 549')
            print('Condition at line 477')
            print('Condition at line 406')
            print('Condition at line 337')
            print('Condition at line 276')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 555')
            print('Condition at line 482')
            print('Condition at line 410')
            print('Condition at line 340')
            print('Condition at line 278')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 561')
            print('Condition at line 487')
            print('Condition at line 414')
            print('Condition at line 343')
            print('Condition at line 280')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 567')
            print('Condition at line 492')
            print('Condition at line 418')
            print('Condition at line 346')
            print('Condition at line 282')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 573')
            print('Condition at line 497')
            print('Condition at line 422')
            print('Condition at line 349')
            print('Condition at line 284')
            currentState = 20
        elif Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 579')
            print('Condition at line 502')
            print('Condition at line 426')
            print('Condition at line 352')
            print('Condition at line 286')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 585')
            print('Condition at line 507')
            print('Condition at line 430')
            print('Condition at line 355')
            print('Condition at line 288')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y >= Robber.y:
            print('Condition at line 591')
            print('Condition at line 512')
            print('Condition at line 434')
            print('Condition at line 358')
            print('Condition at line 290')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y >= Robber.y:
            print('Condition at line 597')
            print('Condition at line 517')
            print('Condition at line 438')
            print('Condition at line 361')
            print('Condition at line 292')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y:
            print('Condition at line 603')
            print('Condition at line 522')
            print('Condition at line 442')
            print('Condition at line 364')
            print('Condition at line 294')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y:
            print('Condition at line 609')
            print('Condition at line 527')
            print('Condition at line 446')
            print('Condition at line 367')
            print('Condition at line 296')
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 615')
            print('Condition at line 532')
            print('Condition at line 450')
            print('Condition at line 370')
            print('Condition at line 298')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 621')
            print('Condition at line 537')
            print('Condition at line 454')
            print('Condition at line 373')
            print('Condition at line 300')
            currentState = 20
    elif currentState == 3:
        print('Condition at line 627')
        print('Condition at line 542')
        print('Condition at line 458')
        print('Condition at line 376')
        print('Condition at line 302')
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            print('Condition at line 632')
            print('Condition at line 546')
            print('Condition at line 461')
            print('Condition at line 378')
            print('Condition at line 303')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 642')
            print('Condition at line 555')
            print('Condition at line 469')
            print('Condition at line 385')
            print('Condition at line 309')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 651')
            print('Condition at line 563')
            print('Condition at line 476')
            print('Condition at line 391')
            print('Condition at line 314')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 11
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 659')
            print('Condition at line 570')
            print('Condition at line 482')
            print('Condition at line 396')
            print('Condition at line 318')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 667')
            print('Condition at line 577')
            print('Condition at line 488')
            print('Condition at line 401')
            print('Condition at line 322')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 675')
            print('Condition at line 584')
            print('Condition at line 494')
            print('Condition at line 406')
            print('Condition at line 326')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 683')
            print('Condition at line 591')
            print('Condition at line 500')
            print('Condition at line 411')
            print('Condition at line 330')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 689')
            print('Condition at line 596')
            print('Condition at line 504')
            print('Condition at line 414')
            print('Condition at line 332')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 695')
            print('Condition at line 601')
            print('Condition at line 508')
            print('Condition at line 417')
            print('Condition at line 334')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 701')
            print('Condition at line 606')
            print('Condition at line 512')
            print('Condition at line 420')
            print('Condition at line 336')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 707')
            print('Condition at line 611')
            print('Condition at line 516')
            print('Condition at line 423')
            print('Condition at line 338')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 713')
            print('Condition at line 616')
            print('Condition at line 520')
            print('Condition at line 426')
            print('Condition at line 340')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 719')
            print('Condition at line 621')
            print('Condition at line 524')
            print('Condition at line 429')
            print('Condition at line 342')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 725')
            print('Condition at line 626')
            print('Condition at line 528')
            print('Condition at line 432')
            print('Condition at line 344')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 731')
            print('Condition at line 631')
            print('Condition at line 532')
            print('Condition at line 435')
            print('Condition at line 346')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 737')
            print('Condition at line 636')
            print('Condition at line 536')
            print('Condition at line 438')
            print('Condition at line 348')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y:
            print('Condition at line 743')
            print('Condition at line 641')
            print('Condition at line 540')
            print('Condition at line 441')
            print('Condition at line 350')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y:
            print('Condition at line 749')
            print('Condition at line 646')
            print('Condition at line 544')
            print('Condition at line 444')
            print('Condition at line 352')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            print('Condition at line 755')
            print('Condition at line 651')
            print('Condition at line 548')
            print('Condition at line 447')
            print('Condition at line 354')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            print('Condition at line 761')
            print('Condition at line 656')
            print('Condition at line 552')
            print('Condition at line 450')
            print('Condition at line 356')
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 767')
            print('Condition at line 661')
            print('Condition at line 556')
            print('Condition at line 453')
            print('Condition at line 358')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 773')
            print('Condition at line 666')
            print('Condition at line 560')
            print('Condition at line 456')
            print('Condition at line 360')
            currentState = 20
        elif Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 779')
            print('Condition at line 671')
            print('Condition at line 564')
            print('Condition at line 459')
            print('Condition at line 362')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y >= Robber.y:
            print('Condition at line 785')
            print('Condition at line 676')
            print('Condition at line 568')
            print('Condition at line 462')
            print('Condition at line 364')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y >= Robber.y:
            print('Condition at line 791')
            print('Condition at line 681')
            print('Condition at line 572')
            print('Condition at line 465')
            print('Condition at line 366')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y >= Robber.y:
            print('Condition at line 797')
            print('Condition at line 686')
            print('Condition at line 576')
            print('Condition at line 468')
            print('Condition at line 368')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y >= Robber.y:
            print('Condition at line 803')
            print('Condition at line 691')
            print('Condition at line 580')
            print('Condition at line 471')
            print('Condition at line 370')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 809')
            print('Condition at line 696')
            print('Condition at line 584')
            print('Condition at line 474')
            print('Condition at line 372')
            currentState = 20
    elif currentState == 4:
        print('Condition at line 815')
        print('Condition at line 701')
        print('Condition at line 588')
        print('Condition at line 477')
        print('Condition at line 374')
        if (Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y):
            print('Condition at line 820')
            print('Condition at line 705')
            print('Condition at line 591')
            print('Condition at line 479')
            print('Condition at line 375')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 829')
            print('Condition at line 713')
            print('Condition at line 598')
            print('Condition at line 485')
            print('Condition at line 380')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 837')
            print('Condition at line 720')
            print('Condition at line 604')
            print('Condition at line 490')
            print('Condition at line 384')
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 844')
            print('Condition at line 726')
            print('Condition at line 609')
            print('Condition at line 494')
            print('Condition at line 387')
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 852')
            print('Condition at line 733')
            print('Condition at line 615')
            print('Condition at line 499')
            print('Condition at line 391')
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 860')
            print('Condition at line 740')
            print('Condition at line 621')
            print('Condition at line 504')
            print('Condition at line 395')
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 867')
            print('Condition at line 746')
            print('Condition at line 626')
            print('Condition at line 508')
            print('Condition at line 398')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 875')
            print('Condition at line 753')
            print('Condition at line 632')
            print('Condition at line 513')
            print('Condition at line 402')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 883')
            print('Condition at line 760')
            print('Condition at line 638')
            print('Condition at line 518')
            print('Condition at line 406')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 891')
            print('Condition at line 767')
            print('Condition at line 644')
            print('Condition at line 523')
            print('Condition at line 410')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 899')
            print('Condition at line 774')
            print('Condition at line 650')
            print('Condition at line 528')
            print('Condition at line 414')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 907')
            print('Condition at line 781')
            print('Condition at line 656')
            print('Condition at line 533')
            print('Condition at line 418')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 915')
            print('Condition at line 788')
            print('Condition at line 662')
            print('Condition at line 538')
            print('Condition at line 422')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 923')
            print('Condition at line 795')
            print('Condition at line 668')
            print('Condition at line 543')
            print('Condition at line 426')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 931')
            print('Condition at line 802')
            print('Condition at line 674')
            print('Condition at line 548')
            print('Condition at line 430')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 939')
            print('Condition at line 809')
            print('Condition at line 680')
            print('Condition at line 553')
            print('Condition at line 434')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 947')
            print('Condition at line 816')
            print('Condition at line 686')
            print('Condition at line 558')
            print('Condition at line 438')
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 955')
            print('Condition at line 823')
            print('Condition at line 692')
            print('Condition at line 563')
            print('Condition at line 442')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 963')
            print('Condition at line 830')
            print('Condition at line 698')
            print('Condition at line 568')
            print('Condition at line 446')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 971')
            print('Condition at line 837')
            print('Condition at line 704')
            print('Condition at line 573')
            print('Condition at line 450')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 979')
            print('Condition at line 844')
            print('Condition at line 710')
            print('Condition at line 578')
            print('Condition at line 454')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 986')
            print('Condition at line 850')
            print('Condition at line 715')
            print('Condition at line 582')
            print('Condition at line 457')
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 994')
            print('Condition at line 857')
            print('Condition at line 721')
            print('Condition at line 587')
            print('Condition at line 461')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1002')
            print('Condition at line 864')
            print('Condition at line 727')
            print('Condition at line 592')
            print('Condition at line 465')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1010')
            print('Condition at line 871')
            print('Condition at line 733')
            print('Condition at line 597')
            print('Condition at line 469')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1018')
            print('Condition at line 878')
            print('Condition at line 739')
            print('Condition at line 602')
            print('Condition at line 473')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 1025')
            print('Condition at line 884')
            print('Condition at line 744')
            print('Condition at line 606')
            print('Condition at line 476')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1032')
            print('Condition at line 890')
            print('Condition at line 749')
            print('Condition at line 610')
            print('Condition at line 479')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            print('Condition at line 1039')
            print('Condition at line 896')
            print('Condition at line 754')
            print('Condition at line 614')
            print('Condition at line 482')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1046')
            print('Condition at line 902')
            print('Condition at line 759')
            print('Condition at line 618')
            print('Condition at line 485')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1053')
            print('Condition at line 908')
            print('Condition at line 764')
            print('Condition at line 622')
            print('Condition at line 488')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1060')
            print('Condition at line 914')
            print('Condition at line 769')
            print('Condition at line 626')
            print('Condition at line 491')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y
            currentState = 13
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1068')
            print('Condition at line 921')
            print('Condition at line 775')
            print('Condition at line 631')
            print('Condition at line 495')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y
            currentState = 13
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1076')
            print('Condition at line 928')
            print('Condition at line 781')
            print('Condition at line 636')
            print('Condition at line 499')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y
            currentState = 14
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1084')
            print('Condition at line 935')
            print('Condition at line 787')
            print('Condition at line 641')
            print('Condition at line 503')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            currentState = 14
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1092')
            print('Condition at line 942')
            print('Condition at line 793')
            print('Condition at line 646')
            print('Condition at line 507')
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 15
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1101')
            print('Condition at line 950')
            print('Condition at line 800')
            print('Condition at line 652')
            print('Condition at line 512')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 15
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1110')
            print('Condition at line 958')
            print('Condition at line 807')
            print('Condition at line 658')
            print('Condition at line 517')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y - 1
            currentState = 15
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1119')
            print('Condition at line 966')
            print('Condition at line 814')
            print('Condition at line 664')
            print('Condition at line 522')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 15
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1128')
            print('Condition at line 974')
            print('Condition at line 821')
            print('Condition at line 670')
            print('Condition at line 527')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y - 1
            currentState = 16
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1136')
            print('Condition at line 981')
            print('Condition at line 827')
            print('Condition at line 675')
            print('Condition at line 531')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 1143')
            print('Condition at line 987')
            print('Condition at line 832')
            print('Condition at line 679')
            print('Condition at line 534')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1150')
            print('Condition at line 993')
            print('Condition at line 837')
            print('Condition at line 683')
            print('Condition at line 537')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1157')
            print('Condition at line 999')
            print('Condition at line 842')
            print('Condition at line 687')
            print('Condition at line 540')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1164')
            print('Condition at line 1005')
            print('Condition at line 847')
            print('Condition at line 691')
            print('Condition at line 543')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 1171')
            print('Condition at line 1011')
            print('Condition at line 852')
            print('Condition at line 695')
            print('Condition at line 546')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1178')
            print('Condition at line 1017')
            print('Condition at line 857')
            print('Condition at line 699')
            print('Condition at line 549')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1185')
            print('Condition at line 1023')
            print('Condition at line 862')
            print('Condition at line 703')
            print('Condition at line 552')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1192')
            print('Condition at line 1029')
            print('Condition at line 867')
            print('Condition at line 707')
            print('Condition at line 555')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 1198')
            print('Condition at line 1034')
            print('Condition at line 871')
            print('Condition at line 710')
            print('Condition at line 557')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1204')
            print('Condition at line 1039')
            print('Condition at line 875')
            print('Condition at line 713')
            print('Condition at line 559')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1210')
            print('Condition at line 1044')
            print('Condition at line 879')
            print('Condition at line 716')
            print('Condition at line 561')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1216')
            print('Condition at line 1049')
            print('Condition at line 883')
            print('Condition at line 719')
            print('Condition at line 563')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 1223')
            print('Condition at line 1055')
            print('Condition at line 888')
            print('Condition at line 723')
            print('Condition at line 566')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1230')
            print('Condition at line 1061')
            print('Condition at line 893')
            print('Condition at line 727')
            print('Condition at line 569')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1237')
            print('Condition at line 1067')
            print('Condition at line 898')
            print('Condition at line 731')
            print('Condition at line 572')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1244')
            print('Condition at line 1073')
            print('Condition at line 903')
            print('Condition at line 735')
            print('Condition at line 575')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 1251')
            print('Condition at line 1079')
            print('Condition at line 908')
            print('Condition at line 739')
            print('Condition at line 578')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1258')
            print('Condition at line 1085')
            print('Condition at line 913')
            print('Condition at line 743')
            print('Condition at line 581')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1265')
            print('Condition at line 1091')
            print('Condition at line 918')
            print('Condition at line 747')
            print('Condition at line 584')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1272')
            print('Condition at line 1097')
            print('Condition at line 923')
            print('Condition at line 751')
            print('Condition at line 587')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 1278')
            print('Condition at line 1102')
            print('Condition at line 927')
            print('Condition at line 754')
            print('Condition at line 589')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1284')
            print('Condition at line 1107')
            print('Condition at line 931')
            print('Condition at line 757')
            print('Condition at line 591')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1290')
            print('Condition at line 1112')
            print('Condition at line 935')
            print('Condition at line 760')
            print('Condition at line 593')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1296')
            print('Condition at line 1117')
            print('Condition at line 939')
            print('Condition at line 763')
            print('Condition at line 595')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 1302')
            print('Condition at line 1122')
            print('Condition at line 943')
            print('Condition at line 766')
            print('Condition at line 597')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1308')
            print('Condition at line 1127')
            print('Condition at line 947')
            print('Condition at line 769')
            print('Condition at line 599')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1314')
            print('Condition at line 1132')
            print('Condition at line 951')
            print('Condition at line 772')
            print('Condition at line 601')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 1321')
            print('Condition at line 1138')
            print('Condition at line 956')
            print('Condition at line 776')
            print('Condition at line 604')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1328')
            print('Condition at line 1144')
            print('Condition at line 961')
            print('Condition at line 780')
            print('Condition at line 607')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1335')
            print('Condition at line 1150')
            print('Condition at line 966')
            print('Condition at line 784')
            print('Condition at line 610')
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 1342')
            print('Condition at line 1156')
            print('Condition at line 971')
            print('Condition at line 788')
            print('Condition at line 613')
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1349')
            print('Condition at line 1162')
            print('Condition at line 976')
            print('Condition at line 792')
            print('Condition at line 616')
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1356')
            print('Condition at line 1168')
            print('Condition at line 981')
            print('Condition at line 796')
            print('Condition at line 619')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 1362')
            print('Condition at line 1173')
            print('Condition at line 985')
            print('Condition at line 799')
            print('Condition at line 621')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1368')
            print('Condition at line 1178')
            print('Condition at line 989')
            print('Condition at line 802')
            print('Condition at line 623')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1374')
            print('Condition at line 1183')
            print('Condition at line 993')
            print('Condition at line 805')
            print('Condition at line 625')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 1381')
            print('Condition at line 1189')
            print('Condition at line 998')
            print('Condition at line 809')
            print('Condition at line 628')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1388')
            print('Condition at line 1195')
            print('Condition at line 1003')
            print('Condition at line 813')
            print('Condition at line 631')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1395')
            print('Condition at line 1201')
            print('Condition at line 1008')
            print('Condition at line 817')
            print('Condition at line 634')
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 1402')
            print('Condition at line 1207')
            print('Condition at line 1013')
            print('Condition at line 821')
            print('Condition at line 637')
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1409')
            print('Condition at line 1213')
            print('Condition at line 1018')
            print('Condition at line 825')
            print('Condition at line 640')
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1416')
            print('Condition at line 1219')
            print('Condition at line 1023')
            print('Condition at line 829')
            print('Condition at line 643')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 1422')
            print('Condition at line 1224')
            print('Condition at line 1027')
            print('Condition at line 832')
            print('Condition at line 645')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1428')
            print('Condition at line 1229')
            print('Condition at line 1031')
            print('Condition at line 835')
            print('Condition at line 647')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1434')
            print('Condition at line 1234')
            print('Condition at line 1035')
            print('Condition at line 838')
            print('Condition at line 649')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1440')
            print('Condition at line 1239')
            print('Condition at line 1039')
            print('Condition at line 841')
            print('Condition at line 651')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1446')
            print('Condition at line 1244')
            print('Condition at line 1043')
            print('Condition at line 844')
            print('Condition at line 653')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1452')
            print('Condition at line 1249')
            print('Condition at line 1047')
            print('Condition at line 847')
            print('Condition at line 655')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1458')
            print('Condition at line 1254')
            print('Condition at line 1051')
            print('Condition at line 850')
            print('Condition at line 657')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            print('Condition at line 1464')
            print('Condition at line 1259')
            print('Condition at line 1055')
            print('Condition at line 853')
            print('Condition at line 659')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1470')
            print('Condition at line 1264')
            print('Condition at line 1059')
            print('Condition at line 856')
            print('Condition at line 661')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1476')
            print('Condition at line 1269')
            print('Condition at line 1063')
            print('Condition at line 859')
            print('Condition at line 663')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1482')
            print('Condition at line 1274')
            print('Condition at line 1067')
            print('Condition at line 862')
            print('Condition at line 665')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1488')
            print('Condition at line 1279')
            print('Condition at line 1071')
            print('Condition at line 865')
            print('Condition at line 667')
            currentState = 20
    elif currentState == 5:
        print('Condition at line 1494')
        print('Condition at line 1284')
        print('Condition at line 1075')
        print('Condition at line 868')
        print('Condition at line 669')
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y):
            print('Condition at line 1499')
            print('Condition at line 1288')
            print('Condition at line 1078')
            print('Condition at line 870')
            print('Condition at line 670')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 8
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1509')
            print('Condition at line 1297')
            print('Condition at line 1086')
            print('Condition at line 877')
            print('Condition at line 676')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1518')
            print('Condition at line 1305')
            print('Condition at line 1093')
            print('Condition at line 883')
            print('Condition at line 681')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1527')
            print('Condition at line 1313')
            print('Condition at line 1100')
            print('Condition at line 889')
            print('Condition at line 686')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1536')
            print('Condition at line 1321')
            print('Condition at line 1107')
            print('Condition at line 895')
            print('Condition at line 691')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 9
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1545')
            print('Condition at line 1329')
            print('Condition at line 1114')
            print('Condition at line 901')
            print('Condition at line 696')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1552')
            print('Condition at line 1335')
            print('Condition at line 1119')
            print('Condition at line 905')
            print('Condition at line 699')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1559')
            print('Condition at line 1341')
            print('Condition at line 1124')
            print('Condition at line 909')
            print('Condition at line 702')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1566')
            print('Condition at line 1347')
            print('Condition at line 1129')
            print('Condition at line 913')
            print('Condition at line 705')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1572')
            print('Condition at line 1352')
            print('Condition at line 1133')
            print('Condition at line 916')
            print('Condition at line 707')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1578')
            print('Condition at line 1357')
            print('Condition at line 1137')
            print('Condition at line 919')
            print('Condition at line 709')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1584')
            print('Condition at line 1362')
            print('Condition at line 1141')
            print('Condition at line 922')
            print('Condition at line 711')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1590')
            print('Condition at line 1367')
            print('Condition at line 1145')
            print('Condition at line 925')
            print('Condition at line 713')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1596')
            print('Condition at line 1372')
            print('Condition at line 1149')
            print('Condition at line 928')
            print('Condition at line 715')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x:
            print('Condition at line 1602')
            print('Condition at line 1377')
            print('Condition at line 1153')
            print('Condition at line 931')
            print('Condition at line 717')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x:
            print('Condition at line 1608')
            print('Condition at line 1382')
            print('Condition at line 1157')
            print('Condition at line 934')
            print('Condition at line 719')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1614')
            print('Condition at line 1387')
            print('Condition at line 1161')
            print('Condition at line 937')
            print('Condition at line 721')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1620')
            print('Condition at line 1392')
            print('Condition at line 1165')
            print('Condition at line 940')
            print('Condition at line 723')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1626')
            print('Condition at line 1397')
            print('Condition at line 1169')
            print('Condition at line 943')
            print('Condition at line 725')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1632')
            print('Condition at line 1402')
            print('Condition at line 1173')
            print('Condition at line 946')
            print('Condition at line 727')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 1638')
            print('Condition at line 1407')
            print('Condition at line 1177')
            print('Condition at line 949')
            print('Condition at line 729')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x:
            print('Condition at line 1644')
            print('Condition at line 1412')
            print('Condition at line 1181')
            print('Condition at line 952')
            print('Condition at line 731')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1650')
            print('Condition at line 1417')
            print('Condition at line 1185')
            print('Condition at line 955')
            print('Condition at line 733')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1656')
            print('Condition at line 1422')
            print('Condition at line 1189')
            print('Condition at line 958')
            print('Condition at line 735')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1662')
            print('Condition at line 1427')
            print('Condition at line 1193')
            print('Condition at line 961')
            print('Condition at line 737')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1668')
            print('Condition at line 1432')
            print('Condition at line 1197')
            print('Condition at line 964')
            print('Condition at line 739')
            currentState = 20
    elif currentState == 6:
        print('Condition at line 1674')
        print('Condition at line 1437')
        print('Condition at line 1201')
        print('Condition at line 967')
        print('Condition at line 741')
        if (Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and
            Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y):
            print('Condition at line 1679')
            print('Condition at line 1441')
            print('Condition at line 1204')
            print('Condition at line 969')
            print('Condition at line 742')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1686')
            print('Condition at line 1447')
            print('Condition at line 1209')
            print('Condition at line 973')
            print('Condition at line 745')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1692')
            print('Condition at line 1452')
            print('Condition at line 1213')
            print('Condition at line 976')
            print('Condition at line 747')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1698')
            print('Condition at line 1457')
            print('Condition at line 1217')
            print('Condition at line 979')
            print('Condition at line 749')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1704')
            print('Condition at line 1462')
            print('Condition at line 1221')
            print('Condition at line 982')
            print('Condition at line 751')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1710')
            print('Condition at line 1467')
            print('Condition at line 1225')
            print('Condition at line 985')
            print('Condition at line 753')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1716')
            print('Condition at line 1472')
            print('Condition at line 1229')
            print('Condition at line 988')
            print('Condition at line 755')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1722')
            print('Condition at line 1477')
            print('Condition at line 1233')
            print('Condition at line 991')
            print('Condition at line 757')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1728')
            print('Condition at line 1482')
            print('Condition at line 1237')
            print('Condition at line 994')
            print('Condition at line 759')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1734')
            print('Condition at line 1487')
            print('Condition at line 1241')
            print('Condition at line 997')
            print('Condition at line 761')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1740')
            print('Condition at line 1492')
            print('Condition at line 1245')
            print('Condition at line 1000')
            print('Condition at line 763')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1746')
            print('Condition at line 1497')
            print('Condition at line 1249')
            print('Condition at line 1003')
            print('Condition at line 765')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1752')
            print('Condition at line 1502')
            print('Condition at line 1253')
            print('Condition at line 1006')
            print('Condition at line 767')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1758')
            print('Condition at line 1507')
            print('Condition at line 1257')
            print('Condition at line 1009')
            print('Condition at line 769')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1764')
            print('Condition at line 1512')
            print('Condition at line 1261')
            print('Condition at line 1012')
            print('Condition at line 771')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1770')
            print('Condition at line 1517')
            print('Condition at line 1265')
            print('Condition at line 1015')
            print('Condition at line 773')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1776')
            print('Condition at line 1522')
            print('Condition at line 1269')
            print('Condition at line 1018')
            print('Condition at line 775')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1782')
            print('Condition at line 1527')
            print('Condition at line 1273')
            print('Condition at line 1021')
            print('Condition at line 777')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1788')
            print('Condition at line 1532')
            print('Condition at line 1277')
            print('Condition at line 1024')
            print('Condition at line 779')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1794')
            print('Condition at line 1537')
            print('Condition at line 1281')
            print('Condition at line 1027')
            print('Condition at line 781')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1800')
            print('Condition at line 1542')
            print('Condition at line 1285')
            print('Condition at line 1030')
            print('Condition at line 783')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1806')
            print('Condition at line 1547')
            print('Condition at line 1289')
            print('Condition at line 1033')
            print('Condition at line 785')
            currentState = 20
        elif Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 1812')
            print('Condition at line 1552')
            print('Condition at line 1293')
            print('Condition at line 1036')
            print('Condition at line 787')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1818')
            print('Condition at line 1557')
            print('Condition at line 1297')
            print('Condition at line 1039')
            print('Condition at line 789')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y >= Robber.y:
            print('Condition at line 1824')
            print('Condition at line 1562')
            print('Condition at line 1301')
            print('Condition at line 1042')
            print('Condition at line 791')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y >= Robber.y:
            print('Condition at line 1830')
            print('Condition at line 1567')
            print('Condition at line 1305')
            print('Condition at line 1045')
            print('Condition at line 793')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y:
            print('Condition at line 1836')
            print('Condition at line 1572')
            print('Condition at line 1309')
            print('Condition at line 1048')
            print('Condition at line 795')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y:
            print('Condition at line 1842')
            print('Condition at line 1577')
            print('Condition at line 1313')
            print('Condition at line 1051')
            print('Condition at line 797')
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1848')
            print('Condition at line 1582')
            print('Condition at line 1317')
            print('Condition at line 1054')
            print('Condition at line 799')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1854')
            print('Condition at line 1587')
            print('Condition at line 1321')
            print('Condition at line 1057')
            print('Condition at line 801')
            currentState = 20
    elif currentState == 7:
        print('Condition at line 1860')
        print('Condition at line 1592')
        print('Condition at line 1325')
        print('Condition at line 1060')
        print('Condition at line 803')
        if (Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            print('Condition at line 1865')
            print('Condition at line 1596')
            print('Condition at line 1328')
            print('Condition at line 1062')
            print('Condition at line 804')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1872')
            print('Condition at line 1602')
            print('Condition at line 1333')
            print('Condition at line 1066')
            print('Condition at line 807')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1878')
            print('Condition at line 1607')
            print('Condition at line 1337')
            print('Condition at line 1069')
            print('Condition at line 809')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1884')
            print('Condition at line 1612')
            print('Condition at line 1341')
            print('Condition at line 1072')
            print('Condition at line 811')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1890')
            print('Condition at line 1617')
            print('Condition at line 1345')
            print('Condition at line 1075')
            print('Condition at line 813')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1896')
            print('Condition at line 1622')
            print('Condition at line 1349')
            print('Condition at line 1078')
            print('Condition at line 815')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1902')
            print('Condition at line 1627')
            print('Condition at line 1353')
            print('Condition at line 1081')
            print('Condition at line 817')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1908')
            print('Condition at line 1632')
            print('Condition at line 1357')
            print('Condition at line 1084')
            print('Condition at line 819')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1914')
            print('Condition at line 1637')
            print('Condition at line 1361')
            print('Condition at line 1087')
            print('Condition at line 821')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1920')
            print('Condition at line 1642')
            print('Condition at line 1365')
            print('Condition at line 1090')
            print('Condition at line 823')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1926')
            print('Condition at line 1647')
            print('Condition at line 1369')
            print('Condition at line 1093')
            print('Condition at line 825')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1932')
            print('Condition at line 1652')
            print('Condition at line 1373')
            print('Condition at line 1096')
            print('Condition at line 827')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1938')
            print('Condition at line 1657')
            print('Condition at line 1377')
            print('Condition at line 1099')
            print('Condition at line 829')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1944')
            print('Condition at line 1662')
            print('Condition at line 1381')
            print('Condition at line 1102')
            print('Condition at line 831')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1950')
            print('Condition at line 1667')
            print('Condition at line 1385')
            print('Condition at line 1105')
            print('Condition at line 833')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 1956')
            print('Condition at line 1672')
            print('Condition at line 1389')
            print('Condition at line 1108')
            print('Condition at line 835')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1962')
            print('Condition at line 1677')
            print('Condition at line 1393')
            print('Condition at line 1111')
            print('Condition at line 837')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1968')
            print('Condition at line 1682')
            print('Condition at line 1397')
            print('Condition at line 1114')
            print('Condition at line 839')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x:
            print('Condition at line 1974')
            print('Condition at line 1687')
            print('Condition at line 1401')
            print('Condition at line 1117')
            print('Condition at line 841')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x:
            print('Condition at line 1980')
            print('Condition at line 1692')
            print('Condition at line 1405')
            print('Condition at line 1120')
            print('Condition at line 843')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 1986')
            print('Condition at line 1697')
            print('Condition at line 1409')
            print('Condition at line 1123')
            print('Condition at line 845')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 1992')
            print('Condition at line 1702')
            print('Condition at line 1413')
            print('Condition at line 1126')
            print('Condition at line 847')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 1998')
            print('Condition at line 1707')
            print('Condition at line 1417')
            print('Condition at line 1129')
            print('Condition at line 849')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 2004')
            print('Condition at line 1712')
            print('Condition at line 1421')
            print('Condition at line 1132')
            print('Condition at line 851')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 2010')
            print('Condition at line 1717')
            print('Condition at line 1425')
            print('Condition at line 1135')
            print('Condition at line 853')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x:
            print('Condition at line 2016')
            print('Condition at line 1722')
            print('Condition at line 1429')
            print('Condition at line 1138')
            print('Condition at line 855')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2022')
            print('Condition at line 1727')
            print('Condition at line 1433')
            print('Condition at line 1141')
            print('Condition at line 857')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 2028')
            print('Condition at line 1732')
            print('Condition at line 1437')
            print('Condition at line 1144')
            print('Condition at line 859')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 2034')
            print('Condition at line 1737')
            print('Condition at line 1441')
            print('Condition at line 1147')
            print('Condition at line 861')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 2040')
            print('Condition at line 1742')
            print('Condition at line 1445')
            print('Condition at line 1150')
            print('Condition at line 863')
            currentState = 20
    elif currentState == 8:
        print('Condition at line 2046')
        print('Condition at line 1747')
        print('Condition at line 1449')
        print('Condition at line 1153')
        print('Condition at line 865')
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            print('Condition at line 2051')
            print('Condition at line 1751')
            print('Condition at line 1452')
            print('Condition at line 1155')
            print('Condition at line 866')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 6
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2060')
            print('Condition at line 1759')
            print('Condition at line 1459')
            print('Condition at line 1161')
            print('Condition at line 871')
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2067')
            print('Condition at line 1765')
            print('Condition at line 1464')
            print('Condition at line 1165')
            print('Condition at line 874')
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2074')
            print('Condition at line 1771')
            print('Condition at line 1469')
            print('Condition at line 1169')
            print('Condition at line 877')
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2081')
            print('Condition at line 1777')
            print('Condition at line 1474')
            print('Condition at line 1173')
            print('Condition at line 880')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2088')
            print('Condition at line 1783')
            print('Condition at line 1479')
            print('Condition at line 1177')
            print('Condition at line 883')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2095')
            print('Condition at line 1789')
            print('Condition at line 1484')
            print('Condition at line 1181')
            print('Condition at line 886')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2102')
            print('Condition at line 1795')
            print('Condition at line 1489')
            print('Condition at line 1185')
            print('Condition at line 889')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2109')
            print('Condition at line 1801')
            print('Condition at line 1494')
            print('Condition at line 1189')
            print('Condition at line 892')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2116')
            print('Condition at line 1807')
            print('Condition at line 1499')
            print('Condition at line 1193')
            print('Condition at line 895')
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 19
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2124')
            print('Condition at line 1814')
            print('Condition at line 1505')
            print('Condition at line 1198')
            print('Condition at line 899')
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 19
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2132')
            print('Condition at line 1821')
            print('Condition at line 1511')
            print('Condition at line 1203')
            print('Condition at line 903')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2138')
            print('Condition at line 1826')
            print('Condition at line 1515')
            print('Condition at line 1206')
            print('Condition at line 905')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2144')
            print('Condition at line 1831')
            print('Condition at line 1519')
            print('Condition at line 1209')
            print('Condition at line 907')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2150')
            print('Condition at line 1836')
            print('Condition at line 1523')
            print('Condition at line 1212')
            print('Condition at line 909')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2156')
            print('Condition at line 1841')
            print('Condition at line 1527')
            print('Condition at line 1215')
            print('Condition at line 911')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2162')
            print('Condition at line 1846')
            print('Condition at line 1531')
            print('Condition at line 1218')
            print('Condition at line 913')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2168')
            print('Condition at line 1851')
            print('Condition at line 1535')
            print('Condition at line 1221')
            print('Condition at line 915')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2174')
            print('Condition at line 1856')
            print('Condition at line 1539')
            print('Condition at line 1224')
            print('Condition at line 917')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y:
            print('Condition at line 2180')
            print('Condition at line 1861')
            print('Condition at line 1543')
            print('Condition at line 1227')
            print('Condition at line 919')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2186')
            print('Condition at line 1866')
            print('Condition at line 1547')
            print('Condition at line 1230')
            print('Condition at line 921')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 2192')
            print('Condition at line 1871')
            print('Condition at line 1551')
            print('Condition at line 1233')
            print('Condition at line 923')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y:
            print('Condition at line 2198')
            print('Condition at line 1876')
            print('Condition at line 1555')
            print('Condition at line 1236')
            print('Condition at line 925')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            print('Condition at line 2204')
            print('Condition at line 1881')
            print('Condition at line 1559')
            print('Condition at line 1239')
            print('Condition at line 927')
            currentState = 20
        elif Cop.x > Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 2210')
            print('Condition at line 1886')
            print('Condition at line 1563')
            print('Condition at line 1242')
            print('Condition at line 929')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            print('Condition at line 2216')
            print('Condition at line 1891')
            print('Condition at line 1567')
            print('Condition at line 1245')
            print('Condition at line 931')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2222')
            print('Condition at line 1896')
            print('Condition at line 1571')
            print('Condition at line 1248')
            print('Condition at line 933')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 2228')
            print('Condition at line 1901')
            print('Condition at line 1575')
            print('Condition at line 1251')
            print('Condition at line 935')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2234')
            print('Condition at line 1906')
            print('Condition at line 1579')
            print('Condition at line 1254')
            print('Condition at line 937')
            currentState = 20
        elif Cop.x > Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2240')
            print('Condition at line 1911')
            print('Condition at line 1583')
            print('Condition at line 1257')
            print('Condition at line 939')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2246')
            print('Condition at line 1916')
            print('Condition at line 1587')
            print('Condition at line 1260')
            print('Condition at line 941')
            currentState = 20
        elif Cop.x > Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2252')
            print('Condition at line 1921')
            print('Condition at line 1591')
            print('Condition at line 1263')
            print('Condition at line 943')
            currentState = 20
    elif currentState == 9:
        print('Condition at line 2258')
        print('Condition at line 1926')
        print('Condition at line 1595')
        print('Condition at line 1266')
        print('Condition at line 945')
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            print('Condition at line 2263')
            print('Condition at line 1930')
            print('Condition at line 1598')
            print('Condition at line 1268')
            print('Condition at line 946')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 6
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2272')
            print('Condition at line 1938')
            print('Condition at line 1605')
            print('Condition at line 1274')
            print('Condition at line 951')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 2279')
            print('Condition at line 1944')
            print('Condition at line 1610')
            print('Condition at line 1278')
            print('Condition at line 954')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 2286')
            print('Condition at line 1950')
            print('Condition at line 1615')
            print('Condition at line 1282')
            print('Condition at line 957')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 2293')
            print('Condition at line 1956')
            print('Condition at line 1620')
            print('Condition at line 1286')
            print('Condition at line 960')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2300')
            print('Condition at line 1962')
            print('Condition at line 1625')
            print('Condition at line 1290')
            print('Condition at line 963')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2307')
            print('Condition at line 1968')
            print('Condition at line 1630')
            print('Condition at line 1294')
            print('Condition at line 966')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2314')
            print('Condition at line 1974')
            print('Condition at line 1635')
            print('Condition at line 1298')
            print('Condition at line 969')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2320')
            print('Condition at line 1979')
            print('Condition at line 1639')
            print('Condition at line 1301')
            print('Condition at line 971')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2326')
            print('Condition at line 1984')
            print('Condition at line 1643')
            print('Condition at line 1304')
            print('Condition at line 973')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2332')
            print('Condition at line 1989')
            print('Condition at line 1647')
            print('Condition at line 1307')
            print('Condition at line 975')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2338')
            print('Condition at line 1994')
            print('Condition at line 1651')
            print('Condition at line 1310')
            print('Condition at line 977')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2344')
            print('Condition at line 1999')
            print('Condition at line 1655')
            print('Condition at line 1313')
            print('Condition at line 979')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2350')
            print('Condition at line 2004')
            print('Condition at line 1659')
            print('Condition at line 1316')
            print('Condition at line 981')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2356')
            print('Condition at line 2009')
            print('Condition at line 1663')
            print('Condition at line 1319')
            print('Condition at line 983')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2362')
            print('Condition at line 2014')
            print('Condition at line 1667')
            print('Condition at line 1322')
            print('Condition at line 985')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2368')
            print('Condition at line 2019')
            print('Condition at line 1671')
            print('Condition at line 1325')
            print('Condition at line 987')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2374')
            print('Condition at line 2024')
            print('Condition at line 1675')
            print('Condition at line 1328')
            print('Condition at line 989')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2380')
            print('Condition at line 2029')
            print('Condition at line 1679')
            print('Condition at line 1331')
            print('Condition at line 991')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 2386')
            print('Condition at line 2034')
            print('Condition at line 1683')
            print('Condition at line 1334')
            print('Condition at line 993')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2392')
            print('Condition at line 2039')
            print('Condition at line 1687')
            print('Condition at line 1337')
            print('Condition at line 995')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 2398')
            print('Condition at line 2044')
            print('Condition at line 1691')
            print('Condition at line 1340')
            print('Condition at line 997')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 2404')
            print('Condition at line 2049')
            print('Condition at line 1695')
            print('Condition at line 1343')
            print('Condition at line 999')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 2410')
            print('Condition at line 2054')
            print('Condition at line 1699')
            print('Condition at line 1346')
            print('Condition at line 1001')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x:
            print('Condition at line 2416')
            print('Condition at line 2059')
            print('Condition at line 1703')
            print('Condition at line 1349')
            print('Condition at line 1003')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x:
            print('Condition at line 2422')
            print('Condition at line 2064')
            print('Condition at line 1707')
            print('Condition at line 1352')
            print('Condition at line 1005')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x:
            print('Condition at line 2428')
            print('Condition at line 2069')
            print('Condition at line 1711')
            print('Condition at line 1355')
            print('Condition at line 1007')
            currentState = 20
    elif currentState == 10:
        print('Condition at line 2434')
        print('Condition at line 2074')
        print('Condition at line 1715')
        print('Condition at line 1358')
        print('Condition at line 1009')
        if (Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            print('Condition at line 2439')
            print('Condition at line 2078')
            print('Condition at line 1718')
            print('Condition at line 1360')
            print('Condition at line 1010')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2448')
            print('Condition at line 2086')
            print('Condition at line 1725')
            print('Condition at line 1366')
            print('Condition at line 1015')
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y < Robber.y:
            print('Condition at line 2456')
            print('Condition at line 2093')
            print('Condition at line 1731')
            print('Condition at line 1371')
            print('Condition at line 1019')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2463')
            print('Condition at line 2099')
            print('Condition at line 1736')
            print('Condition at line 1375')
            print('Condition at line 1022')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2470')
            print('Condition at line 2105')
            print('Condition at line 1741')
            print('Condition at line 1379')
            print('Condition at line 1025')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2477')
            print('Condition at line 2111')
            print('Condition at line 1746')
            print('Condition at line 1383')
            print('Condition at line 1028')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2484')
            print('Condition at line 2117')
            print('Condition at line 1751')
            print('Condition at line 1387')
            print('Condition at line 1031')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y < Robber.y:
            print('Condition at line 2491')
            print('Condition at line 2123')
            print('Condition at line 1756')
            print('Condition at line 1391')
            print('Condition at line 1034')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2498')
            print('Condition at line 2129')
            print('Condition at line 1761')
            print('Condition at line 1395')
            print('Condition at line 1037')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2505')
            print('Condition at line 2135')
            print('Condition at line 1766')
            print('Condition at line 1399')
            print('Condition at line 1040')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 2512')
            print('Condition at line 2141')
            print('Condition at line 1771')
            print('Condition at line 1403')
            print('Condition at line 1043')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 2519')
            print('Condition at line 2147')
            print('Condition at line 1776')
            print('Condition at line 1407')
            print('Condition at line 1046')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2526')
            print('Condition at line 2153')
            print('Condition at line 1781')
            print('Condition at line 1411')
            print('Condition at line 1049')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2533')
            print('Condition at line 2159')
            print('Condition at line 1786')
            print('Condition at line 1415')
            print('Condition at line 1052')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2539')
            print('Condition at line 2164')
            print('Condition at line 1790')
            print('Condition at line 1418')
            print('Condition at line 1054')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2545')
            print('Condition at line 2169')
            print('Condition at line 1794')
            print('Condition at line 1421')
            print('Condition at line 1056')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2551')
            print('Condition at line 2174')
            print('Condition at line 1798')
            print('Condition at line 1424')
            print('Condition at line 1058')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2557')
            print('Condition at line 2179')
            print('Condition at line 1802')
            print('Condition at line 1427')
            print('Condition at line 1060')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2563')
            print('Condition at line 2184')
            print('Condition at line 1806')
            print('Condition at line 1430')
            print('Condition at line 1062')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2569')
            print('Condition at line 2189')
            print('Condition at line 1810')
            print('Condition at line 1433')
            print('Condition at line 1064')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2575')
            print('Condition at line 2194')
            print('Condition at line 1814')
            print('Condition at line 1436')
            print('Condition at line 1066')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2581')
            print('Condition at line 2199')
            print('Condition at line 1818')
            print('Condition at line 1439')
            print('Condition at line 1068')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 2587')
            print('Condition at line 2204')
            print('Condition at line 1822')
            print('Condition at line 1442')
            print('Condition at line 1070')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2593')
            print('Condition at line 2209')
            print('Condition at line 1826')
            print('Condition at line 1445')
            print('Condition at line 1072')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y < Robber.y:
            print('Condition at line 2599')
            print('Condition at line 2214')
            print('Condition at line 1830')
            print('Condition at line 1448')
            print('Condition at line 1074')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2605')
            print('Condition at line 2219')
            print('Condition at line 1834')
            print('Condition at line 1451')
            print('Condition at line 1076')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y >= Robber.y:
            print('Condition at line 2611')
            print('Condition at line 2224')
            print('Condition at line 1838')
            print('Condition at line 1454')
            print('Condition at line 1078')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2617')
            print('Condition at line 2229')
            print('Condition at line 1842')
            print('Condition at line 1457')
            print('Condition at line 1080')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 2623')
            print('Condition at line 2234')
            print('Condition at line 1846')
            print('Condition at line 1460')
            print('Condition at line 1082')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 2629')
            print('Condition at line 2239')
            print('Condition at line 1850')
            print('Condition at line 1463')
            print('Condition at line 1084')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y:
            print('Condition at line 2635')
            print('Condition at line 2244')
            print('Condition at line 1854')
            print('Condition at line 1466')
            print('Condition at line 1086')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2641')
            print('Condition at line 2249')
            print('Condition at line 1858')
            print('Condition at line 1469')
            print('Condition at line 1088')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2649')
            print('Condition at line 2256')
            print('Condition at line 1864')
            print('Condition at line 1474')
            print('Condition at line 1092')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 2657')
            print('Condition at line 2263')
            print('Condition at line 1870')
            print('Condition at line 1479')
            print('Condition at line 1096')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y:
            print('Condition at line 2663')
            print('Condition at line 2268')
            print('Condition at line 1874')
            print('Condition at line 1482')
            print('Condition at line 1098')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 2669')
            print('Condition at line 2273')
            print('Condition at line 1878')
            print('Condition at line 1485')
            print('Condition at line 1100')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y >= Robber.y:
            print('Condition at line 2675')
            print('Condition at line 2278')
            print('Condition at line 1882')
            print('Condition at line 1488')
            print('Condition at line 1102')
            currentState = 20
    elif currentState == 11:
        print('Condition at line 2681')
        print('Condition at line 2283')
        print('Condition at line 1886')
        print('Condition at line 1491')
        print('Condition at line 1104')
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            print('Condition at line 2686')
            print('Condition at line 2287')
            print('Condition at line 1889')
            print('Condition at line 1493')
            print('Condition at line 1105')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2694')
            print('Condition at line 2294')
            print('Condition at line 1895')
            print('Condition at line 1498')
            print('Condition at line 1109')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2701')
            print('Condition at line 2300')
            print('Condition at line 1900')
            print('Condition at line 1502')
            print('Condition at line 1112')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 2708')
            print('Condition at line 2306')
            print('Condition at line 1905')
            print('Condition at line 1506')
            print('Condition at line 1115')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2715')
            print('Condition at line 2312')
            print('Condition at line 1910')
            print('Condition at line 1510')
            print('Condition at line 1118')
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2722')
            print('Condition at line 2318')
            print('Condition at line 1915')
            print('Condition at line 1514')
            print('Condition at line 1121')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2728')
            print('Condition at line 2323')
            print('Condition at line 1919')
            print('Condition at line 1517')
            print('Condition at line 1123')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2734')
            print('Condition at line 2328')
            print('Condition at line 1923')
            print('Condition at line 1520')
            print('Condition at line 1125')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2740')
            print('Condition at line 2333')
            print('Condition at line 1927')
            print('Condition at line 1523')
            print('Condition at line 1127')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2746')
            print('Condition at line 2338')
            print('Condition at line 1931')
            print('Condition at line 1526')
            print('Condition at line 1129')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2752')
            print('Condition at line 2343')
            print('Condition at line 1935')
            print('Condition at line 1529')
            print('Condition at line 1131')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2758')
            print('Condition at line 2348')
            print('Condition at line 1939')
            print('Condition at line 1532')
            print('Condition at line 1133')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2764')
            print('Condition at line 2353')
            print('Condition at line 1943')
            print('Condition at line 1535')
            print('Condition at line 1135')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y:
            print('Condition at line 2770')
            print('Condition at line 2358')
            print('Condition at line 1947')
            print('Condition at line 1538')
            print('Condition at line 1137')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2776')
            print('Condition at line 2363')
            print('Condition at line 1951')
            print('Condition at line 1541')
            print('Condition at line 1139')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 2782')
            print('Condition at line 2368')
            print('Condition at line 1955')
            print('Condition at line 1544')
            print('Condition at line 1141')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 2788')
            print('Condition at line 2373')
            print('Condition at line 1959')
            print('Condition at line 1547')
            print('Condition at line 1143')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            print('Condition at line 2794')
            print('Condition at line 2378')
            print('Condition at line 1963')
            print('Condition at line 1550')
            print('Condition at line 1145')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            print('Condition at line 2800')
            print('Condition at line 2383')
            print('Condition at line 1967')
            print('Condition at line 1553')
            print('Condition at line 1147')
            currentState = 20
        elif Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 2806')
            print('Condition at line 2388')
            print('Condition at line 1971')
            print('Condition at line 1556')
            print('Condition at line 1149')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2812')
            print('Condition at line 2393')
            print('Condition at line 1975')
            print('Condition at line 1559')
            print('Condition at line 1151')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2818')
            print('Condition at line 2398')
            print('Condition at line 1979')
            print('Condition at line 1562')
            print('Condition at line 1153')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2824')
            print('Condition at line 2403')
            print('Condition at line 1983')
            print('Condition at line 1565')
            print('Condition at line 1155')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2830')
            print('Condition at line 2408')
            print('Condition at line 1987')
            print('Condition at line 1568')
            print('Condition at line 1157')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 2836')
            print('Condition at line 2413')
            print('Condition at line 1991')
            print('Condition at line 1571')
            print('Condition at line 1159')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2842')
            print('Condition at line 2418')
            print('Condition at line 1995')
            print('Condition at line 1574')
            print('Condition at line 1161')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 2848')
            print('Condition at line 2423')
            print('Condition at line 1999')
            print('Condition at line 1577')
            print('Condition at line 1163')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 2854')
            print('Condition at line 2428')
            print('Condition at line 2003')
            print('Condition at line 1580')
            print('Condition at line 1165')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y:
            print('Condition at line 2860')
            print('Condition at line 2433')
            print('Condition at line 2007')
            print('Condition at line 1583')
            print('Condition at line 1167')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2866')
            print('Condition at line 2438')
            print('Condition at line 2011')
            print('Condition at line 1586')
            print('Condition at line 1169')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 2872')
            print('Condition at line 2443')
            print('Condition at line 2015')
            print('Condition at line 1589')
            print('Condition at line 1171')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 2878')
            print('Condition at line 2448')
            print('Condition at line 2019')
            print('Condition at line 1592')
            print('Condition at line 1173')
            currentState = 20
    elif currentState == 12:
        print('Condition at line 2884')
        print('Condition at line 2453')
        print('Condition at line 2023')
        print('Condition at line 1595')
        print('Condition at line 1175')
        if (Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and
            Cop.y == Robber.y and Cop.y <= Robber.y):
            print('Condition at line 2889')
            print('Condition at line 2457')
            print('Condition at line 2026')
            print('Condition at line 1597')
            print('Condition at line 1176')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 2897')
            print('Condition at line 2464')
            print('Condition at line 2032')
            print('Condition at line 1602')
            print('Condition at line 1180')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2904')
            print('Condition at line 2470')
            print('Condition at line 2037')
            print('Condition at line 1606')
            print('Condition at line 1183')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2910')
            print('Condition at line 2475')
            print('Condition at line 2041')
            print('Condition at line 1609')
            print('Condition at line 1185')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2916')
            print('Condition at line 2480')
            print('Condition at line 2045')
            print('Condition at line 1612')
            print('Condition at line 1187')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2922')
            print('Condition at line 2485')
            print('Condition at line 2049')
            print('Condition at line 1615')
            print('Condition at line 1189')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2928')
            print('Condition at line 2490')
            print('Condition at line 2053')
            print('Condition at line 1618')
            print('Condition at line 1191')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2934')
            print('Condition at line 2495')
            print('Condition at line 2057')
            print('Condition at line 1621')
            print('Condition at line 1193')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 2940')
            print('Condition at line 2500')
            print('Condition at line 2061')
            print('Condition at line 1624')
            print('Condition at line 1195')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2946')
            print('Condition at line 2505')
            print('Condition at line 2065')
            print('Condition at line 1627')
            print('Condition at line 1197')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            print('Condition at line 2952')
            print('Condition at line 2510')
            print('Condition at line 2069')
            print('Condition at line 1630')
            print('Condition at line 1199')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 2958')
            print('Condition at line 2515')
            print('Condition at line 2073')
            print('Condition at line 1633')
            print('Condition at line 1201')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y:
            print('Condition at line 2964')
            print('Condition at line 2520')
            print('Condition at line 2077')
            print('Condition at line 1636')
            print('Condition at line 1203')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 2970')
            print('Condition at line 2525')
            print('Condition at line 2081')
            print('Condition at line 1639')
            print('Condition at line 1205')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 2976')
            print('Condition at line 2530')
            print('Condition at line 2085')
            print('Condition at line 1642')
            print('Condition at line 1207')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 2982')
            print('Condition at line 2535')
            print('Condition at line 2089')
            print('Condition at line 1645')
            print('Condition at line 1209')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y:
            print('Condition at line 2988')
            print('Condition at line 2540')
            print('Condition at line 2093')
            print('Condition at line 1648')
            print('Condition at line 1211')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            print('Condition at line 2994')
            print('Condition at line 2545')
            print('Condition at line 2097')
            print('Condition at line 1651')
            print('Condition at line 1213')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y > Robber.y:
            print('Condition at line 3000')
            print('Condition at line 2550')
            print('Condition at line 2101')
            print('Condition at line 1654')
            print('Condition at line 1215')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3006')
            print('Condition at line 2555')
            print('Condition at line 2105')
            print('Condition at line 1657')
            print('Condition at line 1217')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 3012')
            print('Condition at line 2560')
            print('Condition at line 2109')
            print('Condition at line 1660')
            print('Condition at line 1219')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 3018')
            print('Condition at line 2565')
            print('Condition at line 2113')
            print('Condition at line 1663')
            print('Condition at line 1221')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3024')
            print('Condition at line 2570')
            print('Condition at line 2117')
            print('Condition at line 1666')
            print('Condition at line 1223')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3030')
            print('Condition at line 2575')
            print('Condition at line 2121')
            print('Condition at line 1669')
            print('Condition at line 1225')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3036')
            print('Condition at line 2580')
            print('Condition at line 2125')
            print('Condition at line 1672')
            print('Condition at line 1227')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3042')
            print('Condition at line 2585')
            print('Condition at line 2129')
            print('Condition at line 1675')
            print('Condition at line 1229')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3048')
            print('Condition at line 2590')
            print('Condition at line 2133')
            print('Condition at line 1678')
            print('Condition at line 1231')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3054')
            print('Condition at line 2595')
            print('Condition at line 2137')
            print('Condition at line 1681')
            print('Condition at line 1233')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3060')
            print('Condition at line 2600')
            print('Condition at line 2141')
            print('Condition at line 1684')
            print('Condition at line 1235')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3066')
            print('Condition at line 2605')
            print('Condition at line 2145')
            print('Condition at line 1687')
            print('Condition at line 1237')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 3072')
            print('Condition at line 2610')
            print('Condition at line 2149')
            print('Condition at line 1690')
            print('Condition at line 1239')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            print('Condition at line 3078')
            print('Condition at line 2615')
            print('Condition at line 2153')
            print('Condition at line 1693')
            print('Condition at line 1241')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3084')
            print('Condition at line 2620')
            print('Condition at line 2157')
            print('Condition at line 1696')
            print('Condition at line 1243')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3090')
            print('Condition at line 2625')
            print('Condition at line 2161')
            print('Condition at line 1699')
            print('Condition at line 1245')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3096')
            print('Condition at line 2630')
            print('Condition at line 2165')
            print('Condition at line 1702')
            print('Condition at line 1247')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3102')
            print('Condition at line 2635')
            print('Condition at line 2169')
            print('Condition at line 1705')
            print('Condition at line 1249')
            currentState = 20
    elif currentState == 13:
        print('Condition at line 3108')
        print('Condition at line 2640')
        print('Condition at line 2173')
        print('Condition at line 1708')
        print('Condition at line 1251')
        if Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 3113')
            print('Condition at line 2644')
            print('Condition at line 2176')
            print('Condition at line 1710')
            print('Condition at line 1252')
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3119')
            print('Condition at line 2649')
            print('Condition at line 2180')
            print('Condition at line 1713')
            print('Condition at line 1254')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 3125')
            print('Condition at line 2654')
            print('Condition at line 2184')
            print('Condition at line 1716')
            print('Condition at line 1256')
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3133')
            print('Condition at line 2661')
            print('Condition at line 2190')
            print('Condition at line 1721')
            print('Condition at line 1260')
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 3141')
            print('Condition at line 2668')
            print('Condition at line 2196')
            print('Condition at line 1726')
            print('Condition at line 1264')
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3149')
            print('Condition at line 2675')
            print('Condition at line 2202')
            print('Condition at line 1731')
            print('Condition at line 1268')
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 3157')
            print('Condition at line 2682')
            print('Condition at line 2208')
            print('Condition at line 1736')
            print('Condition at line 1272')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3165')
            print('Condition at line 2689')
            print('Condition at line 2214')
            print('Condition at line 1741')
            print('Condition at line 1276')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 3173')
            print('Condition at line 2696')
            print('Condition at line 2220')
            print('Condition at line 1746')
            print('Condition at line 1280')
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3179')
            print('Condition at line 2701')
            print('Condition at line 2224')
            print('Condition at line 1749')
            print('Condition at line 1282')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 3185')
            print('Condition at line 2706')
            print('Condition at line 2228')
            print('Condition at line 1752')
            print('Condition at line 1284')
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3193')
            print('Condition at line 2713')
            print('Condition at line 2234')
            print('Condition at line 1757')
            print('Condition at line 1288')
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 3201')
            print('Condition at line 2720')
            print('Condition at line 2240')
            print('Condition at line 1762')
            print('Condition at line 1292')
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3209')
            print('Condition at line 2727')
            print('Condition at line 2246')
            print('Condition at line 1767')
            print('Condition at line 1296')
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 3217')
            print('Condition at line 2734')
            print('Condition at line 2252')
            print('Condition at line 1772')
            print('Condition at line 1300')
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3225')
            print('Condition at line 2741')
            print('Condition at line 2258')
            print('Condition at line 1777')
            print('Condition at line 1304')
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y:
            print('Condition at line 3233')
            print('Condition at line 2748')
            print('Condition at line 2264')
            print('Condition at line 1782')
            print('Condition at line 1308')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 3239')
            print('Condition at line 2753')
            print('Condition at line 2268')
            print('Condition at line 1785')
            print('Condition at line 1310')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 3245')
            print('Condition at line 2758')
            print('Condition at line 2272')
            print('Condition at line 1788')
            print('Condition at line 1312')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 3251')
            print('Condition at line 2763')
            print('Condition at line 2276')
            print('Condition at line 1791')
            print('Condition at line 1314')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 3257')
            print('Condition at line 2768')
            print('Condition at line 2280')
            print('Condition at line 1794')
            print('Condition at line 1316')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            print('Condition at line 3263')
            print('Condition at line 2773')
            print('Condition at line 2284')
            print('Condition at line 1797')
            print('Condition at line 1318')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and Cop.y < Robber.y:
            print('Condition at line 3269')
            print('Condition at line 2778')
            print('Condition at line 2288')
            print('Condition at line 1800')
            print('Condition at line 1320')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            print('Condition at line 3275')
            print('Condition at line 2783')
            print('Condition at line 2292')
            print('Condition at line 1803')
            print('Condition at line 1322')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y < Robber.y:
            print('Condition at line 3281')
            print('Condition at line 2788')
            print('Condition at line 2296')
            print('Condition at line 1806')
            print('Condition at line 1324')
            currentState = 20
        elif Cop.x == Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 3287')
            print('Condition at line 2793')
            print('Condition at line 2300')
            print('Condition at line 1809')
            print('Condition at line 1326')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            print('Condition at line 3293')
            print('Condition at line 2798')
            print('Condition at line 2304')
            print('Condition at line 1812')
            print('Condition at line 1328')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y < Robber.y:
            print('Condition at line 3299')
            print('Condition at line 2803')
            print('Condition at line 2308')
            print('Condition at line 1815')
            print('Condition at line 1330')
            currentState = 20
        elif Cop.x > Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 3305')
            print('Condition at line 2808')
            print('Condition at line 2312')
            print('Condition at line 1818')
            print('Condition at line 1332')
            currentState = 20
        elif Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 3311')
            print('Condition at line 2813')
            print('Condition at line 2316')
            print('Condition at line 1821')
            print('Condition at line 1334')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3317')
            print('Condition at line 2818')
            print('Condition at line 2320')
            print('Condition at line 1824')
            print('Condition at line 1336')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3324')
            print('Condition at line 2824')
            print('Condition at line 2325')
            print('Condition at line 1828')
            print('Condition at line 1339')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3331')
            print('Condition at line 2830')
            print('Condition at line 2330')
            print('Condition at line 1832')
            print('Condition at line 1342')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3337')
            print('Condition at line 2835')
            print('Condition at line 2334')
            print('Condition at line 1835')
            print('Condition at line 1344')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3343')
            print('Condition at line 2840')
            print('Condition at line 2338')
            print('Condition at line 1838')
            print('Condition at line 1346')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3350')
            print('Condition at line 2846')
            print('Condition at line 2343')
            print('Condition at line 1842')
            print('Condition at line 1349')
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3357')
            print('Condition at line 2852')
            print('Condition at line 2348')
            print('Condition at line 1846')
            print('Condition at line 1352')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3364')
            print('Condition at line 2858')
            print('Condition at line 2353')
            print('Condition at line 1850')
            print('Condition at line 1355')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3371')
            print('Condition at line 2864')
            print('Condition at line 2358')
            print('Condition at line 1854')
            print('Condition at line 1358')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3377')
            print('Condition at line 2869')
            print('Condition at line 2362')
            print('Condition at line 1857')
            print('Condition at line 1360')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3384')
            print('Condition at line 2875')
            print('Condition at line 2367')
            print('Condition at line 1861')
            print('Condition at line 1363')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3391')
            print('Condition at line 2881')
            print('Condition at line 2372')
            print('Condition at line 1865')
            print('Condition at line 1366')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3397')
            print('Condition at line 2886')
            print('Condition at line 2376')
            print('Condition at line 1868')
            print('Condition at line 1368')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3404')
            print('Condition at line 2892')
            print('Condition at line 2381')
            print('Condition at line 1872')
            print('Condition at line 1371')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3411')
            print('Condition at line 2898')
            print('Condition at line 2386')
            print('Condition at line 1876')
            print('Condition at line 1374')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3417')
            print('Condition at line 2903')
            print('Condition at line 2390')
            print('Condition at line 1879')
            print('Condition at line 1376')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3424')
            print('Condition at line 2909')
            print('Condition at line 2395')
            print('Condition at line 1883')
            print('Condition at line 1379')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3430')
            print('Condition at line 2914')
            print('Condition at line 2399')
            print('Condition at line 1886')
            print('Condition at line 1381')
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3437')
            print('Condition at line 2920')
            print('Condition at line 2404')
            print('Condition at line 1890')
            print('Condition at line 1384')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3444')
            print('Condition at line 2926')
            print('Condition at line 2409')
            print('Condition at line 1894')
            print('Condition at line 1387')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3450')
            print('Condition at line 2931')
            print('Condition at line 2413')
            print('Condition at line 1897')
            print('Condition at line 1389')
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3457')
            print('Condition at line 2937')
            print('Condition at line 2418')
            print('Condition at line 1901')
            print('Condition at line 1392')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3463')
            print('Condition at line 2942')
            print('Condition at line 2422')
            print('Condition at line 1904')
            print('Condition at line 1394')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3470')
            print('Condition at line 2948')
            print('Condition at line 2427')
            print('Condition at line 1908')
            print('Condition at line 1397')
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3477')
            print('Condition at line 2954')
            print('Condition at line 2432')
            print('Condition at line 1912')
            print('Condition at line 1400')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3484')
            print('Condition at line 2960')
            print('Condition at line 2437')
            print('Condition at line 1916')
            print('Condition at line 1403')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3490')
            print('Condition at line 2965')
            print('Condition at line 2441')
            print('Condition at line 1919')
            print('Condition at line 1405')
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3497')
            print('Condition at line 2971')
            print('Condition at line 2446')
            print('Condition at line 1923')
            print('Condition at line 1408')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3504')
            print('Condition at line 2977')
            print('Condition at line 2451')
            print('Condition at line 1927')
            print('Condition at line 1411')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3511')
            print('Condition at line 2983')
            print('Condition at line 2456')
            print('Condition at line 1931')
            print('Condition at line 1414')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3517')
            print('Condition at line 2988')
            print('Condition at line 2460')
            print('Condition at line 1934')
            print('Condition at line 1416')
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3524')
            print('Condition at line 2994')
            print('Condition at line 2465')
            print('Condition at line 1938')
            print('Condition at line 1419')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3530')
            print('Condition at line 2999')
            print('Condition at line 2469')
            print('Condition at line 1941')
            print('Condition at line 1421')
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3537')
            print('Condition at line 3005')
            print('Condition at line 2474')
            print('Condition at line 1945')
            print('Condition at line 1424')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3544')
            print('Condition at line 3011')
            print('Condition at line 2479')
            print('Condition at line 1949')
            print('Condition at line 1427')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3550')
            print('Condition at line 3016')
            print('Condition at line 2483')
            print('Condition at line 1952')
            print('Condition at line 1429')
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3557')
            print('Condition at line 3022')
            print('Condition at line 2488')
            print('Condition at line 1956')
            print('Condition at line 1432')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3563')
            print('Condition at line 3027')
            print('Condition at line 2492')
            print('Condition at line 1959')
            print('Condition at line 1434')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3570')
            print('Condition at line 3033')
            print('Condition at line 2497')
            print('Condition at line 1963')
            print('Condition at line 1437')
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3577')
            print('Condition at line 3039')
            print('Condition at line 2502')
            print('Condition at line 1967')
            print('Condition at line 1440')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3584')
            print('Condition at line 3045')
            print('Condition at line 2507')
            print('Condition at line 1971')
            print('Condition at line 1443')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3591')
            print('Condition at line 3051')
            print('Condition at line 2512')
            print('Condition at line 1975')
            print('Condition at line 1446')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3597')
            print('Condition at line 3056')
            print('Condition at line 2516')
            print('Condition at line 1978')
            print('Condition at line 1448')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3603')
            print('Condition at line 3061')
            print('Condition at line 2520')
            print('Condition at line 1981')
            print('Condition at line 1450')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3610')
            print('Condition at line 3067')
            print('Condition at line 2525')
            print('Condition at line 1985')
            print('Condition at line 1453')
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3617')
            print('Condition at line 3073')
            print('Condition at line 2530')
            print('Condition at line 1989')
            print('Condition at line 1456')
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3624')
            print('Condition at line 3079')
            print('Condition at line 2535')
            print('Condition at line 1993')
            print('Condition at line 1459')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3630')
            print('Condition at line 3084')
            print('Condition at line 2539')
            print('Condition at line 1996')
            print('Condition at line 1461')
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.y == Robber.y:
            print('Condition at line 3637')
            print('Condition at line 3090')
            print('Condition at line 2544')
            print('Condition at line 2000')
            print('Condition at line 1464')
            currentState = 20
        elif Cop.x == Robber.x and Cop.y == Robber.y:
            print('Condition at line 3643')
            print('Condition at line 3095')
            print('Condition at line 2548')
            print('Condition at line 2003')
            print('Condition at line 1466')
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.y == Robber.y:
            print('Condition at line 3650')
            print('Condition at line 3101')
            print('Condition at line 2553')
            print('Condition at line 2007')
            print('Condition at line 1469')
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.y == Robber.y:
            print('Condition at line 3657')
            print('Condition at line 3107')
            print('Condition at line 2558')
            print('Condition at line 2011')
            print('Condition at line 1472')
            currentState = 20
        elif Cop.x == Robber.x and Cop.y == Robber.y:
            print('Condition at line 3663')
            print('Condition at line 3112')
            print('Condition at line 2562')
            print('Condition at line 2014')
            print('Condition at line 1474')
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.y == Robber.y:
            print('Condition at line 3670')
            print('Condition at line 3118')
            print('Condition at line 2567')
            print('Condition at line 2018')
            print('Condition at line 1477')
            _next_Cop.y = Cop.y - 1
            currentState = 20
    elif currentState == 14:
        print('Condition at line 3677')
        print('Condition at line 3124')
        print('Condition at line 2572')
        print('Condition at line 2022')
        print('Condition at line 1480')
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            print('Condition at line 3682')
            print('Condition at line 3128')
            print('Condition at line 2575')
            print('Condition at line 2024')
            print('Condition at line 1481')
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 6
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3691')
            print('Condition at line 3136')
            print('Condition at line 2582')
            print('Condition at line 2030')
            print('Condition at line 1486')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3698')
            print('Condition at line 3142')
            print('Condition at line 2587')
            print('Condition at line 2034')
            print('Condition at line 1489')
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3705')
            print('Condition at line 3148')
            print('Condition at line 2592')
            print('Condition at line 2038')
            print('Condition at line 1492')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3711')
            print('Condition at line 3153')
            print('Condition at line 2596')
            print('Condition at line 2041')
            print('Condition at line 1494')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3717')
            print('Condition at line 3158')
            print('Condition at line 2600')
            print('Condition at line 2044')
            print('Condition at line 1496')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3723')
            print('Condition at line 3163')
            print('Condition at line 2604')
            print('Condition at line 2047')
            print('Condition at line 1498')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3729')
            print('Condition at line 3168')
            print('Condition at line 2608')
            print('Condition at line 2050')
            print('Condition at line 1500')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3735')
            print('Condition at line 3173')
            print('Condition at line 2612')
            print('Condition at line 2053')
            print('Condition at line 1502')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3741')
            print('Condition at line 3178')
            print('Condition at line 2616')
            print('Condition at line 2056')
            print('Condition at line 1504')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3747')
            print('Condition at line 3183')
            print('Condition at line 2620')
            print('Condition at line 2059')
            print('Condition at line 1506')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3753')
            print('Condition at line 3188')
            print('Condition at line 2624')
            print('Condition at line 2062')
            print('Condition at line 1508')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3759')
            print('Condition at line 3193')
            print('Condition at line 2628')
            print('Condition at line 2065')
            print('Condition at line 1510')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3765')
            print('Condition at line 3198')
            print('Condition at line 2632')
            print('Condition at line 2068')
            print('Condition at line 1512')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3771')
            print('Condition at line 3203')
            print('Condition at line 2636')
            print('Condition at line 2071')
            print('Condition at line 1514')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 3777')
            print('Condition at line 3208')
            print('Condition at line 2640')
            print('Condition at line 2074')
            print('Condition at line 1516')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3783')
            print('Condition at line 3213')
            print('Condition at line 2644')
            print('Condition at line 2077')
            print('Condition at line 1518')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 3789')
            print('Condition at line 3218')
            print('Condition at line 2648')
            print('Condition at line 2080')
            print('Condition at line 1520')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 3795')
            print('Condition at line 3223')
            print('Condition at line 2652')
            print('Condition at line 2083')
            print('Condition at line 1522')
            currentState = 20
        elif Cop.x != Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 3801')
            print('Condition at line 3228')
            print('Condition at line 2656')
            print('Condition at line 2086')
            print('Condition at line 1524')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x:
            print('Condition at line 3807')
            print('Condition at line 3233')
            print('Condition at line 2660')
            print('Condition at line 2089')
            print('Condition at line 1526')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x:
            print('Condition at line 3813')
            print('Condition at line 3238')
            print('Condition at line 2664')
            print('Condition at line 2092')
            print('Condition at line 1528')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x:
            print('Condition at line 3819')
            print('Condition at line 3243')
            print('Condition at line 2668')
            print('Condition at line 2095')
            print('Condition at line 1530')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3825')
            print('Condition at line 3248')
            print('Condition at line 2672')
            print('Condition at line 2098')
            print('Condition at line 1532')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 3831')
            print('Condition at line 3253')
            print('Condition at line 2676')
            print('Condition at line 2101')
            print('Condition at line 1534')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 3837')
            print('Condition at line 3258')
            print('Condition at line 2680')
            print('Condition at line 2104')
            print('Condition at line 1536')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 3843')
            print('Condition at line 3263')
            print('Condition at line 2684')
            print('Condition at line 2107')
            print('Condition at line 1538')
            currentState = 20
    elif currentState == 15:
        print('Condition at line 3849')
        print('Condition at line 3268')
        print('Condition at line 2688')
        print('Condition at line 2110')
        print('Condition at line 1540')
        if (Cop.x != Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and
            Cop.y > Robber.y and Cop.y < Robber.y):
            print('Condition at line 3854')
            print('Condition at line 3272')
            print('Condition at line 2691')
            print('Condition at line 2112')
            print('Condition at line 1541')
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            print('Condition at line 3862')
            print('Condition at line 3279')
            print('Condition at line 2697')
            print('Condition at line 2117')
            print('Condition at line 1545')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3869')
            print('Condition at line 3285')
            print('Condition at line 2702')
            print('Condition at line 2121')
            print('Condition at line 1548')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3876')
            print('Condition at line 3291')
            print('Condition at line 2707')
            print('Condition at line 2125')
            print('Condition at line 1551')
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3883')
            print('Condition at line 3297')
            print('Condition at line 2712')
            print('Condition at line 2129')
            print('Condition at line 1554')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 8
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3892')
            print('Condition at line 3305')
            print('Condition at line 2719')
            print('Condition at line 2135')
            print('Condition at line 1559')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 3901')
            print('Condition at line 3313')
            print('Condition at line 2726')
            print('Condition at line 2141')
            print('Condition at line 1564')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3910')
            print('Condition at line 3321')
            print('Condition at line 2733')
            print('Condition at line 2147')
            print('Condition at line 1569')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3919')
            print('Condition at line 3329')
            print('Condition at line 2740')
            print('Condition at line 2153')
            print('Condition at line 1574')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 9
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3928')
            print('Condition at line 3337')
            print('Condition at line 2747')
            print('Condition at line 2159')
            print('Condition at line 1579')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            print('Condition at line 3934')
            print('Condition at line 3342')
            print('Condition at line 2751')
            print('Condition at line 2162')
            print('Condition at line 1581')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3940')
            print('Condition at line 3347')
            print('Condition at line 2755')
            print('Condition at line 2165')
            print('Condition at line 1583')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 3946')
            print('Condition at line 3352')
            print('Condition at line 2759')
            print('Condition at line 2168')
            print('Condition at line 1585')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3952')
            print('Condition at line 3357')
            print('Condition at line 2763')
            print('Condition at line 2171')
            print('Condition at line 1587')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y:
            print('Condition at line 3958')
            print('Condition at line 3362')
            print('Condition at line 2767')
            print('Condition at line 2174')
            print('Condition at line 1589')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 3964')
            print('Condition at line 3367')
            print('Condition at line 2771')
            print('Condition at line 2177')
            print('Condition at line 1591')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 3970')
            print('Condition at line 3372')
            print('Condition at line 2775')
            print('Condition at line 2180')
            print('Condition at line 1593')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 3976')
            print('Condition at line 3377')
            print('Condition at line 2779')
            print('Condition at line 2183')
            print('Condition at line 1595')
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 3982')
            print('Condition at line 3382')
            print('Condition at line 2783')
            print('Condition at line 2186')
            print('Condition at line 1597')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 3988')
            print('Condition at line 3387')
            print('Condition at line 2787')
            print('Condition at line 2189')
            print('Condition at line 1599')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 3994')
            print('Condition at line 3392')
            print('Condition at line 2791')
            print('Condition at line 2192')
            print('Condition at line 1601')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y:
            print('Condition at line 4000')
            print('Condition at line 3397')
            print('Condition at line 2795')
            print('Condition at line 2195')
            print('Condition at line 1603')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4006')
            print('Condition at line 3402')
            print('Condition at line 2799')
            print('Condition at line 2198')
            print('Condition at line 1605')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 4012')
            print('Condition at line 3407')
            print('Condition at line 2803')
            print('Condition at line 2201')
            print('Condition at line 1607')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 4018')
            print('Condition at line 3412')
            print('Condition at line 2807')
            print('Condition at line 2204')
            print('Condition at line 1609')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4024')
            print('Condition at line 3417')
            print('Condition at line 2811')
            print('Condition at line 2207')
            print('Condition at line 1611')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 4030')
            print('Condition at line 3422')
            print('Condition at line 2815')
            print('Condition at line 2210')
            print('Condition at line 1613')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4036')
            print('Condition at line 3427')
            print('Condition at line 2819')
            print('Condition at line 2213')
            print('Condition at line 1615')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 4042')
            print('Condition at line 3432')
            print('Condition at line 2823')
            print('Condition at line 2216')
            print('Condition at line 1617')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4048')
            print('Condition at line 3437')
            print('Condition at line 2827')
            print('Condition at line 2219')
            print('Condition at line 1619')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 4054')
            print('Condition at line 3442')
            print('Condition at line 2831')
            print('Condition at line 2222')
            print('Condition at line 1621')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4060')
            print('Condition at line 3447')
            print('Condition at line 2835')
            print('Condition at line 2225')
            print('Condition at line 1623')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4066')
            print('Condition at line 3452')
            print('Condition at line 2839')
            print('Condition at line 2228')
            print('Condition at line 1625')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4072')
            print('Condition at line 3457')
            print('Condition at line 2843')
            print('Condition at line 2231')
            print('Condition at line 1627')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4078')
            print('Condition at line 3462')
            print('Condition at line 2847')
            print('Condition at line 2234')
            print('Condition at line 1629')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4084')
            print('Condition at line 3467')
            print('Condition at line 2851')
            print('Condition at line 2237')
            print('Condition at line 1631')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4090')
            print('Condition at line 3472')
            print('Condition at line 2855')
            print('Condition at line 2240')
            print('Condition at line 1633')
            currentState = 20
    elif currentState == 16:
        print('Condition at line 4096')
        print('Condition at line 3477')
        print('Condition at line 2859')
        print('Condition at line 2243')
        print('Condition at line 1635')
        if (Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and
            Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y):
            print('Condition at line 4101')
            print('Condition at line 3481')
            print('Condition at line 2862')
            print('Condition at line 2245')
            print('Condition at line 1636')
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 4109')
            print('Condition at line 3488')
            print('Condition at line 2868')
            print('Condition at line 2250')
            print('Condition at line 1640')
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4116')
            print('Condition at line 3494')
            print('Condition at line 2873')
            print('Condition at line 2254')
            print('Condition at line 1643')
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 8
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 4125')
            print('Condition at line 3502')
            print('Condition at line 2880')
            print('Condition at line 2260')
            print('Condition at line 1648')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 4134')
            print('Condition at line 3510')
            print('Condition at line 2887')
            print('Condition at line 2266')
            print('Condition at line 1653')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4143')
            print('Condition at line 3518')
            print('Condition at line 2894')
            print('Condition at line 2272')
            print('Condition at line 1658')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4152')
            print('Condition at line 3526')
            print('Condition at line 2901')
            print('Condition at line 2278')
            print('Condition at line 1663')
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 9
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 4161')
            print('Condition at line 3534')
            print('Condition at line 2908')
            print('Condition at line 2284')
            print('Condition at line 1668')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4168')
            print('Condition at line 3540')
            print('Condition at line 2913')
            print('Condition at line 2288')
            print('Condition at line 1671')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4175')
            print('Condition at line 3546')
            print('Condition at line 2918')
            print('Condition at line 2292')
            print('Condition at line 1674')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 4182')
            print('Condition at line 3552')
            print('Condition at line 2923')
            print('Condition at line 2296')
            print('Condition at line 1677')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4189')
            print('Condition at line 3558')
            print('Condition at line 2928')
            print('Condition at line 2300')
            print('Condition at line 1680')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4196')
            print('Condition at line 3564')
            print('Condition at line 2933')
            print('Condition at line 2304')
            print('Condition at line 1683')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            print('Condition at line 4202')
            print('Condition at line 3569')
            print('Condition at line 2937')
            print('Condition at line 2307')
            print('Condition at line 1685')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4208')
            print('Condition at line 3574')
            print('Condition at line 2941')
            print('Condition at line 2310')
            print('Condition at line 1687')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 4214')
            print('Condition at line 3579')
            print('Condition at line 2945')
            print('Condition at line 2313')
            print('Condition at line 1689')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4220')
            print('Condition at line 3584')
            print('Condition at line 2949')
            print('Condition at line 2316')
            print('Condition at line 1691')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y:
            print('Condition at line 4226')
            print('Condition at line 3589')
            print('Condition at line 2953')
            print('Condition at line 2319')
            print('Condition at line 1693')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 4232')
            print('Condition at line 3594')
            print('Condition at line 2957')
            print('Condition at line 2322')
            print('Condition at line 1695')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y:
            print('Condition at line 4238')
            print('Condition at line 3599')
            print('Condition at line 2961')
            print('Condition at line 2325')
            print('Condition at line 1697')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4244')
            print('Condition at line 3604')
            print('Condition at line 2965')
            print('Condition at line 2328')
            print('Condition at line 1699')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 4250')
            print('Condition at line 3609')
            print('Condition at line 2969')
            print('Condition at line 2331')
            print('Condition at line 1701')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            print('Condition at line 4256')
            print('Condition at line 3614')
            print('Condition at line 2973')
            print('Condition at line 2334')
            print('Condition at line 1703')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 4262')
            print('Condition at line 3619')
            print('Condition at line 2977')
            print('Condition at line 2337')
            print('Condition at line 1705')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y <= Robber.y:
            print('Condition at line 4268')
            print('Condition at line 3624')
            print('Condition at line 2981')
            print('Condition at line 2340')
            print('Condition at line 1707')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4274')
            print('Condition at line 3629')
            print('Condition at line 2985')
            print('Condition at line 2343')
            print('Condition at line 1709')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 4280')
            print('Condition at line 3634')
            print('Condition at line 2989')
            print('Condition at line 2346')
            print('Condition at line 1711')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 4286')
            print('Condition at line 3639')
            print('Condition at line 2993')
            print('Condition at line 2349')
            print('Condition at line 1713')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4292')
            print('Condition at line 3644')
            print('Condition at line 2997')
            print('Condition at line 2352')
            print('Condition at line 1715')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 4298')
            print('Condition at line 3649')
            print('Condition at line 3001')
            print('Condition at line 2355')
            print('Condition at line 1717')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4304')
            print('Condition at line 3654')
            print('Condition at line 3005')
            print('Condition at line 2358')
            print('Condition at line 1719')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4310')
            print('Condition at line 3659')
            print('Condition at line 3009')
            print('Condition at line 2361')
            print('Condition at line 1721')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4316')
            print('Condition at line 3664')
            print('Condition at line 3013')
            print('Condition at line 2364')
            print('Condition at line 1723')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4322')
            print('Condition at line 3669')
            print('Condition at line 3017')
            print('Condition at line 2367')
            print('Condition at line 1725')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4328')
            print('Condition at line 3674')
            print('Condition at line 3021')
            print('Condition at line 2370')
            print('Condition at line 1727')
            currentState = 20
    elif currentState == 17:
        print('Condition at line 4334')
        print('Condition at line 3679')
        print('Condition at line 3025')
        print('Condition at line 2373')
        print('Condition at line 1729')
        if Cop.x == Robber.x and Cop.x > Robber.x:
            print('Condition at line 4339')
            print('Condition at line 3683')
            print('Condition at line 3028')
            print('Condition at line 2375')
            print('Condition at line 1730')
            currentState = 20
        elif Cop.x >= Robber.x:
            print('Condition at line 4345')
            print('Condition at line 3688')
            print('Condition at line 3032')
            print('Condition at line 2378')
            print('Condition at line 1732')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x < Robber.x:
            print('Condition at line 4351')
            print('Condition at line 3693')
            print('Condition at line 3036')
            print('Condition at line 2381')
            print('Condition at line 1734')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x:
            print('Condition at line 4357')
            print('Condition at line 3698')
            print('Condition at line 3040')
            print('Condition at line 2384')
            print('Condition at line 1736')
            currentState = 20
    elif currentState == 18:
        print('Condition at line 4363')
        print('Condition at line 3703')
        print('Condition at line 3044')
        print('Condition at line 2387')
        print('Condition at line 1738')
        if Cop.x != Robber.x:
            print('Condition at line 4368')
            print('Condition at line 3707')
            print('Condition at line 3047')
            print('Condition at line 2389')
            print('Condition at line 1739')
            currentState = 20
        elif Cop.x > Robber.x:
            print('Condition at line 4374')
            print('Condition at line 3712')
            print('Condition at line 3051')
            print('Condition at line 2392')
            print('Condition at line 1741')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x:
            print('Condition at line 4380')
            print('Condition at line 3717')
            print('Condition at line 3055')
            print('Condition at line 2395')
            print('Condition at line 1743')
            currentState = 20
    elif currentState == 19:
        print('Condition at line 4386')
        print('Condition at line 3722')
        print('Condition at line 3059')
        print('Condition at line 2398')
        print('Condition at line 1745')
        if Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4391')
            print('Condition at line 3726')
            print('Condition at line 3062')
            print('Condition at line 2400')
            print('Condition at line 1746')
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.y != Robber.y:
            print('Condition at line 4398')
            print('Condition at line 3732')
            print('Condition at line 3067')
            print('Condition at line 2404')
            print('Condition at line 1749')
            currentState = 20
        elif Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 4404')
            print('Condition at line 3737')
            print('Condition at line 3071')
            print('Condition at line 2407')
            print('Condition at line 1751')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 4410')
            print('Condition at line 3742')
            print('Condition at line 3075')
            print('Condition at line 2410')
            print('Condition at line 1753')
            currentState = 20
        elif Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4416')
            print('Condition at line 3747')
            print('Condition at line 3079')
            print('Condition at line 2413')
            print('Condition at line 1755')
            currentState = 20
    elif currentState == 20:
        print('Condition at line 4422')
        print('Condition at line 3752')
        print('Condition at line 3083')
        print('Condition at line 2416')
        print('Condition at line 1757')
        if (Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            print('Condition at line 4427')
            print('Condition at line 3756')
            print('Condition at line 3086')
            print('Condition at line 2418')
            print('Condition at line 1758')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4435')
            print('Condition at line 3763')
            print('Condition at line 3092')
            print('Condition at line 2423')
            print('Condition at line 1762')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4442')
            print('Condition at line 3769')
            print('Condition at line 3097')
            print('Condition at line 2427')
            print('Condition at line 1765')
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 4449')
            print('Condition at line 3775')
            print('Condition at line 3102')
            print('Condition at line 2431')
            print('Condition at line 1768')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4455')
            print('Condition at line 3780')
            print('Condition at line 3106')
            print('Condition at line 2434')
            print('Condition at line 1770')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4461')
            print('Condition at line 3785')
            print('Condition at line 3110')
            print('Condition at line 2437')
            print('Condition at line 1772')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 4467')
            print('Condition at line 3790')
            print('Condition at line 3114')
            print('Condition at line 2440')
            print('Condition at line 1774')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4473')
            print('Condition at line 3795')
            print('Condition at line 3118')
            print('Condition at line 2443')
            print('Condition at line 1776')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4479')
            print('Condition at line 3800')
            print('Condition at line 3122')
            print('Condition at line 2446')
            print('Condition at line 1778')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 4485')
            print('Condition at line 3805')
            print('Condition at line 3126')
            print('Condition at line 2449')
            print('Condition at line 1780')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4491')
            print('Condition at line 3810')
            print('Condition at line 3130')
            print('Condition at line 2452')
            print('Condition at line 1782')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4497')
            print('Condition at line 3815')
            print('Condition at line 3134')
            print('Condition at line 2455')
            print('Condition at line 1784')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            print('Condition at line 4503')
            print('Condition at line 3820')
            print('Condition at line 3138')
            print('Condition at line 2458')
            print('Condition at line 1786')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4509')
            print('Condition at line 3825')
            print('Condition at line 3142')
            print('Condition at line 2461')
            print('Condition at line 1788')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4515')
            print('Condition at line 3830')
            print('Condition at line 3146')
            print('Condition at line 2464')
            print('Condition at line 1790')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x:
            print('Condition at line 4521')
            print('Condition at line 3835')
            print('Condition at line 3150')
            print('Condition at line 2467')
            print('Condition at line 1792')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x:
            print('Condition at line 4527')
            print('Condition at line 3840')
            print('Condition at line 3154')
            print('Condition at line 2470')
            print('Condition at line 1794')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4533')
            print('Condition at line 3845')
            print('Condition at line 3158')
            print('Condition at line 2473')
            print('Condition at line 1796')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 4539')
            print('Condition at line 3850')
            print('Condition at line 3162')
            print('Condition at line 2476')
            print('Condition at line 1798')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 4545')
            print('Condition at line 3855')
            print('Condition at line 3166')
            print('Condition at line 2479')
            print('Condition at line 1800')
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 4551')
            print('Condition at line 3860')
            print('Condition at line 3170')
            print('Condition at line 2482')
            print('Condition at line 1802')
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            print('Condition at line 4557')
            print('Condition at line 3865')
            print('Condition at line 3174')
            print('Condition at line 2485')
            print('Condition at line 1804')
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x:
            print('Condition at line 4563')
            print('Condition at line 3870')
            print('Condition at line 3178')
            print('Condition at line 2488')
            print('Condition at line 1806')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            print('Condition at line 4569')
            print('Condition at line 3875')
            print('Condition at line 3182')
            print('Condition at line 2491')
            print('Condition at line 1808')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            print('Condition at line 4575')
            print('Condition at line 3880')
            print('Condition at line 3186')
            print('Condition at line 2494')
            print('Condition at line 1810')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            print('Condition at line 4581')
            print('Condition at line 3885')
            print('Condition at line 3190')
            print('Condition at line 2497')
            print('Condition at line 1812')
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            print('Condition at line 4587')
            print('Condition at line 3890')
            print('Condition at line 3194')
            print('Condition at line 2500')
            print('Condition at line 1814')
            currentState = 20
    return {'currentState': currentState, 'Cop.x': _next_Cop.x, 'Cop.y':
        _next_Cop.y}
