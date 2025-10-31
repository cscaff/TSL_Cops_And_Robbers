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

    def moveL(x):
        x = x - 1
        return x

    def moveR(x):
        x = x + 1
        return x

    def moveU(y):
        y = y - 1
        return y

    def moveD(y):
        y = y + 1
        return y

class _next_Robber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

_MAX_M = None
_MAX_N = None

def MaxX():
    return _MAX_M -1

def MaxY():
    return _MAX_N -1

def MinX():
    return 0

def MinY():
    return 0