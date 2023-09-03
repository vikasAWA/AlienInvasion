import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings and create a screen object.
    pygame.init()
    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien INvasion")
    
    # Make a ship
    ship = Ship(screen)
    
    
    # Start the main loop for the game.
    while True:
        
        # Watch for keyboard and mouse event
        gf.check_events(ship)
        
        # Moving right when Right arrow key is pressed and stop motion when key is released.
        ship.update()
        # Redraw the screen during each pass through the loop.Make the most recent drawn screen visible.
        gf.update_screen(ai_settings, screen, ship)

        
        
run_game()