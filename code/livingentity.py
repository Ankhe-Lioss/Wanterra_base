from settings import *
from stats import *
from status import *
from healthbar import *
class LivingEntity(pygame.sprite.Sprite):
    def __init__(self,groups,game):
        super().__init__((groups,game.all_sprites))
        self.game=game
        self.level=game.level
        #interaction
        self.collision_sprites = game.collision_sprites
        # self.stat
        self.stat=entity_stat[self.name]
        self.raw_hp = self.stat[0]
        self.raw_atk = self.stat[1]
        self.raw_def = self.stat[2]
        self.basespd = self.stat[3]
        self.hp_multiplier = self.stat[4]
        self.atk_multiplier = self.stat[5]
        self.def_multiplier = self.stat[6]
        self.atk_range=self.stat[7]
        self.updstat()
        self.hp = self.maxhp
        self.atk = self.baseatk
        self.def_ = self.basedef
        self.speed = self.basespd
        #status
        self.status = []
        #healthbar
    def updstat(self):
        self.maxhp = self.raw_hp + self.level * self.hp_multiplier
        self.baseatk = self.raw_atk + self.level * self.atk_multiplier
        self.basedef = self.raw_def + self.level * self.def_multiplier
    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                if direction == 'horizontal':
                    if self.direction.x > 0: self.hitbox_rect.right = sprite.rect.left
                    if self.direction.x < 0: self.hitbox_rect.left = sprite.rect.right
                else:
                    if self.direction.y < 0: self.hitbox_rect.top = sprite.rect.bottom
                    if self.direction.y > 0: self.hitbox_rect.bottom = sprite.rect.top
    def take_damage(self, dmg):
        self.hp -= dmg / (1 + 0.01 * self.def_)
        if self.hp <= 0:
            self.destroy()




