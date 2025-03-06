from constants import SCREEN_SIZE, SCREEN
from vector import Vector2
import pygame 

class Object:
    def __init__(self, pos=Vector2(SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2), freez=False, shape="circle", object_param=([5]), velo=Vector2()):
        self.pos = pos
        self.velo = velo
        self.freez = freez
        self.object_param = object_param
        self.shape = shape
        self.screen = SCREEN
        self.color = (255, 255, 122)
        self.drawfunction = self.evaluate()
        self.posind = 1 

                 
    def draw(self):
        print(self.posind)
        self.object_param[self.posind] = self.pos.get()
        self.drawfunction(*self.object_param)

    def update(self):
        print(self.pos.get())
        self.pos += self.velo
    
    def evaluate(self):
        match self.shape:
            case "circle":
                self.posind = 2 
                print(self.posind)
                self.object_param = [self.screen, self.color, self.pos.get(), self.object_param[0]] 
                return pygame.draw.circle
            case "rect":
                return pygame.draw.rect

        
class Objects:
    def __init__(self, objects=[]):
        self.objects = [*objects]
        
    def add_obj(self, obj):
        self.objects.append(obj)
    
    def rem_obj(self, obj):
        self.objects.remove(obj)

    def get(self):
        return self.objects


 

    
