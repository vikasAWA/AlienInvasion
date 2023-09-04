import pygame
import sys

def run_game():
    # Initialize pygame and create a screen object.
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pygame Key Events")

    # Set the background color
    bg_color = (255, 255, 255)  # White background color

    # Start the main loop for the game.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Print the key code when a KEYDOWN event is detected
                print(f"Key pressed: {event.key}")

        # Redraw the screen with the background color
        screen.fill(bg_color)

        # Update the display
        pygame.display.flip()

run_game()
