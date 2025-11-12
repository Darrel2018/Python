import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get it's rect.
        self.image = pygame.image.load("assets/images/BlueShip.png")
        self.image = pygame.transform.scale(self.image, (80, 100)) # so the ship can fit on the screen
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flag: start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.is_moving_right = False
        self.is_moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            self.is_moving_right = True
        else:
            self.is_moving_right = False
        
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            self.is_moving_left = True
        else:
            self.is_moving_left = False
        
        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)