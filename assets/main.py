import pygame
import sys
import random
import pygame_gui
from game_objects import player, screen, manager, fpscap

keys = pygame.key.get_pressed()
clock = pygame.time.Clock()
win = pygame.display.set_mode((1920, 1080))
def run_normal():
    
    Player = player(960, 540)

    running = True
    while running:
        
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
          
            manager.process_events(event)

        win.fill((255, 255, 255))
        Player.direction()
        Player.update_player_pos()
        
        
        Player.draw()
        

        
        manager.update(fpscap)
        manager.draw_ui(screen)
        pygame.display.flip()
      
    


