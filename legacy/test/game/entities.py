class Cop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def moveL(x):
        return x - 1
    
    def moveR(x):
        return x + 1
    
    def moveU(y):
        return y - 1
    
    def moveD(y):
        return y + 1
    
class _next_Cop:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Robber:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        # Movement State
        self.moveL = False
        self.moveR = False
        self.moveU = False
        self.moveD = False

class _next_Robber:
    def __init__(self, x, y):
        self.x = x
        self.y = y
