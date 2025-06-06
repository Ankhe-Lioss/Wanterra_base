import pygame

from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.load_image()
        self.state = 'down'
        self.frame = 0
        self.image = pygame.image.load(join('images', 'player', 'down', '0.png')).convert_alpha()
        self.rect = self.image.get_frect(center=pos)
        self.hitbox_rect = self.rect.inflate(-20,-10)

        # movement 
        self.direction = pygame.Vector2()
        self.speed = 500
        self.collision_sprites = collision_sprites
        self.frame_index = 0
    def load_image(self):
        # Include the 8 directions
        self.frames = {
            'left': [],
            'right': [],
            'up': [],
            'down': [],
            'up_right': [],
            'up_left': [],
            'down_right': [],
            'down_left': []
        }
        # Iterate through all 8 states
        for state in self.frames.keys():
            for folder_path, sub_folder, file_names in walk(join('images', 'player', state)):
                if file_names:
                    for file_name in sorted(file_names, key=lambda x: int(x.split('.')[0])):
                        full_path = join(folder_path, file_name)
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.frames[state].append(surf)
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - int(keys[pygame.K_LEFT] or keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_DOWN] or keys[pygame.K_s]) - int(keys[pygame.K_UP] or keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self, dt):
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')
        self.rect.center = self.hitbox_rect.center

    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                if direction == 'horizontal':
                    if self.direction.x > 0: self.hitbox_rect.right = sprite.rect.left
                    if self.direction.x < 0: self.hitbox_rect.left = sprite.rect.right
                else:
                    if self.direction.y < 0: self.hitbox_rect.top = sprite.rect.bottom
                    if self.direction.y > 0: self.hitbox_rect.bottom = sprite.rect.top
    def update_state(self):
        if self.direction.x != 0 or self.direction.y != 0:
            # Cardinal directions
            if self.direction.x > 0 and self.direction.y == 0:
                self.state = 'right'
            elif self.direction.x < 0 and self.direction.y == 0:
                self.state = 'left'
            elif self.direction.y > 0 and self.direction.x == 0:
                self.state = 'down'
            elif self.direction.y < 0 and self.direction.x == 0:
                self.state = 'up'
            # Diagonal directions
            elif self.direction.x > 0 and self.direction.y > 0:
                self.state = 'down_right'
            elif self.direction.x > 0 and self.direction.y < 0:
                self.state = 'up_right'
            elif self.direction.x < 0 and self.direction.y > 0:
                self.state = 'down_left'
            elif self.direction.x < 0 and self.direction.y < 0:
                self.state = 'up_left'
    def update_animation(self, dt):
        self.frame_index = self.frame_index + (5 * dt if self.direction else 0)
        self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]
    def update(self, dt):
        self.update_state()
        self.input()
        self.move(dt)
        self.update_animation(dt)