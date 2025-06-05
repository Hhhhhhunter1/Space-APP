import pygame
import sys
import random
import pygame_gui
import time
from game_objects import player, enemy, ship, screen, manager, fpscap, clock




def run_normal():
    
    score = 0
    score_timer = 0
    Player = player(960, 540, 1)
    Enemy = enemy(800, 900, 1)
    font = pygame.font.SysFont(None, 48)
    paused = False
    resume_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((780, 350), (100, 60)), text='Resume', manager=manager))
    quit_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((900, 350), (100, 60)), text='Quit', manager=manager))
    gamewallpaper = pygame.image.load("gamewallpaper.png")
    gamewallpaper = pygame.transform.scale(gamewallpaper, (1920, 1080))

    running = True
    while running:
        
        clock.tick(60)
        keys = pygame.key.get_pressed()

       

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused = True
                resume_button.show()
                quit_button.show()
               
                
                
            if event.type == pygame.USEREVENT: 
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == resume_button:
                        paused = False
                    elif event.ui_element == quit_button:     
                        running = False
                        pygame.quit()
                        sys.exit()
               
          
            manager.process_events(event)

        if not paused:
            resume_button.hide()
            quit_button.hide()

        for bullet in Player._bullets[:]:
            bullet_rect = pygame.Rect(bullet['pos'][0], bullet['pos'][1], 10, 10)
            enemy_rect = pygame.Rect(Enemy.get_position(), (Enemy._width, Enemy._height))

            if bullet_rect.colliderect(enemy_rect):
                Player._bullets.remove(bullet)  
                Enemy.hurt()
                if Enemy.die() == True:
                    Enemy._dead = True
                    score += 3
        
        screen.blit(gamewallpaper, (0,0))
        
        if paused:
            pause = font.render("Game Paused", True, (255, 255, 255))
            screen.blit(pause, (780, 200))
                
        
        
        display_score = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(display_score, (1700, 20))
        
        
        if not paused: 

            score_timer += fpscap

            if score_timer >= 1.0:
                score += 1
                score_timer -= 1

            Player.direction()
            Player.update_player_pos()
            Player.shoot(keys)
            Player.draw_bullets()
            Player.draw()

            if not Enemy._dead:
                Enemy.chase(Player)
                Enemy.draw()
        

        
        manager.update(fpscap)
        manager.draw_ui(screen)
        pygame.display.flip()
      
    


