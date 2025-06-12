import pygame
import pygame_gui
import sys
from main import run_normal
from game_objects import screen, manager, fpscap
                
def main_menu():

    def start():
        
        #load the wallpaper of the main menu and buttons for different options in the menu
        mainmenuwallpaper = pygame.image.load("pixil-frame-0.png")
        mainmenuwallpaper = pygame.transform.scale(mainmenuwallpaper, (1920, 1080))
        screen.blit(mainmenuwallpaper, (0,0))
        
        
        Normal_mode_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((760, 450), (400, 60)), text='Normal', manager=manager))
        Ships_mode_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((760, 550), (400, 60)), text='Ships', manager=manager))
        Asteroids_mode_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((760, 650), (400, 60)), text='Asteroids', manager=manager))
        Tutorial_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((760, 750), (400, 60)), text='How to play', manager=manager))
        Exit_game_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((760, 850), (400, 60)), text='Quit game', manager=manager))
        
        all_menu_buttons = [ Normal_mode_button, Ships_mode_button, Asteroids_mode_button, Tutorial_button, Exit_game_button]
        
        screenrunning = True
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
                            run_normal()
                        elif event.ui_element == Ships_mode_button:
                            screenrunning = False
                            hide_menu_buttons()
                            run_ships()
                        elif event.ui_element == Asteroids_mode_button:
                            screenrunning = False  
                            hide_menu_buttons()
                            run_asteroids()
                        elif event.ui_element == Tutorial_button:
                            screenrunning = False
                            hide_menu_buttons()
                            run_tut()
                        elif event.ui_element == Exit_game_button:
                            screenrunning = False
                            pygame.quit()
                            sys.exit()
                    
            
            manager.process_events(event)
            manager.update(fpscap)  
            manager.draw_ui(screen)
            pygame.display.flip()
    start()

main_menu()