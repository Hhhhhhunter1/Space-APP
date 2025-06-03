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
        self._x = x
        self._y = y
        self._width  = 50 
        self._height = 50
        self._playersprite = pygame.image.load('playership.png')
        self._playersprite = pygame.transform.scale(self._playersprite, (self._width, self._height))
        self._rotatedplayersprite = self._playersprite
        self._rect = self._playersprite.get_rect(center=(self._x, self._y))

    def draw(self):
       screen.blit(self._rotatedplayersprite, self._rect)
        
       
    def direction(self):
        #this gets the position of the cursor, and calculates the angle from the player to cursor than rotates the player to the angle
        mousex, mousey = pygame.mouse.get_pos()
        ptoxVector, ptoyVector = mousex - self._x, mousey - self._y
        angle = (180 / math.pi) * -math.atan2(ptoyVector, ptoxVector)
        self._rotatedplayersprite = pygame.transform.rotate(self._playersprite, int(angle))
        self._rect = self._rotatedplayersprite.get_rect(center=(self._x, self._y))
        
    
    def lerp_velocity(self):

        
class enemy(ship):
    def __init__():
        
class asteroid(Game_object):
    def __init__():
        
