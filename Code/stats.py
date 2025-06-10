from load_audio import *
entity_stat = {
#   "enemy_name" : (hp, atk, def, spd, hp_multiplier, atk_multiplier, def_multiplier,atk_range)
    "Player" : (500, 100, 10, 500, 50, 20, 5,0),
    "Poro"   : (250, 50 , 10, 350, 75, 10, 2,64),
    "Meele"   : (300, 50 , 10, 350, 75, 10, 2,64),
    "Karthus"   : (300, 50 , 10, 200, 75, 10,2, 320),
    "Chogath"   : (300, 50 , 10, 350, 75, 10,2, 128)
}
player_projectiles = {
#   "proj" : (atk_scale_multification, speed)
    "Gauntlet_Primary" : (1, 1000,Gauntlet_Primary_sound),
    "Gauntlet_SkillQ" : (3, 1000,Gautlet_SkillQ_sound),
    "Gauntlet_SkillE" : (2, 750,Gauntlet_SkillE_sound)
}
enemy_projectiles = {
#   "proj" : (atk_scale_multification, speed)
    "Karthus_Primary" : (2, 750,Gauntlet_skillE_sound),

}
