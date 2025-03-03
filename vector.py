import math


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __sub__(self, other):
        assert type(other) == Vector2
        return Vector2(self.x - other.x ,self.y - other.y)

    def __add__(self, other):
        assert type(other) == Vector2
        return Vector2(self.x + other.x ,self.y + other.y)
    
    def __mul__(self, scalar):
        assert type(scalar) == int or type(scalar) == float
        return Vector2(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        assert type(scalar) == int or type(scalar) == float
        return Vector2(self.x / scalar, self.y / scalar) 
    
    def length(self):
        return math.sqrt(self.x **2 + self.y**2)
    
    def get(self):
        return [self.x, self.y]
    
    def dot(self, other):
        assert type(other) == Vector2
        return self.x * other.x + self.y * other.y