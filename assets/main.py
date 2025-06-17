import pygame
import sys
import random
import pygame_gui
from game_objects import player, enemy, asteroid, screen, manager, fpscap, clock


# allows main menu to be brought up in game

def main():
    manager.clear_and_reset()
    main_menu()

# homescreen
                
def main_menu():

    def start():
        
        #load the wallpaper of the main menu and buttons for different options in the menu
        mainmenuwallpaper = pygame.image.load("pixil-frame-0.png")
        mainmenuwallpaper = pygame.transform.scale(mainmenuwallpaper, (1920, 1080))
        screen.blit(mainmenuwallpaper, (0,0))

        tutwallpaper = pygame.image.load("gamewallpaper.png")
        tutwallpaper = pygame.transform.scale(tutwallpaper, (1920, 1080))
        tutplayersprite = pygame.image.load("player.png")
        tutplayersprite = pygame.transform.scale(tutplayersprite, (150, 150))
        tutenemysprite = pygame.image.load("enemyship.png")
        tutenemysprite = pygame.transform.scale(tutenemysprite, (150, 150))
        tutasteroidsprite = pygame.image.load("asteroid.png")
        tutasteroidsprite = pygame.transform.scale(tutasteroidsprite, (175, 175))
        font = pygame.font.SysFont(None, 30)
       
        playerdetails = font.render("This is your ship. It follows your cursor and fires it's guns \nwhen you press the space button.", True, (255, 255, 255))
        enemydetails = font.render("This is an enemy ship, try to shoot it before it flies into you. \nThat will reward with you three points.", True, (255, 255, 255))
        asteroiddetails = font.render("This is an asteroid, they can be destroyed with three shots \nand give you five points when they are destroyed. \nTry not to fly into them.", True, (255, 255, 255))
       
        
        Normal_mode_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((760, 450), (400, 60)), text='Normal', manager=manager))
        Ships_mode_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((760, 550), (400, 60)), text='Ships', manager=manager))
        Asteroids_mode_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((760, 650), (400, 60)), text='Asteroids', manager=manager))
        Tutorial_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((760, 750), (400, 60)), text='How to play', manager=manager))
        # exit to main menu from tutorial button
        
        Exit_game_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((760, 850), (400, 60)), text='Quit game', manager=manager))
        all_menu_buttons = [ Normal_mode_button, Ships_mode_button, Asteroids_mode_button, Tutorial_button, Exit_game_button]
        
        screenrunning = True
        intutorial = False
        while screenrunning:
                    
            #Retrieves all events that have happened since the last time this function was called
            for event in pygame.event.get():                      
                if event.type == pygame.QUIT:
                    screenrunning = False
                
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                                  
                        def hide_menu_buttons():
                            for button in all_menu_buttons:
                                button.hide()

                        if event.ui_element == Normal_mode_button:
                            screenrunning = False
                            hide_menu_buttons()            
                            normal = setter(2, 4)
                            normal.rungame()
                            
                        elif event.ui_element == Ships_mode_button:
                            screenrunning = False
                            hide_menu_buttons()   
                            ships = setter(4, 0)
                            ships.rungame()
                        elif event.ui_element == Asteroids_mode_button:
                            screenrunning = False  
                            hide_menu_buttons()
                            asteroids = setter(0, 16)
                            asteroids.rungame()
                        elif event.ui_element == Tutorial_button and not intutorial:
                            hide_menu_buttons()
                            manager.clear_and_reset() 
                            Exit_tutorial_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((760, 750), (400, 60)), text='Exit to main menu', manager=manager))
                            Exit_tutorial_button.show()
                            screen.blit(tutwallpaper, (0,0))
                            intutorial = True

                            screen.blit(tutplayersprite, (700, 150)) 
                            screen.blit(tutenemysprite, (700, 275))
                            screen.blit(tutasteroidsprite, (700, 450))
                            
                            screen.blit(playerdetails, (900, 200))
                            screen.blit(enemydetails, (900, 325))
                            screen.blit(asteroiddetails, (900, 500))

                        
                        elif event.ui_element == Exit_tutorial_button and intutorial:
                                intutorial = False
                                main()

                        elif event.ui_element == Exit_game_button:
                            screenrunning = False
                            pygame.quit()
                            sys.exit()
                    
            
                manager.process_events(event)
                manager.update(fpscap)  
                manager.draw_ui(screen)         
                pygame.display.flip()
    return start()




# game loop



