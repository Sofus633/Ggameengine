import pygame
import time
from scene import Scene
from objectt import Circle
from vector import Vector2
from constants import FPS 
def main():
    scene = Scene()
    scene.add_obj(Circle(velo=Vector2(1, 2)))
    running = True
    while running:
        scene.next_frame()
        time.sleep(0.1)
        scene.pollevent()




main()

