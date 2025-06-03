import pygame
import pygame_gui
import Sprites_images



pygame.init()

def main_menu():

    def start():
        #Initialising screen and manager, manages gui elements like Start game, plus sets caption as "Space APP"
        screen = pygame.display.set_mode(1920, 1080)
        manager = pygame_gui.UIManager(1920, 1080)
        pygame.display.set_caption("Space APP")
        
        #load the wallpaper of the main menu and buttons for different options in the menu
        mainmenuwallpaper = pygame.image.load("In_game_wallpaper.png")
        screen.blit(mainmenuwallpaper)
        
        Normal_mode_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 150), (100, 60)), text='Normal', manager=manager))
        Ships_mode_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 150), (100, 60)), text='Ships', manager=manager))
        Asteroids_mode_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 150), (100, 60)), text='Asteroids', manager=manager))
        Tutorial_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 150), (100, 60)), text='How to play', manager=manager))
        Exit_game_button = (pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 150), (100, 60)), text='Quit game', manager=manager))
        clock = pygame.time.Clock()
        screenrunning = True
        while screenrunning:
            #Set the maximum fps as 60
            fpscap = clock.tick(60) / 1000.0
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
                            pygame.QUIT 
            
            manager.process_events(event)
            #This part updates our game at the rate of fpscap, draws everthing on screen such as ui elements and shows everything that has been drawn since the last update
            manager.update(fpscap) 
            manager.draw_ui(screen)
            pygame.display.flip()
        start()

main_menu()