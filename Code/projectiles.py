from settings import *
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction, groups,enemy_sprites):
        super().__init__(groups)
        self.load_images()
        self.image = self.bullet_surf
        self.enemy_sprites=enemy_sprites
        self.rect = self.image.get_frect(center=pos)
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 1000

        self.direction = direction
        self.speed = 1200
    def load_images(self):
        self.bullet_surf = pygame.image.load(join('..','images', 'gun', 'bullet.png')).convert_alpha()
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        self.bullet_collision()
        if pygame.time.get_ticks() - self.spawn_time >= self.lifetime:
            self.kill()
    def bullet_collision(self):
                collision_sprites=pygame.sprite.spritecollide(self,self.enemy_sprites,False,pygame.sprite.collide_mask)
                if collision_sprites:
                    for sprite in collision_sprites:
                        sprite.destroy()
                    self.kill()