import pygame

class Ship:
    """Ship / player"""

    def __init__(self, ai_game):
        """Initialize starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load ship image and get its rectangle
        self.image = pygame.image.load("./ship.bmp")
        self.rect = self.image.get_rect()
        self.settings = ai_game.settings

        #Ship starts at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Position variables
        self.x = float(self.rect.x)

        #Movement flags
        self.moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect obj from self.x
        self.rect.x = self.x 

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)
