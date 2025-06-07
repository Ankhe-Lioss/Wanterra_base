from settings import *
from projectiles import *
from skill import *

class Weapon(pygame.sprite.Sprite):
    def __init__(self, groups,game):
        # player connection


        self.game=game
        self.player = self.game.player
        self.mouse_direction = self.player.mouse_direction
        # sprite setup
        super().__init__(groups)
        self.gun_surf = pygame.image.load(join('images', 'gun', 'gun.png')).convert_alpha()
        self.image = self.gun_surf
        self.rect = self.image.get_frect(center=self.player.rect.center)
        self.primary=Gauntlet_primary(self)
        self.secondary=Gauntlet_secondary(self)
        self.q_skill=Gauntlet_primary(self)
        self.e_skill=Gauntlet_primary(self)
    def input(self):
        if pygame.mouse.get_pressed()[0]:
            self.primary.execute()
        if pygame.mouse.get_pressed()[2]:
            self.secondary.execute()
    def rotate_gun(self):
        self.mouse_direction = self.player.mouse_direction
        angle = degrees(atan2(self.mouse_direction.x, self.mouse_direction.y))+180
        self.image = pygame.transform.rotozoom(self.gun_surf, angle, 1)

    def update(self, _):
        self.rotate_gun()
        self.input()
        self.rect.center = self.player.rect.center + self.mouse_direction*40
