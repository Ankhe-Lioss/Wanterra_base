from settings import *
from player_projectiles import *
from enemy_projectiles import *
from aoe import *
from aoeinit import *
from load_audio import *
from stat import *

class Skill():
    def __init__(self, user):
        self.user=user
        self.can_cast = True
        self.stat=skill_stats[self.name]
        self.skill_cooldown = self.stat[0]
        self.skill_duration = self.stat[3]
        self.warmup = self.stat[1]
        self.cast_sound = self.stat[4]
        self.cast_time = self.stat[2]

        self.use_time = 0
        self.cooldown=0
        self.duration_run_out = None
    def check(self):
        if self.can_cast:
            self.cast_sound.play()
            self.using_skill()
            self.can_cast = False
            self.use_time = pygame.time.get_ticks()
    def skill_timer(self):
        if not self.can_cast:
            current_time = pygame.time.get_ticks()
            if current_time - self.use_time >= self.skill_cooldown:
                self.can_cast = True
    def turn_off(self):
        self.duration_run_out = None
    def update(self,dt):
        if self.can_cast:
            self.cooldown=0
        else:
            self.cooldown=self.use_time+self.skill_cooldown-pygame.time.get_ticks()
        self.skill_timer()
        if self.duration_run_out is not None:
            if pygame.time.get_ticks() >= self.duration_run_out:
                self.turn_off()
class Gauntlet_primary(Skill):
    def __init__(self, user):
        self.name='Gauntlet_primary'
        super().__init__(user)
    def using_skill(self):
        pos = self.user.rect.center + self.user.mouse_direction * 50
        Gauntlet_Primary(pos, self.user.mouse_direction, self.user.game)

class Gauntlet_skillQ(Skill):
    def __init__(self, user):
        self.name='Gauntlet_skillQ'
        super().__init__(user)
    def using_skill(self):
        pos = self.user.rect.center + self.user.mouse_direction * 50
        Gauntlet_SkillQ(pos, self.user.mouse_direction, self.user.game)

class Gauntlet_skillE(Skill):
    def __init__(self, user):
        self.name='Gauntlet_skillE'
        super().__init__(user)
    def using_skill(self):
        pos = self.user.rect.center + self.user.mouse_direction * 50
        Gauntlet_SkillE(pos, self.user.mouse_direction, self.user.game)

class Teleport(Skill):
    def __init__(self, user):
        self.name='Teleport'
        super().__init__(user)
    def using_skill(self):
        self.user.player.speed = 2000
        self.current_teleport_usingtime = pygame.time.get_ticks()
        self.duration_run_out = self.current_teleport_usingtime + self.skill_duration
    def turn_off(self):
        super().turn_off()
        self.user.player.speed = self.user.player.basespd



class Karthus_primary(Skill):
    def __init__(self, user):
        self.name='Karthus_primary'
        super().__init__(user)
    def using_skill(self):
        Karthus_Primary(self.user,self.user.direction,self.user.game)
        self.user.state='Attacking'
        self.user.speed =0
        self.duration_run_out = pygame.time.get_ticks() + self.skill_duration
    def turn_off(self):
        super().turn_off()
        self.user.speed = self.user.basespd
        self.user.state='Walking'
class Poro_stomp(Skill):
    def __init__(self, user):
        self.name = 'Poro_stomp'
        super().__init__(user)

    def using_skill(self):
        Poro_Stomp(self.user.rect.center,self.user.game,self.user.atk)
        self.user.state = 'Attacking'
        self.user.speed = 0
        self.duration_run_out = pygame.time.get_ticks() + self.skill_duration

    def turn_off(self):
        super().turn_off()
        self.user.speed = self.user.basespd
        self.user.state = 'Walking'
class Chogath_stomp(Skill):
    def __init__(self, user):
        self.name = 'Chogath_stomp'
        super().__init__(user)

    def using_skill(self):
        Spawn_rupture(self.user.player.rect.center, self.user.game, self.user.atk)
        self.user.state = 'Attacking'
        self.user.speed = 0
        self.duration_run_out = pygame.time.get_ticks() + self.skill_duration

    def turn_off(self):
        super().turn_off()
        self.user.speed = self.user.basespd
        self.user.state = 'Walking'
