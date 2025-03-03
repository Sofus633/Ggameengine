import pygame
from constants import SCREEN_SIZE
from object import Objects

class Scene:
    def __init__(self, screen_size=SCREEN_SIZE):
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(self.screen_size)
        self.objects = Objects()

    def display(self):
        for object in self.objects:
            object.draw()

