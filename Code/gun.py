from settings import *
from projectiles import *
class Gun(pygame.sprite.Sprite):
    def __init__(self, groups,game):
        # player connection

        self.distance = 40
        self.player_direction = pygame.Vector2(0, 1)
        self.game=game
        self.player = self.game.player
        # sprite setup
        super().__init__(groups)
        self.gun_surf = pygame.image.load(join('..','images', 'gun', 'gun.png')).convert_alpha()
        self.image = self.gun_surf
        self.rect = self.image.get_frect(center=self.player.rect.center + self.player_direction * self.distance)
        # gun timer
        self.can_shoot = True
        self.shoot_time = 0
        self.gun_cooldown = 1000
    def input(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            pos = self.rect.center + self.player_direction * 50
            Bullet(pos, self.player_direction, (self.game.all_sprites, self.game.bullet_sprites),self.game.enemy_sprites)
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

    def gun_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.gun_cooldown:
                self.can_shoot = True


    def get_direction(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        player_pos = pygame.Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.player_direction = (mouse_pos - player_pos).normalize()

    def rotate_gun(self):
        angle = degrees(atan2(self.player_direction.x, self.player_direction.y)) - 90
        if self.player_direction.x > 0:
            self.image = pygame.transform.rotozoom(self.gun_surf, angle, 1)
        else:
            self.image = pygame.transform.rotozoom(self.gun_surf, abs(angle), 1)
            self.image = pygame.transform.flip(self.image, False, True)

    def update(self, _):
        self.get_direction()
        self.rotate_gun()
        self.gun_timer()
        self.input()
        self.rect.center = self.player.rect.center + self.player_direction * self.distance
