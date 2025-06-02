from settings import *
from enemies import *
def Spawn_poro(pos,game):
    Poro(pos, (game.all_sprites, game.enemy_sprites), game.player, game.enemy_sprites,
         game.collision_sprites)