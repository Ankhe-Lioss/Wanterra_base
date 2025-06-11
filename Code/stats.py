from load_audio import *
entity_stat = {
#   "enemy_name" : (hp, atk, def, spd, hp_multiplier, atk_multiplier, def_multiplier,atk_range)
    "Player" : (500, 100, 10, 450, 50, 20, 5,0),
    "Poro"   : (250, 50 , 10, 500, 75, 10, 2,64),
    "Meele"   : (300, 50 , 10, 350, 75, 10, 2,64),
    "Karthus"   : (250, 50 , 10, 250, 75, 10,2, 382),
    "Chogath"   : (300, 50 , 10, 350, 75, 10,2, 128)
}
player_projectiles = {
#   "proj" : (atk_scale_multification, speed)
    "Gauntlet_Primary" : (1, 1000,Gauntlet_Primary_sound),
    "Gauntlet_SkillQ" : (2, 1000,Gautlet_SkillQ_sound),
    "Gauntlet_SkillE" : (1, 750,Gauntlet_SkillE_sound)
}
enemy_projectiles = {
#   "proj" : (atk_scale_multification, speed)
    "Karthus_Primary" : (2, 1200,hit_sound),

}
skill_stats = {
#   "Skill" : (cooldown, warmup, cast_time,duration)

    #Gautlet Skill
    "Gauntlet_primary" : (1000, 0, 0,0,Gauntlet_primary_sound),
    "Teleport" : (1500, 0, 0,75,Gauntlet_primary_sound),
    "Gauntlet_skillQ" : (5000, 0, 0,0,Gauntlet_skillQ_sound),
    "Gauntlet_skillE" : (15000, 0, 0,0,Gauntlet_skillE_sound),
    #Enemy Skill
    "Karthus_primary" : (1000, 0, 0,500,Gauntlet_primary_sound),
    "Poro_stomp":(1000, 0, 0,1000,Gauntlet_primary_sound),
    "Chogath_stomp": (1000, 0, 0, 500, Gauntlet_primary_sound)

}
