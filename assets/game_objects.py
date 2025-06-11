import pygame
import pygame_gui
import time 
import math
import random
import ctypes

#fixes OS scaling bug that windows does automatically making the game zoom in, makes pygame "dpi aware"
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1) 
except AttributeError:
   
    pass

pygame.init()

#Initialising screen and manager, manages gui elements 
screen = pygame.display.set_mode((1920, 1080))
manager = pygame_gui.UIManager((1920, 1080))
clock = pygame.time.Clock()
fpscap = clock.tick(60) / 1000.0
clock = pygame.time.Clock()


    


class Game_object():
    def __init__(self, x, y, health):
        self._x = x
        self._y = y
        self._health = health
    
    def get_position(self):
        return self._x, self._y
    
    def hitbox_area(self, player, enemy):
        distancex = player[0] - enemy[0]
        distancey = player[1] - enemy[1]
        distancesquared = (distancex)**2 + (distancey)**2
        sumofradiuss = 80
        return distancesquared <= (sumofradiuss)**2
    
    def hurt(self):
        self._health -= 1

    def die(self):
        if self._health <= 0:
            return True
    
class ship(Game_object):
   
   
    
    def __init__(self, x, y, health):
        super().__init__(x, y, health)
        self._bullets = []
        self._bullet_speed = 7
        self._cooldown = 5
      
        
    def shoot(self, keys):
        mousex, mousey = pygame.mouse.get_pos()
        ptoxVector, ptoyVector = mousex - self._x, mousey - self._y
        angle = math.atan2(ptoyVector, ptoxVector)
        if keys[pygame.K_SPACE]:
            if self._cooldown <= 0:
                offset = 40  
                bullet_x = self._x + math.cos(angle) * offset
                bullet_y = self._y + math.sin(angle) * offset
                bullet = {'pos': [bullet_x, bullet_y], 'angle': angle}
                self._bullets.append(bullet)
                self._cooldown = 15
            if self._cooldown > 0:
                self._cooldown -= 1

    def draw_bullets(self):
        for bullet in self._bullets[:]:
            bullet['pos'][0] += math.cos(bullet['angle']) * self._bullet_speed
            bullet['pos'][1] += math.sin(bullet['angle']) * self._bullet_speed
    
            if (bullet['pos'][0] < 0 or bullet['pos'][0] > 1920 or
                bullet['pos'][1] < 0 or bullet['pos'][1] > 1080):
                self._bullets.remove(bullet)
            else:
                pygame.draw.circle(screen, (255, 255, 255), (int(bullet['pos'][0]), int(bullet['pos'][1])), 5)

       
   
        
class player(ship):
    def __init__(self, x, y, health):
        super().__init__(x, y, health)
        self._width  = 50 
        self._height = 50
        self._playersprite = pygame.image.load('player.png')
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

        stiffnessconstant = 1.5
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
    def __init__(self, x, y, health):
        super().__init__(x, y, health)
        self._width = 32
        self._height = 32
        self._enemysprite = pygame.image.load('enemyship.png')
        self._enemysprite = pygame.transform.scale(self._enemysprite, (self._width, self._height))
        self._rect = self._enemysprite.get_rect(center=(self._x, self._y))
        self._dead = False
        self._speed = random.randint(1, 2)

    
    def chase(self, target: ship):
        tx, ty = target.get_position()
        if self._x < tx:
            self._x += min(self._speed, tx - self._x)
        elif self._x > tx:
            self._x -= min(self._speed, self._x - tx)
        if self._y < ty:
            self._y += min(self._speed, ty - self._y)
        elif self._y > ty:
            self._y -= min(self._speed, self._y - ty)

        self._rect.center = (int(self._x), int(self._y))
    def draw(self):
        screen.blit(self._enemysprite, self._rect)

        
class asteroid(Game_object):
    def __init__(self, x, y, health):
        super.__init__(x, y, health)
        self._width = 50
        self._height = 50
        self._asteroidsprite = pygame.image.load('asteroid.png')
        self._asteroidsprite = pygame.transform.scale(self._asteroidsprite, (self._width, self._height))
        self._rect = self._asteroidsprite.get_rect(center=(self._x, self._y))
        self._dead = False
    
   
    def astmove(self):
        startxy = random.randint(-30, 0), random.randint(0, 1080)
        targetxy = random.randint(1981, 2000), random.randint(0, 1080)

    def draw(self):
        screen.blit(self._asteroidsprite, self._rect)

    

        
        
