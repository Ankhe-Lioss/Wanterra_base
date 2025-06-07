from settings import *
from enemies import *
from entity_stat import *

def Spawn_poro(pos,game):
    Poro(pos, entity_stat["Poro"], (game.all_sprites, game.enemy_sprites), game)
def Spawn_meele(pos,game):
    Meele(pos, entity_stat["Meele"], (game.all_sprites, game.enemy_sprites), game)