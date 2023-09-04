import pygame

class Rocket():
    def __init__(self, screen):
        self.screen = screen
        self.speed_factor = 1.5 
        
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
        # flags moving right and left
        self.moving_right = False
        self.moving_left = False
        
        #flags moving up and down
        self.moving_up = False
        self.moving_down = False
        
        
        self.center = float(self.rect.centerx)
        self.center_vertical = float(self.rect.centery)
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center_vertical -= self.speed_factor
        if self.moving_down and self.rect.bottom < 800:
            self.center_vertical += self.speed_factor
            
        self.rect.centerx = self.center
        self.rect.centery = self.center_vertical
        
    def draw(self):
        self.screen.blit(self.image, self.rect)
            
        