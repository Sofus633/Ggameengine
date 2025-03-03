from constants import SCREEN_SIZE
from vector import Vector2


class Object:
    def __init__(self, pos=(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2), freez=False, shape="circle"):
        self.pos = pos
        self.velo = Vector2()
        self.freez = freez
        self.shape = shape
    def draw(self):
        
        
class Objects:
    def __init__(self, objects):
        self.objects = [*objects]
        
    def add_obj(self, obj):
        self.objects.append(obj)
    
    def rem_obj(self, obj):
        self.objects.remove(obj)


