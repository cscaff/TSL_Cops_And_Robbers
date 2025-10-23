
from datetime import datetime
from operator import itemgetter
from entities import Robber, Cop, _next_Cop
from logger import trace_to_natural_language

def log_condition(cond_str, current_state, actions):
    print(f"- - - - - - - - - - - - - - - - -")
    # print(f"t = {datetime.now().strftime("%H:%M:%S")}")
    # print(f"[TRACE] Current State = {current_state}")
    # print(f"[TRACE] Chosen Next Event Condition: {cond_str}")
    # print(f"[TRACE]   Actions to Perform: [{'\n'.join(actions)}]")

    formal_log = f""" Current time = {datetime.now().strftime("%H:%M:%S")}. I am in state {current_state}. The next event I chose is because I
    am in this condition: {cond_str}. Because I meet this condition, I will perform the following list of actions: [{'\n'.join(actions)}].
    """

    trace_to_natural_language(formal_log)

def updateState(_inputs_and_cells):
    currentState, Robber.x, Robber.y, Cop.x, Cop.y = itemgetter('currentState',
        'Robber.x', 'Robber.y', 'Cop.x', 'Cop.y')(_inputs_and_cells)
    if currentState == 0:
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y):
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(1)']
                )
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=(Cop.y + 1)', 'currentState=(2)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y + 1)', 'currentState=(2)']
                )
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=(Cop.y + 1)', 'currentState=(2)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.y=(Cop.y + 1)', 'currentState=(2)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=Cop.y', '_next_Cop.y=(Cop.y + 1)', 'currentState=(2)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=(Cop.y + 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(2)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=(Cop.y - 1)', 'currentState=(3)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(3)']
                )
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=(Cop.y - 1)', 'currentState=(3)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(3)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(4)']
                )
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 4
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.y=Cop.y', 'currentState=(5)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y
            currentState = 5
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.y=(Cop.y + 1)', 'currentState=(5)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            currentState = 5
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            log_condition(
                '(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x:
            log_condition('(Cop.x == Robber.x and Cop.x > Robber.x)',
                currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x:
            log_condition('(Cop.x == Robber.x and Cop.x < Robber.x)',
                currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x:
            log_condition('(Cop.x > Robber.x and Cop.x < Robber.x)',
                currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                '(Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition('(Cop.y == Robber.y and Cop.y > Robber.y)',
                currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition('(Cop.y == Robber.y and Cop.y < Robber.y)',
                currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition('(Cop.y > Robber.y and Cop.y < Robber.y)',
                currentState, ['currentState=(20)'])
            currentState = 20
    elif currentState == 1:
        log_condition('(currentState == 1)', currentState, [])
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=(Cop.y + 1)', 'currentState=(6)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 6
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=Cop.y', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y + 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y >
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y >
    Robber.y and Cop.y < Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y >
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y >
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.x != Robber.x and Cop.y == Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y:
            log_condition(
                '(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y:
            log_condition(
                '(Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y <=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <=
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
    elif currentState == 2:
        log_condition('(currentState == 2)', currentState, [])
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y):
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.y=(Cop.y + 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(8)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 8
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=Cop.y', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y + 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 9
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', 'currentState=(10)'])
            _next_Cop.y = Cop.y + 1
            currentState = 10
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', 'currentState=(10)'])
            _next_Cop.y = Cop.y + 1
            currentState = 10
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y + 1)', 'currentState=(10)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 10
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <=
    Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.y <= Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y >= Robber.y:
            log_condition(
                '(Cop.x == Robber.x and Cop.x > Robber.x and Cop.y >= Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y:
            log_condition(
                '(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y:
            log_condition(
                '(Cop.x > Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                '(Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition('(Cop.y == Robber.y and Cop.y > Robber.y)',
                currentState, ['currentState=(20)'])
            currentState = 20
    elif currentState == 3:
        log_condition('(currentState == 3)', currentState, [])
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=Cop.y', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y + 1)', 'currentState=(11)']
                )
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 11
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=(Cop.y + 1)', 'currentState=(12)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y + 1)', 'currentState=(12)']
                )
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y + 1)', 'currentState=(12)']
                )
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y:
            log_condition(
                '(Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            log_condition(
                '(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            log_condition(
                '(Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                '(Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition('(Cop.y == Robber.y and Cop.y < Robber.y)',
                currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition('(Cop.y > Robber.y and Cop.y < Robber.y)',
                currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                '(Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
    elif currentState == 4:
        log_condition('(currentState == 4)', currentState, [])
        if (Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y):
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=(Cop.y - 1)', 'currentState=(1)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(1)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y < Robber.y)"""
                , currentState, ['_next_Cop.y=(Cop.y - 1)', 'currentState=(1)']
                )
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.y=Cop.y', '_next_Cop.y=(Cop.y - 1)', 'currentState=(1)']
                )
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(1)']
                )
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and Cop.y >
    Robber.y and Cop.y < Robber.y)"""
                , currentState, ['_next_Cop.y=(Cop.y - 1)', 'currentState=(1)']
                )
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=(Cop.y + 1)', 'currentState=(2)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y + 1)', 'currentState=(2)']
                )
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=(Cop.y + 1)', 'currentState=(2)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.y=(Cop.y + 1)', 'currentState=(2)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=(Cop.y + 1)', 'currentState=(2)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 2
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=(Cop.y - 1)', 'currentState=(3)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(3)']
                )
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=(Cop.y - 1)', 'currentState=(3)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(3)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=(Cop.y - 1)', 'currentState=(3)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y - 1
            currentState = 3
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.x=(Cop.x - 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=Cop.y', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y + 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.x=(Cop.x - 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=Cop.y', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y + 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y < Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y >
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y >
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y >
    Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=Cop.y', 'currentState=(13)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y
            currentState = 13
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y >
    Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=Cop.y', 'currentState=(13)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y
            currentState = 13
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.y=Cop.y', 'currentState=(14)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y
            currentState = 14
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.y=(Cop.y + 1)', 'currentState=(14)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            currentState = 14
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(15)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 15
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(15)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 15
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=Cop.y', '_next_Cop.y=(Cop.y - 1)', 'currentState=(15)']
                )
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y - 1
            currentState = 15
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y + 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(15)']
                )
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 15
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(16)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y - 1
            currentState = 16
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y < Robber.y)"""
                , currentState, ['_next_Cop.x=Cop.x', 'currentState=(20)'])
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <=
    Robber.y)"""
                , currentState, ['_next_Cop.x=Cop.x', 'currentState=(20)'])
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <=
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.x=Cop.x', 'currentState=(20)'])
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['_next_Cop.x=Cop.x', 'currentState=(20)'])
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <=
    Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <=
    Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >=
    Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <=
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y < Robber.y)"""
                , currentState, ['_next_Cop.y=Cop.y', 'currentState=(20)'])
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <=
    Robber.y)"""
                , currentState, ['_next_Cop.y=Cop.y', 'currentState=(20)'])
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <=
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.y=Cop.y', 'currentState=(20)'])
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['_next_Cop.y=Cop.y', 'currentState=(20)'])
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <=
    Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <=
    Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >=
    Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <=
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <=
    Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <=
    Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <=
    Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y - 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <=
    Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y - 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y - 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <=
    Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y >
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y >
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y >
    Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y >
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y >
    Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <=
    Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
    elif currentState == 5:
        log_condition('(currentState == 5)', currentState, [])
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y):
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.y=(Cop.y + 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(8)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 8
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=Cop.y', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=Cop.y', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y + 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 9
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(17)'])
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(17)'])
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(17)'])
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x:
            log_condition(
                '(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x:
            log_condition(
                '(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <=
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y >
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            log_condition(
                '(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x:
            log_condition('(Cop.x == Robber.x and Cop.x > Robber.x)',
                currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                '(Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
    elif currentState == 6:
        log_condition('(currentState == 6)', currentState, [])
        if (Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and
            Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y):
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <=
    Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.y <= Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y >= Robber.y:
            log_condition(
                '(Cop.x == Robber.x and Cop.x > Robber.x and Cop.y >= Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y:
            log_condition(
                '(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y:
            log_condition(
                '(Cop.x > Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                '(Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition('(Cop.y == Robber.y and Cop.y > Robber.y)',
                currentState, ['currentState=(20)'])
            currentState = 20
    elif currentState == 7:
        log_condition('(currentState == 7)', currentState, [])
        if (Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x:
            log_condition(
                '(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x:
            log_condition(
                '(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <=
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y >
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            log_condition(
                '(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x:
            log_condition('(Cop.x == Robber.x and Cop.x < Robber.x)',
                currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                '(Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.x <= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
    elif currentState == 8:
        log_condition('(currentState == 8)', currentState, [])
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=(Cop.y + 1)', 'currentState=(6)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 6
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', 'currentState=(12)'])
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y <=
    Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', 'currentState=(12)'])
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <=
    Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', 'currentState=(12)'])
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y <=
    Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y >
    Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(19)']
                )
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 19
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(19)']
                )
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 19
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.x != Robber.x and Cop.y > Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y:
            log_condition(
                '(Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            log_condition(
                '(Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.x > Robber.x and Cop.y > Robber.y and Cop.y < Robber.y)',
                currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <=
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y > Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
    elif currentState == 9:
        log_condition('(currentState == 9)', currentState, [])
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=(Cop.y + 1)', 'currentState=(6)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 6
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y > Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y >
    Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            log_condition(
                '(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                '(Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.x != Robber.x and Cop.y == Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.x != Robber.x and Cop.y > Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x:
            log_condition('(Cop.x > Robber.x and Cop.x < Robber.x)',
                currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x:
            log_condition(
                '(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x:
            log_condition(
                '(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x)'
                , currentState, ['currentState=(20)'])
            currentState = 20
    elif currentState == 10:
        log_condition('(currentState == 10)', currentState, [])
        if (Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=Cop.y', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y < Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y <=
    Robber.y and Cop.y < Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y <=
    Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y > Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <=
    Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                '(Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y >
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y:
            log_condition(
                '(Cop.x > Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.y=Cop.y', 'currentState=(20)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(20)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y > Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y > Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
    elif currentState == 11:
        log_condition('(currentState == 11)', currentState, [])
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <=
    Robber.y and Cop.y < Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 9
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                '(Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.x != Robber.x and Cop.y > Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            log_condition(
                '(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            log_condition(
                '(Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                '(Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <=
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y >
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
    elif currentState == 12:
        log_condition('(currentState == 12)', currentState, [])
        if (Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and
            Cop.y == Robber.y and Cop.y <= Robber.y):
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y >
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <=
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y >
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y:
            log_condition(
                '(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y > Robber.y:
            log_condition(
                '(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y > Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                '(Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.x <= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
    elif currentState == 13:
        log_condition('(currentState == 13)', currentState, [])
        if Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            log_condition(
                '(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                '(Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            log_condition(
                '(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x)'
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.x=(Cop.x + 1)', 'currentState=(20)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                '(Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)'
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.x=(Cop.x + 1)', 'currentState=(20)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            log_condition(
                '(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x)'
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.x=(Cop.x - 1)', 'currentState=(20)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                '(Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)'
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.x=(Cop.x - 1)', 'currentState=(20)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            log_condition(
                '(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x)'
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', 'currentState=(20)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                '(Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)'
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', 'currentState=(20)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            log_condition(
                '(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                '(Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            log_condition(
                '(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x)'
                , currentState,
                ['_next_Cop.y=Cop.y', '_next_Cop.y=(Cop.y + 1)', 'currentState=(20)']
                )
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                '(Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)'
                , currentState,
                ['_next_Cop.y=Cop.y', '_next_Cop.y=(Cop.y + 1)', 'currentState=(20)']
                )
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            log_condition(
                '(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x)'
                , currentState,
                ['_next_Cop.y=Cop.y', '_next_Cop.y=(Cop.y - 1)', 'currentState=(20)']
                )
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                '(Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)'
                , currentState,
                ['_next_Cop.y=Cop.y', '_next_Cop.y=(Cop.y - 1)', 'currentState=(20)']
                )
            _next_Cop.y = Cop.y
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            log_condition(
                '(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x)'
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(20)']
                )
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                '(Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)'
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(20)']
                )
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y == Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y >
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y >
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and Cop.y >
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y >
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y >
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.x=Cop.x', 'currentState=(20)'])
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y - 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.x=Cop.x', 'currentState=(20)'])
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.y=Cop.y', 'currentState=(20)'])
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['_next_Cop.x=Cop.x', 'currentState=(20)'])
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['_next_Cop.y=Cop.y', 'currentState=(20)'])
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y - 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.x=Cop.x', 'currentState=(20)'])
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y - 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.x=Cop.x', 'currentState=(20)'])
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.y=Cop.y', 'currentState=(20)'])
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['_next_Cop.x=Cop.x', 'currentState=(20)'])
            _next_Cop.x = Cop.x
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['_next_Cop.y=Cop.y', 'currentState=(20)'])
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y - 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.y=Cop.y', 'currentState=(20)'])
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x - 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['_next_Cop.y=Cop.y', 'currentState=(20)'])
            _next_Cop.y = Cop.y
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.y=(Cop.y - 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.y == Robber.y:
            log_condition('(Cop.x == Robber.x and Cop.y == Robber.y)',
                currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.y == Robber.y:
            log_condition('(Cop.x == Robber.x and Cop.y == Robber.y)',
                currentState, ['_next_Cop.x=(Cop.x + 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.y == Robber.y:
            log_condition('(Cop.x == Robber.x and Cop.y == Robber.y)',
                currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(20)'])
            _next_Cop.x = Cop.x - 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.y == Robber.y:
            log_condition('(Cop.x == Robber.x and Cop.y == Robber.y)',
                currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.y == Robber.y:
            log_condition('(Cop.x == Robber.x and Cop.y == Robber.y)',
                currentState, ['_next_Cop.y=(Cop.y + 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y + 1
            currentState = 20
        elif Cop.x == Robber.x and Cop.y == Robber.y:
            log_condition('(Cop.x == Robber.x and Cop.y == Robber.y)',
                currentState, ['_next_Cop.y=(Cop.y - 1)', 'currentState=(20)'])
            _next_Cop.y = Cop.y - 1
            currentState = 20
    elif currentState == 14:
        log_condition('(currentState == 14)', currentState, [])
        if (Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=Cop.x', '_next_Cop.y=(Cop.y + 1)', 'currentState=(6)']
                )
            _next_Cop.x = Cop.x
            _next_Cop.y = Cop.y + 1
            currentState = 6
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(18)'])
            _next_Cop.x = Cop.x + 1
            currentState = 18
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            log_condition(
                '(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                '(Cop.x != Robber.x and Cop.y == Robber.y and Cop.y > Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.x != Robber.x and Cop.y == Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.x != Robber.x and Cop.y > Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x:
            log_condition('(Cop.x == Robber.x and Cop.x > Robber.x)',
                currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x < Robber.x:
            log_condition('(Cop.x > Robber.x and Cop.x < Robber.x)',
                currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x:
            log_condition(
                '(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <=
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y >
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.y > Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
    elif currentState == 15:
        log_condition('(currentState == 15)', currentState, [])
        if (Cop.x != Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and
            Cop.y > Robber.y and Cop.y < Robber.y):
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and Cop.y >
    Robber.y and Cop.y < Robber.y)"""
                , currentState, ['_next_Cop.y=(Cop.y - 1)', 'currentState=(1)']
                )
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y >
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y >
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['_next_Cop.x=(Cop.x - 1)', 'currentState=(7)']
                )
            _next_Cop.x = Cop.x - 1
            currentState = 7
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.y=(Cop.y + 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(8)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 8
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=Cop.y', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=Cop.y', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y + 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 9
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y >
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y >
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y <=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <=
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y:
            log_condition(
                '(Cop.x == Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.x <= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
    elif currentState == 16:
        log_condition('(currentState == 16)', currentState, [])
        if (Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and
            Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y):
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y < Robber.y)"""
                , currentState, ['_next_Cop.y=(Cop.y - 1)', 'currentState=(1)']
                )
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y < Robber.y)"""
                , currentState, ['_next_Cop.y=(Cop.y - 1)', 'currentState=(1)']
                )
            _next_Cop.y = Cop.y - 1
            currentState = 1
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.y=(Cop.y + 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(8)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.y = Cop.y + 1
            _next_Cop.y = Cop.y - 1
            currentState = 8
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=Cop.y', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y - 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y - 1
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=Cop.y', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y
            currentState = 9
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', '_next_Cop.x=(Cop.x - 1)', '_next_Cop.y=(Cop.y + 1)', 'currentState=(9)']
                )
            _next_Cop.x = Cop.x + 1
            _next_Cop.x = Cop.x - 1
            _next_Cop.y = Cop.y + 1
            currentState = 9
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(17)'])
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(17)'])
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(17)'])
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(17)'])
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(17)'])
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y >
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.y != Robber.y and Cop.y >
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.y > Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y <=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y <=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <=
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y <=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x > Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x and Cop.y <= Robber.y:
            log_condition(
                '(Cop.x == Robber.x and Cop.x > Robber.x and Cop.y <= Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x and Cop.y >
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y >
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
    elif currentState == 17:
        log_condition('(currentState == 17)', currentState, [])
        if Cop.x == Robber.x and Cop.x > Robber.x:
            log_condition('(Cop.x == Robber.x and Cop.x > Robber.x)',
                currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x >= Robber.x:
            log_condition('(Cop.x >= Robber.x)', currentState,
                ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x < Robber.x:
            log_condition('(Cop.x != Robber.x and Cop.x < Robber.x)',
                currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x:
            log_condition('(Cop.x <= Robber.x and Cop.x < Robber.x)',
                currentState, ['currentState=(20)'])
            currentState = 20
    elif currentState == 18:
        log_condition('(currentState == 18)', currentState, [])
        if Cop.x != Robber.x:
            log_condition('(Cop.x != Robber.x)', currentState,
                ['currentState=(20)'])
            currentState = 20
        elif Cop.x > Robber.x:
            log_condition('(Cop.x > Robber.x)', currentState,
                ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x:
            log_condition('(Cop.x == Robber.x and Cop.x <= Robber.x)',
                currentState, ['currentState=(20)'])
            currentState = 20
    elif currentState == 19:
        log_condition('(currentState == 19)', currentState, [])
        if Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                '(Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)'
                , currentState,
                ['_next_Cop.y=(Cop.y + 1)', 'currentState=(12)'])
            _next_Cop.y = Cop.y + 1
            currentState = 12
        elif Cop.y != Robber.y:
            log_condition('(Cop.y != Robber.y)', currentState,
                ['currentState=(20)'])
            currentState = 20
        elif Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition('(Cop.y > Robber.y and Cop.y < Robber.y)',
                currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                '(Cop.y == Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
    elif currentState == 20:
        log_condition('(currentState == 20)', currentState, [])
        if (Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and
            Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y):
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(17)'])
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(17)'])
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState,
                ['_next_Cop.x=(Cop.x + 1)', 'currentState=(17)'])
            _next_Cop.x = Cop.x + 1
            currentState = 17
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y <= Robber.y and Cop.y < Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y !=
    Robber.y and Cop.y > Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x and Cop.y ==
    Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x:
            log_condition(
                '(Cop.x != Robber.x and Cop.x > Robber.x and Cop.x < Robber.x)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x:
            log_condition(
                '(Cop.x == Robber.x and Cop.x <= Robber.x and Cop.x < Robber.x)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y != Robber.y and Cop.y <=
    Robber.y and Cop.y >= Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y >
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y == Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                """(Cop.x <= Robber.x and Cop.x < Robber.x and Cop.y > Robber.y and Cop.y <
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x:
            log_condition(
                '(Cop.x != Robber.x and Cop.x <= Robber.x and Cop.x >= Robber.x)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x == Robber.x and Cop.x > Robber.x:
            log_condition('(Cop.x == Robber.x and Cop.x > Robber.x)',
                currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >= Robber.y:
            log_condition(
                """(Cop.x >= Robber.x and Cop.y != Robber.y and Cop.y <= Robber.y and Cop.y >=
    Robber.y)"""
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y:
            log_condition(
                '(Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y > Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.x >= Robber.x and Cop.y == Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
        elif Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y:
            log_condition(
                '(Cop.x >= Robber.x and Cop.y > Robber.y and Cop.y < Robber.y)'
                , currentState, ['currentState=(20)'])
            currentState = 20
    return {'currentState': currentState, 'Cop.x': _next_Cop.x, 'Cop.y':
        _next_Cop.y}
