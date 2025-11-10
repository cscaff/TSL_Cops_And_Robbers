from operator import itemgetter

class Cop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class _next_Cop:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Robber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def updateState(_inputs_and_cells):
  currentState, Robber.x, Cop.x = itemgetter("currentState", "Robber.x", "Cop.x")(_inputs_and_cells)

  if currentState == 0:
    if (Cop.x != Robber.x) and (Cop.x == 3) and (Robber.x == 0) and (Cop.x > Robber.x):
      _next_Cop.x = Cop.x - 1
      currentState = 1
    elif (Cop.x != Robber.x) and (Cop.x == 3) and (Robber.x == 0) and (Cop.x <= Robber.x):
      _next_Cop.x = Cop.x
      currentState = 2
    elif (Cop.x != Robber.x) and (Cop.x == 3) and (Robber.x == 0) and (Cop.x <= Robber.x):
      _next_Cop.x = Cop.x - 1
      currentState = 2
    elif (Cop.x == Robber.x):
      currentState = 3
    elif (Cop.x != 3):
      currentState = 3
    elif (Robber.x != 0):
      currentState = 3
  elif currentState == 1:
    if (Cop.x == Robber.x) and (Cop.x != 3) and (Robber.x == 0):
      _next_Cop.x = Cop.x
      currentState = 2
    elif (Cop.x == Robber.x) and (Cop.x != 3) and (Robber.x == 0):
      _next_Cop.x = Cop.x - 1
      currentState = 2
    elif (Cop.x != Robber.x) and (Robber.x == 0) and (Cop.x > Robber.x):
      _next_Cop.x = Cop.x
      currentState = 2
    elif (Cop.x != Robber.x) and (Robber.x == 0) and (Cop.x <= Robber.x):
      _next_Cop.x = Cop.x - 1
      currentState = 2
    elif (Cop.x == Robber.x) and (Cop.x == 3):
      currentState = 3
    elif (Cop.x == Robber.x) and (Cop.x == 3):
      _next_Cop.x = Cop.x - 1
      _next_Cop.x = Cop.x
      currentState = 3
    elif (Cop.x == Robber.x) and (Robber.x != 0):
      currentState = 3
    elif (Cop.x == Robber.x) and (Robber.x != 0):
      _next_Cop.x = Cop.x - 1
      _next_Cop.x = Cop.x
      currentState = 3
    elif (Robber.x != 0) and (Cop.x <= Robber.x):
      currentState = 3
    elif (Robber.x != 0) and (Cop.x <= Robber.x):
      _next_Cop.x = Cop.x - 1
      _next_Cop.x = Cop.x
      currentState = 3
    elif (Cop.x != Robber.x) and (Robber.x != 0) and (Cop.x > Robber.x):
      _next_Cop.x = Cop.x - 1
      _next_Cop.x = Cop.x
      currentState = 3
  elif currentState == 2:
    if (Cop.x == Robber.x) and (Cop.x != 3) and (Robber.x == 0):
      _next_Cop.x = Cop.x
      currentState = 2
    elif (Cop.x == Robber.x) and (Cop.x != 3) and (Robber.x == 0):
      _next_Cop.x = Cop.x - 1
      currentState = 2
    elif (Cop.x != Robber.x) and (Robber.x == 0):
      _next_Cop.x = Cop.x
      currentState = 2
    elif (Cop.x == Robber.x) and (Cop.x == 3):
      currentState = 3
    elif (Cop.x == Robber.x) and (Cop.x == 3):
      _next_Cop.x = Cop.x - 1
      _next_Cop.x = Cop.x
      currentState = 3
    elif (Robber.x != 0):
      currentState = 3
    elif (Robber.x != 0):
      _next_Cop.x = Cop.x - 1
      _next_Cop.x = Cop.x
      currentState = 3
  elif currentState == 3:
    if (Cop.x == Robber.x):
      currentState = 3
    elif (Cop.x <= Robber.x):
      currentState = 3
    elif (Cop.x != Robber.x) and (Cop.x > Robber.x):
      currentState = 3

  return {"currentState": currentState, "Cop.x": _next_Cop.x}

if __name__ == '__main__':
    Robber_x = 0
    Cop_x = 3
    state = 0

    while Cop_x != Robber_x:
        out = updateState(
                        {
                            "currentState": state,
                            "Robber.x": Robber_x,
                            "Cop.x": Cop_x
                        }
                        )
        Cop_x = out["Cop.x"]
        state = out["currentState"]

        print("Cop: ", Cop_x)
    
    print("Cop Captures Robber")

    