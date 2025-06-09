from pytmx.pytmx import rotate

from settings import *
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction, groups,game):
        super().__init__(groups)
        self.direction = direction
        self.angle = degrees(atan2(self.direction.x, self.direction.y)) -90
        self.enemy_sprites=game.enemy_sprites
        self.collision_sprites=game.collision_sprites
        self.frame = []
        self.load_images()
        self.frame_index = 0
        self.image = self.frame[self.frame_index]
        self.animation_speed = 2
        self.rect = self.image.get_frect(center=pos)
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 1000

        self.direction = direction
        self.speed = 1200
    def load_images(self):
        folder,folder1=(self.name).split('_')
        for i in range(4):
            surf = pygame.image.load(join('images', 'projectiles', f'{folder}',f'{folder1}',f'{i}.png')).convert_alpha()
            surf=pygame.transform.rotozoom(surf, self.angle, 1)
            self.frame.append(surf)
    def animate(self, dt):
        self.frame_index+=self.animation_speed*dt
        self.image = self.frame[int(self.frame_index) % len(self.frame)]
    def bullet_collision(self):
        collision_sprites=pygame.sprite.spritecollide(self,self.enemy_sprites,False,pygame.sprite.collide_mask)
        if collision_sprites:
            for sprite in collision_sprites:
                sprite.destroy()
                self.kill()
    def collision(self):
        if pygame.sprite.spritecollide(self,self.collision_sprites,False,pygame.sprite.collide_mask):
            self.kill()
    def update(self, dt):
        self.animate(dt)
        self.rect.center += self.direction * self.speed * dt
        self.collision()
        self.bullet_collision()
        if pygame.time.get_ticks() - self.spawn_time >= self.lifetime:
            self.kill()
class Gauntlet_Primary(Bullet):
    def __init__(self, pos, direction, groups,game):
        self.name='Gauntlet_Primary'
        super().__init__(pos,direction,groups,game)
class Gauntlet_Secondary(Bullet):
    def __init__(self, pos, direction, groups,game):
        self.name='Gauntlet_Secondary'
        super().__init__(pos, direction, groups, game)
class Gauntlet_SkillR(Bullet):
    def __init__(self, pos, direction, groups,game):
        self.name='Gauntlet_SkillR'
        super().__init__(pos, direction, groups, game)
    def bullet_collision(self):
        collision_sprites=pygame.sprite.spritecollide(self,self.enemy_sprites,False,pygame.sprite.collide_mask)
        if collision_sprites:
            for sprite in collision_sprites:
                sprite.destroy()