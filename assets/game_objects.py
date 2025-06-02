import pygame
import math

class Game_object():
    def __init__(self, velocity=0, x, y):
        self.Velocity = velocity
        self._x = x
        self._y = y
    
    def get_position(self):
        return self._x, self._y
    
class ship(Game_object):
    def __init__(self, x, y):
        super().__init__(x, y)

    def shoot():

    def area(x, y):
        rectwidthx = x - 16
        rectwidthy = y - 16
        
    
class player(ship):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw():
        width  = 50  # Or whatever size you want it to be.
        height = 50
        playersprite = pygame.image.load('Untitled.png').convert()
        playersprite = pygame.transform.scale(playersprite, (width, height))
       
    def direction(playersprite):
        mousex, mousey = pygame.mouse.get_pos()
        ptoxVector, ptoyVector = mousex - self._x, mousey - self._y
        angle = (180 / math.pi) * -math.atan2(ptoyVector, ptoxVector)
        
    
    def direction():
        
class enemy(ship):
    def __init__():
        
class asteroid(Game_object):
    def __init__():
        
