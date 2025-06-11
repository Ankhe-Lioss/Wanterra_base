from pytmx.pytmx import rotate

from settings import *
from projectiles import *
from stats import *
from status import *
class Player_projectiles(Projectiles):
    def __init__(self, pos, direction, game):
        super().__init__(pos,direction,game)
        self.enemy_sprites=game.enemy_sprites
        #load combat stat
        self.atk=player_projectiles[self.name][0]
        self.speed=player_projectiles[self.name][1]
        self.sound=player_projectiles[self.name][2]
        self.user=game.player
class Gauntlet_Primary(Player_projectiles):
    def __init__(self, pos, direction, game):
        self.name='Gauntlet_Primary'
        super().__init__(pos,direction,game)
class Gauntlet_SkillQ(Player_projectiles):
    def __init__(self, pos, direction, game):
        self.name='Gauntlet_SkillQ'
        super().__init__(pos, direction, game)
class Gauntlet_SkillE(Player_projectiles):
    def __init__(self, pos, direction, game):
        self.name='Gauntlet_SkillE'
        super().__init__(pos, direction,game)
        self.enemy_piercing=True
        self.wall_penetrate=True
    def special_effect(self,sprite):
        Slowed=Status('Slow',3000)
        sprite.status.append(Slowed)