class setter():
    def __init__(self, a, b): 
        self._score = 0
        self._score_timer = 0
        self._Player = player(960, 540, 1)
        self._font = pygame.font.SysFont(None, 48)
        #enemy spawning variables
        self._enemies = a
        self._aliveenemies = []
        self._newenemies = True
        self._newEscore = 10
        #asteroid spawning variables
        self._asteroids = b
        self._currentasteroids = []
        self._newasteroids = True
        #pause screen variables
        self._paused = False
        self._resume_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((890, 350), (100, 60)), text='Resume', manager=manager))
        self._quit_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((890, 550), (100, 60)), text='Quit', manager=manager))
        self._backtomenu_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((890, 450), (100, 60)), text='Exit to menu', manager=manager))
        gamewallpaper = pygame.image.load("gamewallpaper.png")
        self._gamewallpaper = pygame.transform.scale(gamewallpaper, (1920, 1080))
        deadgamewallpaper = pygame.image.load("deadgamewallpaper.png")
        self._deadgamewallpaper = pygame.transform.scale(deadgamewallpaper, (1920, 1080))

        self._setenemies()
        self._setasteroids() 

    #random spawn of enemies off screen
    def _setenemies(self):
            for _ in range(self._enemies):
                randoffscreenx = random.randint(0, 1920)
                randoffscreeny = random.randint(1, 100)
                randoffscreeny = randoffscreeny * -1
                newenemy = enemy(randoffscreenx, randoffscreeny, 1)
                self._aliveenemies.append(newenemy)
        
    

        #random spawn of asteroids off screen
    def _setasteroids(self):
            for _ in range(self._asteroids):
        
                decider = random.randint(1,2)
                if decider == 2:
                    startx = random.randint(0, 30)
                    startx = startx * -1
                else:
                    startx = random.randint(1981, 2000)
                
                starty = random.randint(0, 1080)
                newasteroid = asteroid(startx, starty, 3)
                self._currentasteroids.append(newasteroid)

    
      
    
    def rungame(self):
    
        running = True
        while running:
        
            clock.tick(60)
            keys = pygame.key.get_pressed()

            #pausescreen
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self._paused = True
                    self._resume_button.show()
                    self._quit_button.show()
                    self._backtomenu_button.show()
               
                # pause screen buttons
                
                if event.type == pygame.USEREVENT: 
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self._resume_button:       
                            self._paused = False
                        elif event.ui_element == self._backtomenu_button:
                            running = False
                            main()
                        elif event.ui_element == self._quit_button:     
                            running = False
                            pygame.quit()
                            sys.exit()
                        
               
          
                manager.process_events(event)

            if not self._paused:
                self._resume_button.hide()
                self._quit_button.hide()
                self._backtomenu_button.hide()

           
            bulletstoremove = []
            pdead = False   # whether player is dead or alive 
            gameover = False

            #calculate collisions between bullets, enemies and asteroids
            for bullet in self._Player._bullets[:]:
                bullet_rect = pygame.Rect(bullet['pos'][0], bullet['pos'][1], 10, 10)
                bulletcollision = False
                for e in self._aliveenemies[:]:
              
                        if bullet_rect.colliderect(e._rect):
                            bulletstoremove.append(bullet) 
                            e.hurt()
                        if e.die():
                            self._aliveenemies.remove(e) 
                            self._score += 3
                            bulletcollision = True
                            break

                if bulletcollision:
                    continue

                for a in self._currentasteroids[:]:
                    

                    if bullet_rect.colliderect(a._rect):
                        bulletstoremove.append(bullet) 
                        a.hurt()
                        if a.die() == True:
                            self._currentasteroids.remove(a) 
                            self._score += 3
                            
                            break

            for b in bulletstoremove:
                if b in self._Player._bullets:
                    self._Player._bullets.remove(b)

            for e in self._aliveenemies[:]:
                    for a in self._currentasteroids[:]:
                   
                        

                        if a._rect.colliderect(e._rect):
                            e.hurt()
                        if e.die() == True:
                            self._aliveenemies.remove(e) 
                            break
                                               

            #makes the player die if they collide with enemies or asteroids
            for e in self._aliveenemies:
                  
                if e._rect.colliderect(self._Player._rect):
                    pdead = True
                    break

            for a in self._currentasteroids:
                  
                if a._rect.colliderect(self._Player._rect):
                    pdead = True
                    break
        
            screen.blit(self._gamewallpaper, (0,0))

            if pdead == True:
                 gameover = True
                 screen.blit(self._deadgamewallpaper, (0,0))
                 self._backtomenu_button.show()
                 self._quit_button.show()
        
            #pause screen
            if self._paused:
                pause = self._font.render("Game Paused", True, (255, 255, 255))
                screen.blit(pause, (830, 200))
                 
            display_score = self._font.render(f"Score: { self._score}", True, (255, 255, 255))
            screen.blit(display_score, (1700, 20))
        
            #setting up game
            if not gameover:
                if not self._paused: 

                    self._score_timer += fpscap

                    if  self._score_timer >= 1.0:
                        self._score += 1
                        self._score_timer -= 1
        
                    self._Player.direction()
                    self._Player.update_player_pos()
                    self._Player.shoot(keys)
                    self._Player.draw_bullets()
                    self._Player.draw()

                    for e in self._aliveenemies:
                        e.chase(self._Player)
                        e.draw()

                    for a in self._currentasteroids:
                        a.astmove()
                        a.draw()
                    
                    if self._score < self._newEscore:
                        self._newenemies = True
                
                    while self._score >= self._newEscore and self._newenemies and self._newasteroids:
                        if self._enemies > 0:
                            self._enemies += 2
                        if self._asteroids > 0:
                            self._asteroids += 1
                        self._setenemies()
                        self._setasteroids()
                        self._newenemies = False
                        self._newEscore += 20
            
            manager.update(fpscap)
            manager.draw_ui(screen)
            pygame.display.flip()
    
    # end of game loop



main_menu()

           


    


