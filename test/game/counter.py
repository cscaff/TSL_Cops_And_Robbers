# Unrealizableß
  if currentState == 0:
    if   _next_Cop.x = Cop.x:
      (Cop.x >= Robber.x) and (minX == 0) and (maxX == 3) and (MinX < MaxX) and (Robber.x <= MaxX) and (Robber.x >= MinX) and (Robber.x == 1) and (Cop.x >= MinX) and (Cop.x <= MaxX)
      currentState = 0
    elif   _next_Cop.x = Cop.x:
      (Cop.x <= Robber.x) and (minX == 0) and (maxX == 3) and (MinX < MaxX) and (Robber.x <= MaxX) and (Robber.x >= MinX) and (Robber.x == 1) and (Cop.x >= MinX) and (Cop.x <= MaxX)
      currentState = 0
    elif   _next_Cop.x = Cop.x + 1:
      (Cop.x >= Robber.x) and (Cop.x != Robber.x) and (minX == 0) and (maxX == 3) and (MinX < MaxX) and (Robber.x <= MaxX) and (Robber.x >= MinX) and (Robber.x == 1) and (Cop.x >= MinX) and (Cop.x <= MaxX)
      currentState = 0
    elif   _next_Cop.x = Cop.x - 1:
      (Cop.x <= Robber.x) and (Cop.x != Robber.x) and (minX == 0) and (maxX == 3) and (MinX < MaxX) and (Robber.x <= MaxX) and (Robber.x >= MinX) and (Robber.x == 1) and (Cop.x >= MinX) and (Cop.x <= MaxX)
      currentState = 0



# Natural Language:
# IF