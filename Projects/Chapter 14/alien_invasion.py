import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        pygame.mixer.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Load music and sounds
        pygame.mixer.music.load("assets/audio/game_music_Airlock.mp3")
        self.shoot_sound = pygame.mixer.Sound("assets/audio/game_sound_laserShoot.mp3")
        self.alien_dead_sound = pygame.mixer.Sound("assets/audio/game_sound_alienExplosion.mp3")
        self.next_level_sound = pygame.mixer.Sound("assets/audio/game_sound_nextLevel.mp3")
        self.player_dead_sound = pygame.mixer.Sound("assets/audio/game_sound_playerDead.mp3")
        self.game_over_sound = pygame.mixer.Sound("assets/audio/game_sound_gameOver.mp3")

        # Create an instance to store game statistics,
        # and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Skip next level sound bool
        self.next_level_sound_skipped = 0

        self._create_fleet()

        # Load background image
        self.bg = pygame.image.load("assets/images/background.jpg").convert()

        # Start Alien Invasion in an active state.
        self.game_active = False

        # Make the Play Button
        self.play_button = Button(self, "Play")

        # For controlling background image
        self.bg_x = -1000
        self.bg_y = -100
        self.bg_max_speed = 1.0
        self.bg_cur_speed = 0.0

        # Start background music
        pygame.mixer.music.play(-1) # -1 means it will loop the audio
        pygame.mixer.music.set_volume(0.1)

        # Setup sounds
        self.shoot_sound.set_volume(0.03)
        self.alien_dead_sound.set_volume(0.1)
        self.next_level_sound.set_volume(0.2)
        self.player_dead_sound.set_volume(0.5)
        self.game_over_sound.set_volume(0.5)

# GPT Summary
# Initializes Pygame (graphics and sound modules).
# Sets up the game window size, caption, and frame rate control via a clock.
# Loads settings, background image, and sound effects (music, shooting, explosions, etc.).
# Creates key game objects, including:
# Ship (the player’s character),
# Bullet and Alien sprite groups,
# GameStats and Scoreboard for tracking progress,
# and a Play button to start the game.
# Initializes the alien fleet and background motion variables.
# Starts looping background music and sets individual sound volumes.
# Initial game state: game_active is False (waiting to start).
# In short: this function sets up all the core resources, visuals, sounds, and objects needed to start and run the Alien Invasion game.

    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self.update_bullets()
                self._update_aliens()
            
            self._update_screen()
            self.clock.tick(60) # set frame rate
        
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.game_active:

            # Reset the game settings.
            self.settings.initialize_dynamic_settings()

            # Start a new game when the player clicks Play.
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True # move the ship to the right.
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True # move the ship to the left.
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False # stop the ship moving to the right
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False # stop the ship moving to the left

    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.shoot_sound.play()


    def update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet postions
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
             if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
    
    
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():  
                self.stats.score += self.settings.alien_points * len(aliens)
                self.alien_dead_sound.play()

            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()


    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 6 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            
            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height
        
        if self.next_level_sound_skipped >= 2:
            self.next_level_sound.play()
        else:
            self.next_level_sound_skipped += 1
                  

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)


    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()


    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""

        for alien in self.aliens.sprites():
                alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1


    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""

        if self.stats.ships_left > 0:
            # Decrement ships_left, and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            self.player_dead_sound.play()

            # Pause
            sleep(2.0)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
            self.game_over_sound.play()


    
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.bg, (self.bg_x, self.bg_y))
        self.ship.blitme()
        self.aliens.draw(self.screen)


        # for moving the background image.
        if self.ship.is_moving_right:
            self.bg_cur_speed = self.lerp(self.bg_cur_speed, -self.bg_max_speed, 0.1)
        elif self.ship.is_moving_left:
            self.bg_cur_speed = self.lerp(self.bg_cur_speed, self.bg_max_speed, 0.1)
        else:
            self.bg_cur_speed = self.lerp(self.bg_cur_speed, 0.0, 0.01)
        
        if self.game_active: 
            self.bg_x += self.bg_cur_speed
        else:
            self.bg_cur_speed = 0.0


        # Draw the score information
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Make the most recently drawn screen visible.
        pygame.display.flip()
    

    def lerp(self, a: float, b: float, t: float) -> float:
        """
        Performs linear interpolation between two values, a and b.

        Args:
            a (float): The starting value.
            b (float): The ending value.
            t (float): The interpolation factor (typically between 0.0 and 1.0).

        Returns:
            float: The interpolated value.
        """
        return (1 - t) * a + t * b


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()