from pytmx.pytmx import rotate

from settings import *
from projectiles import *
from stats import *
from status import *
class Enemy_projectiles(Projectiles):
    def __init__(self, user, direction, game):
        self.user=user
        pos=user.rect.center
        super().__init__(pos,direction,game)
        self.enemy_sprites=game.player_sprites
        #load combat stat
        self.atk=enemy_projectiles[self.name][0]
        self.speed=enemy_projectiles[self.name][1]
        self.sound=enemy_projectiles[self.name][2]
class Karthus_Primary(Enemy_projectiles):
    def __init__(self, user, direction,game):
        self.name='Karthus_Primary'
        super().__init__(user,direction,game)
