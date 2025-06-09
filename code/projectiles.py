from settings import *
from stats import *
class Projectiles(pygame.sprite.Sprite):
    def __init__(self, pos, direction, groups,game):
        super().__init__(groups)
        #load interaction
        self.collision_sprites=game.collision_sprites
        #load bullet direction
        self.direction = direction
        self.angle = degrees(atan2(self.direction.x, self.direction.y)) -90
        #load graphic
        self.frames = []
        self.load_images()
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.animation_speed = 2
        #load rect
        self.rect = self.image.get_frect(center=pos)
        #load live stat
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 1000
        #load combat stat
    def load_images(self):
        folder,folder1=(self.name).split('_')
        for i in range(4):
            surf = pygame.image.load(join('images', 'projectiles', f'{folder}',f'{folder1}',f'{i}.png')).convert_alpha()
            surf=pygame.transform.rotozoom(surf, self.angle, 1)
            self.frames.append(surf)
    def animate(self, dt):
        self.frame_index+=self.animation_speed*dt
        self.image = self.frames[int(self.frame_index) % len(self.frames)]

    def bullet_collision(self):
        dmg = self.atk * self.user.atk

        # Initialize a hit tracker if it doesn't exist yet
        if not hasattr(self, 'hit_enemies'):
            self.hit_enemies = set()

        # Check for collisions
        collision_sprites = pygame.sprite.spritecollide(self, self.enemy_sprites, False, pygame.sprite.collide_mask)
        if collision_sprites:
            for sprite in collision_sprites:
                if sprite not in self.hit_enemies:
                    sprite.take_damage(dmg)
                    if hasattr(self,'special_effect'):
                        self.special_effect(sprite)
                    # Kill bullet if not piercing
                    if hasattr(self, 'enemy_piercing'):
                        self.hit_enemies.add(sprite)
                    else:
                        self.kill()
                        break

    def collision(self):
        if pygame.sprite.spritecollide(self,self.collision_sprites,False,pygame.sprite.collide_mask):
            if not hasattr(self,'wall_penetrate'):
                self.kill()
    def move(self,dt):
        self.rect.center += self.direction * self.speed * dt

    def update(self, dt):
        self.animate(dt)
        self.move(dt)
        self.collision()
        self.bullet_collision()
        if pygame.time.get_ticks() - self.spawn_time >= self.lifetime:
            self.kill()