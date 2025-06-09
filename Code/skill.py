from settings import *
from projectiles import *
class Skill():
    def __init__(self, weapon):
        self.weapon=weapon
        self.can_skill = True
        self.use_time = 0
    def check(self):
        if self.can_skill:
            self.using_skill()
            self.can_skill = False
            self.use_time = pygame.time.get_ticks()
    def skill_timer(self):
        if not self.can_skill:
            current_time = pygame.time.get_ticks()
            if current_time - self.use_time >= self.skill_cooldown:
                self.can_skill = True
    def execute(self):
        self.skill_timer()
        self.check()
class Gauntlet_primary(Skill):
    def __init__(self, weapon):
        super().__init__(weapon)
        self.skill_cooldown = 1000
    def using_skill(self):
        pos = self.weapon.rect.center + self.weapon.mouse_direction * 50
        Gauntlet_Primary(pos, self.weapon.mouse_direction, (self.weapon.game.all_sprites, self.weapon.game.bullet_sprites),self.weapon.game)
class Gauntlet_secondary(Skill):
    def __init__(self, weapon):
        super().__init__(weapon)
        self.skill_cooldown = 3000

    def using_skill(self):
        pos = self.weapon.rect.center + self.weapon.mouse_direction * 50
        Gauntlet_Secondary(pos, self.weapon.mouse_direction,
                         (self.weapon.game.all_sprites, self.weapon.game.bullet_sprites), self.weapon.game)
class Gauntlet_skillR(Skill):
    def __init__(self, weapon):
        super().__init__(weapon)
        self.skill_cooldown = 3000

    def using_skill(self):
        pos = self.weapon.rect.center + self.weapon.mouse_direction * 50
        Gauntlet_SkillR(pos, self.weapon.mouse_direction,
                         (self.weapon.game.all_sprites, self.weapon.game.bullet_sprites), self.weapon.game)










class Teleport(Skill):
    def __init__(self, weapon):

        super().__init__(weapon)
        self.normal_speed = self.weapon.player.speed
        self.skill_cooldown = 1500
        self.skill_duration = 100
        self.speed_reset_time = None
    def using_skill(self):
        self.weapon.player.speed = 2000
        self.current_teleport_usingtime = pygame.time.get_ticks()
        self.speed_reset_time = self.current_teleport_usingtime + self.skill_duration
    def turn_off(self):
        self.weapon.player.speed = self.normal_speed
        self.speed_reset_time = None

