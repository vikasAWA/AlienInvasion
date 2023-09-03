import pygame

class Ship():
    
    def __init__(self, screen):
        """Initialize the ship and set its starting posotion."""
        self.screen = screen
    
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Creating a moving left and right flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        # Moving right if the flag is on.
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
            
    def draw(self):
        """Draw the ship at it's current position."""
        self.screen.blit(self.image, self.rect)
   
    