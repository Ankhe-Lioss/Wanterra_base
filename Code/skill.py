from settings import *
from projectiles import *
class Shoot():
    def __init__(self, weapon):
        self.weapon=weapon
        self.can_shoot = True
        self.shoot_time = 0
        self.gun_cooldown = 1000
    def input(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            pos = self.weapon.rect.center + self.weapon.player_direction * 50
            Bullet(pos, self.weapon.player_direction, (self.weapon.game.all_sprites, self.weapon.game.bullet_sprites),self.weapon.game.enemy_sprites)
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

    def gun_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.gun_cooldown:
                self.can_shoot = True