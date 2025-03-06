from vector import Vector2
import pygame


class Circle:
    def __init__(self, pos=Vector2(400, 400), velo=Vector2(), rad=10,color=(255, 255, 122)):
        self.pos = pos
        self.velo = velo
        self.rad = rad
        self.color = color

    def update(self):
        self.pos += self.velo
        if pos.x > SCREEN_SIZE[0]:
            self.collide()
        if pos.y > SCREEN_SIZE[1]:
            self.collide()
        if 
        print(self.pos.get())

    def get(self):
        return [self.color, self.pos.get(), self.rad]

