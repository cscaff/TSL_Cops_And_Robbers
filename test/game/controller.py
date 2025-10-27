
from datetime import datetime
from operator import itemgetter
from entities import Robber, Cop, _next_Cop

def log_condition(cond_str, current_state, actions):
    print(f"- - - - - - - - - - - - - - - - -")
    print(f"t = {datetime.now().strftime("%H:%M:%S")}")
    print(f"[TRACE] Current State = {current_state}")
    print(f"[TRACE] Chosen Next Event Condition: {cond_str}")
    print(f"[TRACE]   Actions to Perform: [{'\n'.join(actions)}]")

def updateState(_inputs_and_cells):
    currentState, Robber.x, Robber.y, Cop.x, Cop.y = itemgetter('currentState',
        'Robber.x', 'Robber.y', 'Cop.x', 'Cop.y')(_inputs_and_cells)
    if currentState == 0:
        if (Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and
            Cop.x <= Robber.x):
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=Cop.y', 'currentState=(0)'])
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.y=Cop.moveD(Cop.y)', '_next_Cop.x=Cop.x', 'currentState=(0)']
                )
            _next_Cop.y = Cop.moveD(Cop.y)
            _next_Cop.x = Cop.x
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.y=Cop.moveU(Cop.y)', '_next_Cop.x=Cop.x', 'currentState=(0)']
                )
            _next_Cop.y = Cop.moveU(Cop.y)
            _next_Cop.x = Cop.x
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.y=Cop.moveD(Cop.x)', '_next_Cop.x=Cop.x', 'currentState=(0)']
                )
            _next_Cop.y = Cop.moveD(Cop.x)
            _next_Cop.x = Cop.x
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.y=Cop.moveU(Cop.x)', '_next_Cop.x=Cop.x', 'currentState=(0)']
                )
            _next_Cop.y = Cop.moveU(Cop.x)
            _next_Cop.x = Cop.x
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveR(Cop.x)', '_next_Cop.y=Cop.y', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveR(Cop.x)
            _next_Cop.y = Cop.y
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveR(Cop.x)', '_next_Cop.y=Cop.moveD(Cop.y)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveR(Cop.x)
            _next_Cop.y = Cop.moveD(Cop.y)
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveR(Cop.x)', '_next_Cop.y=Cop.moveU(Cop.y)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveR(Cop.x)
            _next_Cop.y = Cop.moveU(Cop.y)
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveR(Cop.x)', '_next_Cop.y=Cop.moveD(Cop.x)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveR(Cop.x)
            _next_Cop.y = Cop.moveD(Cop.x)
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveR(Cop.x)', '_next_Cop.y=Cop.moveU(Cop.x)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveR(Cop.x)
            _next_Cop.y = Cop.moveU(Cop.x)
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveL(Cop.x)', '_next_Cop.y=Cop.y', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveL(Cop.x)
            _next_Cop.y = Cop.y
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveL(Cop.x)', '_next_Cop.y=Cop.moveD(Cop.y)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveL(Cop.x)
            _next_Cop.y = Cop.moveD(Cop.y)
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveL(Cop.x)', '_next_Cop.y=Cop.moveU(Cop.y)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveL(Cop.x)
            _next_Cop.y = Cop.moveU(Cop.y)
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveL(Cop.x)', '_next_Cop.y=Cop.moveD(Cop.x)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveL(Cop.x)
            _next_Cop.y = Cop.moveD(Cop.x)
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveL(Cop.x)', '_next_Cop.y=Cop.moveU(Cop.x)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveL(Cop.x)
            _next_Cop.y = Cop.moveU(Cop.x)
            currentState = 0
        elif Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveR(Cop.x)', '_next_Cop.y=Cop.y', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveR(Cop.x)
            _next_Cop.y = Cop.y
            currentState = 0
        elif Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveR(Cop.x)', '_next_Cop.y=Cop.moveD(Cop.y)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveR(Cop.x)
            _next_Cop.y = Cop.moveD(Cop.y)
            currentState = 0
        elif Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveR(Cop.x)', '_next_Cop.y=Cop.moveU(Cop.y)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveR(Cop.x)
            _next_Cop.y = Cop.moveU(Cop.y)
            currentState = 0
        elif Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveR(Cop.x)', '_next_Cop.y=Cop.moveD(Cop.x)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveR(Cop.x)
            _next_Cop.y = Cop.moveD(Cop.x)
            currentState = 0
        elif Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveR(Cop.x)', '_next_Cop.y=Cop.moveU(Cop.x)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveR(Cop.x)
            _next_Cop.y = Cop.moveU(Cop.x)
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x > Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x >
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveL(Cop.x)', '_next_Cop.y=Cop.y', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveL(Cop.x)
            _next_Cop.y = Cop.y
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x > Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x >
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveL(Cop.x)', '_next_Cop.y=Cop.moveD(Cop.y)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveL(Cop.x)
            _next_Cop.y = Cop.moveD(Cop.y)
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x > Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x >
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveL(Cop.x)', '_next_Cop.y=Cop.moveU(Cop.y)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveL(Cop.x)
            _next_Cop.y = Cop.moveU(Cop.y)
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x > Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x >
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveL(Cop.x)', '_next_Cop.y=Cop.moveD(Cop.x)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveL(Cop.x)
            _next_Cop.y = Cop.moveD(Cop.x)
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x > Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y and Cop.x >
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveL(Cop.x)', '_next_Cop.y=Cop.moveU(Cop.x)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveL(Cop.x)
            _next_Cop.y = Cop.moveU(Cop.x)
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.y=Cop.moveU(Cop.y)', '_next_Cop.x=Cop.x', 'currentState=(0)']
                )
            _next_Cop.y = Cop.moveU(Cop.y)
            _next_Cop.x = Cop.x
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveR(Cop.x)', '_next_Cop.y=Cop.moveU(Cop.y)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveR(Cop.x)
            _next_Cop.y = Cop.moveU(Cop.y)
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveL(Cop.x)', '_next_Cop.y=Cop.moveU(Cop.y)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveL(Cop.x)
            _next_Cop.y = Cop.moveU(Cop.y)
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.y=Cop.moveD(Cop.y)', '_next_Cop.x=Cop.x', 'currentState=(0)']
                )
            _next_Cop.y = Cop.moveD(Cop.y)
            _next_Cop.x = Cop.x
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveR(Cop.x)', '_next_Cop.y=Cop.moveD(Cop.y)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveR(Cop.x)
            _next_Cop.y = Cop.moveD(Cop.y)
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveL(Cop.x)', '_next_Cop.y=Cop.moveD(Cop.y)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveL(Cop.x)
            _next_Cop.y = Cop.moveD(Cop.y)
            currentState = 0
        elif Cop.x < Robber.x and Cop.x > Robber.x:
            log_condition('(Cop.x < Robber.x and Cop.x > Robber.x)',
                currentState, ['currentState=(0)'])
            currentState = 0
        elif Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition('(Cop.y > Robber.y and Cop.y < Robber.y)',
                currentState, ['currentState=(0)'])
            currentState = 0
        elif Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveR(Cop.x)', '_next_Cop.y=Cop.moveU(Cop.y)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveR(Cop.x)
            _next_Cop.y = Cop.moveU(Cop.y)
            currentState = 0
        elif Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y and Cop.x <= Robber.x:
            log_condition(
                """(Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y and Cop.x <=
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveR(Cop.x)', '_next_Cop.y=Cop.moveD(Cop.y)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveR(Cop.x)
            _next_Cop.y = Cop.moveD(Cop.y)
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y and Cop.x > Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y and Cop.x >
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveL(Cop.x)', '_next_Cop.y=Cop.moveU(Cop.y)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveL(Cop.x)
            _next_Cop.y = Cop.moveU(Cop.y)
            currentState = 0
        elif Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y and Cop.x > Robber.x:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y and Cop.x >
    Robber.x)"""
                , currentState,
                ['_next_Cop.x=Cop.moveL(Cop.x)', '_next_Cop.y=Cop.moveD(Cop.y)', 'currentState=(0)']
                )
            _next_Cop.x = Cop.moveL(Cop.x)
            _next_Cop.y = Cop.moveD(Cop.y)
            currentState = 0
    return {'currentState': currentState, 'Cop.x': _next_Cop.x, 'Cop.y':
        _next_Cop.y}
