import pygame 
from rocket_settings import Settings
import rocket_functions as rf
from make_rocket import Rocket


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_hieght))
    pygame.display.set_caption("Rocket")
    rocket = Rocket(screen)
    
    while True:
        rf.check_events(rocket)
        rocket.update()
        rf.update_screen(screen, ai_settings, rocket)
        
run_game()
        
                
        