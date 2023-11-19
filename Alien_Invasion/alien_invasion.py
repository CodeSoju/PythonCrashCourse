import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from random import randint

class AlienInvasion:
    """OVerall class to manage game assets and behavior."""

    def __init__(self):
        """Initalize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()  # group that holds the bullets
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        self._create_stars()

        self._create_fleet() # creates a fleet of aliens
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: 
                    self._check_keydown_events(event)
            elif event.type ==pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed: 
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        #Update bullet position
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _create_star(self, x_position, y_position): 
        """Create a star and place it in the grid."""
        new_star = Star(self)
        new_star.rect.x = x_position + self._get_star_offset()
        new_star.rect.y = y_position +self._get_star_offset()
        self.stars.add(new_star)

    def _create_stars(self):
        """Create a sky full of stars."""
        #Create a star and keep adding stars until there's no room left. 
        # Spacing between stars is two star widths.
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = 2*star_width, 2*star_height
        while current_y < (self.settings.screen_height - 3 * star_height):
            while current_x < (self.settings.screen_width - 2*star_width):
                self._create_star(current_x, current_y)
                current_x += 2*star_width
            
            # Finished a row; reset x value, and increment y value
            current_x = 2*star_width
            current_y += 2*star_height 
    
    def _get_star_offset(self):
        """Return a random adjustment to a star's position."""
        offset_size = 15
        return randint(-1*offset_size, offset_size)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left
        # Spacing betwee aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size   #alien width of our first alien
        current_x, current_y = alien_width, alien_height
        # keep adding aliens while there's room to place one
        # to determine whether there's room to place another alien, compare current_x to some max 
        # value
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width   #current_x = current_x + 2*alien_width

            # Finished a row; reset x value, and increment y value
            current_x = alien_width
            current_y += 2*alien_height
        
    def _create_alien(self, x_position, y_position):
        ''' Create an alien and place it in the fleet.'''
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullets()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.stars.draw(self.screen)
            
        # Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
