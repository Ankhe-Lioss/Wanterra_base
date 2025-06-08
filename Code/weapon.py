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
        self.secondary=Teleport(self)
        self.q_skill=Gauntlet_secondary(self)
        self.e_skill=Gauntlet_secondary(self)
        self.r_skill=Gauntlet_skillR(self)
    def input(self):
        if pygame.mouse.get_pressed()[0]:
            self.primary.execute()
        if pygame.mouse.get_pressed()[2]:
            self.secondary.execute()
        if pygame.key.get_pressed()[pygame.K_q]:
            self.q_skill.execute()
        if pygame.key.get_pressed()[pygame.K_e]:
            self.e_skill.execute()
        if pygame.key.get_pressed()[pygame.K_r]:
            self.r_skill.execute()
    def rotate_gun(self):
        self.mouse_direction = self.player.mouse_direction
        angle = degrees(atan2(self.mouse_direction.x, self.mouse_direction.y))+180
        self.image = pygame.transform.rotozoom(self.gun_surf, angle, 1)

    def update(self, _):
        self.rotate_gun()
        self.input()
        if self.secondary.speed_reset_time!=None:
            if pygame.time.get_ticks()>=self.secondary.speed_reset_time:
                self.player.speed = self.secondary.normal_speed
                self.secondary.speed_reset_time = None

        self.rect.center = self.player.rect.center + self.mouse_direction*40
