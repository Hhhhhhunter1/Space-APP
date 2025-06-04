import pygame
import pygame_gui
import sys
from main import run_normal
from game_objects import screen, manager, fpscap


def main_menu():

    def start():
        
        #load the wallpaper of the main menu and buttons for different options in the menu
        mainmenuwallpaper = pygame.image.load("In_game_wallpaper.png")
        mainmenuwallpaper = pygame.transform.scale(mainmenuwallpaper, (1920, 1080))
        screen.blit(mainmenuwallpaper, (0,0))
        
        Normal_mode_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 350), (100, 60)), text='Normal', manager=manager))
        Ships_mode_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 450), (100, 60)), text='Ships', manager=manager))
        Asteroids_mode_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 550), (100, 60)), text='Asteroids', manager=manager))
        Tutorial_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 650), (100, 60)), text='How to play', manager=manager))
        Exit_game_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 750), (100, 60)), text='Quit game', manager=manager))
        screenrunning = True
        while screenrunning:
            
            #Retrieves all events that have happened since the last time this function was called
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    screenrunning = False

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == Normal_mode_button:
                            screenrunning = False
                            run_normal()
                        if event.ui_element == Ships_mode_button:
                            screenrunning = False
                            run_ships()
                        if event.ui_element == Asteroids_mode_button:
                            screenrunning = False  
                            run_asteroids()
                        if event.ui_element == Tutorial_button:
                            screenrunning = False
                            run_tut()
                        if event.ui_element == Exit_game_button:
                            screenrunning = False
                            pygame.quit()
                            sys.exit()
            
            manager.process_events(event)
            #This part updates our game at the rate of fpscap, draws everthing on screen such as ui elements and shows everything that has been drawn since the last update
            manager.update(fpscap) 
            manager.draw_ui(screen)
            pygame.display.flip()
    start()

main_menu()