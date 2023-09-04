import pygame

class Ship():
    
    def __init__(self, screen, ai_settings):
        """Initialize the ship and set its starting posotion."""
        self.screen = screen
        self.ai_settings = ai_settings
        
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
        
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        
    def update(self):
        # Moving right if the flag is on.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.speed_factor
            
        # Update the rect object from self.center
        self.rect.centerx = self.center
                    
    def draw(self):
        """Draw the ship at it's current position."""
        self.screen.blit(self.image, self.rect)
   
    