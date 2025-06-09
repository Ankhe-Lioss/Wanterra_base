from settings import *
class Poro_stomp(pygame.sprite.Sprite):
    def __init__(self,pos,groups,enemy):
        super().__init__(groups)
        super().__init__(groups)
        self.frame_index = 0
        self.frames=[]
        self.load_frame()
        self.animation_speed = 3
        self.lifetime=1000
        self.spawn_time=pygame.time.get_ticks()
        self.image = self.frames[0]
        self.rect = self.image.get_frect(center=pos)
    def load_frame(self):
        for i in range(3):
            surf=pygame.image.load(join('images', 'aoe','Poro_stomp', f'{i}.png')).convert_alpha()
            self.frames.append(surf)
    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        self.image = self.frames[int(self.frame_index % len(self.frames))]
    def update(self, dt):
        self.animate(dt)
        if pygame.time.get_ticks()-self.spawn_time>=self.lifetime:
            self.kill()
