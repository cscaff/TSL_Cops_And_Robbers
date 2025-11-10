
from datetime import datetime
from operator import itemgetter
from entities import Robber, Cop, _next_Cop, _next_Robber

def log_condition(cond_str, current_state, actions):
    print(f"- - - - - - - - - - - - - - - - -")
    print(f"t = {datetime.now().strftime("%H:%M:%S")}")
    print(f"[TRACE] Current State = {current_state}")
    print(f"[TRACE] Chosen Next Event Condition: {cond_str}")
    print(f"[TRACE]   Actions to Perform: [{'\n'.join(actions)}]")

def updateState(_inputs_and_cells):
  currentState, Robber.moveD, Robber.moveL, Robber.moveR, Robber.moveU, Robber.stayX, Robber.stayY, Robber.x, Robber.y, Cop.x, Cop.y = itemgetter("currentState", "Robber.moveD", "Robber.moveL", "Robber.moveR", "Robber.moveU", "Robber.stayX", "Robber.stayY", "Robber.x", "Robber.y", "Cop.x", "Cop.y")(_inputs_and_cells)

  if currentState == 0:
    if (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.y = Cop.moveD(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.y = Cop.moveU(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveD(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveU(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveD(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveU(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.y = Cop.moveD(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.y = Cop.moveU(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveD(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveU(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveD(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveU(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.y = Cop.moveD(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.y = Cop.moveU(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveD(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveU(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveD(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveU(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.y = Cop.moveU(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveU(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveU(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.y = Cop.moveU(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveU(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveU(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.y = Cop.moveU(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveU(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveU(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.y = Cop.moveD(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveD(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveD(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.y = Cop.moveD(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveD(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveD(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.y = Cop.moveD(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveD(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.y = Cop.moveD(Cop.y)
      _next_Cop.x = Cop.x
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.y
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.x > Robber.x):
      currentState = 0
    elif (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 0
    elif not Robber.moveL and not Robber.moveR and not Robber.stayX:
      currentState = 0
    elif Robber.moveL and Robber.moveR:
      currentState = 0
    elif Robber.moveL and Robber.stayX:
      currentState = 0
    elif Robber.moveR and Robber.stayX:
      currentState = 0
    elif not Robber.moveD and not Robber.moveU and not Robber.stayY:
      currentState = 0
    elif Robber.moveD and Robber.moveU:
      currentState = 0
    elif Robber.moveD and Robber.stayY:
      currentState = 0
    elif Robber.moveU and Robber.stayY:
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x <= Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveR(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y) and (Cop.x > Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveU(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and not Robber.moveR and Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x > Robber.x) and not Robber.moveL and Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x > Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and not Robber.moveU and Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x > Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and not Robber.moveD and Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0
    elif (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y) and (Cop.x > Robber.x) and Robber.moveL and not Robber.moveR and not Robber.stayX and Robber.moveD and not Robber.moveU and not Robber.stayY:
      _next_Cop.x = Cop.moveL(Cop.x)
      _next_Cop.y = Cop.moveD(Cop.y)
      currentState = 0

  return {"currentState": currentState, "Cop.x": _next_Cop.x, "Cop.y": _next_Cop.y}