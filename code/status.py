class Status:
    def __init__(entity, effect_type, duration):
        entity.effect_type = effect_type
        entity.duration = duration



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