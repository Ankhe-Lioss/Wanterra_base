import pygame
from os.path import join

from settings import *

# Initialize pygame mixer
pygame.mixer.init()  # Ensure the mixer is initialized before using sound features

# Load background audio
background = pygame.mixer.Sound(join('audio', 'background.ogg'))
background.set_volume(0.6)

Gauntlet_Primary_sound=pygame.mixer.Sound(join('audio','projectiles', 'Gauntlet_Primary_Hit.ogg'))
Gautlet_SkillQ_sound=pygame.mixer.Sound(join('audio','projectiles', 'Gauntlet_SkillQ_Hit.ogg'))
Gauntlet_SkillE_sound=pygame.mixer.Sound(join('audio','projectiles', 'Gauntlet_SkillE_Hit.ogg'))
Gauntlet_primary_sound = pygame.mixer.Sound(join('audio','skill','Gauntlet_Primary_Start.ogg'))
Gauntlet_skillQ_sound=pygame.mixer.Sound(join('audio','skill', 'Gauntlet_SkillQ_Start.ogg'))
Gauntlet_skillE_sound=pygame.mixer.Sound(join('audio', 'skill','Gauntlet_SkillE_Start.ogg'))
hit_sound=pygame.mixer.Sound(join('audio','impact.ogg'))