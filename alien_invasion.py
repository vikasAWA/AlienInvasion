import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
def run_game():
    # Initialize pygame, settings and create a screen object.
    pygame.init()
    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien INvasion")
    
    # Make a ship
    ship = Ship(screen, ai_settings)
    bullets = Group()
    
    
    # Start the main loop for the game.
    while True:
        
        # Watch for keyboard and mouse event
        gf.check_events(ai_settings, screen, ship, bullets)
        # Moving right when Right arrow key is pressed and stop motion when key is released.
        ship.update()
        gf.update_bullets(bullets)
        # Redraw the screen during each pass through the loop.Make the most recent drawn screen visible.
        gf.update_screen(ai_settings, screen, ship, bullets)
       
run_game()