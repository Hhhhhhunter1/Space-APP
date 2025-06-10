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
    font = pygame.font.SysFont(None, 48)
    #enemy spawning
    enemies = 10
    aliveenemies = []
    #pause screen variables
    paused = False
    resume_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((840, 350), (100, 60)), text='Resume', manager=manager))
    quit_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1080, 350), (100, 60)), text='Quit', manager=manager))
    gamewallpaper = pygame.image.load("gamewallpaper.png")
    gamewallpaper = pygame.transform.scale(gamewallpaper, (1920, 1080))

    for _ in range(enemies):
            randoffscreenx = random.randint(0, 1920)
            randoffscreeny = random.randint(1, 100)
            randoffscreeny = randoffscreeny * -1
            newenemy = enemy(randoffscreenx, randoffscreeny, 1)
            aliveenemies.append(newenemy)

    running = True
    while running:
        
        clock.tick(60)
        keys = pygame.key.get_pressed()

        #random spawn of enemies off screen
        

        #pausescreen
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

        player_rect = pygame.Rect(Player.get_position(), (Player._width, Player._height))
        for bullet in Player._bullets[:]:
            bullet_rect = pygame.Rect(bullet['pos'][0], bullet['pos'][1], 10, 10)
           
            for e in aliveenemies[:]:
                enemy_rect = pygame.Rect(e.get_position(), (e._width, e._height))

                if bullet_rect.colliderect(enemy_rect):
                    Player._bullets.remove(bullet)  
                    e.hurt()
                    if e.die() == True:
                        aliveenemies.remove(e) 
                        score += 3
                    break

        for e in aliveenemies:
            enemy_rect = pygame.Rect(e.get_position(), (e._width, e._height))    
            if enemy_rect.colliderect(player_rect):
                running = False
                break
        
        screen.blit(gamewallpaper, (0,0))
        
        if paused:
            pause = font.render("Game Paused", True, (255, 255, 255))
            screen.blit(pause, (890, 200))
                
        
        
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

            for e in aliveenemies:
                e.chase(Player)
                e.draw()
                
        

        
        manager.update(fpscap)
        manager.draw_ui(screen)
        pygame.display.flip()
      
    


