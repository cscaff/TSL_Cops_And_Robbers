from operator import itemgetter
from entities import Robber, Cop, _next_Cop

# INJECT START
def updateState(_inputs_and_cells):
  currentState, Robber.x, Robber.y, Cop.x, Cop.y = itemgetter("currentState", "Robber.x", "Robber.y", "Cop.x", "Cop.y")(_inputs_and_cells)

  if currentState == 0:
    if (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y - 1
      currentState = 1
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y + 1
      currentState = 2
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y + 1
      currentState = 2
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y + 1
      currentState = 2
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.y = Cop.y + 1
      currentState = 2
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y
      _next_Cop.y = Cop.y + 1
      currentState = 2
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y + 1
      _next_Cop.y = Cop.y - 1
      currentState = 2
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y - 1
      currentState = 3
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y - 1
      currentState = 3
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y - 1
      currentState = 3
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.y = Cop.y - 1
      currentState = 3
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y - 1
      currentState = 4
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.y = Cop.y
      currentState = 5
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.y = Cop.y + 1
      currentState = 5
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x):
      currentState = 20
    elif (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
  elif currentState == 1:
    if (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y + 1
      currentState = 6
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y
      currentState = 7
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y + 1
      currentState = 7
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 9
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
  elif currentState == 2:
    if (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.y = Cop.y + 1
      _next_Cop.y = Cop.y - 1
      currentState = 8
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y + 1
      currentState = 9
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y + 1
      currentState = 10
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y + 1
      currentState = 10
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y + 1
      currentState = 10
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
  elif currentState == 3:
    if (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y - 1
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y + 1
      currentState = 11
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y + 1
      currentState = 12
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y + 1
      currentState = 12
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y + 1
      currentState = 12
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.y != Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y):
      currentState = 20
    elif (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.y == Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.y == Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
  elif currentState == 4:
    if (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y - 1
      currentState = 1
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.y = Cop.y - 1
      currentState = 1
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y - 1
      currentState = 1
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y
      _next_Cop.y = Cop.y - 1
      currentState = 1
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y + 1
      _next_Cop.y = Cop.y - 1
      currentState = 1
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y - 1
      currentState = 1
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y + 1
      currentState = 2
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y + 1
      currentState = 2
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y + 1
      currentState = 2
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.y = Cop.y + 1
      currentState = 2
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y + 1
      currentState = 2
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y - 1
      currentState = 3
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y - 1
      currentState = 3
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y - 1
      currentState = 3
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.y = Cop.y - 1
      currentState = 3
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y - 1
      currentState = 3
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.x = Cop.x - 1
      currentState = 7
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      currentState = 7
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y
      currentState = 7
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y + 1
      currentState = 7
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 7
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.x = Cop.x - 1
      currentState = 7
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      currentState = 7
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y
      currentState = 7
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y + 1
      currentState = 7
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 7
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 7
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 7
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 7
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 7
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 7
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y
      currentState = 13
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y
      currentState = 13
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.y = Cop.y
      currentState = 14
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.y = Cop.y + 1
      currentState = 14
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y - 1
      currentState = 15
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y - 1
      currentState = 15
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y
      _next_Cop.y = Cop.y - 1
      currentState = 15
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y + 1
      _next_Cop.y = Cop.y - 1
      currentState = 15
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.y = Cop.y - 1
      currentState = 16
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y <= Robber.y):
      _next_Cop.x = Cop.x
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y <= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y <= Robber.y):
      _next_Cop.y = Cop.y
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y + 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y <= Robber.y):
      _next_Cop.y = Cop.y + 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y + 1
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y + 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y + 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y):
      _next_Cop.y = Cop.y + 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y + 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y - 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y):
      _next_Cop.y = Cop.y - 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y - 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
  elif currentState == 5:
    if (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.y = Cop.y + 1
      _next_Cop.y = Cop.y - 1
      currentState = 8
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y - 1
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y + 1
      currentState = 9
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 17
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 17
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 17
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x < Robber.x):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x):
      currentState = 20
    elif (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
  elif currentState == 6:
    if (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
  elif currentState == 7:
    if (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x < Robber.x):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
  elif currentState == 8:
    if (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y + 1
      currentState = 6
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y + 1
      currentState = 12
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y + 1
      currentState = 12
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y + 1
      currentState = 12
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y + 1
      _next_Cop.y = Cop.y - 1
      currentState = 19
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y + 1
      _next_Cop.y = Cop.y - 1
      currentState = 19
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.y != Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
  elif currentState == 9:
    if (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y + 1
      currentState = 6
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x):
      currentState = 20
  elif currentState == 10:
    if (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y
      currentState = 7
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y - 1
      currentState = 7
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.y = Cop.y
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.y = Cop.y - 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y >= Robber.y):
      currentState = 20
  elif currentState == 11:
    if (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 9
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y):
      currentState = 20
    elif (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
  elif currentState == 12:
    if (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 7
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 7
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
  elif currentState == 13:
    if (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x):
      currentState = 20
    elif (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x):
      _next_Cop.x = Cop.x
      _next_Cop.x = Cop.x + 1
      currentState = 20
    elif (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.x = Cop.x + 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x):
      _next_Cop.x = Cop.x
      _next_Cop.x = Cop.x - 1
      currentState = 20
    elif (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.x = Cop.x - 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      currentState = 20
    elif (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x):
      currentState = 20
    elif (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x):
      _next_Cop.y = Cop.y
      _next_Cop.y = Cop.y + 1
      currentState = 20
    elif (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y
      _next_Cop.y = Cop.y + 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x):
      _next_Cop.y = Cop.y
      _next_Cop.y = Cop.y - 1
      currentState = 20
    elif (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y
      _next_Cop.y = Cop.y - 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x):
      _next_Cop.y = Cop.y + 1
      _next_Cop.y = Cop.y - 1
      currentState = 20
    elif (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y + 1
      _next_Cop.y = Cop.y - 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.y != Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y + 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y - 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y + 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y - 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y + 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y - 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y + 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y - 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y + 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y - 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.y == Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.y == Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.y == Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.y == Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.y == Robber.y):
      _next_Cop.y = Cop.y + 1
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.y == Robber.y):
      _next_Cop.y = Cop.y - 1
      currentState = 20
  elif currentState == 14:
    if (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x
      _next_Cop.y = Cop.y + 1
      currentState = 6
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 18
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x < Robber.x):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
  elif currentState == 15:
    if (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y - 1
      currentState = 1
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 7
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 7
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x - 1
      currentState = 7
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.y = Cop.y + 1
      _next_Cop.y = Cop.y - 1
      currentState = 8
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y - 1
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y + 1
      currentState = 9
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x < Robber.x) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
  elif currentState == 16:
    if (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y - 1
      currentState = 1
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      _next_Cop.y = Cop.y - 1
      currentState = 1
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.y = Cop.y + 1
      _next_Cop.y = Cop.y - 1
      currentState = 8
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y - 1
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y
      currentState = 9
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      _next_Cop.x = Cop.x - 1
      _next_Cop.y = Cop.y + 1
      currentState = 9
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 17
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 17
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 17
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 17
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 17
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x) and (Cop.y <= Robber.y):
      currentState = 20
    elif (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x < Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
  elif currentState == 17:
    if (Cop.x == Robber.x) and (Cop.x > Robber.x):
      currentState = 20
    elif (Cop.x >= Robber.x):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x < Robber.x):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.x < Robber.x):
      currentState = 20
  elif currentState == 18:
    if (Cop.x != Robber.x):
      currentState = 20
    elif (Cop.x > Robber.x):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x):
      currentState = 20
  elif currentState == 19:
    if (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.y = Cop.y + 1
      currentState = 12
    elif (Cop.y != Robber.y):
      currentState = 20
    elif (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.y == Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
  elif currentState == 20:
    if (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 17
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 17
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      _next_Cop.x = Cop.x + 1
      currentState = 17
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y > Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x) and (Cop.x < Robber.x):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x <= Robber.x) and (Cop.x < Robber.x):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x <= Robber.x) and (Cop.x < Robber.x) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x != Robber.x) and (Cop.x <= Robber.x) and (Cop.x >= Robber.x):
      currentState = 20
    elif (Cop.x == Robber.x) and (Cop.x > Robber.x):
      currentState = 20
    elif (Cop.x >= Robber.x) and (Cop.y != Robber.y) and (Cop.y <= Robber.y) and (Cop.y >= Robber.y):
      currentState = 20
    elif (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y > Robber.y):
      currentState = 20
    elif (Cop.x >= Robber.x) and (Cop.y == Robber.y) and (Cop.y < Robber.y):
      currentState = 20
    elif (Cop.x >= Robber.x) and (Cop.y > Robber.y) and (Cop.y < Robber.y):
      currentState = 20

  return {"currentState": currentState, "Cop.x": _next_Cop.x, "Cop.y": _next_Cop.y}
# INJECT END 