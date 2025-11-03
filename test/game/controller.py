from datetime import datetime
from operator import itemgetter
from entities import Robber, Cop, _next_Cop, _next_Robber, MaxX, MaxY, MinX, MinY

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
      print("error 1")
    elif (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 0
      print("error 2")
    elif not Robber.moveL and not Robber.moveR and not Robber.stayX:
      currentState = 0
      print("error 3")
    elif Robber.moveL and Robber.moveR:
      currentState = 0
      print("error 4")
    elif Robber.moveL and Robber.stayX:
      currentState = 0
      print("error 5")
    elif Robber.moveR and Robber.stayX:
      currentState = 0
      print("error 6")
    elif not Robber.moveD and not Robber.moveU and not Robber.stayY:
      currentState = 0
      print("error 7")
    elif Robber.moveD and Robber.moveU:
      currentState = 0
      print("error 8")
    elif Robber.moveD and Robber.stayY:
      currentState = 0
      print("error 9")
    elif Robber.moveU and Robber.stayY:
      currentState = 0
      print("error 10")
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