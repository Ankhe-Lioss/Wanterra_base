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
from player_projectiles import *
from setlevel import *
from cursor import *
from load_audio import *
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
        self.player_sprites = pygame.sprite.GroupSingle()
        # setup
        setlevel(self)
        self.spawn_numb=0
        self.wave=0
    def run(self):
        background.play(-1)
        while self.running:
            # dt
            dt = self.clock.tick(FPS) / 1000
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # update
            self.all_sprites.update(dt)
            if self.spawn_numb==0:
                spawn_enmey_wave((self.wave)%len(self.spawnlist),self)
                self.wave+=1
            # draw
            self.display_surface.fill('darkgray')
            self.all_sprites.draw(self.player.rect.center)
            cursor(self)
            pygame.display.update()
        pygame.quit()
if __name__ == '__main__':
    game = Game()
    game.run()