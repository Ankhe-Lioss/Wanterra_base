import pygame
class Status:
    def __init__(entity, effect_type, duration):
        entity.effect_type = effect_type
        entity.duration = duration/1000

def check_status(entity,dt):
    for statu in entity.status:
        if statu.effect_type=='Slow':
            entity.speed=entity.basespd*0.5
            statu.duration-=dt
            if statu.duration<=0:
                entity.speed=entity.basespd
                entity.status.remove(statu)
        if statu.effect_type=='Poison':
            entity.take_damage(40*dt)
            statu.duration-=dt
            if statu.duration<=0:
                entity.status.remove(statu)
        if statu.effect_type=='Cant_move_attack':
            if entity.state!='Attacking':
                entity.state='Attacking'
            entity.speed=0
            statu.duration-=dt
            if statu.duration<=0:
                entity.speed=entity.basespd
                entity.state='Walking'
                entity.status.remove(statu)
        if statu.effect_type=='damaged':
            if pygame.time.get_ticks() % 150< 75:  # Visible half the time
                entity.visible = False
            else:
                entity.visible = True
            statu.duration-=dt
            if statu.duration<=0:
                entity.visible = True
                entity.status.remove(statu)
#Status
