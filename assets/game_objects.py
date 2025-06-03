import pygame
import time 
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
        ewewe

    def hitbox_area(self, player, enemy):
        distancex = player[0] - enemy[0]
        distancey = player[1] - enemy[1]
        distancesquared = (distancex)**2 + (distancey)**2
        sumofradiuss = 80
        return distancesquared <= (sumofradiuss)**2
        
      
        
    
class player(ship):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._width  = 50 
        self._height = 50
        self._playersprite = pygame.image.load('playership.png')
        self._playersprite = pygame.transform.scale(self._playersprite, (self._width, self._height))
        self._rotatedplayersprite = self._playersprite
        self._rect = self._playersprite.get_rect(center=(self._x, self._y))
        self._last_time = time.perf_counter()
        
    def draw(self):
        screen.blit(self._rotatedplayersprite, self._rect)
        
       
    def direction(self):
        #this gets the position of the cursor, and calculates the angle from the player to cursor than rotates the player to the angle
        mousex, mousey = pygame.mouse.get_pos()
        ptoxVector, ptoyVector = mousex - self._x, mousey - self._y
        angle = (180 / math.pi) * - math.atan2(ptoyVector, ptoxVector)
        self._rotatedplayersprite = pygame.transform.rotate(self._playersprite, int(angle))
        self._rect = self._rotatedplayersprite.get_rect(center=(self._x, self._y))
        
    def lerp_velocity(self):
        #
        currentT = time.perf_counter()
        delta_time = currentT - self._last_time
        self._last_time = currentT

        stiffnessconstant = 4
        interpolation_factor = stiffnessconstant * delta_time

        if interpolation_factor > 1:
            interpolation_factor = 1
        #Get current mouse position than use it in the formula shown in the project folio in project description, player logic
        M_xold, M_yold = pygame.mouse.get_pos()
        Pxnew = self._x + (interpolation_factor * (M_xold - self._x))
        Pynew = self._y + (interpolation_factor * (M_yold - self._y))
        return Pxnew, Pynew
    
    def update_player_pos(self):
        #update x and y coordinates
        self._x, self._y = self.lerp_velocity()

class enemy(ship):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._width = 32
        self._height = 32
        self._enemysprite = pygame.image.load('enemyship.png')
        self._enemysprite = pygame.transform.scale(self._enemysprite, (self._width, self._height))
        self._rect = self._enemysprite.get_rect(center=(self._x, self._y))

    
    def chase(self, target: ship):
        tx, ty = target.get_position()
        speed = 2 
        if self._x < tx:
            self._x += min(speed, tx - self._x)
        elif self._x > tx:
            self._x -= min(speed, self._x - tx)
        if self._y < ty:
            self._y += min(speed, ty - self._y)
        elif self._y > ty:
            self._y -= min(speed, self._y - ty)

    def draw(self):
        screen.blit(self._enemysprite, self._rect)

        
class asteroid(Game_object):
    def __init__(self, x, y):
        super.__init__(x, y)
        self._width = 32
        self._height = 32
        self._asteroidsprite = pygame.image.load('enemyship.png')
        self._asteroidsprite = pygame.transform.scale(self._enemysprite, (self._width, self._height))
        self._rect = self._enemysprite.get_rect(center=(self._x, self._y))

        
        
