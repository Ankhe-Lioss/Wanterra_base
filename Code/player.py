import pygame

from settings import *
from skill import *
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, game):
        super().__init__(groups)
        #game interaction
        self.collision_sprites = game.collision_sprites
        #graphic loading
        self.load_image()
        self.facing = 'down'
        self.frame_index = 0
        self.facings=("up", "up_right", "right", "down_right", "down", "down_left", "left", "up_left")
        self.image =self.frames[self.facing][self.frame_index]
        #hitbox loading
        self.rect = self.image.get_frect(center=pos)
        self.hitbox_rect = self.rect.inflate(-20,-10)
        #mouse input
        self.mouse_direction = pygame.Vector2()
        # movement 
        self.direction = pygame.Vector2()
        #load player stat
        self.speed = 500
    def get_mouse_direction(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        player_pos = pygame.Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.mouse_direction = (mouse_pos - player_pos).normalize() if (mouse_pos-player_pos) else (mouse_pos-player_pos)

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
        # Iterate through all 8 direction
        for facing in self.frames.keys():
            for folder_path, sub_folder, file_names in walk(join('images', 'player', facing)):
                if file_names:
                    for file_name in sorted(file_names, key=lambda x: int(x.split('.')[0])):
                        full_path = join(folder_path, file_name)
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.frames[facing].append(surf)
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
    def update_facing(self):
        angle = - degrees(atan2(self.mouse_direction.x,self.mouse_direction.y)) + 180

        self.facing = self.facings[int((angle + 22.5 if angle <= 337.5 else angle + 22.5 - 360) / 45)]
    def update_animation(self, dt):
        self.frame_index = self.frame_index + (6 * dt if self.direction else 0)
        self.image = self.frames[self.facing][int(self.frame_index) % len(self.frames[self.facing])]
    def update(self, dt):

        self.get_mouse_direction()
        self.update_facing()
        self.input()
        self.move(dt)
        self.get_mouse_direction()
        self.update_animation(dt)