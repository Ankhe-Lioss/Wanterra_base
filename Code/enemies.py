from settings import *
from livingentity import *
class Enemy(LivingEntity):
    def __init__(self, pos,groups, game):
        #load object to interact
        self.level=game.level
        super().__init__(groups)
        self.player=game.player
        self.game=game
        self.collision_sprites=game.collision_sprites
        self.enemy_sprite=game.enemy_sprites
        #side calculation
        self.animation_speed = 6

        self.death_time=0
        self.death_duration=400
        #load default state
        self.frame_index = 0
        self.states=['Walking','Attacking']
        self.state='Walking'
        #load image
        self.load_frames()
        # image
        self.image = self.frames['Walking'][0]
        # rect
        self.rect = self.image.get_frect(center=pos)
    def load_frames(self):
        self.frames = {}
        for i in self.states :
            self.frames[i] = []
            for k in range(0, 6):
                surf = pygame.image.load(join('images', 'enemies',f'{self.name}',f'{i}',f'{k}.png')).convert_alpha()
                self.frames[i].append(surf)

    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]
        if hasattr(self, 'asymmetry') and self.direction.x < 0:
            self.image = pygame.transform.flip(self.image, True, False)


    def move_enemy(self, dt):
        # get direction
        player_pos = pygame.Vector2(self.player.rect.center)
        enemy_pos = pygame.Vector2(self.rect.center)
        self.direction = (player_pos - enemy_pos).normalize() if (player_pos-enemy_pos) else (player_pos-enemy_pos)

        # update the rect position + collision
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.enemy_collision('horizontal',dt)
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')
        self.enemy_collision('vertical',dt)
        self.rect.center = self.hitbox_rect.center
    def enemy_collision(self,direction,dt):
        for sprite in self.enemy_sprite:
                if self!=sprite:
                    if sprite.rect.colliderect(self.hitbox_rect):
                        if direction == 'horizontal':
                            self.hitbox_rect.x -= self.direction.x * self.speed * dt
                        else:
                            self.hitbox_rect.y -= self.direction.y * self.speed * dt
    def destroy(self):
        self.death_time=pygame.time.get_ticks()
        destroy_surf=pygame.mask.from_surface(self.frames['Walking'][0]).to_surface()
        destroy_surf.set_colorkey('black')
        self.image=destroy_surf
    def death_timer(self):
        if pygame.time.get_ticks()-self.death_time>=self.death_duration:
            self.kill()

    def update(self, dt):
        if self.death_time==0:
            self.move_enemy(dt)
            self.animate(dt)
        else:
            self.death_timer()


class Poro(Enemy):
    def __init__(self, pos, groups, game):
        self.name='Poro'
        super().__init__(pos,groups,game)

        self.hitbox_rect = self.rect.inflate(0, 0)
class Meele(Enemy):
    def __init__(self, pos,groups, game):
        self.name='Meele'
        super().__init__(pos,groups,game)
        self.hitbox_rect = self.rect.inflate(0, 0)
        self.asymmetry=True