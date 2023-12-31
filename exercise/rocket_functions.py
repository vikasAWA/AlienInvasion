import pygame 
import sys

def check_keydown_events(event, rocket):
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_UP:
        rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True
        
def check_keyup_events(event, rocket):
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False

def check_events(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            # Check Keydown Events
            check_keydown_events(event, rocket)
        
        elif event.type == pygame.KEYUP:
            # check keyup events
            check_keyup_events(event, rocket)
            
def update_screen(screen, ai_settings, rocket):
    screen.fill(ai_settings.bg_color)
    rocket.draw()
    pygame.display.flip()
        