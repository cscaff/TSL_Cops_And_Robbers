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