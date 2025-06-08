#import lib
import os

import pygame.sprite
from random import randint, choice
from pytmx.util_pygame import load_pygame
#import code
import player
from settings import *
from player import Player
from sprites import *
from groups import *
from spawn import *
from enemies import *
from weapon import *
from projectiles import *
from setlevel import *
from cursor import *
class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Warnterra')
        self.clock = pygame.time.Clock()
        self.running = True
        pygame.mouse.set_visible(False)
        # groupsz
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        # setup
        setlevel(self)
    def run(self):
        while self.running:
            # dt
            dt = self.clock.tick(FPS) / 1000

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # update
            self.all_sprites.update(dt)
            # draw
            self.display_surface.fill('black')
            self.all_sprites.draw(self.player.rect.center)
            cursor(self)
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':

    game = Game()
    game.run()