from settings import *
from enemies import *
from entity_stat import *

def Spawn_poro(pos,game):
    Poro(pos, (game.all_sprites, game.enemy_sprites), game)


def Spawn_meele(pos,game):
    Meele(pos, (game.all_sprites, game.enemy_sprites), game)


def Spawn_animation(pos,game,enemy_name):
    Spawn_animation(pos,(game.all_sprites),game,enemy_name)
class Spawn_animation(pygame.sprite.Sprite):
    def __init__(self, pos,groups,game,enemy_name):
        super().__init__(groups)
        self.game=game
        self.frame_index = 0
        self.frames=[]
        self.load_frame()
        self.enemy_name=enemy_name
        self.animation_speed = 10
        self.lifetime=1500
        self.spawn_time=pygame.time.get_ticks()
        self.image = self.frames[0]
        self.rect = self.image.get_frect(topleft=pos)

    def load_frame(self):
        for i in range(15):
            surf=pygame.image.load(join('images', 'enviroment','enemy_spawn_animation', f'{i}.png')).convert_alpha()
            self.frames.append(surf)
    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        self.image = self.frames[int(self.frame_index % len(self.frames))]
    def spawn(self):
        if pygame.time.get_ticks()-self.spawn_time>=self.lifetime:
            self.kill()
            if self.enemy_name=='Poro':
                Spawn_poro((self.rect.center),self.game)
            if self.enemy_name=='Meele':
                Spawn_meele((self.rect.center),self.game)
    def update(self, dt):
        self.animate(dt)
        self.spawn()