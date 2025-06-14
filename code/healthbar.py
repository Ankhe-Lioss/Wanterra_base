from settings import *
from livingentity import *
import pygame
from os.path import join

health_bar_full_image = pygame.image.load(join('images', 'UI', 'health_bar', '5.png'))
health_bar_empty_image = pygame.image.load(join('images', 'UI', 'health_bar', '0.png'))
class Healthbar():
    def __init__(self,user):
        Background_healthbar(user)
        Percentage_healthbar(user)

class Background_healthbar(pygame.sprite.Sprite):
    def __init__(self,user):
        super().__init__(user.game.all_sprites)
        self.user = user
        self.image = health_bar_empty_image
        self.rect = self.image.get_rect(topleft=(user.rect.x + 10, user.rect.y - 10))
    def update(self, dt):
        if self.user.hp <= 0:
            self.kill()
            return
        self.rect.topleft = (self.user.rect.x + 10, self.user.rect.y - 10)

class Percentage_healthbar(pygame.sprite.Sprite):
    def __init__(self, user):
        super().__init__(user.game.all_sprites)
        self.user = user
        self.original_image = health_bar_full_image  # Keep the original full bar image
        self.image = self.original_image.copy()  # Create an editable copy
        self.rect = self.image.get_rect(topleft=(user.rect.x + 10, user.rect.y - 10))

    def update(self, dt):
        if self.user.hp <= 0:
            self.kill()
            return

        # Update position
        self.rect.topleft = (self.user.rect.x + 10, self.user.rect.y - 10)

        # Calculate health percentage, clamped between 0 and 1
        health_percentage = max(0, min(1, self.user.hp / self.user.maxhp))

        # Get dimensions of the original image
        full_width = self.original_image.get_width()
        full_height = self.original_image.get_height()

        # Calculate new width for the chopped health bar
        new_width = 1+int((full_width-2) * health_percentage)

        # Create a rectangle for the subsurface
        chopped_rect = pygame.Rect(0, 0, new_width, full_height)

        # Extract subsurface safely
        self.image = self.original_image.subsurface(chopped_rect).copy()

