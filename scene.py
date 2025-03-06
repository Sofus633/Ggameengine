import pygame
from constants import SCREEN_SIZE, SCREEN
from objectt import Circle
from objects import Objects

class Scene:
    def __init__(self, screen_size=SCREEN_SIZE):
        self.screen_size = screen_size
        self.screen = SCREEN
        self.objects = Objects()

    def display(self):
        for objectt in self.objects.get():
            self.draw(objectt)

    def draw(self, obj):
        if type(obj) == Circle:
            pygame.draw.circle(self.screen, obj.color, obj.pos.get(), obj.rad)
        
    def update(self):
        for objectt in self.objects.get():
            objectt.update()

    def pollevent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    def next_frame(self):
        self.screen.fill(100)
        self.update()
        self.display()
        pygame.display.flip()
        print("flipped")
    
    def add_obj(self, obj):
        self.objects.add_obj(obj)

