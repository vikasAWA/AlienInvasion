import sys 
import pygame 

class Characters():
    def __init__(self, screen, ship_speed_factor):
        self.screen = screen
        
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ship_speed_factor = ship_speed_factor
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        # Moving right flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        # Update the ship's position on base of flag.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ship_speed_factor
            
        self.rect.centerx = self.center
            
    def draw(self):
        self.screen.blit(self.image, self.rect)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    ship_speed_factor = 1.5
    
    ship = Characters(screen, ship_speed_factor)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False
        ship.update()
    
        screen.fill((230, 230, 230))
        ship.draw()
        pygame.display.flip()
    
run_game()