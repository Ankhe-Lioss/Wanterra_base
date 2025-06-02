from settings import *
class Poro(pygame.sprite.Sprite):
    def __init__(self, pos, groups, player,enemysprite,collision_sprites):
        super().__init__(groups)
        self.player = player
        #load
        self.load_frames()
        # image
        self.frame_index=0
        self.image = self.frames[self.frame_index]
        self.animation_speed = 6
        self.enemy_sprite=enemysprite
        # rect
        self.rect = self.image.get_frect(center=pos)
        self.hitbox_rect = self.rect.inflate(0, 0)
        self.collision_sprites = collision_sprites
        self.direction = pygame.Vector2()
        self.speed = 350
        self.death_time=0
        self.death_duration=400

    def load_frames(self):
        self.frames = []

        for i in range(0, 6):
            surf = pygame.image.load(join('..','images', 'enemies', 'Poro', f'{i}.png')).convert_alpha()
            self.frames.append(surf)

    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        self.image = self.frames[int(self.frame_index) % len(self.frames)]

    def move(self, dt):
        # get direction
        player_pos = pygame.Vector2(self.player.rect.center)
        enemy_pos = pygame.Vector2(self.rect.center)
        self.direction = (player_pos - enemy_pos).normalize() if (player_pos-enemy_pos) else (player_pos-enemy_pos)

        # update the rect position + collision
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal',dt)
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision('vertical',dt)
        self.rect.center = self.hitbox_rect.center

    def collision(self, direction,dt):
        for sprite in self.collision_sprites:
                if sprite.rect.colliderect(self.hitbox_rect):
                    if direction == 'horizontal':
                        if self.direction.x > 0: self.hitbox_rect.right = sprite.rect.left
                        if self.direction.x < 0: self.hitbox_rect.left = sprite.rect.right
                    else:
                        if self.direction.y < 0: self.hitbox_rect.top = sprite.rect.bottom
                        if self.direction.y > 0: self.hitbox_rect.bottom = sprite.rect.top
        for sprite in self.enemy_sprite:
                if self!=sprite:
                    if sprite.rect.colliderect(self.hitbox_rect):
                        if direction == 'horizontal':
                            self.hitbox_rect.x -= self.direction.x * self.speed * dt
                        else:
                            self.hitbox_rect.y -= self.direction.y * self.speed * dt
    def destroy(self):
        self.death_time=pygame.time.get_ticks()
        destroy_surf=pygame.mask.from_surface(self.frames[0]).to_surface()
        destroy_surf.set_colorkey('black')
        self.image=destroy_surf
    def death_timer(self):
        if pygame.time.get_ticks()-self.death_time>=self.death_duration:
            self.kill()

    def update(self, dt):
        if self.death_time==0:
            self.move(dt)
            self.animate(dt)
        else:
            self.death_timer()

